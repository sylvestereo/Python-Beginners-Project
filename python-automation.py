import requests
import schedule
import time

mobile_number = '+2349074694130'

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Na sylvester, I just wan say you no fit find love and I be agba coder😂😂',
        'key': 'textbelt',
    })
    print(resp.json())

# schedule.every().day.at('13:30').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)