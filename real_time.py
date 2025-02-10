import json
from websocket import WebSocketApp
from db.store_elasticsearch import store_order_es

def on_message(ws, message, es, trading_pair):
    """
    Handle incoming WebSocket messages for real-time order book updates.
    """
    data = json.loads(message)

    if data.get("e") == "depthUpdate":
        bids = data.get("b", [])
        asks = data.get("a", [])
        timestamp = data.get("E", None)

        order_data = {
            "bids": bids[:5],
            "asks": asks[:5],
            "timestamp": timestamp
        }

        store_order_es(es, "orderbook_ws", trading_pair, order_data)

        print(f"Stored real-time order book data for {trading_pair} in Elasticsearch.")

def start_websocket(trading_pair, es):
    url = f"wss://stream.binance.com:9443/ws/{trading_pair.lower()}@depth"
    ws = WebSocketApp(
        url,
        on_message=lambda ws, msg: on_message(ws, msg, es, trading_pair)
    )
    ws.run_forever()

