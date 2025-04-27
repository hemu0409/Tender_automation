# 📄 Tender Automation Project

A Python-based automation tool to download, extract, and analyze tender BOQ documents from the Rajasthan eProcurement Portal, focusing on DI Pipe entries.

---

## ✨ Features
- 🔍 Automated search and download of tender ZIP files (PHED Jodhpur & Jaipur).
- 📦 Extracts and processes BOQ Excel files inside the ZIPs.
- 🔎 Searches for a specific item code (**8329 - DI Pipes**).
- 📊 Generates a final Excel report listing tenders containing DI pipes.
- 🛠️ Detailed logging for easier troubleshooting.

---

## 🛠️ Tech Stack
- 🐍 Python
- 🖥️ Selenium WebDriver
- 📈 OpenPyXL (Excel handling)
- 🐧 Bash scripting (for automation)

---

## 📂 Project Structure

tender_automation/ 
├── downloads/ # Folder where ZIP files are saved after downloading. 
├── extracted/ # Folder where BOQ Excel files are saved after extraction. 
├── output/ # Folder where the final DI Pipes Excel report is saved. 
├── check_boq.py # Script to process BOQ files and check for item code 8329. 
├── tender_scraper.py # Main script to automate the scraping and downloading of tenders. 
├── run.sh # Shell script to run the entire automation process. 
├── tender_scraper.log # Log file generated during script execution. 
├── chromedriver.exe # ChromeDriver executable needed for Selenium. 
├── README.md # Project documentation (this file).

---

## 🚀 How to Run

1. Install the required Python libraries:
   ```bash
   pip install selenium openpyxl.
2. Ensure you have the correct version of chromedriver.exe matching your Chrome browser.
3. Run the tender scraper:
   python tender_scraper.py
4. After downloading tenders, process the BOQs:
   python check_boq.py

---

## 📝 Conclusion

The **Tender Automation Project** is designed to streamline the process of scraping tenders, extracting BOQ files, and identifying relevant items such as **DI Pipes** from government procurement data. This automation tool saves time and effort by processing large amounts of tender data efficiently.

Feel free to use, improve, or contribute to this project. Contributions are welcome, and feedback is appreciated. Together, we can make this tool even better!

Happy coding! 🚀
