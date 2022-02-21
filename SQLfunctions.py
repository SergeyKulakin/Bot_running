import sqlite3

token = "2073864492:AAH0ksHyEU_9fR-EEVV0_ANe110e0GSWbvM"
#--------------------------------
# Функции работы с БД

def commit(query, msg, text):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(query, (msg.from_user.id, text))
        con.commit()

# добавить пробежку в БД
def insertRunIntoDB(msg, text):
    commit('INSERT INTO runningData (user_id, run) VALUES (?, ?)', (msg.from_user.id, text))

# добавить награду в БД
def insertRewardIntoDB(msg, reward):
    commit('INSERT INTO rewardData (user_id, reward) VALUES (?, ?)', (msg.from_user.id, reward))

# выбрать все пробежки из БД
def selectRunsfromDB(msg):
    commit('SELECT run FROM runningData WHERE user_id=={}'.format(msg.from_user.id))


# выбрать все награды из БД
def selectRewardsfromDB(msg):
        commit('SELECT reward FROM rewardData WHERE user_id=={}'.format(msg.from_user.id))

# удаление пробежки из БД
def deleteRunFromDB(msg):
    commit('DELETE FROM runningData WHERE user_id == ? AND run == ?', (msg.from_user.id, msg.text))

# удаление всех пробежек из БД
def deleteAllRunsFromDB(msg):
    commit('DELETE FROM runningData WHERE user_id =={}'.format(msg.from_user.id))

# удаление всех наград из БД
def deleteAllRewardsFromDB(msg):
    commit('DELETE FROM rewardData WHERE user_id =={}'.format(msg.from_user.id))
#--------------------------------