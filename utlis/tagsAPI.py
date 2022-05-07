import requests
import re

APIKEY = '65c425a0f1mshc61460168d6ff78p1c4feejsn34a46948cd22'

class TagsAPI:

    def __init__(self, listLength):
        self.listLength = listLength
        self.url = "https://tasty.p.rapidapi.com/tags/list"
        self.headers = {
                "X-RapidAPI-Host": "tasty.p.rapidapi.com",
                "X-RapidAPI-Key": APIKEY
        }
        self.response = requests.request("GET", self.url, headers=self.headers)


    def UrlList(self, list):
        urlList = []
        for i in list:
            i = re.sub(r"[^\w\s]", '', i)
            i = "_".join(i.split())
            urlList.append(i.lower())
        return(urlList)

    def DisplayList(self, type, remove = []):
        tags = self.response.json()
        displayList = []
        for i in tags["results"]:
            x = i.get("type")
            if x == type:
                item = i.get('display_name')
                displayList.append(item)

        return(displayList[:self.listLength])    

    def List(self, type, remove = []):
        displayList = self.DisplayList(type)
        urlList = self.UrlList(displayList)
        list = []
        for index, i in enumerate(displayList):
            item = {'display': i, 'url': urlList[index]}
            list.append(item)
    
        return(list)



    # def HolidayList():
    #     removeHoliday = ['Pride Month','Black History Month', 'Asian Pacific American Heritage Month']
    #     tags = response.json()
    #     holidayList = []
    #     for i in tags["results"]:
    #         x = i.get("type")
    #         if x == "holiday":
    #             holiday = i.get('display_name')
    #             holidayList.append(holiday)
        
    #     for i in holidayList:
    #         for x in removeHoliday:
    #             if i == x:
    #                 holidayList.remove(i)
    #     return(holidayList[:listLength])
