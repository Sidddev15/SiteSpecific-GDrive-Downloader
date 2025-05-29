import os
import requests
from bs4 import BeautifulSoup
import gdown

# Folders & File paths
os.makedirs("website_docs", exist_ok=True)
input_links_file = "input_links.txt"
downloaded_log_file = "downloaded_drive_links.txt"
failed_log_file = "failed_links.txt"

# Read all page URLs
with open(input_links_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Load already-downloaded Google Drive links into a set
downloaded_links = set()
if os.path.exists(downloaded_log_file):
    with open(downloaded_log_file, "r") as f:
        downloaded_links = set(line.strip() for line in f if line.strip())

# Scrape and download logic
for url in urls:
    print(f"\n🌍 Processing: {url}")
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        continue

    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a", href=True)
    drive_links = [a['href'] for a in links if "drive.google.com" in a['href']]

    print(f"🔎 Found {len(drive_links)} Google Drive link(s)")

    with open(downloaded_log_file, "a") as dl_log, open(failed_log_file, "a") as fail_log:
        for drive_link in drive_links:
            if drive_link in downloaded_links:
                print(f"⏭️ Already downloaded: {drive_link}")
                continue

            print(f"⬇️ Downloading: {drive_link}")
            try:
                gdown.download(drive_link, output="website_docs/", quiet=False, fuzzy=True)
                dl_log.write(drive_link + "\n")
                downloaded_links.add(drive_link)
            except Exception as e:
                print(f"⚠️ Skipped (Error): {e}")
                fail_log.write(drive_link + "\n")
                continue
