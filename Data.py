#  @author ZHChain
#  @File:Data.py
#  @createTime 2021/01/12 20:22:12

import BasicInfoGetter

# 在此输入你的用户名与密码
userName = ''
passWord = ''

# 在此输入你要选的课的ID，输入前请仔细查看可选课程列表（CourseList.csv）
# 例：coursePool = [23124, 23412, 45632]
coursePool = []

# 在此填入选课开始时间
# 例2021年1月5日21：05：12
startTime = (2021, 1, 5, 21, 5, 12)

# 下面的内容只有你知道这是什么的时候才能改
threadNum = 100
cookieGetNum = 20  # 要是你内存大可以适当改大一点，会提升选课体验:)

# 下面的内容不要动！
headerMain = {
    'Host': 'lxjw.lixin.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '24',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://lxjw.lixin.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!defaultPage.action?electionProfile.id=167',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': ''
}

headerCourseList = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'If-None-Match': '1610430476642_397741',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!defaultPage.action?electionProfile.id=167',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': ''
}

data = {
    'operator0': ''
}

urlMain = 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!defaultPage.action?electionProfile.id=167'
urlCourseList = 'https://lxjw.lixin.edu.cn/edu/lesson/std/std-elect-course!data.action?profileId=167'
