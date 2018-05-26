import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print("ERROR")
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    pass


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://s71.chatango.com:8081/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        header=[
            "Cookie: _ga=GA1.2.783058670.1517265373; "
            "cookies_enabled.chatango.com=yes; "
            "fph.chatango.com=https; "
            "__utma=216059204.783058670.1517265373.1527346781.1527346781.1; "
            "__utmc=216059204; "
            "__utmz=216059204.1527346781.1.1.utmcsr=google|utmccn=("
            "organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; "
            "__utmb=216059204.1.10.1527346781; "
            "_gid=GA1.2.1756799105.1527346804",
            "Origin: https://st.chatango.com",
            "Sec-WebSocket-Extensions: "
            "permessage-deflate; "
            "client_max_window_bits",
            "Sec-WebSocket-Key: "
            "f/ccDYotKjXecw06mmnpPA==",
            "Sec-WebSocket-Version: 13",
            "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        ])
    ws.on_open = on_open
    ws.run_forever()
