from plyer import notification
import requests 
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\Coding Playground\COVID-19 LiveCase Notifier\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
   # notifyMe("Faisal","Lets stop the spread of this virus together")
        myHTMLData = getData("https://www.mohfw.gov.in/")
        
        soup = BeautifulSoup(myHTMLData, 'html.parser')
        table = soup.find_all( "table", attrs = {"class":"table table-striped table-dark"} )
        myDataStr = ""
        for tr  in soup.find_all('table')[7].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")


        states = ['Delhi','Bihar','Maharashtra']
        for item in itemList[0:27]:
            dataList = item.split('\n')
            if dataList[1] in states:
                
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)



    
