import requests 
from bs4 import BeautifulSoup
from random import randint


def response_news():
    response = requests.get("https://ixbt.games/news/").text

    soup = BeautifulSoup(response, "lxml")

    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    artice_text = soup.find_all("div", class_="d-flex d-sm-block my-2")

    article_index = randint(0, len(article_title))

    print((article_title[article_index].text).strip())
    print((article_author[article_index].text).strip())
    print((artice_text[article_index].text).strip())


def response_reviews():
    response = requests.get("https://ixbt.games/reviews/").text

    soup = BeautifulSoup(response, "lxml")

    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    artice_text = soup.find_all("div", class_="d-flex d-sm-block my-2")

    article_index = randint(0, len(article_title))

    print((article_title[article_index].text).strip())
    print((article_author[article_index].text).strip())
    print((artice_text[article_index].text).strip())


def response_results():
    response = requests.get("https://ixbt.games/results/").text

    soup = BeautifulSoup(response, "lxml")

    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    artice_text = soup.find_all("div", class_="d-flex d-sm-block my-2")

    article_index = randint(0, len(article_title))

    print((article_title[article_index].text).strip())
    print((article_author[article_index].text).strip())
    print((artice_text[article_index].text).strip())


def response_instruments():
    response = requests.get("https://ixbt.games/tools/").text

    soup = BeautifulSoup(response, "lxml")

    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    artice_text = soup.find_all("div", class_="d-flex d-sm-block my-2")

    article_index = randint(0, len(article_title))

    print((article_title[article_index].text).strip())
    print((article_author[article_index].text).strip())
    print((artice_text[article_index].text).strip())



choice = input("Какая категория вас интересует: ")

match choice.lower():
    case "новости":
        response_news()
    case "обзоры":
        response_reviews()
    case "итоги":
        response_results()
    case "инструментарий":
        response_instruments()
