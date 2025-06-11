import requests, json
import random
# threading import removed
NUM_THREADS = 10

r = '\033[0;31m'
g = '\033[0;32m'

telegram_token = '5865928935:AAE5bkG5g-A6mi9jXItcsIaeW0KTRW7orQo'
telegram_chat_id = '5046267899'

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(url, data=json.dumps(payload), headers=headers)
    except requests.RequestException as e:
        print(f"خطأ أثناء إرسال الرسالة إلى تيليجرام: {e}")


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
    if 'userId' in str(response_data):
            print(response_data)
    else:
            print(response_data)
else:
    print("Failed to generate token. Exiting.")
