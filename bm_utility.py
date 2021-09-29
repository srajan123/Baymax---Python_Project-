from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import webbrowser
from requests import get

def sanitize(text):
    text = re.sub(r'[^\w\s]', '', text)
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word.lower() in stopwords.words()]
    temp = set()
    fquery = [ele for ele in tokens_without_sw if not (ele in temp or temp.add(ele))]
    fquery = " ".join(fquery)
    return fquery

def search_google(query):
    url = "https://www.google.com.tr/search?q={}".format(query)
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)


