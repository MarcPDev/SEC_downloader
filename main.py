from bs4 import BeautifulSoup
import requests

# Helferfunktion, um Redundanz zu vermeiden
def get_soup(ticker):
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + ticker + '&Find=Search&owner=exclude&action=getcompany'
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    return soup


# holt Firmennamen anhand des Tickers
def get_companyname(ticker):
    soup = get_soup(ticker)
    for link in soup.find_all('span', class_='companyName'):
        return(link.next_element)

    
# holt CIK anhand des Tickers
def get_company_cik(ticker):
    soup = get_soup(ticker)
    for link in soup.find_all('link', href=True):
        found_pos = str(link).find('CIK')
        if found_pos > -1:
            return(str(link)[found_pos+4:found_pos+14])
    return 0


def get_10k_files(ticker):
    cik = get_company_cik(ticker)
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=' + str(cik) + '&type=10-K&dateb=&owner=include&count=40'
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all('a', href=True, id='documentsbutton'):
        
        print('https://www.sec.gov' + link['href'])

#https://www.sec.gov/Archives/edgar/data/320193/000162828016020309/a201610-k9242016.htm
#https://www.sec.gov/Archives/edgar/data/320193/000032019317000070/a10-k20179302017.htm    
#https://www.sec.gov/Archives/edgar/data/320193/000032019317000070/0000320193-17-000070-index.htm

    #https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=10-K&dateb=&owner=include&count=40


#get_10k_files('AAPL')

# TODO
# aus den gefundenen Links den zum 10-K finden
#url = 'https://www.sec.gov/Archives/edgar/data/320193/000119312515356351/0001193125-15-356351-index.htm'
url = 'https://www.sec.gov/Archives/edgar/data/320193/000032019317000070/0000320193-17-000070-index.htm'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify)
