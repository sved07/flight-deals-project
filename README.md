# Flight Deal Finder & Automation Tracker

An automated Python application that monitors flight prices between a designated home airport (default: `IAH`) and specified global destinations. The app tracks budget thresholds using a Google Sheets backend, queries live price data using the Google Flights engine, and instantly broadcasts alert notifications via WhatsApp when a deal is detected.

## 🚀 Features
* **Google Sheets Backend:** Utilizes the **Sheety API** to pull target destinations and baseline budget limits, updating them dynamically when lower prices are found.
* **Live Flight Monitoring:** Leverages the **SerpApi (Google Flights Engine)** to dynamically scan for the cheapest outbound and return flights within a 6-month window.
* **Instant WhatsApp Alerts:** Integrates the **Twilio API** to dispatch real-time flight details directly to your phone when a price drops below your threshold.
* **Aggressive Cache Optimization:** Implements `requests_cache` to minimize redundant external API calls, whitelisting critical data updates while caching flight queries for 1 hour.

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.x
* **APIs Used:** * SerpApi (Google Flights Engine)
    * Sheety API (Google Sheets integration)
    * Twilio API (WhatsApp Business Gateway)
* **Key Packages:** `requests`, `requests_cache`, `twilio`, `python-dotenv`

### Project Structure
* `main.py` - Core execution loop managing application orchestration.
* `data_manager.py` - Manages read/write REST operations with the Sheety API.
* `flight_search.py` - Structured interface for querying SerpApi.
* `flight_data.py` - Utility classes and parser to extract and compare the lowest fares.
* `notification_manager.py` - Wraps the Twilio client configuration for alert dispatches.

---

