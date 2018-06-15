#from Connection import *
import Connection

def stringMatching(stringInput):
    connectionObj=Connection.Config()
    cursor=connectionObj.cursor
    str1=stringInput
    flag=0
    
    if flag==0:
        index=1
        cursor.execute("select count(*) from user_commands;")
        table_row=cursor.fetchone()
        
        while index<=table_row[0]:
            sql2="select command,cmdvalue from user_commands where id='"+str(index)+"'"
            cursor.execute(sql2)
            query_row=cursor.fetchone()            
            str2=query_row[0]
            if (str1==str2):
                return query_row[1]
            else:
                flag=1
            index+=1
    if flag==1:
        b= stringMatching2(str1)
        return b

def stringMatching2(stringInput):
    connectionObj=Connection.Config()
    cursor=connectionObj.cursor
    db=connectionObj.db

    flag = 0
    c=0
    pasString=''
    savestate = 0
    start = 1
    cursor.execute("select count(*) from commands;")
    table_row=cursor.fetchone()
    strInput=stringInput.split()
    while(start <= table_row[0]):
        cursor.execute("select command from commands where id='"+str(start)+"'")
        query_row=cursor.fetchone()
        selectedString=query_row[0]
        str1=selectedString.split()
        a=0
        while(a<len(str1)):
            b=0
            while(b<len(strInput)):
                if flag == 1:
                    if strInput[b] == str1[c]:
                        pasString+=strInput[b]+' '
                        c+=1
                        if pasString.rstrip()==selectedString:
                                sql2 = "select cmdvalue from commands where id='" + str(start) + "'"
                                cursor.execute(sql2)
                                query_row = cursor.fetchone()
                                returnValue=query_row[0]
                                str2 = "insert into user_commands(command,cmdvalue) values('" + stringInput + "'," + str(returnValue) + ");"
                                try:
                                    cursor.execute(str2)
                                    db.commit()
                                except:
                                    db.rollback()
                                return query_row[0]
                    else:
                        b = savestate
                        flag = 0
                        c=0
                        break
                else:
                    if(str1[a] == strInput[b]):
                        savestate = b
                        pasString=''
                        b-=1
                        flag = 1                       
                b+=1
            a+=1
        start+=1
