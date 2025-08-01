import requests
import json
import os
from datetime import datetime, timedelta

# Cache file path
CACHE_FILE = os.path.join(os.path.dirname(__file__), 'exchange_rate_cache.json')
# Cache expiration time in hours
CACHE_EXPIRATION_HOURS = 24

def _load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def _save_cache(data):
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)

def get_usd_to_jpy_rate():
    cache = _load_cache()
    current_time = datetime.now()

    # Check if cache is valid
    if 'rate' in cache and 'timestamp' in cache:
        cached_time = datetime.fromisoformat(cache['timestamp'])
        if current_time - cached_time < timedelta(hours=CACHE_EXPIRATION_HOURS):
            return cache['rate']

    # Fetch new rate if cache is invalid or not present
    try:
        response = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        usd_data = data.get('usd', {})
        jpy_rate = usd_data.get('jpy')

        if jpy_rate:
            new_cache = {
                'rate': jpy_rate,
                'timestamp': current_time.isoformat()
            }
            _save_cache(new_cache)
            return jpy_rate
        else:
            print("Error: JPY rate not found in API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from exchange rate API.")
        return None

if __name__ == '__main__':
    rate = get_usd_to_jpy_rate()
    if rate:
        print(f"Current USD to JPY rate: {rate}")
    else:
        print("Failed to get USD to JPY rate.")
