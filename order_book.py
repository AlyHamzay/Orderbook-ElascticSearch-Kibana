from binance.fetch_data import fetch_order_book
from binance.real_time import start_websocket
from db.store_elasticsearch import connect_elasticsearch, store_order_es

def main():
    # Connect to Elasticsearch
    es = connect_elasticsearch()

    # Ask user for the trading pair
    trading_pair = input("Enter the trading pair (e.g., BTCUSDT): ").strip().upper()

    # Choose between REST API snapshot or WebSocket
    mode = input("Enter '1' for REST API snapshot or '2' for real-time WebSocket updates: ").strip()

    if mode == '1':
        try:
            print(f"Fetching order book for {trading_pair} using REST API...\n")
            order_book_data = fetch_order_book(trading_pair)

            # Elasticsearch me store karna
            store_order_es(es, "orderbook_rest", trading_pair, order_book_data)

            print(f"Stored REST API data for {trading_pair} in Elasticsearch.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif mode == '2':
        print(f"Starting WebSocket for {trading_pair}...")
        start_websocket(trading_pair, es)

    else:
        print("Invalid option. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
