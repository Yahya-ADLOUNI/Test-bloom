import fitz, re
from db import insert
from pdf2 import searchFiles
from pdfminer.high_level import extract_pages, extract_text

files_to_read = searchFiles('./assets/')

PHONE_REGEX= "(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})"
EMAIL_REGEX= "^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"
FULLNAME_REGEX = "^([a-zA-Z0-9]+|[a-zA-Z0-9]+\s{1}[a-zA-Z0-9]{1,}|[a-zA-Z0-9]+\s{1}[a-zA-Z0-9]{3,}\s{1}[a-zA-Z0-9]{1,})$"
LINKEDIN_REGEX = "(linkedin)"
FORMATION_REGEX = "^(formation|education)"
EXPERIENCE_REGEX = "^(experience|experiences\s*professionnelles|professionnelles)"

def readFile(file):
    doc = fitz.open(file)
    file_text = extract_text(file)
    file_lines = file_text.split('\n')
    i = 0
    foramtion = False
    experience = False
    foramtion_array = []
    experience_array = []
    result = {}
    for line in file_lines:
        clean_line = line.strip()
        if len(clean_line) != 0:
            if (
                re.search(PHONE_REGEX, clean_line) or
                re.search(EMAIL_REGEX, clean_line) or
                re.search(FULLNAME_REGEX, clean_line) or
                re.search(LINKEDIN_REGEX, clean_line, re.IGNORECASE) or
                re.search(FORMATION_REGEX , clean_line, re.IGNORECASE) or
                re.search(EXPERIENCE_REGEX , clean_line, re.IGNORECASE)
            ):
                if i ==0 and re.search(FULLNAME_REGEX, clean_line):
                    result['name'] = clean_line
                    i += 1
                elif re.search(EMAIL_REGEX, clean_line):
                    result['email'] = clean_line
                elif re.search(PHONE_REGEX, clean_line):
                    result['phone'] = clean_line
                elif re.search(LINKEDIN_REGEX, clean_line, re.IGNORECASE):
                    result['linkedin'] = clean_line
                elif re.search(FORMATION_REGEX, clean_line, re.IGNORECASE):
                    foramtion = True
                    experience = False
                elif re.search(EXPERIENCE_REGEX, clean_line, re.IGNORECASE):
                    foramtion = False
                    experience = True
            if foramtion:
                foramtion_array.append(clean_line)
            if experience:
                experience_array.append(clean_line)
    result['experience'] = experience_array
    result['formation'] = foramtion_array
    return result

def main(files):
    if files["valid"] == False : return "Unvalid files"
    if len(files["valid_files"]) == 0 : return "No files"
    for file in files["valid_files"]:
        data = readFile(file)
        insert(
            name= data['name'],
            email= data['email'],
            phone= data['phone'],
            linkedin= data['linkedin'],
            experience= str(data['experience']),
            education= str(data['formation']),
        )
        
main(files_to_read)