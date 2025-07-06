from flask import Flask, render_template, request
import re
from urllib.parse import urlparse
import requests

app = Flask(__name__)


API_KEY = "AIzaSyD6ecD4wtYaOh8GB2YRSJ4anFnNjlZiNaY" 

# ✅ Rule-Based Detection
def is_phishing_url(url):
    parsed = urlparse(url)

    if re.match(r"^(http[s]?://)?\d{1,3}(\.\d{1,3}){3}", url):
        return "🔴 Phishing: IP address used as domain"

    if '@' in url:
        return "🔴 Phishing: URL contains '@' symbol"

    if parsed.hostname and parsed.hostname.count('-') > 3:
        return "🟠 Suspicious: Too many hyphens in domain"

    phishing_keywords = ['secure', 'account', 'webscr', 'login', 'update', 'signin', 'verify', 'banking']
    if any(keyword in url.lower() for keyword in phishing_keywords):
        return "🟠 Suspicious: Contains phishing-related keywords"

    if len(url) > 75:
        return "🟠 Suspicious: URL too long"

    return "🟢 Safe: No suspicious patterns found"

# ✅ Google Safe Browsing API
def check_google_safe_browsing(url, api_key):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    body = {
        "client": {
            "clientId": "phishing-scanner",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(api_url, json=body)
        print("🔍 API Status Code:", response.status_code)
        print("🔍 API Response:", response.text)

        if response.status_code == 200:
            data = response.json()
            if data.get("matches"):
                return "🔴 Google Safe Browsing: This URL is unsafe!"
            else:
                return None
        else:
            return f"⚠️ API Error: {response.status_code}"
    except Exception as e:
        print("⚠️ Exception during API call:", str(e))
        return "⚠️ Exception occurred during API request"

# ✅ Flask Route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        rule_result = is_phishing_url(url)
        api_result = check_google_safe_browsing(url, API_KEY)

        result = rule_result
        if api_result:
            result += f"<br>{api_result}"

    return render_template('index.html', result=result)

# ✅ Run Flask Server
if __name__ == '__main__':
    app.run(debug=True)
