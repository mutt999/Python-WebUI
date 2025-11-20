import json
import typing
import http.server
import socketserver
import threading
import re
    
class RpcServices:

    def __init__(self):
        self.services = {}

    def RegisterService(self, service):
        name = type(service).__name__
        self.services[name] = service

    def HandleRequest(self, rpcJson):
        rpc = json.loads(rpcJson)
        className = rpc["ClassName"]
        service = self.services[className]
        methodName = rpc["MethodName"]
        argumentsJson = rpc["ArgumentsAsJsonString"]
        arguments = json.loads(argumentsJson)
        if hasattr(service, methodName):
            slot = getattr(service, methodName)
            result = slot(*arguments)
            return json.dumps(result)
        else:
            pass  # pass error-message

    def StartHttpServer(self):
        PORT = 9000
        httpd =  socketserver.ThreadingTCPServer(("", PORT), RpcServiceHttpHandler)
        RpcServiceHttpHandler.api = self
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()    

class RpcServiceHttpHandler(http.server.SimpleHTTPRequestHandler): 

    def do_OPTIONS(self):
        self.send_response(http.server.HTTPStatus.OK)
        self.end_headers()

    def do_POST(self):
        if re.search("/HandleRequest/*", self.path):
            ctype = self.headers.get("content-type")
            if ctype.startswith("application/json"):
                length = int(self.headers.get("content-length"))
                rfile_str = self.rfile.read(length).decode("utf8")
                res = self.api.HandleRequest(rfile_str)
                self.send_response(http.server.HTTPStatus.OK)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(res.encode('utf-8'))
            else:
                self.send_response(http.server.HTTPStatus.BAD_REQUEST, "Bad Request: must give data")
                self.end_headers()
        else:
            self.send_response(http.server.HTTPStatus.FORBIDDEN)
            self.end_headers()
