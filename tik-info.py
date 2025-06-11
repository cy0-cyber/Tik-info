#@gqpgqpg on tele | @oeuc on tik
import requests, json
import random
NUM_THREADS = 10


url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser"
params = {'key': "AIzaSyAZqmylIOE4fQmf0pemugc2iBH33rSeMkg"}
payload = json.dumps({"returnSecureToken": True})
headers = {
        'User-Agent': "okhttp/3.12.1",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-client-version': "ReactNative/JsCore/7.8.1/FirebaseCore-web"
    }

# Generate token once
try:
    response = requests.post(url, params=params, data=payload, headers=headers, timeout=10)
    response.raise_for_status()
    response_data = response.json()
    token = response_data.get("idToken")
except requests.RequestException as e:
    print(f"Error generating token : {e}")
    token = None

if token:
    username = input("Enter the username to check: ")

    url = "https://us-central1-tikfans-prod-a3557.cloudfunctions.net/getTikTokUserInfo"
    payload = json.dumps({"data": {"username": username}})
    headers = {
            'User-Agent': "okhttp/3.12.1",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'authorization': f"Bearer {token}"
        }

    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    print(response_data)
