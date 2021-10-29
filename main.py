import openpyxl
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common.exceptions import NoSuchElementException

#Credentials and auth for Google sheets
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)

BASE_URL = "https://www.markastok.com"
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
row_index = 2

#Read excel file
file = Path('C:\\Users\\HP\\PycharmProjects\\pythonProject', "URL.xlsx")
urls = openpyxl.load_workbook(file)

urls_sheet = urls.active
sheet = client.open("Markastok Ürün Raporu").sheet1
sheet.insert_row(["URL","Product Name", "Offer", "Product Price", "Sale Price", "Availability", "Product Code"], 1)
#Iterate through URl list
for row in urls_sheet.iter_rows(max_row=1000):
    url = row[0].value
    main_url = BASE_URL + url
    driver.get(main_url)
    #Find product page
    try:
        name = driver.find_element(By.ID, "product-name")
        #Find if product is available
        try:
            offer = driver.find_element(By.CLASS_NAME, "detay-indirim").text
            productPrice = driver.find_element(By.CLASS_NAME, "currencyPrice").text
            salePrice = driver.find_element(By.CLASS_NAME, "product-price").text
        #If not available, fill with null prices
        except NoSuchElementException:
            offer = "null"
            productPrice = "null"
            salePrice = "null"

        #Get product feature text and split
        sku = driver.find_element(By.CLASS_NAME, "product-feature-content")
        split_sku = sku.text.split("\n\n")
        productNumber = split_sku[-1].split("\n")[-1]

        #Calculate availability
        availability = driver.find_element(By.CLASS_NAME, "new-size-variant")
        availability_text = availability.get_attribute("innerHTML")
        count = 0
        availability_text = availability_text.split("<a")
        for word in availability_text:
            if "passive" in word:
                count += 1
        avl_count = (100-((count / (len(availability_text)-1))*100))
        # Insert Row to Google Sheets
        insertRow = [main_url, name.text, offer, productPrice, salePrice, avl_count, productNumber]

        sheet.insert_row(insertRow, row_index)
        row_index += 1
    #If not product, pass
    except NoSuchElementException:
        pass

driver.quit()
