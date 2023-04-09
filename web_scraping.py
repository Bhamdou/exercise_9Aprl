import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Fetch the web page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the text from the 'p' tags
    paragraphs = soup.find_all("p")
    text = " ".join([paragraph.get_text() for paragraph in paragraphs])

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)

    # Display the sentiment scores
    print(f"Polarity: {analysis.sentiment.polarity}")
    print(f"Subjectivity: {analysis.sentiment.subjectivity}")

else:
    print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")
