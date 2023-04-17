import sqlite3

connection = sqlite3.connect('ledger.db')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE ledger
    (date DATE, debited TEXT, credited TEXT, amount INTEGER)
""")
cursor.execute("""INSERT INTO ledger VALUES
    ('2022-02-20', 'Bank', 'Cash', 10000),
    ('2022-02-23', 'Cash', 'Van', 45000)
""")
connection.commit()