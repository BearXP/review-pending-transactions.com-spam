from requests import Session
import random
import json
import time
import schedule

# Load in my passwords and config file
with open("passwords.txt", "r") as f:
    passwords = f.readlines()
with open("config.json", "r") as f:
    conf = json.load(f)
# Shuffle the passwords, and remove the linebreaks.
random.shuffle(passwords)
passwords = [text.strip() for text in passwords]

# Schedule the password
def login_and_post_password():
    global passwords
    global conf
    with Session() as s:
        # Collect a cookie
        headers = conf["homepage"]
        resp = s.get(
            url="https://review-pending-transaction.com/",
            headers=headers,
        )
        print(" login resp: ")
        print(resp.content)
        time.sleep(4)
        # Send the details
        params = {
            "currentpage": "login",
            "username": random.randint(100000000, 999999999),
            "password": passwords.pop(),
        }
        headers = s.headers.copy()
        headers = headers.update(conf["posting"])
        resp = s.post(
            url="https://review-pending-transaction.com/core/actions.php?action=send_data",
            headers=headers,
            data=params,
        )
        print(params)


login_and_post_password()

schedule.every(4).seconds.do(login_and_post_password)

while True:
    schedule.run_pending()
    time.sleep(1)
