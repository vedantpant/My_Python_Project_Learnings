from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# cent_price = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"full_price = {dollar_price}.{cent_price}.")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# go_button = driver.find_element(By.ID, value="submit")
# print(go_button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# search_bar = driver.find_elements(By.CSS_SELECTOR, value=".do-not-print")
# for _ in search_bar:
#     print(_.text)
time_list = []
name_list = []
menu = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
for item in menu:
    list_of_time = item.find_elements(By.TAG_NAME, value="time")
    for time in list_of_time:
        time_ = time.text
        time_list.append(time_)
    list_of_event_name = item.find_elements(By.TAG_NAME, value='a')
    for name in list_of_event_name:
        name_ = name.text
        name_list.append(name_)

indexed_dict = {i+1: {time_list: name_list} for i, (time_list, name_list) in enumerate(zip(time_list, name_list))}
print(indexed_dict)





# driver.close()
# driver.quit()
