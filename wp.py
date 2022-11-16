import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse


# page = requests.get("https://www.google.com/search?q=cara+streaming+tv+di+vlc+android")
# soup = BeautifulSoup(page.content, "html.parser")
# links = soup.findAll("a")
# for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
#     d = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0] 
#     domain = urlparse(d).netloc
#     print(domain.replace('www.', ''))

# import requests
# from bs4 import BeautifulSoup
# import re
def wpDetect(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10).text
        if "wp-content" in response:
            writeFile(url, '')
            print(f"{url} [OK] This is a Wordpress website")
        else:
            # writeFile(url, '[NotWP]')
            print(f"{url} [NotWP] This is not a Wordpress website")
    except:
        writeFile(url, 'ERROR')
        print(f"{url}  Connection Error")

# Write File
def writeFile(url, status):
    with open('wordPress_site_detector.html', 'a') as file:
        file.write(f"<a href='{url}/wp-admin' target='_blank'>{url}</a> \t {status}<br>\n")


query = input("Masukkan Link : ")
# query = "cara streaming tv di vlc android"
search = query.replace(' ', '+')
results = 100
url = (f"https://www.google.com/search?q={search}&num={results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
links = soup_link.find_all("a")
no = 1
for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      title = link.find_all('h3')
      if len(title) > 0:
        url = link.get('href').split("?q=")[1].split("&sa=U")[0]
        domain = urlparse(url).netloc
        print("https://"+domain)
        #   print(title[0].getText())
        wpDetect("https://"+domain)


