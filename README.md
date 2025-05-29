# 📁 Specific Web Document Downloader

A focused Python-based script built to scrape a **specific website**, extract **Google Drive links**, and automatically download those files into a local folder. It also logs downloaded links to avoid duplicates and skips inaccessible or broken links gracefully.

## 🚀 Features

- 🔗 Scrapes all specified URLs from a `links.txt` file.
- 🧠 Extracts only valid Google Drive links.
- 📥 Downloads files to `website_docs/` folder.
- 🔁 Skips files already downloaded (uses `downloaded_drive_links.txt`).
- ❌ Gracefully skips broken/inaccessible links.
- 🧾 Maintains logs for extracted and downloaded links.

## 🧰 Tech Stack

- Python 3.8+
- `requests`, `beautifulsoup4`, `gdown`
- Linux Shell compatible

## ⚙️ Setup & Usage
1. Clone the Repo
   ```bash
   git clone https://github.com/your-username/Specific_Web_Document_Downloader.git
   cd Specific_Web_Document_Downloader
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py
---

## 🔐 Important Notes
- This script is custom-built for a specific site structure.
- It currently handles only Google Drive links.
- Make sure your environment has internet access and Python 3.8+.

---
## 🛠️ Contributing
- Pull requests are welcome! If you'd like to add functionality, optimize performance, or improve documentation, feel free to fork and PR.
---
## Issues
- Please use the [issues](https://github.com/Sidddev15/SiteSpecific-GDrive-Downloader/issues) tab to report bugs or request features.
---
## 🙌 Acknowledgments
Built with ❤️ by Siddharth Singh
Special thanks to gdown, beautifulsoup4, and Python’s awesome community.
---
## 💬 Let's Connect

Let me know if you want me to:

- Generate dynamic badges (e.g., `python version`, `last updated`, `stars`)
- Create a cover or diagram image
- Add license, `.gitignore`, and `requirements.txt` boilerplate

Just say the word and I’ll prep it all!
---
## 📂 Folder Structure

```plaintext
Specific_Web_Document_Downloader/
├── website_docs/                   # All downloaded files go here
├── links.txt                       # List of URLs to scrape
├── drive_links_extracted.txt       # All Drive links found
├── downloaded_drive_links.txt      # Only downloaded Drive links
├── main.py                         # Main executable script
└── README.md
