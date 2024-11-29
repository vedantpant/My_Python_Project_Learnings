from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

items_and_prices = {}

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

time_out = time.time() + 5
five_minutes = time.time() + 60 * 5  # 5 minutes from now

while True:
    cookie.click()

    if time.time() > time_out:
        print("Taking a break for 5 seconds...")
        time.sleep(5)  # Pause for 5 seconds

        all_prices = driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_prices = []

        for prices in all_prices:
            price_element = prices.text
            if price_element != "":
                cost = price_element.split("-")[1].strip().replace(",", "")
                item_prices.append(cost)

        items_and_prices = {item_id: item_price for (item_id, item_price) in zip(item_ids, item_prices)}
        print(items_and_prices)

        # cookie count
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        cookies = int(money)

        # most expensive items
        # Collect affordable items with their prices (use item names as keys, prices as values)
        affordable_items = {}
        for name, price in items_and_prices.items():
            if int(price) <= cookies:  # Include items that can be purchased with available cookies
                affordable_items[name] = int(price)

                # Find all affordable items and click each one
                for item_name in affordable_items:
                    print(f"Purchasing {item_name} for {affordable_items[item_name]} cookies.")
                    try:
                        select_item = driver.find_element(By.ID, value=item_name)
                        print(f"Clicking on {select_item.text}")
                        select_item.click()
                    except Exception as e:
                        print(f"Could not click {item_name}: {e}")
        # Reset the timeout to take a break after the next cycle
        time_out = time.time() + 5

        if time.time() > five_minutes:
            cookie_per_second = driver.find_element(By.ID, value="cps")
            print(f"cookie per second : {cookie_per_second.text}")
            driver.quit()


