import subprocess
import psutil
import time
import os

def check_chrome_sandbox():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        print(" Chrome not found at:", chrome_path)
        return

    print("Checking Chrome Sandboxing Effectiveness...\n")

    process = subprocess.Popen([
        chrome_path,
        "--enable-sandbox",
        "--disable-extensions",
        "--no-first-run",
        "--remote-debugging-port=9222",
        "--headless",
        "about:blank"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        time.sleep(3)  # wait for startup
        pid = process.pid
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)

        print(f" Chrome Main PID: {pid}")
        print(f" Sandboxed Child Processes: {len(children)}")

        for c in children:
            try:
                info = c.as_dict(attrs=["pid", "name", "username"])
                print(f"  - PID: {info['pid']} | User: {info['username']} | Name: {info['name']}")
            except psutil.AccessDenied:
                print(f"  - PID: {c.pid} (Access Denied)")

        user = parent.username()
        print(f"\n Chrome main process runs as: {user}")
        if "system" in user.lower():
            print(" High privileges detected — Sandbox may not be fully active.")
        else:
            print(" User-level privileges — Sandbox isolation active.")
    finally:
        process.terminate()
        process.wait()
        print("\n Chrome closed.\n")

if __name__ == "__main__":
    check_chrome_sandbox()
