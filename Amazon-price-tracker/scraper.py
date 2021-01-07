import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Sony-Full-frame-Mirrorless-Interchangeable-Lens-ILCE7M3K/dp/B07B45D8WV' 
#item you want to track on amazon^

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[3:]) #adjust according to how expensive the amazon item is 

    print(converted_price)
    print(title.strip())

    if(converted_price<200):  #adjust according to how expensive the amazon item is 
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '') #(your email, generated app password)

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Sony-Full-frame-Mirrorless-Interchangeable-Lens-ILCE7M3K/dp/B07B45D8WV' #link the item you want

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '', #enter email address
        '', #enter email address
        msg
    )
    print('Hey the email has been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)

