#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import unittest
from time import sleep

class testDouyu(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        #self.driver = webdriver.PhantomJS()
    def testCase(self):

        #截取全屏
        self.driver.save_screenshot("1.png")
        self.driver.get("https://www.douyu.com/directory/all")
        while True:

            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            roomTypeList = soup.find_all("span",{"class":"tag ellipsis"})
            list1 = []
            list2 = []
            list3 = []
            for roomTypeName in roomTypeList:
                list1.append(roomTypeName.get_text())
            renqiNameList = soup.find_all("span", {"class": "dy-num fr"})
            for renqi in renqiNameList:
                list2.append(renqi.get_text())
            roomNameList = soup.find_all("h3", {"class": "ellipsis"})
            for roomName in roomNameList:
                list3.append(roomName.get_text())
            #获取三个值
            for i in range(len(list2)):
                print(list3[i].strip()+"\t\t\t\t"+list1[i].strip()+"\t"+list2[i])

            if self.driver.page_source.find("shark-pager-next shark-pager-disable shark-pager-disable-next") != -1:
                break
            elif self.isElementExist()==True:
                self.driver.find_element_by_class_name("shark-pager-next").click()
                sleep(2)
            else:
                print("没找到元素！")

                #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def isElementExist(self):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_class_name("shark-pager-next")
            return flag

        except:
            flag = False
            return flag

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()