from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

functions = {}
root_dir = ""

HOST_NAME = "localhost"
HOST_PORT = 8000


def readFile(path):
    f = open(path)
    return "".join(f.readlines())


def doGETcalls(text):
    for key in functions:
        if key+"()" in text 
            out = functions[key]()
            text = text.replace(key+"()", json.dumps(out))
    return text


def doPOSTcalls(text, json_data):
    json_data = json.loads(json_data)
    for key in json_data:
        if key in functions:
            functions[key](json_data[key])

    for key in functions:
        if key+"()" in text:
            out = functions[key]()
            text = text.replace(key+"()", json.dumps(out))
    return text


def apiMethod(func):
    functions[func.__name__] = func
    return func


class ApyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        data = readFile(root_dir+self.path+".json")
        data = doGETcalls(data)

        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        data_in = self.rfile.read(int(self.headers['content-length']))
        data_in = str(data_in, "utf-8")

        data = readFile(root_dir+self.path+".json")
        data = doPOSTcalls(data, data_in)

        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))


def run(path):
    global root_dir
    root_dir = (path[:-1] if path[-1:] == "/" else path)
    apyServer = HTTPServer((HOST_NAME, HOST_PORT), ApyServer)

    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, HOST_PORT))

    try:
        apyServer.serve_forever()
    except KeyboardInterrupt:
        pass

    apyServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, HOST_PORT))
