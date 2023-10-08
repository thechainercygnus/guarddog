import logging
import os
from werkzeug.serving import WSGIRequestHandler

from flask import Flask, request, jsonify

from guarddog.models import HeartbeatData, MonitorData, MsgData

app = Flask(__name__)

if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    filename=os.path.join('logs', "guarddog.log"),
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger("guarddog")


@app.route("/")
def hello_world():
    return "<h1 text-align='center'>Guard Dog</h1>"

@app.route("/dump", methods=["POST"])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        logger.info(json)
    else:
        pass
    return "", 200

@app.route("/status_change", methods=["POST"])
def process_status_change():
    # Check if the request has a JSON content type
    if request.headers.get('Content-Type') != 'application/json':
        error_message = 'Invalid Content-Type header. Please send a JSON request.'
        return jsonify({'error': error_message}), 400

    try:
        # Attempt to parse the JSON data from the request body
        data = request.get_json()
        if 'heartbeat' in data and 'monitor' in data:
            # Handle heartbeat and monitor data
            heartbeat = HeartbeatData(**data['heartbeat'])
            monitor = MonitorData(**data['monitor'])
            msg = data.get('msg')
            
            # Perform processing and storage logic here
            
            return jsonify({"message": "Data received and processed successfully"})

        elif 'msg' in data:
            # Handle msg data
            msg_data = MsgData(**data)
            
            # Perform processing and storage logic here
            
            return jsonify({"message": "Msg data received and processed successfully"})

    except Exception as e:
        # Handle any unexpected errors
        error_message = 'An error occurred while processing the request.'
        return jsonify({'error': error_message, 'details': str(e)}), 500

    


if __name__ == "__main__":
    WSGIRequestHandler.handler_class = lambda *args, **kwargs: logging.NullHandler()
    app.run(host="0.0.0.0", port=9001)