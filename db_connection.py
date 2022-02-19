import sqlite3

token = "2073864492:AAH0ksHyEU_9fR-EEVV0_ANe110e0GSWbvM"
#--------------------------------
# Функции работы с БД

def insertRunIntoBD(msg, text):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO runningData (user_id, run) VALUES (?, ?)', (msg.from_user.id, text))
        con.commit()

def insertRewardIntoBD(msg, reward):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO rewardData (user_id, reward) VALUES (?, ?)',(msg.from_user.id, reward))
        con.commit()

def selectRunsfromBD(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT run FROM runningData WHERE user_id=={msg.from_user.id}')
        runsList = cursor.fetchall()
        return runsList

def selectRewardsfromBD(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT reward FROM rewardData WHERE user_id=={msg.from_user.id}')
        rewardList = cursor.fetchall()
        return rewardList

def deleteRunFromBD(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM runningData WHERE user_id == ? AND run == ?', (msg.from_user.id, msg.text))

def deleteAllRunsFromBD(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM runningData WHERE user_id =={msg.from_user.id}')

def deleteAllRewardsFromBD(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM rewardData WHERE user_id =={msg.from_user.id}')
#--------------------------------