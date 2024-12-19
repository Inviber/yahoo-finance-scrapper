from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys

# if there are no CLI parameters
if len(sys.argv) <= 1:
    print('Ticker symbol CLI argument missing!')
    sys.exit(2)

ticker_symbol = sys.argv[1]

url = f'https://finance.yahoo.com/quote/{ticker_symbol}/'

# initialize a web driver instance to control a chrome window
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.set_window_size(1920, 1080)
driver.get(url)


# scrapping logic
print("Scrapping site")

# close the browser and free up the resources
driver.quit()