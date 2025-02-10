import requests

def fetch_order_book(symbol):
    """
    Fetch the order book for the specified trading pair from Binance REST API.
    """
    base_url = "https://api.binance.com/api/v3/depth"
    params = {"symbol": symbol.upper(), "limit": 10}  # Fetch top 10 levels

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        order_book = response.json()

        # Structuring data for Elasticsearch
        return {
            "bids": order_book.get("bids", []),
            "asks": order_book.get("asks", []),
            "timestamp": order_book.get("lastUpdateId", None)
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from Binance: {e}")
