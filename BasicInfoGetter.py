#  @author ZHChain
#  @File:BasicInfoGetter.py
#  @createTime 2021/01/12 18:34:12

import json
import requests
from selenium import webdriver
import time
import Data
import re
import pandas as pd
import threading


class infoInit:
    """
    Cookies获取类
    """

    def __init__(self, url, user_name, pass_word):
        self.cookie = ''
        self.url = url
        self.userName = user_name
        self.passWord = pass_word

    def cookieGetter(self):
        """
        获取登陆用的Cookies
        cookies信息会被写入Cookie.txt中

        Args:
            None

        Returns:
            cookies:返回未经处理的cookies
        """
        # requests.session()

        # 登录校园网
        option = webdriver.ChromeOptions()
        # 设置option后台运行chrome
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        try:
            driver.get(self.url)
        except:
            print('\033[1;30;41m 网络阻塞，请检查网络!\033[0m')
        user_name_tag = driver.find_element_by_xpath('//*[@id="username"]')
        pass_word_tag = driver.find_element_by_xpath('//*[@id="password"]')
        user_name_tag.send_keys(self.userName)
        pass_word_tag.send_keys(self.passWord)
        button = driver.find_element_by_xpath('//*[@id="fm1"]/div[4]/div/input[5]')
        button.click()
        time.sleep(5)

        # 获取cookies并写入文件
        cookies = driver.get_cookies()
        with open('Cookie.txt', 'w') as file:
            json.dump(cookies, file)

        self.setCookie()
        self.cookie = cookies
        driver.quit()

        return cookies

    def setCookie(self):
        """
        设置header中的cookie

        Args:
            None

        Returns:
            cookie:返回处理完成的cookie
        """
        with open('Cookie.txt', 'r') as file:
            data = json.load(file)

        # print('jsessionid:', data[3]['value'])
        # print('urp_profile:', data[0]['value'])
        # print('urp_sid:', data[1]['value'])
        # print('serverid:', data[2]['value'])

        cookie = 'JSESSIONID=' + str(data[3]['value']) + '; URP_PROFILE=' + str(
            data[0]['value']) + 'semesterId%22%3A1640420201%7D%7D' + '; URP_SID=' + str(
            data[1]['value']) + '; SERVERID=' + str(data[2]['value'])

        Data.headerMain['Cookie'] = cookie
        Data.headerCourseList['Cookie'] = cookie

        print('\033[1;30;42m cookie获取完成！\033[0m')
        print('cookie:', cookie)

        return cookie

    def main(self):
        thread = []
        for i in range(0, Data.cookieGetNum):
            thread.append(
                threading.Thread(target=self.cookieGetter, args=()))
            thread[i].daemon = 1

        for i in range(len(thread)):
            thread[i].start()

        # for i in range(len(thread)):
        #     thread[i].join()

        while True:
            if len(self.cookie) > 0:
                break


class courseListGetter:
    """
    课程列表获取类
    """

    def __init__(self):
        pass

    def courseGetter(self):
        """
        获取原始选课列表

        Args:
            None

        Returns:
            courseData:原始选课文件
        """
        response = requests.get(url=Data.urlCourseList, headers=Data.headerCourseList, verify=False)
        with open('Source.txt', 'w', encoding='utf8') as file:
            file.write(response.text)
            print('033[1;30;42m 课程列表已保存！\033[0m')
        pattern = re.compile(
            "id:(.*?),no:'(.*?)',name:'(.*?)',code:'(.*?)',credits:(.?).*?,courseTypeName:'(.*?)',.*?,teachers:'(.*?)',"
            ".*?,arrangeInfo:\[(.*?)\]")
        courseData = re.findall(pattern, response.text)
        return courseData

    def courseList(self, courseData):
        """
        生成选课列表（CourseList.csv）

        Args:
            courseData:原始选课列表数据

        Returns:
            dataFrame:返回选课列表（pandas.DataFrame）
        """
        dfColumns = ['CourseId', 'CourseNo', 'CourseName', 'CourseCode', 'CourseCredits', 'CourseTypeName',
                     'CourseTeachers', 'CourseDay', 'StartUnit', 'EndUnit']
        dataFrame = pd.DataFrame(columns=dfColumns)
        pattern = re.compile("weekDay:(.*?),.*?,startUnit:(.*?),endUnit:(.*?),")
        partLen = 7  # 不算课程时间的元组长度
        for row in range(len(courseData)):
            data = []
            for i in range(0, partLen):
                data.append(courseData[row][i])
            # 检查是否有课程时间安排
            if len(courseData[row][7]) != 0:
                tmp = re.findall(pattern, courseData[row][7])
                for i in range(0, 3):
                    data.append(tmp[0][i])
            # 补齐空缺位
            else:
                for i in range(7, 10):
                    data.append(0)
            dataFrame.loc[row] = data
        print(dataFrame)
        dataFrame.to_csv('CourseList.csv', encoding='gbk')

        return dataFrame
