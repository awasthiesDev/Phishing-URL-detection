from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import re
from urllib.parse import urlparse
import tldextract

app = Flask(__name__)

# Load trained model
model = pickle.load(open('phishing_random_forest_model.pkl', 'rb'))

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['hostname_length'] = len(urlparse(url).hostname)
    features['num_dots'] = url.count('.')
    features['num_hyphens'] = url.count('-')
    features['num_slashes'] = url.count('/')
    features['num_at'] = url.count('@')
    features['num_question_marks'] = url.count('?')
    features['num_equals'] = url.count('=')
    features['num_ampersands'] = url.count('&')
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['num_special_chars'] = sum(c in "!#$%^&*()+=[]" for c in url)
    features['has_ip'] = 1 if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", urlparse(url).hostname or "") else 0
    ext = tldextract.extract(url)
    features['subdomain_length'] = len(ext.subdomain)
    features['tld_length'] = len(ext.suffix)
    return features

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url', '')

    # Extract features
    features = extract_features(url)
    df_features = pd.DataFrame([features])

    # Predict probability
    probability = model.predict_proba(df_features)[0][1]  # Probability of being legitimate

    legitimacy_percentage = round(probability * 100, 2)
    safety_status = f"{legitimacy_percentage}% safe" if legitimacy_percentage >= 50 else f"{100 - legitimacy_percentage}% unsafe"

    return jsonify({'legitimacy_percentage': legitimacy_percentage, 'status': safety_status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
