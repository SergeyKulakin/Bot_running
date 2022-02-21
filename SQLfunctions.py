import sqlite3

token = "2073864492:AAH0ksHyEU_9fR-EEVV0_ANe110e0GSWbvM"
#--------------------------------
# Функции работы с БД

# добавить пробежку в БД
def insertRunIntoDB(msg, text):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO runningData (user_id, run) VALUES (?, ?)', (msg.from_user.id, text))
        con.commit()

# добавить награду в БД
def insertRewardIntoDB(msg, reward):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO rewardData (user_id, reward) VALUES (?, ?)',(msg.from_user.id, reward))
        con.commit()

# выбрать все пробежки из БД
def selectRunsfromDB(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT run FROM runningData WHERE user_id=={}'.format(msg.from_user.id))
        runsList = cursor.fetchall()
        return runsList

# выбрать все награды из БД
def selectRewardsfromDB(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT reward FROM rewardData WHERE user_id=={}'.format(msg.from_user.id))
        rewardList = cursor.fetchall()
        return rewardList

# удаление пробежки из БД
def deleteRunFromDB(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM runningData WHERE user_id == ? AND run == ?', (msg.from_user.id, msg.text))

# удаление всех пробежек из БД
def deleteAllRunsFromDB(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM runningData WHERE user_id =={}'.format(msg.from_user.id))

# удаление всех наград из БД
def deleteAllRewardsFromDB(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM rewardData WHERE user_id =={}'.format(msg.from_user.id))
#--------------------------------