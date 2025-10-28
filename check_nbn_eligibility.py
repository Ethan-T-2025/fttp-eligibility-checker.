import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def check_eligibility(address):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.nbnco.com.au/connect-home-or-business/check-your-address")
        time.sleep(2)

        input_box = driver.find_element(By.ID, "address-search")
        input_box.send_keys(address)
        time.sleep(2)

        submit_button = driver.find_element(By.CLASS_NAME, "search-button")
        submit_button.click()
        time.sleep(5)

        result = driver.find_element(By.CLASS_NAME, "result-text").text
        return result
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        driver.quit()

if __name__ == "__main__":
    address = sys.argv[1]
    print(check_eligibility(address))
