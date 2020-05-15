import flask
from flask import request
import zipfile
import requests
from io import BytesIO

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def main():
    myZipFile = request.data
    headers = flask.request.headers
    zipdata = BytesIO()
    zipdata.write(myZipFile)
    with open(zipdata, 'wb') as result:
        result.write(base64.b64decode(d))
    print(headers)
    pID = headers.get('parent-id')
    print(pID)
    with zipfile.ZipFile(zipdata) as zip_ref:
        for info in zip_ref.infolist():
            data = info.filename
            myHTML = zip_ref.read(data)
            headToSend = {'parent-id' : pID}
            req = requests.post('https://ccdev3-moneyspot.cs57.force.com/services/apexrest/GetSeperateFiles/', data=myHTML, headers=headToSend)
            print(req)
    return 'Success'

if __name__ == "__main__":
    app.run(debug=True)