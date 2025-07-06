# 🛡️ Phishing Link Scanner 🔍

A simple yet powerful cybersecurity tool built in Python to scan and detect potential phishing URLs. This tool analyzes links based on domain structure, IP address usage, suspicious keywords, and optionally integrates with VirusTotal for further verification. Comes with a clean front-end using both **Streamlit** (quick setup) and **Flask** (custom web UI).

---

## 📦 Features

- ✅ URL validation
- ⚠️ Phishing indicator detection (keywords, IP-based URLs)
- 🔐 Trusted domain cross-check
- 🌐 Web interfaces: Streamlit & Flask versions
- 📊 Export scan results as CSV
- 🔌 Optional: VirusTotal threat intelligence integration

---


## 🚀 How to Run the Project (after cloning)

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/Arun-sangeeth/Brainwave_matrix_intern.git
cd phishing_link_scanner





🧪 Step 2: Create Virtual Environment (Optional but Recommended)

    python -m venv venv
    source venv/bin/activate     # On Windows: venv\Scripts\activate




📦 Step 3: Install Dependencies

    pip install -r requirements.txt



## 💻 Run the Flask App**

```bash
python app.py


-----------------------------------------------------------------------------------------

🧠 Optional: Enable VirusTotal Integration
Get an API key from https://www.virustotal.com

Create a .env file or directly add the key in your utils.py or scanner.py

Use virustotal-python package to enhance scans

-----

🤝 Contributing
Pull requests and issues are welcome! If you find bugs or want to add features, feel free to fork the repo and contribute.

-----

📜 License
This project is open-source and available under the MIT License.

🙌 Author
Arun Sangeeth G C
📍 Kozhikode, Kerala
