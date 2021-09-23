import json
import logging
import numpy as np
import time
import websocket

# Set logging parameters
log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

# Set exchange
EXCHANGE = "Binance"

# Set websocket
SOCKET = "wss://stream.binance.com:9443/ws"

# Set seconds to run test
RUNTIME = 15

# Set subscription message
subscribe = {
    "method": "SUBSCRIBE",
    "params": [
        "btcusdt@bookTicker"
    ],
    "id": 1
}


# Define callback functions for websocket connection
def on_open(ws):
    logging.info(f"{EXCHANGE} Socket open")
    ws.send(json.dumps(subscribe, ensure_ascii=False).encode('utf8'))


def on_message(ws, message):
    global count
    global counts
    global starttime

    endtime = time.time()
    interval = (endtime - starttime)
    count += 1

    if interval >= 1:
        logging.info(f'{count} messages received in {interval} seconds.')
        starttime = endtime
        counts.append(count)
        count = 0

    if (endtime - begin) >= RUNTIME:
        ws.close()


def on_close(ws):
    logging.info(f"{EXCHANGE} Socket closed")


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_message=on_message, on_close=on_close)

if __name__ == "__main__":
    count = 0
    counts = []
    stop_interval = 0
    starttime = time.time()
    begin = time.time()

    ws.run_forever()

    if len(counts) != 0:
        logging.info(f"Average messages per second: {np.average(counts)}")
    else:
        logging.info(f"No Messages received")
