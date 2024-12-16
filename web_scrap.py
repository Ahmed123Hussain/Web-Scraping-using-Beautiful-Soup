import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_Hindi_films"

#HTTP requests GET function to get the page
page = requests.get(url)

#Beautiful soup takes 2 params page.content for content of the page and html  parser to get html document structure as object
soap = BeautifulSoup(page.content, "html.parser")
#print(soap)
# Extract all tables
#read_html function finds all tables in from the string converted soap object
#soap object contains the html structure 
tables = pd.read_html(str(soap))  # Reads all tables from the HTML content
#req. info
print(tables[0])
#convert dataframe to csv file or excel file
#pd.to_excel("data.xlsx)
pd.to_csv("hindi_films_data.csv", index = False)
