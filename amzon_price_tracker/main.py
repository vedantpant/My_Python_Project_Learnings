import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
import requests
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

response = requests.get("https://appbrewery.github.io/instant_pot/")
amazon_page = response.text
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


port = 587

# soup = BeautifulSoup(amazon_page, "html.parser")
# price = soup.find(name="span", class_="a-offscreen")
# product_name = soup.find(name="span", class_="a-size-large product-title-word-break")
# product_name = product_name.getText()
# product_price = price.getText().split("$")[1]
# price_to_float = float(product_price)

headers = {"Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/128.0.0.0 Safari/537.36"}

header_response = requests.get(url=live_url, headers=headers)
amazon_live_page = header_response.text

soup = BeautifulSoup(amazon_live_page, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
price_to_float = float(price.getText().split("$")[1])
product_name = soup.find(name="span", class_="a-size-large product-title-word-break")
product_name = product_name.getText()

subject = "Amazon Price Alert!"
body = f"{product_name} is available at ${price_to_float}\n\nBuy it here: {live_url}"

# Set up email message
msg = MIMEMultipart()
msg['From'] = os.environ["EMAIL_ADDRESS"]
msg['To'] = os.environ["EMAIL_ADDRESS"]
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain', 'utf-8'))


# Send email if price is below threshold
if price_to_float < 100:
    context = ssl.create_default_context()
    with smtplib.SMTP(os.environ["smtp_address"], port) as server:
        server.starttls(context=context)
        server.login(msg['From'], os.environ["amazon_app_tracker_password"])
        server.sendmail(from_addr=msg["From"],
                        to_addrs=msg['To'],
                        msg=msg.as_string())

    print("Email sent successfully!")