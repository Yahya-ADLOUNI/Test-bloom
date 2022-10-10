# Module Imports
import mariadb
import sys

# Get Cursor
def create (cur) :
    try:
        cur.execute(
        """
            CREATE TABLE `TESTTABLE` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `name` varchar(255) DEFAULT NULL,
                `email` varchar(255) DEFAULT NULL,
                `phone` varchar(255) DEFAULT NULL,
                `linkedin` varchar(255) DEFAULT NULL,
                `experience` longtext DEFAULT NULL,
                `education` longtext DEFAULT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)
    except mariadb.Error as e:
        print(f"Error: {e}")

def connect () :
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="databasefortest"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

def insert(name, email, phone, linkedin, experience, education):
    conn = connect()
    cur = conn.cursor()
    # create(cur)
    values = '( `' + 'NULL' + '`,`' + email + '`, `' + phone + '`,`' + linkedin + '`,`' + experience + '`,`' + education + '`);'
    print(values)
    try:
        cur.execute(
        "INSERT INTO databasefortest.testtable (name, email, phone, linkedin, experience, education) VALUES(?,?,?,?,?,?);", 
        (name, email, phone, linkedin, experience, education))
    except mariadb.Error as e:
        print(f"Error: {e}")
    conn.commit() 
    conn.close()
