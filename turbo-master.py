import os , time, pathlib, re

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC



# options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# options.add_argument("--headless")
# options.add_argument('user-agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--disable-logging")
# options.add_argument('log-level=3')
# options.add_argument('--window-size=1920,1080')
# options.add_argument('--disable-gpu')

# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe"
options = Options()
# options = webdriver.ChromeOptions()
# options.binary_location = r"{}".format(chrome_path)
# if user_agent != 0:
    # options.add_argument('--headless')
    # options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get("https://vsmobile.bet9ja.com/bet9ja-mobile/login/?mode=premier_turbo")




xpath = '//*[@id="button-next-event"]'

# search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
# print('geee')
while True:
    try:
        iframe_xpath = '//*[@id="playAreaFrame"]'
        iframe = driver.find_element_by_xpath(iframe_xpath)
        time.sleep(2)
        driver.switch_to.frame(iframe)
        break
    except:
        pass
print('switch to iframe')

while True:

    try:

        # a = driver.find_element_by_xpath('//*[@id="ui-id-1"]').text
        # print(a)
        # time.sleep(1)
        # a = driver.find_element_by_xpath(xpath).text
        b = driver.find_element_by_xpath('//*[@id="idleague"]').text
        c = driver.find_element_by_xpath('//*[@id="leagueWeekNumber"]').text
        print(b, c)
        time.sleep(1)
        driver.execute_script("arguments[0].removeAttribute('disabled');",driver.find_element_by_xpath(xpath))
        # time.sleep(1)
        # driver.execute_script("arguments[0].setAttribute('enable');",driver.find_element_by_xpath(xpath))
        # print('True here')
        time.sleep(3)
        driver.find_element_by_xpath(xpath).click()
        # time.sleep(2)

        search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))

        driver.find_element_by_xpath('//*[@id="bet"]/div[1]/div[1]/span[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="a_bet_results"]').click()
        # time.sleep(10)
        # search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//*[@id="results_content"]/div[2]/div[1]')))
        # time.sleep(10)

        # results = driver.find_element_by_xpath('//*[@id="results-div-header-mainTable"]').find_elements_by_tag_name('td')[-30:]

        # results = [result.text for result in results]
        # print(results)
        results = []



        matrix = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21], [22,23,24], [25,26,27], [28,29,30], [31,32,33], [34,35,36], [37,38]]

        for i in range(len(matrix)):
            print('kkkk->', c)
            if int(c) in matrix[i]:
                row = i+1
                col = (matrix[i].index(int(c))+1)
        # while True:
        #     try:
        #         for i in range(2, 16):
        #             result = driver.find_element_by_xpath(f'//*[@id="results-div-header-mainTable"]/tbody/tr[{row}]/td[{col}]/table/tbody/tr[{i-1}]')
        #             result = result.find_elements_by_tag_name('td')
        #             res = [r.text for r in result]
        #             results.append(res)

        #         # results = results[-1].find_elements_by_tag_name('tr')
        #         print(results)
        #         break
        #     except Exception as e:
        #         print(e)

        while True:
            try:

                results = driver.find_elements_by_xpath('//td[@style="width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px"]')
                tr = results[-1].find_elements_by_tag_name('tr')
                print(len(results))
                print(len(tr))

                driver.find_element_by_xpath('//*[@id="bet"]/div[1]/div[1]/span[1]/a').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="a_bet_bet"]').click()
                break
            except Exception as e:
                print(e)
        time.sleep(3)



    except Exception as e:
        print(e)
    time.sleep(1)

print('success')

