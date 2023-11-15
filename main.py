from pprint import pprint

import requests
import re

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import csv
info = []
def charlottebusinessbrokers():
    page = load_site('https://www.charlottebusinessbrokers.com/Listings/Listings.php')
    html = page.text
    metaConRE = re.compile("<meta.*?>")
    sourceRE = re.compile('href="Listing_detail.*?"')
    source = sourceRE.findall(html)
    priceRE = re.compile('Business Price</td>.*?</td',re.DOTALL)
    revenueRE = re.compile('Revenue</td>.*?[0-9].*?</td', re.DOTALL)
    cashFlowRE = re.compile('Cash Flow</td>.*?[0-9].*?</td',re.DOTALL)
    nameRE = re.compile('<title>.*?</script>',re.DOTALL)
    info = []
    for each in source:
        url = 'https://www.charlottebusinessbrokers.com/Listings/'+each[6:-1]
        page = load_site(url)
        htmlBus = page.text
        print(page.text)
        name = nameRE.findall(htmlBus)
        name = metaConRE.findall(name[0])
        price = priceRE.findall(htmlBus)
        rev = revenueRE.findall(htmlBus)
        cash = cashFlowRE.findall(htmlBus)
        price = price[0].split(';')[1].split('<')[0]
        rev = rev[0].split('$')[1].split('<')[0]
        cash = cash[0].split('$')[1].split('<')[0]
        name = name[1].split('"')
        price = price.replace(',',"")
        rev = rev.replace(',','')
        rev = rev.strip()
        cash = cash.replace(',','')
        cash = cash.strip()
        info.append([url,name[1],price,rev,cash,'NA'])
    csvAppend(info)

def gottesmanscrape():
    page = load_site('https://gottesman-company.com/opportunities/')
    html = page.text
    print(html)
    sellerSource = re.compile('href="https://gottesman-company.com/active_sellers/.*?"')
    sources = sellerSource.findall(html)
    eachSoFar = []
    for each in sources:
        if each not in eachSoFar:
            eachSoFar.append(each)
    allInfoRE = re.compile(
        """<td class="seller-industry">.*?</td><td class="seller-sales">.*?</td><td class="seller-ebitda">.*?</td>""")
    count = 0
    for each in allInfoRE.findall(html):

        each = re.sub('<.*?>',' ',each)
        each.replace(',','')
        each = each.split('$')
        for every in [1,2]:
            each[every] = each[every].replace('M','')
            each[every] = each[every].replace(' ', '')
            try:
                each[every]=str(float(each[every])*1000000)
            except:
                each[every] ="NA"
        eachSoFar[count]=eachSoFar[count].replace('href','')
        eachSoFar[count] = eachSoFar[count].replace('"','')
        eachSoFar[count] = eachSoFar[count][1:]
        info.append([eachSoFar[count],each[0],"NA",each[1],"NA",each[2]])
        count+=1
    csvWrite(info)
def csvWrite(rows):
    with open('Deals.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['source','Description','price','Revenue','Cash Flow','EBITA'])
        writer.writerows(rows)
def csvAppend(rows):
    with open('Deals.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def greenAndCo():
    driver = webdriver.Chrome()
    driver.get("https://greenandco.biz/search-listings/")
    print(driver.title)
    driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/form/div[3]/input[1]')
    print(driver.current_url)
    driver.close()

def numberOfPages(number,busReg):
        for each in range(1, number):
            page = load_site(f'https://www.bizquest.com/businesses-for-sale/page-{each}/')
            html = page.text
            bus = busReg.findall(html)
            eachSoFar =[]
            for each in bus:
                each = each.split('"')[1]
                if each not in eachSoFar:
                    busPageSearch(each)
                    eachSoFar.append(each)
def busPageSearch(url):
        global info
        page = load_site(url)
        html = page.text
        priceRE = re.compile('''<b class='price'>.*?</b>''')
        revRE = re.compile('''<b class="text-info">Gross Revenue:</b>.*?<hr''', re.DOTALL)
        otherRE = re.compile('''<b class='other-financial'>.*?</b>''')
        CashRE = re.compile('''<b class="text-info">Cash Flow:</b>.*?<hr''', re.DOTALL)
        EBITRE = re.compile('''<b class="text-info">EBITDA:</b>.*?<hr''', re.DOTALL)
        pri = priceRE.findall(html)
        try:
            pri = pri[0].split('$')[1].split('<')[0]
        except:
            pri = "NA"
        print(url)
        rev = revRE.findall(html)
        cash = CashRE.findall(html)
        EBITA = EBITRE.findall(html)
        try:
            rev = otherRE.findall(rev[0])
        except:
            rev ="NA"
        try:
            cash = otherRE.findall(cash[0])
        except:
            cash = "NA"
        try:
            EBITA = otherRE.findall(EBITA[0])
        except:
            EBITA ="NA"
        other = [otherRE.findall(rev[0])if rev.type==list else 'NA', otherRE.findall(cash[0]), otherRE.findall(EBITA[0])]
        otherFin = []
        for each in other:
            try:
                otherFin.append(each[0].split("$")[1].split("<")[0])
            except:
                otherFin.append('NA')
        info.append([url,pri.replace(',',''),otherFin[0].replace(',',''),otherFin[1].replace(',',''),otherFin[2].replace(',','')])


def load_site(url: str)->requests:
    r=requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
    return r

def bizquest():
    page = load_site('https://www.bizquest.com/businesses-for-sale/page-1/')
    html = page
    print(html)
    pageRe = re.compile( '<li class="page-item"><a class="page-link" href="https://www.bizquest.com/businesses-for-sale/.*?>.*?</a></li>')
    numberRe = re.compile("-[0-9]+")
    maxPage = 100
    pages = pageRe.findall(html)
    for each in pages:
        number=numberRe.findall(pages)
        maxPage = int(number[1:]) if (int(number[1:])>maxPage) else maxPage

    busRe = re.compile('href="https://www.bizquest.com/business-for-sale/.*?"')
    numberOfPages(maxPage,busRe)
    bus = busRe.findall(html)
    csvWrite(info)


if __name__ == '__main__':
    gottesmanscrape()
    charlottebusinessbrokers()


