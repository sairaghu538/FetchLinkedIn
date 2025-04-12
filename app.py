from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Proxycurl API setup
API_KEY = "mLdfG--VXEWPXG2Sb9nDeQ"  # Directly using the API key for testing
API_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_linkedin', methods=['GET'])
def fetch_linkedin():
    linkedin_url = request.args.get('url')
    if not linkedin_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    try:
        response = requests.get(API_ENDPOINT, params={'url': linkedin_url}, headers=HEADERS)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
