from elasticsearch import Elasticsearch

def connect_elasticsearch():
    """
    Connect to Elasticsearch.
    """
    es = Elasticsearch(["http://localhost:9200"])  # Update if needed
    if es.ping():
        print("Connected to Elasticsearch")
    else:
        print("Failed to connect to Elasticsearch")
    return es

def store_order_es(es, index_name, trading_pair, data):
    """
    Store order book data into Elasticsearch.
    """
    if not es:
        print("No active Elasticsearch connection.")
        return

    doc = {
        "pair": trading_pair,
        "bids": data.get("bids", []),
        "asks": data.get("asks", []),
        "timestamp": data.get("timestamp", None)
    }

    try:
        es.index(index=index_name, body=doc)
        print(f"Stored order book data for {trading_pair} in Elasticsearch.")
    except Exception as e:
        print(f"Error storing data in Elasticsearch: {e}")

