import requests
from bs4 import BeautifulSoup

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def main():
    preurl = "https://"
    namerul = input("input blog's name:  ")
    page = input("input the page:  ")
    if (page == 1):
        surl = ".github.io/page/" + page + '/'
    else:
        surl = ".github.io"
    url = preurl + namerul + surl
    html = gethtmltext(url)
    soup = BeautifulSoup(html, "html.parser")
    f = open('hexo', 'w')
    for link in soup.find_all('a', class_ = "post-title-link"):
        hrefs = url + link.get('href')
        newurl = url + link.get('href')
        newhtml = gethtmltext(newurl)
        newsoup = BeautifulSoup(newhtml, "html.parser")
        titles = newsoup.find('h2', class_="post-title").get_text()
        bodys = newsoup.find('div', class_ = "post-body").get_text()
        print(titles)
        f.writelines("标题:  " + titles + '\n')
        f.writelines("连接:  " + hrefs + '\n')
        f.writelines(bodys)
        f.write("--------------------------------------" + '\n' + '\n' + '\n' + '\n')


main()