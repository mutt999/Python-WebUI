from threading import Thread
import webview
import jsonrpc
import sys

import eventservice

if __name__ == "__main__":

    develop = True
    debugger = False

    if len(sys.argv) > 1 and sys.argv[1] == 'prod':
        (develop,debugger) = (False,False)

    api = jsonrpc.RpcServices()

    api.RegisterService(eventservice.IEventService())

    if develop:
        api.StartHttpServer()

    window = webview.create_window(
        "WebUI",
        "http://localhost:5173" if develop else "webui-app/dist/index.html",
        js_api=api,
        min_size=(640, 480),
        width=800,
        height=600
    )
    
    webview.start(None, window, debug=debugger,user_agent="pywebview")
