Goatlings Shop Parser
=====================

A simple Python script to help Goatlings players organize their shop inventory.

Safety & Running Scripts
------------------------

It's great that you're interested in using a tool to make your game experience better! However, it's very important to be careful when running scripts or programs you find online. Since many people in the community might not be familiar with coding, here are a few tips to help you stay safe.

**1\. Understand What the Script Does (and Doesn't Do)**Before running anything, read the description. A trustworthy script will tell you exactly what it does. This script, for example, is designed _only_ to read a file you've already saved on your computer (shop.htm) and write a new file (shop.csv). It **does not** connect to the internet, it **does not** ask for your Goatlings password, and it **does not** interact with the Goatlings website at all. That's how you know it's safe. But don’t take my word for it! Look through it yourself, and use some of the checks described in the next section.

**2\. How to Spot a Potentially Unsafe Script (Even if You Don't Code)**You can open the .py script file in a simple text editor (like Notepad) and look for suspicious keywords. Be very careful if you see a script that contains words related to:

*   **Logging in:** password, username, login
    
*   **Sending data online:** requests, http, post, upload, socket
    

Seeing these doesn't automatically mean a script is malicious, but if a simple tool for local file sorting has them, it's a huge red flag. This script only uses functions for opening (open), reading (read), and writing (write) files on your computer, which is exactly what it promises to do.

If you’re not 100% sure what a script does or how it works, there are a couple things you can do to see. You can upload it to a free service like Virustotal to check for malicious code, or send a copy of the script to an AI like ChatGPT or Gemini and have it explain to you what running the code on your device will do, line by line if you want it to. Err on the side of caution, don’t run anything on your device that you aren’t 100% comfortable running. This also applies to running command line prompts or Powershell prompts, make sure you know exactly what it’s doing before you run it, _**especially**_ if you need administrator permission.

One of the best things about sharing code on a platform like GitHub is that it's completely open for public review. Anyone can look at the code to verify that it's safe. Always prefer tools that are open-source and have clear explanations over downloading random programs from unknown links.

Features
--------

*   Parses item name, price, stock, value, and description.
    
*   Works entirely offline with a local shop.htm file.
    
*   **Does not interact with Goatlings servers** and is safe to use according to the site's Terms of Service to the best of my knowledge.
    

How to Use
----------

1.  **Install Python:** If you don't already have it, download and install Python from [python.org](https://www.python.org/downloads/).
    
2.  pip install beautifulsoup4
    
3.  **Download the Script:** Download the goatlings\_parser.py file from this repository and place it in a folder on your computer.
    
4.  **Save Your Shop Page:**
    
    *   Go to your shop's inventory page on Goatlings.
        
    *   Right-click anywhere on the page and select "Save As..." or press Ctrl+S.
        
    *   Save the file as shop.htm in the **exact same folder** where you put the Python script.
        
5.  python goatlings\_parser.py
    
6.  **Find Your CSV:** The script will ask you to enter a folder path. After you provide one, it will create a shop.csv file in that location. If you leave the path blank and press Enter, the file will be saved in the same folder as the script.
    

How to Use the CSV Data (Importing into Spreadsheets)
-----------------------------------------------------

Once you have your shop.csv file, you can import it into a spreadsheet program to sort and analyze your data. Here’s how to do it in a few popular applications.

### Google Sheets (Free, Web-Based)

1.  Open [Google Sheets](https://sheets.google.com).
    
2.  Start a new blank spreadsheet.
    
3.  Go to File -> Import.
    
4.  Click on the Upload tab and select your shop.csv file.
    
5.  An "Import file" window will appear. Google Sheets is usually smart enough to detect the settings automatically. Just click Import data.
    

The advantage is being able to easily access and store the data on your Google account if you have one.

### Microsoft Excel (Paid)

1.  Open Excel and create a new blank workbook.
    
2.  Go to the Data tab on the ribbon.
    
3.  Click From Text/CSV.
    
4.  Find and select your shop.csv file.
    
5.  An import window will appear, showing you a preview. It should correctly identify the comma as the delimiter.
    
6.  Click Load. Your data will now be in the spreadsheet.
    

The advantage is having the most cohesive and professional set of spreadsheet management actions on the market.

### LibreOffice Calc (Free, Open-Source)

1.  Open LibreOffice Calc.
    
2.  Go to File -> Open... and select your shop.csv file.
    
3.  A "Text Import" wizard will open.
    
4.  In the "Separator Options," make sure that only Comma is checked.
    
5.  Click OK.
    

The advantage is running a free program locally on your computer.

Where to Get Spreadsheet Software
---------------------------------

*   **Google Sheets:** Free with a Google account. It runs directly in your web browser, so there's nothing to install. You can access it at [sheets.google.com](https://sheets.google.com).
    
*   **LibreOffice:** A free and open-source office suite that is a popular alternative to Microsoft Office. You can download it for free from the [official LibreOffice website](https://www.libreoffice.org/download/download-libreoffice/).
    
*   **Microsoft Excel:** Part of the paid Microsoft 365 (formerly Office 365) suite. You can find purchasing options on the [official Microsoft website](https://www.microsoft.com/en-us/microsoft-365/excel).
    

Disclaimer
----------

This tool is for personal, offline use only. It does not automate any gameplay, interact with the Goatlings website, or violate the Terms of Service to the best of my knowledge. It simply helps you organize data you have already accessed.
