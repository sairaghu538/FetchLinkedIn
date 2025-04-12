from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Your Proxycurl API key and endpoint
API_KEY = os.getenv('PROXY_URL_LINKEDIN')  # Make sure the API key is stored in .env
API_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

# Route to serve the main page with form
@app.route('/')
def home():
    return render_template('index.html')  # Renders the initial page with input form

# Route to fetch LinkedIn profile
@app.route('/fetch_linkedin', methods=['GET'])
def fetch_linkedin():
    linkedin_url = request.args.get('url')
    if not linkedin_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    # Fetch LinkedIn profile data from Proxycurl API
    response = requests.get(API_ENDPOINT, params={'url': linkedin_url}, headers=HEADERS)
    
    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()  # Convert the API response to JSON
        # Render the profile data in an HTML page (profile.html)
        return render_template('profile.html', data=data)
    else:
        return jsonify({"error": "Error fetching data from Proxycurl"}), 500

if __name__ == '__main__':
    app.run(debug=True)
