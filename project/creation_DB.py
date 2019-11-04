import sqlite3
from sqlite3 import Error


def create_connection(file):
    connect = None
    try:
        connect = sqlite3.connect(file)
    except Error as e:
        print(e)
        raise e
    return connect

def creation_table(connect,creation_table):
    try:
        conn = connect.cursor()
        conn.execute(creation_table)
    except Error as e:
        print(e)
        raise e
def main():

    table_game == """CREATE TABLE 'game' (
                	'Name' TEXT(20) DEFAULT 'The web tech smash',
                	'Nbgame' INT(8),
                	'NbWinPlayer1' INT(8),
                	'NbWinPlayer2' INT(8),
                	'AverageTime' INT(20),
                	PRIMARY KEY ('Name'));"""
    table_

if __name__ == '__main__':
    create_connection(r"game.db")
