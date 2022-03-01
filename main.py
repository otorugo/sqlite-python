from sqlite3 import Connection


with Connection('test.db') as connection:
    
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS testing(
            test_id INTEGER,
            test_name TEXT,
            description TEXT
        )''')
    connection.commit()
    cursor.execute('''INSERT OR IGNORE INTO testing VALUES(1,'simple_test','test my test should check db')''')
    connection.commit()



with Connection('test.db') as connection:
    
    cursor = connection.cursor()
    
    result = cursor.execute("SELECT * FROM testing").fetchall()
    
    print(result)