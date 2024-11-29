from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
upvote_list = []
for article in articles:
    article_text = article.get_text()
    article_link = article.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvote = soup.find_all(name="span", class_="score")
for upvote in article_upvote:
    up = int(upvote.get_text().split()[0])
    upvote_list.append(up)

print(upvote_list)
# print(article_texts)
# print(article_links)

largest_upvote = max(upvote_list)
largest_index = upvote_list.index(largest_upvote)

print(article_texts[largest_index])
print(article_links[largest_index])












































# import lxml
#
# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# #
# # print(soup.a)
# # print(soup.li)
#
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
#
# heading = soup.findAll(name="h1", id="name")
# print(heading)
#
# class_heading = soup.find(name="h3", class_="heading")
# print(class_heading.getText("class"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# print(soup.select(".heading"))

