import sqlite3

with open('pass.txt') as file:
    token = file.readline().strip()

#--------------------------------
# Функции работы с БД

def insert_run_into_db(msg, text):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO runningData (user_id, run) VALUES (?, ?)', (msg.from_user.id, text))
        con.commit()

def insert_reward_into_db(msg, reward):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('INSERT INTO rewardData (user_id, reward) VALUES (?, ?)',(msg.from_user.id, reward))
        con.commit()

def select_runs_from_db(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT run FROM runningData WHERE user_id=={msg.from_user.id}')
        runsList = cursor.fetchall()
        return runsList

def select_rewards_from_db(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT reward FROM rewardData WHERE user_id=={msg.from_user.id}')
        rewardList = cursor.fetchall()
        return rewardList

def delete_run_from_db(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute('DELETE FROM runningData WHERE user_id == ? AND run == ?', (msg.from_user.id, msg.text))

def delete_all_runs_from_db(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM runningData WHERE user_id =={msg.from_user.id}')

def delete_all_rewards_from_db(msg):
    with sqlite3.connect('running.db') as con:
        cursor = con.cursor()
        cursor.execute(f'DELETE FROM rewardData WHERE user_id =={msg.from_user.id}')
#-------------------------------