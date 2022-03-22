import sqlite3

# cursor.execute('''CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     username VARCHAR(50) UNIQUE NOT NULL,
#     password VARCHAR(50),
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     email VARCHAR(50) UNIQUE NOT NULL
# )
#                    ''')

# cursor.execute('''CREATE TABLE results (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER REFERENCES users(id) NOT NULL,
#     result TEXT NOT NULL,
#     opponent VARCHAR(50) NOT NULL,
#     turns INTEGER NOT NULL
# )
#                    ''')

# cursor.execute('''PRAGMA auto_vacuum = full
#                    ''')

def add_user(user_id, username, password, first_name, last_name, email):
    connection = sqlite3.connect('connect_four.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO users
               VALUES ({user_id}, '{username}', '{password}', '{first_name}', '{last_name}', '{email}')''')
    connection.commit()
    connection.close()

def add_result(result_id, user_id, result, opponent, turns):
    connection = sqlite3.connect('connect_four.db')
    cursor = connection.cursor()
    cursor.execute(f'''INSERT INTO results
               VALUES ({result_id}, {user_id}, '{result}', '{opponent}', {turns})''')
    connection.commit()
    connection.close()
    
def get_account_info(userid):
    connection = sqlite3.connect('connect_four.db')
    cursor = connection.cursor()
    info = cursor.execute(f'''SELECT users.username, 
                          COUNT(*) as games_played,
                          COUNT(*) FILTER (WHERE result = 'Win') as wins,
                          COUNT(*) FILTER (WHERE result = 'Loss') as losses,
                          COUNT(*) FILTER (WHERE result = 'Draw') as draws
                   FROM users, results
                   WHERE users.id = results.user_id
                   AND users.id = {userid}
                   GROUP BY 1
               ''').fetchone()
    connection.commit()
    connection.close()
    # simple print to display in user friendly way. All info is stored in info and select statemtn however
    print('Username: ', info[0])
    print('Games Played: ' , info[1])
    print('Games Won: ', info[2])
    print('Games Lost: ', info[3])
    print('Games Drawn: ', info[4])
    return info

def get_user_results(userid):
    connection = sqlite3.connect('connect_four.db')
    cursor = connection.cursor()
    info = cursor.execute(f'''SELECT opponent,
                          result, 
                          turns
                   FROM results
                   WHERE user_id = {userid}
               ''').fetchall()
    connection.commit()
    connection.close()
    # simple print to display in user friendly way. All info is stored in info and select statemtn however
    for r in info:
        print('Opponent: ', r[0])
        print('Result: ' , r[1])
        print('Turns: ', r[2])
    return info

def leaderboard1():
    connection = sqlite3.connect('connect_four.db')
    cursor = connection.cursor()
    info = cursor.execute(f'''SELECT users.username,
                          COUNT(*) AS wins
                   FROM users, results
                   WHERE users.id = results.user_id
                   AND results.result = 'Win'
                   GROUP BY 1
                   ORDER BY wins DESC
               ''').fetchall()
    connection.commit()
    connection.close()
    # simple print to display in user friendly way. All info is stored in info and select statemtn however
    for r in info:
        print('User: ', r[0])
        print('Total Wins: ' , r[1])
    return info
