from flask import Flask, request

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def save_to_file():
    data = request.data.decode('utf-8')
    with open('data.txt', 'a') as file:
        file.write(data + '\n')
    return "Data saved to file successfully!", 200

if __name__ == '__main__':
    app.run(debug=True, port=1234)
