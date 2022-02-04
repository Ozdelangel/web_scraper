# from turtle import title
import requests
from bs4 import BeautifulSoup

# PRACTICE
# Grabbing the content
# URL = 'https://en.wikipedia.org/wiki/Paul_John_Knowles'
# page = requests.get(URL)

# # print(page.content)

# # using beautiful soup/parsing
# # beautiful soup has an HTML parser

# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup)

# # grabbing the information using find
# results = soup.find(class_='mw-parser-output')
# # print(results.prettify())

# # grab all the h3's

# titles = results.find_all('h3')
# # print(titles)

# second_result = soup.find(class_='mw-headline')
# # print(second_result)

# titles_2 = results.find_all('h3')
# # print(titles_2)

# sections = results.find(id='September')
# # print(sections)

# paragraphs = sections.find_all('p')
# print(paragraphs)

def get_citations_needed_count():
    URL = 'https://en.wikipedia.org/wiki/Paul_John_Knowles'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(title='This claim needs references to reliable sources. (August 2017)')
    count = 0
    # print(results)

    for _ in results:
        count += 1
    print(count)
    return count

get_citations_needed_count()

def get_citations_needed_report():
    URL = 'https://en.wikipedia.org/wiki/Paul_John_Knowles'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(title='This claim needs references to reliable sources. (August 2017)')
    paragraphs = results.find_all('p')
    print(paragraphs)
    

    

get_citations_needed_report()


# titles = results.find_all('h3')
# print(titles)
    

