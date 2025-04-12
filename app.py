# backend.py
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)

# Proxycurl API Setup
API_KEY = 'mLdfG--VXEWPXG2Sb9nDeQ'
API_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

@app.route('/fetch_linkedin', methods=['GET'])
def fetch_linkedin():
    linkedin_url = request.args.get('url')
    if not linkedin_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
        

    if not API_KEY:
        return jsonify({"error": "Missing API key"}), 401

    try:
        response = requests.get(API_ENDPOINT, params={'url': linkedin_url}, headers=HEADERS)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
