# FetchLinkedIn

# FetchLinkedIn

 FetchLinkedIn
A sleek web app that fetches and displays LinkedIn profile data from a URL.

![🔗 FetchLinkedIn - visual selection](https://github.com/user-attachments/assets/1a63cbd8-a3a5-49e3-99e0-3625773ef69c)

🚀 Overview
FetchLinkedIn is a simple yet powerful web application that allows users to input a LinkedIn profile URL and fetch detailed profile information using the Proxycurl API. It's built with Flask and offers a clean UI to view professional data at a glance.

![🔗 FetchLinkedIn - visual selection (1)](https://github.com/user-attachments/assets/ea363105-a356-4719-96ec-8c237b2d3171)


✨ Features
🔍 Enter a LinkedIn profile URL to fetch real-time data

👤 Displays:

Profile picture

Name & headline

Experience & education

Accomplishments

🧩 Toggle project descriptions for a better viewing experience

![🔗 FetchLinkedIn - visual selection (2)](https://github.com/user-attachments/assets/7a71acc0-e195-461f-ac1d-db5ca419f2dd)



📦 Prerequisites
Python 3.x
Flask
requests library
Proxycurl API Key (for LinkedIn scraping)

![🔗 FetchLinkedIn - visual selection (3)](https://github.com/user-attachments/assets/75e54e8e-e25e-40b9-b0f1-ab26d993a013)


⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/sairaghu538/FetchLinkedIn.git cd FetchLinkedIn 

2. Install dependencies:

pip install -r requirements.txt 

3. Run the Flask server:

py backend.py 



🌐 API Endpoint

GET

http://127.0.0.1:5000/fetch_linkedin?url=<linkedin_profile_url> 

Replace <linkedin_profile_url> with the full LinkedIn URL of the profile you want to fetch.
