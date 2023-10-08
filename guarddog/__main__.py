from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 text-align='center'>Guard Dog</h1>"

@app.route("/dump", methods=["POST"])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json)
    else:
        pass

if __name__ == "__main__":
    app.run()