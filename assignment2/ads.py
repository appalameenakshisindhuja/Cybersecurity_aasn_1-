# ads.py
import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # auto driver management

# --- CONFIG ---
CHROME_BINARY = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ULAA_BINARY   = r"C:\Program Files\Zoho\Ulaa\Application\ulaa.exe"

CHROME_PROFILE = r"C:\Users\home\AppData\Local\Google\Chrome\User Data\Profile 1"
ULAA_PROFILE   = r"C:\Users\home\AppData\Local\Zoho\Ulaa\User Data\Default Developer"

TEST_URL = "https://www.cnn.com"

AD_TRACKER_DOMAINS = [
    "doubleclick.net",
    "googleadservices.com",
    "googlesyndication.com",
    "adservice.google.com",
    "ads.yahoo.com",
    "facebook.net",
    "track.adform.net"
]

def launch_browser_and_collect(profile_path, binary_path, headless=True, wait=10):
    chrome_opts = Options()
    chrome_opts.binary_location = binary_path
    chrome_opts.add_argument(f"--user-data-dir={profile_path}")
    if headless:
        chrome_opts.add_argument("--headless=new")
        chrome_opts.add_argument("--disable-gpu")
    chrome_opts.add_argument("--no-sandbox")
    chrome_opts.add_argument("--disable-dev-shm-usage")
    chrome_opts.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])

    service = Service(ChromeDriverManager().install())  # automatically fetch correct driver

    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=chrome_opts)
        driver.get(TEST_URL)
        time.sleep(wait)

        matched = []
        for req in driver.requests:
            try:
                url = req.url
            except Exception:
                continue
            if any(domain in url for domain in AD_TRACKER_DOMAINS):
                matched.append(url)
        return matched
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    print("=== Chrome Ads/Trackers ===")
    try:
        chrome_hits = launch_browser_and_collect(CHROME_PROFILE, CHROME_BINARY, headless=True, wait=12)
        for url in chrome_hits or ["No matching ad/tracker requests detected"]:
            print(url)
    except Exception as e:
        print("Chrome run error:", type(e).__name__, e)

    print("\n=== Ulaa Ads/Trackers ===")
    try:
        ulaa_hits = launch_browser_and_collect(ULAA_PROFILE, ULAA_BINARY, headless=True, wait=12)
        for url in ulaa_hits or ["No matching ad/tracker requests detected"]:
            print(url)
    except Exception as e:
        print("Ulaa run error:", type(e).__name__, e)
