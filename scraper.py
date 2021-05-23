import requests
from bs4 import BeautifulSoup
import string
import os


def save_article(furl):
    # print("********************************")
    art_url = 'https://www.nature.com' + str(furl)
    print('Article URL:',  art_url)
    sa_r = requests.get(art_url)
    sa_soup = BeautifulSoup(sa_r.content, 'html.parser')
    title = sa_soup.find('h1', {'class': 'article-item__title'}).text.strip()
    print("Title:", title)
    sa_text = ""
    # if sa_soup.find('div', {'class': 'article__body'}).text.strip() != "":
    try:
        sa_text = sa_soup.find('div', {'class': 'article__body'}).text.strip()
    except AttributeError:
        pass
    # if sa_soup.find('div', {'class': 'article-item__body'}).text.strip() != "":
    try:
        sa_text = sa_soup.find('div', {'class': 'article-item__body'}).text.strip()
    except AttributeError:
        pass
    print("Text:", sa_text)
    temp = []
    for c in title:
        if c not in string.punctuation:
            temp.append(c)
    temp_2 = ['_' if c == ' ' else c for c in temp]
    # [num if num >= 0 else 0 for num in old_list]
    file_name = "".join(temp_2)
    fname = file_name + ".txt"
    file = open(fname, 'wb')
    file.write(bytes(sa_text, encoding='utf-8'))
    file.close()
    # saved_articles.append(file_name)


# saved_articles = []  # tu będziemy zapisywać listę artykułów
num_pages = int(input())  # z ilu stron będziemy ściągać dane
art_type = input()  # jakiego typu artykułu szukamy

# url = 'https://www.nature.com/nature/articles'  # stąd ciągniemy dane
for i in range(num_pages):
    dirname = 'Page_' + str(i + 1)
    if os.access(dirname, os.F_OK) is not True:
        os.mkdir(dirname)
    os.chdir(dirname)
    print("jesteśmy teraz w:", os.getcwd())
    url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page=' + str(i + 1)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        article_url = article.find('a').get('href')
        # article_title = article.find('a').text
        # print(article_title)
        article_type = article.find('span', {'data-test': 'article.type'}).text.strip()
        # print(article.find('span', {'data-test': 'article.type'}).text.strip())
        print(article_type)
        print(type(article_type))
        print("Len:", len(article_type))
        print(article_url)
        # if str(article.find('span', {'data-test': 'article.type'}).text) == "News":
        if article_type == art_type:
            save_article(article_url)

    os.chdir('..')

# print(saved_articles)

# ##################################
# Tu Stage 3/5
# inp_url = input()
# # inp_url = 'https://www.facebook.com/'
#
# r = requests.get(inp_url)
#
# if r.status_code == 200:
#     page_content = r.content
#     file = open('source.html', 'wb')
#     file.write(page_content)
#     file.close()
#     print("Content saved.")
# else:
#     print("The URL returned", r.status_code)


# url = input("Input the URL:\n")
# r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# soup = BeautifulSoup(r.content, "html.parser")
# try:
#     title = soup.find("title").text
#     description = soup.find("div", class_="summary_text").text.strip()
#     film_dict = {"title": title, "description": description}
#     print(film_dict)
# except:
#     print("Invalid movie page!")
