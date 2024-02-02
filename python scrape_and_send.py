import telebot
import requests
from bs4 import BeautifulSoup 
import time

# Initialize the Telegram bot
bot_token = "6594009854:AAEtGz5rsjM9arC19BWW7qGobI4NeH_Z7Yo"
bot = telebot.TeleBot(bot_token)

def scrape_data():
    url = 'https://www.thecrazytourist.com/15-best-places-visit-ethiopia/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("figure")
    items2 = soup.find_all("h2")
    data = []
    i = 0
    while items[i] != items[14]:
        photo_url = items[i].find("img")["src"]
        text = items2[i].text.strip()
        data.append((photo_url, text))
        i += 1
    return data

def send_data_to_telegram_channel():
    chat_id = "2006596184"
    data = scrape_data()
    for image_url, text in data:
        time.sleep(5)
        bot.send_photo(chat_id, image_url, caption=text)

if __name__ == "__main__":
    send_data_to_telegram_channel()