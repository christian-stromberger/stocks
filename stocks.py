import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Each stock has a name (ticker symbol), how many shares I own, and initialPrice(total on purchace)
class Stock:
    
    def __init__(self, name, shares, initialPrice):
        self.name = name
        self.shares = shares
        self.ip = initialPrice
        self.value = getPrice(self.name)

    # change the total number of shares
    def setShares(self, s):
        self.shares = s

    def getShares(self):
        return self.shares

    # how much are all the shares worth
    def value(self):
        return self.shares * self.value

    def profit(self):
        return (self.value * self.shares) - self.ip

    # adding s shares at p price each
    def addShares(self, s, p):
        self.ip = self.ip + (s * p)
        self.shares = self.shares + s

# gets price of stock via scraping, name is the ticker symbol
def getPrice(name):
    url = "https://www.marketwatch.com/investing/stock/" + name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = str(soup.find_all("bg-quote")[45])[150:-11]
    return float(price)

def portfolioProfit(portfolio):
    total = 0
    for stock in portfolio:
        total += portfolio[stock].profit()
    return total

def portfolioWorth(portfolio):
    total = 0
    for stock in portfolio:
        total += portfolio[stock].value
    return total

def addtoPortfolio(name, stock, portfolio):
    portfolio[name] = stock
    
adbe = Stock("adbe", 1, 310.51 * 1)
dis = Stock("dis", 5, 137.00 * 5)
nke = Stock("nke", 2, 84.87 * 2)
tsla = Stock("tsla", 10, 54.97 * 10)
nflx = Stock("nflx", 2, 103.15 * 2)
sbux = Stock("sbux", 5, 48.69 * 5)
aapl = Stock("aapl", 8, 23.35 * 8)

portfolio = {}

addtoPortfolio("Adobe", adbe, portfolio)
addtoPortfolio("Disney", dis, portfolio)
addtoPortfolio("Nike", nke, portfolio)
addtoPortfolio("Tesla", tsla, portfolio)
addtoPortfolio("Netflix", nflx, portfolio)
addtoPortfolio("Starbucks", sbux, portfolio)
addtoPortfolio("Apple", aapl, portfolio)

print("Company\t\tShares\tPrice\t\tProfit")

for s in portfolio:
    if (len(s) > 6):
        print(s + ":\t" + str(portfolio[s].getShares()) + "\t" + str(getPrice(portfolio[s].name)) + "\t\t" + str(portfolio[s].profit()))
    else:
        print(s + ":\t\t" + str(portfolio[s].getShares()) + "\t" + str(getPrice(portfolio[s].name)) + "\t\t" + str(portfolio[s].profit()))

print("Total\t\t\t" + str(portfolioWorth(portfolio)) + "\t\t" + str(portfolioProfit(portfolio)))
