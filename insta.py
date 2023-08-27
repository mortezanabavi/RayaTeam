import re
import requests
from urllib.parse import urlencode
# Define the constants
user_constant = "@singledevx"
pass_constant = "Morteza##09"
ua_constant = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

# Extract username from user_constant using regex
user = user_constant.replace('@', '')
print(user)

# Get the length of the encoded password
password_encoded = "%23PWD_INSTAGRAM_BROWSER%3a0%3a1628896342%3a" + pass_constant
password_length = len(f"username={user}&enc_password={password_encoded}")

# Set the headers
headers = {
    "User-Agent": ua_constant,
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "*/*",
    "Referer": "https://www.instagram.com/",
    "X-IG-App-ID": "936619743392459",
    "X-IG-WWW-Claim": "0",
    "X-Instagram-AJAX": "c1dcf20d99d7",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-CSRFToken": "missing",
    "Host": "www.instagram.com",
    "Connection": "Keep-Alive",
    "Content-Length": str(password_length),
}

# Create the data payload
data_payload = {
    "username": user,
    "enc_password": password_encoded,
}

# Make the POST request
response = requests.post(
    "https://www.instagram.com/accounts/login/ajax/",
    data=data_payload,
    headers=headers
)

# Print the response
print(response.text)