from flask import Flask, request

app = Flask(__name__)

@app.route("/image", methods=['POST'])
def hello_world():
    if 'file' not in request.files:
        print("not file")
    file = request.files['file']
    print(file)
    return "<p>Hello, World!</p>"


app.run(debug=True)