import flask
import base64
from flask import request, redirect

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main():
    state = request.args.get("state")
    code = request.args.get("code")
    data = decode(state).split('##')
    print(data)
    state = encode(data[0])
    redirectURL = data[1] + '?state=' + state + '&code=' + code
    print(redirectURL)
    return redirect(redirectURL)

def decode(message):
    base64_message = message
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

def encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

if __name__ == "__main__":
    app.run(debug=True)