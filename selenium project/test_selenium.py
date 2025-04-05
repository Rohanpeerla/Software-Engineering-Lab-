from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://127.0.0.1:5002")
    wait = WebDriverWait(driver, 10)


    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card-title")))
    time.sleep(1)

    dropdown_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle")))
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_button)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", dropdown_button)
    time.sleep(1)

    ai_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "toggleAI")))
    driver.execute_script("arguments[0].scrollIntoView(true);", ai_checkbox)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", ai_checkbox)
    time.sleep(1)

    ai_card = driver.find_element(By.ID, "aiCard")
    assert ai_card.value_of_css_property("display") == "none"

    driver.execute_script("arguments[0].click();", ai_checkbox)
    time.sleep(1)
    assert ai_card.value_of_css_property("display") != "none"

    for category in ['market', 'ai', 'elections']:
        summary = driver.find_element(By.ID, f"{category}Summary")
        read_more_btn = driver.find_element(By.XPATH, f"//button[@onclick=\"showNews('{category}')\"]")
        driver.execute_script("arguments[0].scrollIntoView(true);", read_more_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", read_more_btn)
        time.sleep(2)

        news_detail = driver.find_element(By.ID, f"{category}News")
        assert summary.value_of_css_property("display") == "none"
        assert news_detail.value_of_css_property("display") != "none"


        back_btn = news_detail.find_element(By.CLASS_NAME, "btn-secondary")
        driver.execute_script("arguments[0].scrollIntoView(true);", back_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", back_btn)
        time.sleep(1)
        assert summary.value_of_css_property("display") != "none"

    time.sleep(5) 
    print("✅ All sections tested successfully.")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()
