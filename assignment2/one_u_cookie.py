from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from webdriver_manager.chrome import ChromeDriverManager

ulaa_path = r"C:\Program Files\Zoho\Ulaa\Application\ulaa.exe"

options = Options()
options.binary_location = ulaa_path

# If you want DevTools / not headless, don't enable headless.
#options.add_argument("--headless=new")  # optional

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

# Get cookies
cookies = driver.get_cookies()
print("Total cookies set:", len(cookies))

# Save cookies
with open("ulaa_cookies.json", "w") as f:
    json.dump(cookies, f, indent=4)

driver.quit()
