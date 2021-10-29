# WebScrapingSelenium
Case Study for AnalyticaHouse

Report -> https://1drv.ms/p/s!AkVMi-KPYsK3sVle13mryB_YTKCO?e=70g1C6

This project is a web scraping application that uses Python and Selenium tool. The URLs file is scanned and each URL that contains a product is searched for the following metrics: 
- Product Name
- Offer 
- Product Price
- Sale Price
- Product Availability
- Product Code

The scraped variables are written to Google Sheets using gspread library and a Google Cloud Platform service account for Google Drive and Google Sheets APIs. 


Data sheet is sorted using Google Apps Script code and the file can be sent to a mail provided in the code. 


-- Additional Questions -- 
1. If I’d have 10.000 urls that I should visit, then it takes hours to finish. What
can we make to fasten this process?

1000 urls take nearly 1.5 hours to finish for this project. To fasten it, multithreading can be used for larger projects.

2. What can we make or use to automate this process to run once a day?
Write your recommendations.

If the program is running on Windows, the Task Scheduler could be used. Or, the "schedule" library of Python could be called inside the main application code for scheduling it to run once a day. 

3. Please briefly explain what an API is and how it works.

API is an interface for communication between two applications as it can be understood from its name "Application Programming Interface". It works by requests and responses. The request asks for the data and if the request is valid, the response will be the data. 
