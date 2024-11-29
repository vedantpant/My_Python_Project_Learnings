import requests
from twilio.rest import Client

STOCK_NAME = "RELIANCE.BSE"
COMPANY_NAME = "Reliance Industries Ltd"
api_key = "6VK94R2QBAKSOC8Z"
news_api_key = "023bb7d072d649c28cef99c9086e371f"

account_sid = "ACc445136bd6822ec19de0a37f32bafeee"
auth_token = "8b19b53a53cca93afac31850550c8ab3"

Parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    # "function": "SYMBOL_SEARCH",
    "outputsize": "compact",
    # "keywords": "reliance",
    "apikey": api_key
}

news_parameter = {
    "q": COMPANY_NAME,
    "from": "2024-07-02",
    "apikey": news_api_key,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then
# print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list
# comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive
#  difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price
#  the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=Parameters)
response.raise_for_status()

data = response.json()

time_series_data = data["Time Series (Daily)"]
time_series_list = [value['4. close'] for (key, value) in time_series_data.items()]
yesterday_stock_price = time_series_list[0]
day_before_yesterday_stock_price = time_series_list[1]
positive_difference = abs(float(yesterday_stock_price) - float(day_before_yesterday_stock_price))
percentage_difference = (positive_difference / float(yesterday_stock_price)) * 100
print(percentage_difference)

if percentage_difference > 0.5:
    print("Get News")
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_response.raise_for_status()

    data = news_response.json()
    news_articles = data["articles"]
    top_three_article = news_articles[:3]
    new_article_data = [(article["title"], article["description"]) for article in top_three_article]

    client = Client(account_sid, auth_token)

    message1 = client.messages.create(
        body=f"{new_article_data[0]}",
        from_="whatsapp:+14155238886",
        to="whatsapp:+917982603081",
    )

    message2 = client.messages.create(
        body=f"{new_article_data[1]}",
        from_="whatsapp:+14155238886",
        to="whatsapp:+917982603081",
    )

    message3 = client.messages.create(
        body=f"{new_article_data[2]}",
        from_="whatsapp:+14155238886",
        to="whatsapp:+917982603081",
    )

    print(message1.status)
    print(message1.body)
    print(message2.status)
    print(message2.body)
    print(message3.status)
    print(message3.body)

else:
    print(f"percentage difference:{percentage_difference}")


# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near 
 the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of 
March 31st, near the height of the coronavirus market crash.
"""
