from bs4 import BeautifulSoup
import requests, openpyxl
import pandas, numpy


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "phone_name"
sheet.append(['phone_name'])

try:
    response = requests.get("https://www.gsmarena.com/makers.php3")
    soupe = BeautifulSoup(response.text, 'html.parser')
    #print(soupe)

    mobile = soupe.find("div", class_ = 'st-text').find_all('td')
    #print(mobile)

    for phone in mobile:
        phone_name = phone.find('a').text
        #print(phone_name)
        sheet.append([phone_name])

except Exception as e:
    print(e)
    
excel.save('Phone_name.xlsx')





