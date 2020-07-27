#!/bin/bash
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
    msg = '�Զ������CI/CD����'
    title= "�Զ������CI/CD����:�����鿴�Զ�������"
    os.system("rm -rf reports")
    #os.system("rmdir/s /q reports")
    os.system("mkdir reports")
    dir = os.path.dirname(os.path.abspath("__name__"))
    test_path = os.path.join(dir,"testsuites","login_suit.yml")
    print(test_path)
    os.system(f"hrun % s" % test_path)
    #��ȡ���µĲ��Ա���
    lastest_report = os.listdir("./reports")[-1]
    #���ز��Ա��浽nginx��
    os.system(f"cp /data/project/python/workspace/hruntest/reports/*  /usr/local/docker/nginx_v/reports")
    #���Ͷ�������
    send_ding_msg(msg=msg,title=title,msg_url=f"http://139.9.179.188:8080/{lastest_report}")


