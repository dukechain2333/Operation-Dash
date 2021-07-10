#  @author ZHChain
#  @File:Electing.py
#  @createTime 2021/01/12 20:15:12

import Data
import logging
import requests
import threading
import pandas as pd


class Electing(threading.Thread):
    """
    核心选课类
    """

    def __init__(self, courseID):
        super().__init__()
        self.data = pd.read_csv('CourseList.csv', index_col=None, encoding='gbk')
        assert courseID in list(self.data['CourseId']), "CourseID:" + str(courseID) + "的课程不在可选课程内！"
        self.courseID = courseID

    def electCourse(self, threadID):
        """
        选课函数

        Args:
            threadID:线程ID

        Returns:
            None
        """
        url = 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!batchOperator.action?profileId=167'
        data = Data.data
        data['operator0'] = str(self.courseID) + ':true:0'
        # print(data)
        # 发送选课请求
        try:
            response = requests.post(url=url, data=data, headers=Data.headerMain, verify=False)
        except:
            print('\033[1;30;41m 网络阻塞，请检查网络!\033[0m')

        print('\033[1;30;42m' + str(self.courseID) + '课程第' + str(threadID) + '号线程选课成功！' + '\033[0m')

    def refundCourse(self, threadID):
        """
        退课函数

        Args:
            threadID:线程ID

        Returns:
            None
        """
        url = 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!batchOperator.action?profileId=167'
        data = Data.data
        data['operator0'] = str(self.courseID) + ':false'
        # print(data)
        # 发送退课请求
        try:
            response = requests.post(url=url, data=data, headers=Data.headerMain, verify=False)
        except:
            print('\033[1;30;41m 网络阻塞，请检查网络!\033[0m')

        print('\033[1;30;42m' + str(self.courseID) + '课程第' + str(threadID) + '号线程退课成功！' + '\033[0m')

    def run(self):
        threads = []
        logging.captureWarnings(True)
        try:
            for i in range(0, Data.threadNum):
                threads.append(threading.Thread(target=self.electCourse, args=(i,)))
                # 退课选项
                # threads.append(threading.Thread(target=self.refundCourse, args=(i,)))
                threads[i].start()

            for t in threads:
                t.join()

        except Exception:
            print('\033[1;30;43m 线程阻塞！请耐心等待!\033[0m')
