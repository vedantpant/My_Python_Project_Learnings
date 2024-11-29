import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

movie_list = []

response = requests.get(URL)
empire_content = response.text

soup = BeautifulSoup(empire_content, "html.parser")
list_of_movies = soup.find_all(name="h3", class_="title")
for movie in list_of_movies:
    movie_list.append(movie.getText())

original_movie_list = movie_list[::-1]
print(original_movie_list)

with open("movies.txt", "w+", encoding="utf-8") as file:
    file.writelines("\n" .join(original_movie_list))

print("File written successfully!!")

file.close()
