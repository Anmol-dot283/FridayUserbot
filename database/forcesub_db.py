from re import L, U
from sqlite3.dbapi2 import Cursor, connect
from system.datas_sqlite import Connect
from collections import OrderedDict
from sqlite3 import OperationalError
conn =  Connect()

CHANNEL_ = {}
CHANNEL = []
c = conn.cursor()

import sqlite3
def Connect():
    conn = sqlite3.connect(f"forcesub.db")
    return conn

    
conn = Connect()
c = conn.cursor()





def CreateTable():
  try:
    conn.execute(f"""CREATE TABLE chats (
    chat TEXT, 
    channels TEXT
    )""")
#   conn.execute(f"""CREATE TABLE channels (
#     channel TEXT
#     )""")
  except OperationalError:
      pass
  try:
   conn.execute(f"""CREATE TABLE safe_user (
    id TEXT 
    )""")
  except OperationalError:
      pass
  conn.commit()

try:
 CreateTable()
except OperationalError:
    pass


def CreateSafeUser(ida):
    ids=ida
    c.execute("INSERT INTO safe_user VALUES (?)", ((ids,)))
    conn.commit()





def Allchats(channel = None):
#    //
        
    # insert_chet(["@tea_timea", "@black_lightning_channel"])
    c.execute("SELECT * FROM chats")
    s = c.fetchall()
    return list(s)

def AllsafeUsers():
    #    //
        
    c.execute("SELECT * FROM safe_user")
    s = c.fetchall()
    return list(s)


chats = []
for i in Allchats():
   a=(i[0])
   chats.append(a)

safe_users = []
for i in AllsafeUsers():
    a=(i[0])
    safe_users.append(a)


def chet(username  = None, id:bool=False):

    c.execute("SELECT channels FROM chats")     
    return c.fetchall()

def get_safe_user(id_):

    ids = [] 

    c.execute(f"SELECT * FROM safe_user WHERE id == '%{id_}%'")
    a = c.fetchall()
    for i in a:
        ids.append(i[0])
    
    if id_ in ids:
        return True
    else:
        return False
 
safe = []
for i in  get_safe_user():
    safe.append(i[0])
safeniggas = list(OrderedDict.fromkeys(safe))

def insert_chet(chat, channel):
    
    c.execute("INSERT INTO chats VALUES (?, ?)", (chat, channel))


    conn.commit()



d ={}
ah=c.execute("SELECT * FROM chats")     
ah=c.fetchall()
for i in ah:
         d.update({
         f'{i[0]}': f'{i[1]}',})

    
CreateTable()
