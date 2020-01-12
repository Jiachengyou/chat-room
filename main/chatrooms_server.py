import mysql.connector
import os
from termcolor import colored,cprint

'''YOUR DATABASE DETAILS'''
chatroom_serv=mysql.connector.connect(
    host=os.getenv('HOST', None),
    user=os.getenv("USER", None),
    passwd=os.getenv('PASSWORD', None),

    database = 'user_info'
)
# print(os.getenv('USER', None))

rooms=chatroom_serv.cursor()

def all_rooms():
    room_list=[]
    rooms.execute("SELECT server_rooms FROM chatserver")
    chat_rooms_list=rooms.fetchall()
    for i in range(len(chat_rooms_list)):
        room_list.append(chat_rooms_list[i][0])
    return room_list

def new_room(room_name):
    sql= "INSERT INTO chatserver (server_rooms, id) VALUE (%s, %s)"
    val=(room_name, 0)

    rooms.execute(sql,val)
    chatroom_serv.commit()

def insert_message(val):
    sql = "INSERT INTO messages (id,server_rooms,user, message) VALUE (%s, %s, %s, %s)"
    rooms.execute(sql,val)
    chatroom_serv.commit()

def get_message(chatroom):
    # print("Message history:")
    # fuck this bug
    sql = "SELECT user, message FROM messages WHERE server_rooms = '{0}'".format(chatroom)
    rooms.execute(sql)
    message_list=rooms.fetchall()
    for i in range(len(message_list)):
        print(colored("[{}]: {}".format(message_list[i][0], message_list[i][1]), "yellow"))
        


    