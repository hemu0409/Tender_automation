from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

BASE_DIR = os.path.abspath(os.getcwd()) 
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True) 

options = webdriver.ChromeOptions()

download_path = DOWNLOAD_DIR.replace("/", "\\")
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://eproc.rajasthan.gov.in/nicgep/app?page=FrontEndTendersByOrganisation&service=page")
print("⚠️ Manually solve CAPTCHA, then search/filter for PHED - C.E. (Project), Jodhpur.")
input("✅ Once tender list is visible, press ENTER to start downloading ZIPs...")

try:
    rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr")
    print(f"📄 Found {len(rows)} rows in tender table.")

    for i in range(min(48, len(rows))): 
        try:
            rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr")
            row = rows[i]

            # Try to find a link in any <td>
            link_found = False
            for td in row.find_elements(By.TAG_NAME, "td"):
                try:
                    a = td.find_element(By.TAG_NAME, "a")
                    tender_title = a.text.strip().replace("/", "_").replace(" ", "_")
                    print(f"🔍 Opening tender: {tender_title}")
                    a.click()
                    link_found = True
                    break
                except:
                    continue

            if not link_found:
                print(f"⚠️ No link found in row {i+1}, skipping.")
                continue

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Download as zip file')]"))
            )
            zip_link = driver.find_element(By.XPATH, "//a[contains(text(),'Download as zip file')]")
            zip_link.click()
            print(f"✅ Downloaded ZIP for: {tender_title}")

            time.sleep(5)  # Wait for download to complete
            driver.back()
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ Error on row {i+1}: {e}")
            try:
                driver.back()
            except:
                pass
            time.sleep(2)

except Exception as e:
    print(f"❌ Top-level error: {e}")

driver.quit()
