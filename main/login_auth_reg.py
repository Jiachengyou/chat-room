import mysql.connector
import os
import env_platform
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')
user_db=mysql.connector.connect(
    host=os.getenv('HOST', None),
    port=os.getenv('PORT'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD', None),
    database="user_info",
)


user_details=user_db.cursor()

def register( user_idf,name,username,passwd):

    sql="INSERT INTO user_info.user (name,username,passwod) VALUES (%s, %s, %s)"
    val=(name,username,passwd)
    
    try:
        user_details.execute(sql,val)
        user_db.commit()
        return 0
    except:
        return 1

def login(usrname,passwd):

    user_details.execute("SELECT username,passwod FROM user_info.user")
    result=user_details.fetchall()
    chk=0
    for i in range(len(result)):
        temp=[]
        temp=result[i]
        
        if temp[0]==usrname and temp[1]==passwd:
            chk=chk+1
        else:
            pass
    if chk>0:
        return 0
    else:
        return 1

def searchuser_password():

    user_details.execute("SELECT username,passwod FROM user_info.user")
    userinfo=user_details.fetchall()
    return userinfo

# def searchuser_password():
#     user_details.execute("SELECT username,passwod FROM user_info.user")
#     userinfo=user_details.fetchall()
#     return userinfo

'''
a=dict()
b=searchuser_password()
for i in range(len(b)):
    a[b[i][0]]=b[i][1]
print(a)
'''