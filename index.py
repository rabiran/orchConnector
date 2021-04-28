import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
from flask import Flask, request, Response
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import xmltodict, json
import xmlyikes

# parsed_yikes2 = readfromstring(yikes2)
# print(json2xml.Json2xml(parsed_yikes2).to_xml())

# obj = xmltodict.parse(xmlyikes)
# print(json.dumps(obj))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

print(os.environ.get("USERR"))

username = os.environ.get("USERR")
password = os.environ.get("PASS")
domain = os.environ.get("DOMAIN")
orch_url = os.environ.get("ORCH_URL")

port = os.environ.get("PORT")

kerberos_auth=HTTPKerberosAuth(principal=username+"@"+domain+":"+password, delegate=True)

print (username+"@"+domain+":"+password)

app = Flask(__name__)


@app.route('/')
def healthCheck():
    return Response("service up", status=200)


@app.route('/', methods=['POST'])
def orchProxy():
    print(request.json)

    if ('method' not in request.json or 'url' not in request.json or 'data' not in request.json):
        return Response("need method, url, data", status=400)

    url = request.json['url']
    method = request.json['method']
    data = request.json['data']

    r = None

    if method == 'GET':
        print('get with '+data)
        r = requests.get(url, auth=kerberos_auth)
    elif method == 'POST':
        print('post with '+data)
        r = requests.post(url, data=data, auth=kerberos_auth)
    else:
        return Response("method can only be GET or POST", status=400)


    if r.status_code is not 200:
            return Response("orch failed with "+str(r.status_code), status=r.status_code)

    return Response("ok", status=200)


if __name__=="__main__":
    app.run(port=port, host='0.0.0.0')
