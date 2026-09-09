# Flight Deal Finder & Automation Tracker

An automated Python application that monitors flight prices between a designated home airport (default: `IAH`) and specified global destinations. The app tracks budget thresholds using a Google Sheets backend, queries live price data using the Google Flights engine, and instantly broadcasts alert notifications via WhatsApp when a deal is detected.

## Features
* **Google Sheets Backend:** Utilizes the **Sheety API** to pull target destinations and baseline budget limits, updating them dynamically when lower prices are found.
* **Live Flight Monitoring:** Leverages the **SerpApi (Google Flights Engine)** to dynamically scan for the cheapest outbound and return flights within a 6-month window.
* **Instant WhatsApp Alerts:** Integrates the **Twilio API** to dispatch real-time flight details directly to your phone when a price drops below your threshold.
* **Aggressive Cache Optimization:** Implements `requests_cache` to minimize redundant external API calls, whitelisting critical data updates while caching flight queries for 1 hour.

---

## Architecture & Tech Stack

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

## Setup & Installation

### 1. Prerequisites
Clone the repository to your local machine:
```bash
git clone https://github.com/ItzNotCheetah/flight-deals-project.git
cd flight-deal-finder
```
Install the Required Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Variables
Create a file named `.env` in the root directory of your project and populate it with your credentials:

```env
# Sheety API Configuration
SHEETY_TOKEN=your_sheety_bearer_token

# SerpApi Configuration
SERP_API_KEY=your_serpapi_private_key

# Twilio API Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM=+1XXXXXXXXXX
TWILIO_WHATSAPP_TO=+1XXXXXXXXXX
```

### 3. Google Sheet Setup
Make a copy of this google sheet and set it up using Sheety api: https://docs.google.com/spreadsheets/d/1JCruIebyQvOpOMX_y3TkwOxKODr3H9L6hwXq0Xhd3pI/edit?usp=sharing
