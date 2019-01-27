# tcping TOOL
restart = 0
import os

while restart == 0:
    ipaddress = input("tcping 목적지 IP 주소 및 포트 입력: ")
    command = "tcping " + ipaddress
    os.system(command)
    input()
    os.system("CLS")