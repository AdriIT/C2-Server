#websocket
import websocket
import _thread
import time
import json

#reverse shell commands
import os
import socket
import subprocess
import sys
import time
#import rel

def on_message(ws, message):

    
    data = json.loads(message)
    #print(data)
    print(data.get("message"))
    if data.get("message") == "You are now connected to device 45":
        # Ignora il messaggio predefinito e non fare nulla
        #print("ping")#successful
        cwd = os.getcwd()
        ws.send(json.dumps({"message": '$'+cwd+' > '}))
        
    elif data["message"] == "ciao":
        print('$' + cwd + '> Hello Server')
        ws.send(json.dumps({"message": '$' + cwd + '> Hello Server'}))
        return
    

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### Closing Connection ###")
    print("Close Status Code:", close_status_code)
    print("Close message:", close_msg)
    out = ("Close Status Code:", close_status_code)
    print("Commencing Lookup Requests...")


def on_open(ws):
    print("Opened connection with Server on Websocket port 45")
    print(subprocess.getoutput('ps'))


def connect():
    # Create a new WebSocket connection
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/devices/45/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    # Run the WebSocket connection asynchronously without blocking
    ws.run_forever()


if __name__ == "__main__":
    #websocket.enableTrace(True)
    connect()
    #    time.sleep(2)
#ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly  
#rel.signal(2, rel.abort)  # Keyboard Interrupt
#<Signal Object | Callback:"abort">
#rel.dispatch()  