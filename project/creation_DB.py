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
    path = r"\static\game.db"

    table_game = """CREATE TABLE 'game' (
                	'Name' TEXT(20) DEFAULT 'The web tech smash',
                	'Nbgame' INT(8),
                	'NbWinPlayer1' INT(8),
                	'NbWinPlayer2' INT(8),
                	'AverageTime' INT(20),
                	PRIMARY KEY ('Name'));"""

    table_characters = """CREATE TABLE 'Characters' (
                    	'id' INT(5) NOT NULL AUTO_INCREMENT,
                    	'Name' TEXT,
                    	'Path picture' TEXT,
                    	'NbUse' INT(10),
                    	PRIMARY KEY ('id'));"""

    table_map = """CREATE TABLE 'Map' (
                    	'id' INT(5) NOT NULL AUTO_INCREMENT,
                    	'Name' TEXT,
                    	'Path picture' TEXT,
                    	'NbUse' INT(10),
                    	PRIMARY KEY ('id'));"""
    table_match = """CREATE TABLE 'Match' (
	                   'Player1Win' BOOLEAN,
                    	'Player2Win' BOOLEAN,
                    	'NbHitPlayer1' INT,
                    	'NbHitPlayer2' INT,
                    	'Time' INT,
                    	'ID' INT NOT NULL AUTO_INCREMENT,
                    	PRIMARY KEY ('ID'));"""

    connection = create_connection(path)

    # create tables
    if connection is not None:
        # create projects table
        creation_table(connection, table_game)
        creation_table(connection, table_characters)
        creation_table(connection, table_map)
        creation_table(connection, table_match)
    else:
        print("no connection.")

if __name__ == '__main__':
    main()
