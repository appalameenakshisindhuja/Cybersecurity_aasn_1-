from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Get cookies
cookies = driver.get_cookies()
print("Total cookies set:", len(cookies))

# Save cookies
with open("chrome_cookies.json", "w") as f:
    json.dump(cookies, f, indent=4)

driver.quit()
