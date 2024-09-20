import time
import requests

# Configuration du bot Telegram
# Replace 'YOUR_TOKEN' with your actual Telegram bot token
TOKEN = 'YOUR_TOKEN'
# Replace 'YOUR_CHAT_ID' with your actual chat ID
CHAT_ID = 'YOUR_CHAT_ID'

# Fonction pour envoyer un message à Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error: {response.status_code}")

def detect_wake_from_sleep():
    last_time = time.time()  
    threshold = 60  # If the time jump is greater than 1 minute

    print("Surveillance de la sortie de veille activée...")

    while True:
        current_time = time.time()
        if current_time - last_time > threshold:
            send_telegram_message("Le PC est sorti de veille !")
            print("PC sorti de veille")
        
        last_time = current_time
        time.sleep(10)  

if __name__ == '__main__':
    try:
        detect_wake_from_sleep()
    except KeyboardInterrupt:
        print("Surveillance arrêtée.")
