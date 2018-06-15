from socket import *
import pymysql
import splitter
import threading
import actions
import time
import api

flag = 1
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
#tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

m=threading.Thread(target=api.apiRefresh,args=())
m.start()
while True:
    if flag != 0:
        try:
            #check how much time for the server waited
            
            tcpCliSock, addr = tcpSerSock.accept()
            time.sleep(0.01)
            data=''
            data = tcpCliSock.recv(BUFSIZE).decode()
            actions.act(str(splitter.stringMatching(data)),data)
            
        except Exception as e:
            flag = 0
    else:
        try:
            conn = pymysql.connect("50.62.209.121","mypatshala","Sagar@Rohit1","qwala",connect_timeout=2)
            cursor = conn.cursor()
            cursor.execute("select count(*) from searchdb;")
            count = cursor.fetchone()
            if count[0] > 0:
                count_inc = 1
                count_chk = 0
                while count_chk != count[0]:
                    sql1 = "select query from searchdb where id = %d" % count_inc
                    count_chk = count_inc
                    cursor.execute(sql1)
                    result = cursor.fetchone()
                    #splitter.stringMatching(result)
                    print("result is %s" % result)
                    count_inc += 1
                cursor.execute("truncate searchdb;")
                count_chk = 0
                count_inc = 1
            flag = 1
        except:
            flag = 1
tcpSerSock.close()
