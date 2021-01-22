from bs4 import BeautifulSoup
import re
from urllib import request
import os
import urllib
import time
import xlwt
import selenium
# encoding=utf8


base_url = "https://github.com"


def main():
    language = ['Java', 'C++', 'Python']
    func = ['%E6%8E%92%E5%BA%8F', '%E5%8A%A0%E5%AF%86'] # 排序 加密
    for lang in language:
        for each in func:
            url = "https://github.com/search?l=" + lang + "&q=" + each +"&type=Repositories"
        # url = "https://github.com/search?l=Java&q=%E6%8E%92%E5%BA%8F&type=Repositories"
            addr = get_repositories_addr(url)
            git_addr = get_git_addr(addr)
            print("cloning language: " + lang + " function: " + each  + " address: " + git_addr[0] )
            os.system("git clone "+ git_addr[0])
            # for add in git_addr:
            #     os.system("git clone " + add)


def get_git_addr(addresses):
    addr = []
    for address in addresses:
        page = BeautifulSoup(askURL(address), 'html.parser')
        git_addr = page.find_all(name="input", attrs={"class": "form-control input-monospace input-sm bg-gray-light"})[0]
        addr.append(git_addr.attrs['aria-label'])
    return addr


def get_repositories_addr(url):
    page = BeautifulSoup(askURL(url), 'html.parser')
    all_address = page.find_all(name="a", attrs={"class": "v-align-middle"})
    hrefs = []
    for addr in all_address:
        hrefs.append(base_url + addr.attrs['href'])
    return hrefs


# 获取页面信息函数
def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36 "
    }
    req = request.Request(url, headers=header)
    response = request.urlopen(req)
    html = response.read().decode()
    return html


if __name__ == "__main__":
    main()
