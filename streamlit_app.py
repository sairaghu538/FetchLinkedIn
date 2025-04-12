# streamlit_app.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Proxycurl API
API_KEY = os.getenv('PROXY_URL_LINKEDIN')
API_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

# Streamlit App
st.set_page_config(page_title="LinkedIn Profile Fetcher", layout="centered")
st.title("🔗 LinkedIn Profile Fetcher")

st.markdown("Enter a public LinkedIn profile URL to fetch details using the Proxycurl API.")

# Input for LinkedIn Profile URL
linkedin_url = st.text_input("🔗 LinkedIn Profile URL", placeholder="https://www.linkedin.com/in/username/")

# Fetch data when user clicks button
if st.button("🚀 Fetch Profile"):
    if not linkedin_url:
        st.warning("Please enter a LinkedIn URL.")
    elif not API_KEY:
        st.error("API key not found. Please set `PROXY_URL_LINKEDIN` in your environment.")
    else:
        with st.spinner("Fetching profile data..."):
            response = requests.get(API_ENDPOINT, params={"url": linkedin_url}, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                st.success("Profile fetched successfully!")
                st.subheader("📄 Raw JSON Output:")
                st.json(data)
            else:
                st.error(f"Failed to fetch profile. Status Code: {response.status_code}")
                try:
                    st.json(response.json())
                except Exception:
                    pass
