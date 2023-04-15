import gzip
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException



# chromedriver
# path is for chromedriver.exe file needed to run a Selenium Chromedriver
path = "C:/Users/18102/CS260/solar-scraper/chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument("--headless")
userAgent = "Chrome/96.0.4664.45"
chrome_options.add_argument(f"user-agent={userAgent}")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get("https://web.healthsparq.com/healthsparq/public/#/one/insurerCode=MEDICA_I&brandCode=MEDICA/machine-readable-transparency-in-coverage")


fileCountTextXPath = '//*[@id="ember10"]/div/div/div/div[1]/div/div/div[3]'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, fileCountTextXPath)))
fileCountText = driver.find_element(By.XPATH, fileCountTextXPath)
print(fileCountText.text)

fileCount = int(fileCountText[len(fileCountText) - 1])
print(fileCount)

for i in range(1, 5):
    downloadButtonXpath = f'//*[@id="ember10"]/div/div/div/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[4]/button'






# jsonFileIn = 'C:/Users/18102/Puzzles/2022-11-01_Medica-Insurance-Company_index.json.gz'
# jsonFileOut = 'C:/Users/18102/Puzzles/2022-11-01_Medica-Insurance-Company_index.json'
# with gzip.open(jsonFileIn, 'r') as fin:        # 4. gzip
#     json_bytes = fin.read()                      # 3. bytes (i.e. UTF-8)

# json_str = json_bytes.decode('utf-8')            # 2. string (i.e. JSON)
# data = json.loads(json_str)


# with open(jsonFileOut, "w") as write_file:
#     json.dump(data, write_file, indent=4)