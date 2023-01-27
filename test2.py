import time
from selenium import webdriver
from bs4 import BeautifulSoup

#pic = "https://avatars.cloudflare.steamstatic.com/6d55c5a1aa1042257b53fc6a7d5fbcec1740864f_medium.jpg"
#name = "Webbo"


def find_profile(name, pic):
    url = "https://steamcommunity.com/search/users/#page={page}&text=" + name

    page_src = ""

    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    for i in range(1, 20):
        driver.get(url.format(page=i))
        time.sleep(0.5)
        html = driver.page_source
        if pic in html:
            # print("page you are looking for is " + str(i))
            page_src = html
            break
    driver.quit()

    soup = BeautifulSoup(page_src, 'html.parser')
    a = soup.find("img", src=pic).parent
    p_link = a.get('href')
    return p_link
# print(p_link)
