from bs4 import BeautifulSoup
import requests

contents = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
soup = BeautifulSoup(contents, "html.parser")

movies = soup.find_all("h3", class_="title")
movies_list = [i.get_text() for i in movies][::-1]
print(movies_list)
with open("top_movies.txt", "w") as file:
    for i in movies_list:
        file.write(f"{i}\n")