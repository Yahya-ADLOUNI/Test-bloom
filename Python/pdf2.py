from PyPDF2 import PdfFileReader
import os

def checkFile(fullfile):
    if fullfile.endswith('.pdf') == False : return False
    with open(fullfile, 'rb') as f:
        try:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            if info:
                return True
            else:
                return False
        except:
            return False

def searchFiles(dirpath):
    result = {
        "valid_files" : [],
        "invalid_files" : [],
        "valid" : True,
    }
    if os.access(dirpath, os.R_OK):
        listfiles = os.listdir(dirpath)
        for f in listfiles:
            fullfile = os.path.join(dirpath, f)
            if checkFile(fullfile):
                result["valid_files"].append(fullfile)
            else:
                result["invalid_files"].append(fullfile)
    else:
        result["valid"] = False
    return result