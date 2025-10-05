import subprocess
import psutil
import time
import os

def check_ulaa_sandbox():
    ulaa_path = r"C:\Program Files\Zoho\Ulaa\Application\ulaa.exe"
    if not os.path.exists(ulaa_path):
        print("❌ Ulaa not found at:", ulaa_path)
        return

    print("🧪 Checking Ulaa Sandboxing Effectiveness...\n")

    process = subprocess.Popen([
        ulaa_path,
        "--enable-sandbox",
        "--disable-extensions",
        "--no-first-run",
        "--remote-debugging-port=9223",
        "--headless",
        "about:blank"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        time.sleep(3)
        pid = process.pid
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)

        print(f"🧠 Ulaa Main PID: {pid}")
        print(f"🧩 Sandboxed Child Processes: {len(children)}")

        for c in children:
            try:
                info = c.as_dict(attrs=["pid", "name", "username"])
                print(f"  - PID: {info['pid']} | User: {info['username']} | Name: {info['name']}")
            except psutil.AccessDenied:
                print(f"  - PID: {c.pid} (Access Denied)")

        user = parent.username()
        print(f"\n🔐 Ulaa main process runs as: {user}")
        if "system" in user.lower():
            print("⚠️ High privileges detected — Sandbox may not be fully active.")
        else:
            print("✅ User-level privileges — Sandbox isolation active.")
    finally:
        process.terminate()
        process.wait()
        print("\n🛑 Ulaa closed.\n")

if __name__ == "__main__":
    check_ulaa_sandbox()
