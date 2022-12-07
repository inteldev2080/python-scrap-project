import time, json, re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions

def scrapWebsite(required_url):

    options = EdgeOptions()
    options.headless = True         # hides the browser
    path = "./msedgedriver.exe"

    driver = webdriver.Edge(path, options=options) # added options

    # driver = webdriver.Edge(path)
    # driver.set_window_size(1024, 728)
    # driver.maximize_window()


    # driver.get("https://coinmarketcap.com/")
    # driver.get("https://coinmarketcap.com/all/views/all/")
    
    driver.get(required_url)

    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
    time.sleep(0.2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")

    # time.sleep(4)
    locate_body = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody'))


    try:
        find_tr = locate_body.find_elements(By.TAG_NAME, 'tr')

        all_data = []

        print("scrapping....")
        # for i in range(len(find_tr)-90):        
        for i in range(len(find_tr)):        
            each_td = find_tr[i].find_elements(By.TAG_NAME, 'td')
            td_text = each_td

            new_obj = {}

            new_obj["name"] = re.sub(r"[\n]", " ", each_td[2].text)
            new_obj["price"] = re.sub(r"[$,]", "", each_td[3].text)
            new_obj["perhour"] = re.sub(r"[%]", "", each_td[4].text)
            new_obj["day"] = re.sub(r"[%]", "", each_td[5].text)
            new_obj["week"] = re.sub(r"[%]", "", each_td[6].text)
            new_obj["marketcap"] = re.sub(r"[$,]", "", each_td[7].text)
            new_obj["volume"] = re.sub(r"[$,]", "", each_td[8].text.split("\n")[0])
            new_obj["cirulating_supply"] = re.sub(r"[$,]", "", each_td[3].text)
                
            all_data.append(new_obj)
        
        # with open('json_data.json', 'w') as f:
        #     json.dump(all_data, f)

        print("Total objects =>", len(all_data))

        return all_data


    except:
        print("timeout")

    # time.sleep(4) # delay before quiting the browser
