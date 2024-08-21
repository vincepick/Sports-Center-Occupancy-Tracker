from bs4 import BeautifulSoup
import requests

url = 'https://sport.wp.st-andrews.ac.uk/'
# url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue';

# page=requests.get(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page = requests.get(url, headers=headers)

# HTML parser
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)