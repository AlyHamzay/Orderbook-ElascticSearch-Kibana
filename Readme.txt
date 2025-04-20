# Binance Order Book to ELK Stack

This is an ongoing project where I fetch real-time Binance order book data via REST API, transform it, and send it to **Elasticsearch** for visualization in **Kibana**.

---

## 🚀 Purpose

To simulate a simplified **SOAR-like pipeline** using the ELK Stack:
- **Fetch** data from Binance using REST APIs
- **Enrich and filter** the data (e.g., top 10 buy/sell orders)
- **Ingest** the data into Elasticsearch
- **Visualize and alert** using Kibana

This mimics how Security Orchestration, Automation, and Response (SOAR) systems work by integrating:
- REST API use
- Structured data processing
- Real-time monitoring
- Potential for automation and alerting

---

## 🛠️ Tech Stack

- Python
- Binance REST API
- Elasticsearch
- Kibana
- Logstash (planned)
- Alerts (planned)

---

## ✅ Current Progress

- ✅ Successfully fetches order book data using Binance API
- ✅ Extracts top 10 buy/sell orders
- ✅ Formats the data in JSON
- 🔄 Working on ingestion to Elasticsearch

---

## 🔮 Roadmap

- [ ] Complete Elasticsearch ingestion
- [ ] Build Kibana dashboard for order book data
- [ ] Add alerts for anomalies (e.g. price/volume spikes)
- [ ] Simulate SOAR-style automated responses based on alerts

---

## 💡 Future Plans

Once data is flowing into Elasticsearch, I plan to configure Kibana to:
- Visualize real-time order changes
- Set up alerting (e.g., spike in buy volume)
- Experiment with Elasticsearch SIEM capabilities

---

## 📂 Structure

```bash
.
├── fetch_orderbook.py   # Main script to fetch and filter data
├── config.json          # Binance API and other settings (optional)
├── README.md            # Project overview
