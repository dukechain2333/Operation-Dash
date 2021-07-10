#  @author ZHChain
#  @File:Main.py
#  @createTime 2021/01/12 21:20:12

from Electing import *
from BasicInfoGetter import *
from datetime import datetime
import Data
import logging
import time

if __name__ == '__main__':
    logging.captureWarnings(True)
    # 判断程序运行条件是否达标
    assert len(Data.userName) > 0 and len(Data.passWord) > 0, '请先转到Data.py填入学生用户名与密码！'
    assert len(Data.coursePool) != 0, '选课池内缺少课程，请前往Data.py中填入用户名与课程ID！'
    assert (datetime(Data.startTime[0], Data.startTime[1], Data.startTime[2], Data.startTime[3], Data.startTime[4],
                     Data.startTime[5]) - datetime.now()).total_seconds() > 0, '选课开始时间已过时，请重新去Data.py设定一个未来的时间点!'

    # 创建课程线程池并实例化对象
    targetPool = []
    for courseNum in range(len(Data.coursePool)):
        targetPool.append(Electing(Data.coursePool[courseNum]))

    # 创建cookie对象
    info = infoInit(Data.urlMain, Data.userName, Data.passWord)

    # 设置程序休眠机制
    timeSleep = (datetime(Data.startTime[0], Data.startTime[1], Data.startTime[2], Data.startTime[3], Data.startTime[4],
                          Data.startTime[5]) - datetime.now()).total_seconds()

    print('距离选课开始还有' + str(timeSleep) + '秒，程序将进入休眠状态，请勿关闭程序！')
    time.sleep(int(timeSleep))

    print('\033[1;30;42m 选课开始！\033[0m')

    print('正在试图获取cookie!系统可能出现卡顿，请耐心等待（实际情况依运行设备和网络环境决定）..........')

    # 运行获取cookie
    info.main()

    # 发送选课请求线程运行
    for target in targetPool:
        target.start()

    for target in targetPool:
        target.join()

    print('\033[1;30;42m All done! 请查看选课页面做最后确认！\033[0m')
