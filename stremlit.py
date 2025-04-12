import streamlit as st
import requests

# Streamlit app for interacting with the Flask API
st.title('LinkedIn Profile Fetcher')

# Input field for LinkedIn profile URL
linkedin_url = st.text_input("Enter LinkedIn profile URL", '')

if st.button('Fetch Profile'):
    if linkedin_url:
        # Call Flask API to fetch LinkedIn profile data
        api_url = f'http://127.0.0.1:5000/fetch_linkedin?url={linkedin_url}'
        
        try:
            response = requests.get(api_url)
            data = response.json()

            # Display the profile data
            if "error" in data:
                st.error(f"Error: {data['error']}")
            else:
                st.subheader(f"Name: {data['first_name']} {data['last_name']}")
                st.write(f"Headline: {data['headline']}")
                st.write(f"Location: {data['location']}")
                st.write("**Education**:")
                for edu in data.get('education', []):
                    st.write(f"- {edu['degree']} from {edu['school']}")
                st.write("**Work Experience**:")
                for work in data.get('work_experience', []):
                    st.write(f"- {work['title']} at {work['company']}")

        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")
    else:
        st.warning("Please enter a LinkedIn URL.")
