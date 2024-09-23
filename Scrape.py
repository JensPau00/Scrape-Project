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
state_names = ["Alaska", "Alabama", "Arkansas","canada", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
for each in range(len(state_names)):
    state_names[each]=state_names[each].replace(" ","-")

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
    with open('Brokers.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def axial995():
    axial995Entry = []
    page = load_site('https://www.axial.net/forum/companies/business-brokers/')
    soup = BeautifulSoup(page.text, 'html.parser')
    brokers = soup.select('.teaser1-title a')
    brokersMaster = set()
    for each in brokers:
        brokersMaster.add(each)

    for each in range(2,50):
        page = load_site(f'https://www.axial.net/forum/companies/business-brokers/{each}/')
        soup = BeautifulSoup(page.text, 'html.parser')
        brokers = soup.select('.teaser1-title a')
        links = soup.select('.button1.-ghost')
        for every in brokers:
            brokersMaster.add(every)
    count =0
    brokersMaster = list(brokersMaster)
    for each in range(len(brokersMaster)):
        try:
            brokersMaster[each] = str(brokersMaster[each])
            brokersMaster[each] = brokersMaster[each].split('itemprop="name" target="_blank">')
        except:
            pass
    linkList = []
    with open('axial995.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["link",'company', 'Type', "HQ", "Site"])
    def axialThread(link):
        browser = webdriver.Chrome()
        browser.get(f"https://{link}")
        # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
        Company = "NA"
        Flag = True
        while Company == "NA" and Flag:
            time.sleep(5)
            # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
            company = (
                browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/div/span'))
            Type = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[1]/p'))
            HQ = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[1]/p'))
            Site = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[1]/p'))
            type = "NA"
            site = "NA"
            Hq = "NA"
            Company = "NA"
            try:
                print(Site.get_attribute('href'))
            except:
                pass
            try:
                Company = company[0].text
            except:
                pass
            try:
                Hq = HQ[0].text
            except:
                pass
            try:
                type = Type[0].text
            except:
                pass
            try:
                site = Site[0].get_attribute("href")
            except:
                pass
            Flag =False
        axial995Entry.append([link,site, type, Company, Hq])
    for each in brokersMaster:
        link = each[0].split(':')
        link = link[1].replace("\""," ")
        link = link.replace(" ","")
        link = link[2:]
        linkList.append(link)
    chunks = [linkList[x:x + 15] for x in range(0, len(linkList), 15)]
    for alls in chunks:
        threads = []
        axial995Entry = []
        for link in alls:
            threads.append(Thread(target=axialThread, args=[link]))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        with open('axial995.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for each in axial995Entry:
                writer.writerow(each)

def axial1770():
    axial1770Entry = []
    page = load_site('https://www.axial.net/forum/companies/business-brokers/')
    soup = BeautifulSoup(page.text, 'html.parser')
    brokers = soup.select('.teaser1-title a')
    brokersMaster = set()
    for each in brokers:
        brokersMaster.add(each)

    for each in range(2,89):
        page = load_site(f'https://www.axial.net/forum/companies/business-brokers/{each}/')
        soup = BeautifulSoup(page.text, 'html.parser')
        brokers = soup.select('.teaser1-title a')
        links = soup.select('.button1.-ghost')
        for every in brokers:
            brokersMaster.add(every)
    count =0
    brokersMaster = list(brokersMaster)
    for each in range(len(brokersMaster)):
        try:
            brokersMaster[each] = str(brokersMaster[each])
            brokersMaster[each] = brokersMaster[each].split('itemprop="name" target="_blank">')
        except:
            pass
    linkList = set()
    with open('axial1770.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Link",'company', 'Type', "HQ", "Site"])
    def axialThread(link):
            browser = webdriver.Chrome()
            browser.get(f"https://{link}")
            # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
            Company = "NA"
            Flag=True
            while Company == "NA" and Flag:
                time.sleep(5)
                company = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/div/span'))
                Type = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[1]/p'))
                HQ = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[2]/p/span[1]'))
                Site = (browser.find_elements(By.XPATH, '//*[@id="sidenav-content"]/axl-account-profile/ion-content/div/axl-account-profile-header/div/div[1]/div[2]/form/div[3]/p/a'))
                typo = "NA"
                site = "NA"
                Hq = "NA"
                Company = "NA"
                try:
                    print(Site.get_attribute('href'))
                except:
                    pass
                try:
                    Company = company[0].text
                except:
                    pass
                try:
                    Hq = HQ[0].text
                except:
                    pass
                try:
                    typo = Type[0].text
                except:
                    pass
                try:
                    site = Site[0].get_attribute("href")
                except:
                    pass
                Flag = False
            axial1770Entry.append([link,Company, typo, Hq, site,])
    for each in brokersMaster:
        link = each[0].split(':')
        link = link[1].replace("\""," ")
        link = link.replace(" ","")
        link = link[2:]
        linkList.add(link)

    linkList= list(linkList)
    chunks = [linkList[x:x + 10] for x in range(0, len(linkList), 10)]
    for alls in chunks:
        threads = []
        axial1770Entry = []
        for link in alls:
            threads.append(Thread(target=axialThread, args=[link]))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        with open('axial1770.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for each in axial1770Entry:
                writer.writerow(each)

def buisBrok():
    brokersEntry = []
    brokersMaster = set()
    for state in state_names:
        page = load_site(f'https://www.businessbroker.net/brokers/{state}.aspx')
        soup = BeautifulSoup(page.text, 'html.parser')
        brokers = soup.select("p.buttons.notFeatured")
        for each in brokers:
            try:
                changed = each.select('a')
                print((changed))
                changed=(changed.pop()).get_attribute_list("href")
                print(changed)
                brokersMaster.add("https://www.businessbroker.net" + str(changed[0]))
            except:
                pass
    print(brokersMaster)
    with open('buisbroknet.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Person', 'Company', "Street", "Location"])
    def threadedBuisBroker(link):
        browser = webdriver.Chrome()
        browser.get(f"{link}")
        # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
        Company = "NA"
        Flag = True
        while Company == "NA" and Flag:
            time.sleep(5)
            # content > div.content-area > div > section > div.brokers__profile--left > div.brokers__profile--leftLink > a:nth-child(1)
            name = (
                browser.find_elements(By.XPATH,
                                      '//*[@id="banner"]/div/div/table/tbody/tr/td/h1'))
            company = (browser.find_elements(By.XPATH,
                                          '//*[@id="banner"]/div/div/div[1]/h2'))
            loc = (browser.find_elements(By.XPATH,
                                        '//*[@id="banner"]/div/div/div[1]/p[2]'))
            street = (browser.find_elements(By.XPATH,
                                          '//*[@id="banner"]/div/div/div[1]/p[1]'))
            Name = "NA"
            Company = "NA"
            Street = "NA"
            Loc = "NA"
            try:
                Company = company[0].text
            except:
                pass
            try:
                Name = name[0].text
            except:
                pass
            try:
                Loc = loc[0].text
            except:
                pass
            try:
                Street = street[0].text
            except:
                pass
            Flag = False
        brokersEntry.append( [Name, Company, Street, Loc])
    linkList = list(brokersMaster)
    print(brokersMaster)
    chunks = [linkList[x:x + 15] for x in range(0, len(linkList), 15)]
    for alls in chunks:
        threads = []
        brokersEntry = []
        for link in alls:
            threads.append(Thread(target=threadedBuisBroker, args=[link]))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        with open('buisbroknet.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for each in brokersEntry:
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
def load_site(url: str) -> requests:
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
    return r
if __name__ == '__main__':
    axial1770()
    # csvWriteBroker()
