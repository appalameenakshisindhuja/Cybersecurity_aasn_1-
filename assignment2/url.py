import sqlite3
import os
import shutil

def fetch_urls(profile_path, browser_name):
    history_db = os.path.join(profile_path, "History")
    if not os.path.exists(history_db):
        print(f"{browser_name} history not found at {history_db}")
        return []

    tmp_db = f"tmp_{browser_name}_history"
    shutil.copy2(history_db, tmp_db)  # copy to avoid lock issues

    urls = []
    try:
        conn = sqlite3.connect(tmp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC")
        urls = [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error reading {browser_name} history:", e)
    finally:
        conn.close()
        os.remove(tmp_db)

    return urls

if __name__ == "__main__":
    # Paths to Chrome and Ulaa profiles
    chrome_profile = r"C:\Users\home\AppData\Local\Google\Chrome\User Data\Profile 1"
    ulaa_profile   = r"C:\Users\home\AppData\Local\Zoho\Ulaa\User Data\Default Developer"

    print("=== Chrome URLs ===")
    chrome_urls = fetch_urls(chrome_profile, "chrome")
    for url in chrome_urls[:20]:  # show top 20
        print(url)

    print("\n=== Ulaa URLs ===")
    ulaa_urls = fetch_urls(ulaa_profile, "ulaa")
    for url in ulaa_urls[:20]:
        print(url)
