#!/bin/bash
#coding=utf-8
import os
import requests
def send_ding_msg(msg,title,msg_url):
    url = "https://oapi.dingtalk.com/robot/send?access_token=93fe896e9a02d9343c3b9dc6d5e80eb87374199060051c6398711fc0d8b2a3c9"
    headers = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    ding_msg = {
        "msgtype":"link",
        "link":{
            "text":msg,
            "title":title,
            "messageUrl":msg_url
        }

    }
    requests.post(url=url,json=ding_msg,headers=headers)

if __name__ == "__main__":
    msg = '自动化测试报告CI/CD提醒'
    title= "自动化测试报告CI/CD提醒:请点击查看自动化报告"
    os.system("rm -rf reports")
    #os.system("rmdir/s /q reports")
    os.system("mkdir reports")
    dir = os.path.dirname(os.path.abspath("__name__"))
    test_path = os.path.join(dir,"testsuites","login_suit.yml")
    print(test_path)
    os.system(f"hrun % s" % test_path)
    #获取最新的测试报告
    lastest_report = os.listdir("./reports")[-1]
    #挂载测试报告到nginx下
    os.system("cp /data/project/python/workspace/hruntest/reports/*  /usr/local/docker/nginx_v/reports")
    #发送钉钉报告
    send_ding_msg(msg=msg,title=title,msg_url=f"http://139.9.179.188:8081/{lastest_report}")


