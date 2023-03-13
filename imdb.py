import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

base_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

page = requests.get(base_url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

# list to store data
imdb = []

# finding all movie titles html elements
imdb_list = soup.find_all('td', class_='titleColumn')

# extracting the movie titles
for val in imdb_list:
    title = val.find('a', href=True).text
    imdb.append(title)

# write to csv
imdb_file = open('imdb_csv.csv', 'w', encoding='utf-8', newline='')
ti = 'Title\n'
imdb_file.write(ti)
for a in imdb:
    imdb_file.write(a)
    imdb_file.write('\n')
imdb_file.close()