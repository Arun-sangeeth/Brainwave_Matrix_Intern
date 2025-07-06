import requests

API_KEY = "YOUR_KEY_HERE"
url_to_check = "http://malicious-site.com"

api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

body = {
    "client": {
        "clientId": "test-client",
        "clientVersion": "1.0"
    },
    "threatInfo": {
        "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
        "platformTypes": ["ANY_PLATFORM"],
        "threatEntryTypes": ["URL"],
        "threatEntries": [{"url": url_to_check}]
    }
}

response = requests.post(api_url, json=body)
print("Status Code:", response.status_code)
print("Response:", response.text)
