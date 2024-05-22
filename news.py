import requests
from bs4 import BeautifulSoup

def news_all_today():
  try:
    response = requests.get("https://www.indiatoday.in/india")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_class = soup.find_all('p')
        news_classlist = [p.get_text() for p in news_class]
        if news_classlist:
               return news_classlist
        else:
           net_error = "Please Check your network connection"
           return net_error
    else:
        net_error = "Please Check your network connection"
        return net_error
  except Exception as fr:
      pass
