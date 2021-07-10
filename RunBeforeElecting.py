#  @author ZHChain
#  @File:RunBeforeElecting.py
#  @createTime 2021/01/13 09:06:13


from BasicInfoGetter import *
import Data
import logging

"""
本文件用于在第一次选课期间（通常不采用先到先得）获取可选课程列表以供参考
"""

if __name__ == '__main__':
    logging.captureWarnings(True)
    assert len(Data.userName) > 0 and len(Data.passWord) > 0, '请先转到Data.py填入学生用户名与密码！'

    # 创建cookie对象并获取cookie
    info = infoInit(Data.urlMain, Data.userName, Data.passWord)
    info.main()

    # 创建courseList实例并获取courseList
    cList = courseListGetter()
    data = cList.courseGetter()
    cList.courseList(data)
    print('\033[1;30;42m 本学期可选课程列表已经生成，请在CourseList.csv中查看！\033[0m')
