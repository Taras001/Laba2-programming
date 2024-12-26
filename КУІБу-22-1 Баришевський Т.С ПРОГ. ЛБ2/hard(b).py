import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
@app.route('/post', methods=['POST'])
def save_to_db():
    data = request.data.decode('utf-8')
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (text_data) VALUES (?)', (data,))
    conn.commit()
    conn.close()
    return "Data saved to database successfully!", 200
if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=1234)
