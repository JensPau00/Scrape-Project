from pprint import pprint

import requests
import re
import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import csv
ibbaEntry =[]
info = []
Entry = {}
def csvWrite(rows):
    with open('Deals.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['source', 'Description', 'price', 'Revenue', 'Cash Flow', 'EBITA'])
        writer.writerows(rows)

def csvAppend(rows):
    with open('Deals.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def csvWriteBroker(rows):
    with open('Brokers.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Telephone', 'Company', 'Website', 'Email'])

def csvAppendBroker(rows):
    with open('Brokers.csv.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def axial995():
    page = load_site('https://www.axial.net/forum/companies/business-brokers/')
    soup = BeautifulSoup(page.text, 'html.parser')
    brokers = soup.select('.teaser1-title a')
    brokersMaster = set()
    for each in brokers:
        brokersMaster.add(each)

    for each in range(2,31):
        page = load_site(f'https://www.axial.net/forum/companies/business-brokers/{each}/')
        soup = BeautifulSoup(page.text, 'html.parser')
        brokers = soup.select('.teaser1-title a')
        links = soup.select('.button1.-ghost')
        for each in brokers:
            brokersMaster.add(each)
    count =0
    brokersMaster = list(brokersMaster)
    for each in range(len(brokersMaster)):
        try:
            brokersMaster[each] = str(brokersMaster[each])
            brokersMaster[each] = brokersMaster[each].split('itemprop="name" target="_blank">')
        except:
            pass
    with open('axial995.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['link', 'Broker'])
        for each in brokersMaster:
            writer.writerow(each)
def ibba():
    global ibbaEntry
    state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado",
                   "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii",
                   "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
                   "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North-Carolina",
                   "North-Dakota", "Nebraska", "New-Hampshire", "New-Jersey", "New-Mexico", "Nevada", "New-York",
                   "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode-Island", "South-Carolina",
                   "South-Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington",
                   "Wisconsin", "West-Virginia", "Wyoming"]
    with open('ibbabrokers.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Telephone", "Company", "Website", "Email"])
    links = []
    for each in state_names:
        try:
            browser = webdriver.Chrome()
            browser.get(f'https://www.ibba.org/state/{each}/')
            html = browser.page_source
            elements = (browser.find_elements(By.CSS_SELECTOR, 'div.brokers__item'))
            for every in elements:
                every = every.find_elements(By.TAG_NAME,'a')[0]
                every = every.get_attribute('href')
                links.append(every)
            html = browser.page_source
        except:
            pass
    chunks = [links[x:x + 15] for x in range(0, len(links), 15)]
    threads = []
    for alls in chunks:
        for link in alls:
            threads.append(Thread(target=threaded_ibba, args=[link]))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        with open('ibbabrokers.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for i in ibbaEntry:
                    writer.writerow(i)
        threads = []
        ibbaEntry =[]
def threaded_ibba(link):
    browser = webdriver.Chrome()
    browser.get(link)
    # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
    telephone_Email = (browser.find_elements(By.CSS_SELECTOR, 'div.brokers__profile--leftPhone'))
    Website = (browser.find_element(By.CSS_SELECTOR, 'div.brokers__profile--leftLink a'))
    name = (browser.find_elements(By.CSS_SELECTOR, 'span.breadcrumb_last'))
    Company = (browser.find_elements(By.CSS_SELECTOR, 'div.brokers__profile--leftAddress'))
    tele = "NA"
    email ="NA"
    website ="NA"
    company = "NA"
    try:
            print(Website.get_attribute('href'))
    except:
        pass
    try:
        name = name[0].text
    except:
        pass
    try:
        tele = telephone_Email[0].text
    except:
        pass
    try:
        email = telephone_Email[1].text
    except:
        pass
    try:
        website = Website.get_attribute("href")
    except:
        pass
    try:
        company = Company[0].text
    except:
        pass
    ibbaEntry.append([name,tele,company,website,email])
def BizBuySell():
    global Entry
    browser = webdriver.Chrome()
    subPages1 = set()
    subPages2 = set()
    subPages3 = set()
    subPages4 = set()
    new_height = 0
    Entry = {"1": [], "2": [], "3": [], "4": []}
    telephoneRe = re.compile('href="tel:.*?"')
    nameRe = re.compile('"name": ".*?"')
    websiteRe = re.compile('rel="nofollow" href=".*?"')
    CnameRe = re.compile('>Contact:.*?<')
    with open('Brokers.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Telephone", "Company", "Website", "Email"])
    for every in range(1, 242):
        browser = webdriver.Chrome()
        browser.get(f"https://www.bizbuysell.com/business-brokers/directory/{every}/")
        elements = (browser.find_elements(By.CSS_SELECTOR, 'a.pointer.ng-star-inserted'))
        for each in range(len(elements)):
            if each % 4 == 1:
                subPages1.add(elements[each].get_attribute("href"))
            if each % 4 == 2:
                subPages2.add(elements[each].get_attribute("href"))
            if each % 4 == 3:
                subPages3.add(elements[each].get_attribute("href"))
            if each % 4 == 0:
                subPages4.add(elements[each].get_attribute("href"))
        browser.close()
        t1 = Thread(target=threaded_Biz, args=(subPages1, telephoneRe, nameRe, websiteRe, CnameRe, "1"))# There is a much better way to write this, just being lazyish, should prob make a class
        t2 = Thread(target=threaded_Biz, args=(subPages2, telephoneRe, nameRe, websiteRe, CnameRe, "2"))
        t3 = Thread(target=threaded_Biz, args=(subPages3, telephoneRe, nameRe, websiteRe, CnameRe, "3"))
        t4 = Thread(target=threaded_Biz, args=(subPages4, telephoneRe, nameRe, websiteRe, CnameRe, "4"))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        with open('Brokers.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for i in Entry:
                for each in Entry[i]:
                    writer.writerow(each)
        subPages1 = set()
        subPages2 = set()
        subPages3 = set()
        subPages4 = set()
        Entry = {"1": [], "2": [], "3": [], "4": []}
def threaded_Biz(subPages, telephoneRe, nameRe, websiteRe, CnameRe, thread):
    print(f"executing{thread}")
    for alls in subPages:
        browser = webdriver.Chrome()
        browser.get(alls)
        html = browser.page_source
        try:
            telephone = telephoneRe.findall(html)[0]
        except:
            telephone = "NA"
        try:
            name = nameRe.findall(html)[0]
        except:
            name = "NA"
        try:
            website = websiteRe.findall(html)[0]
        except:
            website ="NA"
        try:
            Cname = CnameRe.findall(html)[0]
        except:
            Cname ="NA"
        Entry[thread].append([telephone, name, website, Cname, "NA"])
        browser.close()
def axial():
    browser = webdriver.Chrome()
    browser.get("https://www.axial.net/closed-deals/")
    new_height = 0
    Advisors = []
    acquirers = []
    Businesses = []
    Entry = []
    allText = []
    execepts = []
    count = 0
    while True:
        elements = (browser.find_elements(By.CSS_SELECTOR, 'article.expgrid1-entry'))
        for each in elements:
            raw_text = each.get_attribute("data-id")
            start_text = raw_text
            if raw_text not in allText:
                count += 1
                allText.append(raw_text)
                raw_text = raw_text.replace("-", " ")
                raw_text = raw_text.split('advises')
                if len(raw_text) == 1:
                    raw_text = raw_text[0].split('advised-by')
                    try:
                        if len(raw_text[0].split("acquired")) != 1:
                            Advisor = raw_text[1]
                            raw_text = raw_text[0].split("acquired")
                            acquirer = raw_text[0]
                            bus = raw_text[1]

                    except:
                        raw_text = raw_text
                    if len(raw_text) == 1:
                        raw_text = raw_text[0].split('acquired')
                        Advisor = "NA"
                        try:
                            acquirer = raw_text[0]
                            bus = raw_text[1]
                        except:
                            if len(raw_text[0].split('acquires')) == 1:
                                Advisor = raw_text[0]
                                acquirer = "unchecked"
                                bus = "unchecked"
                            else:
                                raw_text = raw_text[0].split('acquires')
                                acquirer = raw_text[0]
                                bus = raw_text[1]
                    else:
                        Advisor = raw_text[0]
                        acquirer = "unchecked"
                        bus = "unchecked"
                else:
                    Advisor = raw_text[0]
                    try:
                        acquirer = raw_text[1].split('on acquisition by')[0]
                        bus = raw_text[1].split('on acquisition by')[1]
                    except:
                        try:
                            acquirer = raw_text[1].split('in acquisition by')[0]
                            bus = raw_text[1].split('in acquisition by')[1]
                        except:
                            acquirer = raw_text[1]
                            bus = "uncheched exeption"
                Advisors.append(Advisor)
                acquirers.append(acquirer)
                Businesses.append(bus)
                Entry.append([start_text, Advisor, acquirer, bus])
        browser.execute_script(f"window.scrollTo(0, document.body.scrollHeight/20*{new_height});")
        time.sleep(1)
        new_height += 1

        if new_height == 21:
            break

    with open('Advi.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['source', 'Advisors', 'Aqurirers', "Busniesses"])
        for each in Entry:
            writer.writerow(each)
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
        rev = "NA"
    try:
        cash = otherRE.findall(cash[0])
    except:
        cash = "NA"
    try:
        EBITA = otherRE.findall(EBITA[0])
    except:
        EBITA = "NA"
    other = [otherRE.findall(rev[0]) if rev.type == list else 'NA', otherRE.findall(cash[0]), otherRE.findall(EBITA[0])]
    otherFin = []
    for each in other:
        try:
            otherFin.append(each[0].split("$")[1].split("<")[0])
        except:
            otherFin.append('NA')
    info.append([url, pri.replace(',', ''), otherFin[0].replace(',', ''), otherFin[1].replace(',', ''),
                 otherFin[2].replace(',', '')])


def load_site(url: str) -> requests:
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
    return r
if __name__ == '__main__':
    ibba()
    # csvWriteBroker()


