# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup


# Define the URL of the website to scrape
url = 'https://example.com'

# Send an HTTP request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print(f"Successfully accessed {url}")
else:
    print(f"Failed to access {url}")

# Parse the HTML content of the web page
soup = BeautifulSoup(response.content, 'html.parser')

# Find and print the title of the web page
title = soup.find('title').get_text()
print(f"Title of the web page: {title}")

# Find and print all paragraph texts on the web page
paragraphs = soup.find_all('p')
print("Paragraph texts on the web page:")
for paragraph in paragraphs:
    print(paragraph.get_text())
