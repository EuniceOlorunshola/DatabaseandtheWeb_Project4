# import the mongoClient class from the pymongo library
from pymongo import MongoClient
# use sys for system arguments passed to script
import sys
# connect to the MongoDB server
myclient = MongoClient('mongodb://localhost:27017/')
# create a database called baseballDB
mydb = myclient["baseballDB"]
# Clear the collections before loading data
mydb["teams"].drop()
mydb["games"].drop()
# Use create_index method to set team code as primary key
mydb.teams.create_index("code", unique=True)
# Load the teams and games data from the input file and insert it into the collections
teams_data = open(sys.argv[1], 'r')
games_data = open(sys.argv[2], 'r')
# If the length of the argument in the command line is less then 3 it shows the print statement
if len(sys.argv) < 3:
    print("Python program file , teams.dat and games.dat file name should be included in the command line argument in the terminal Ex: python3(This is the version of python I am using) loadData.py teams.dat games.dat")

# Parse the teams data and insert into the teams collection
teams = {}
for line in teams_data:
    # These belong in the rows for the teams data that will be inserted into the teams collection
    name, location, team_code = line.strip().split(":")
    teams[team_code] = {"teamname": name, "teamlocation": location, "code": team_code}
    # inserts the new document into the teams collection and creates a new collection
    mydb["teams"].insert_one(teams[team_code])


# Parse the games data and insert into the games collection
for line in games_data:
    # These belong in the row for the games data that will be inserted into the games collection
    date, visiting_team, home_team, visiting_score, home_score = line.strip().split(":")
    # check if both the visiting and home teams exist in the teams collection
    if visiting_team not in teams or home_team not in teams:
        continue  # skip this game if either team is not in the teams collection
    game = {"gamedate": date, "visitingteamcode": teams[visiting_team], "hometeamcode": teams[home_team], "visitingteamscore": int(visiting_score), "hometeamscore": int(home_score)}
    # inserts the new document into the games collection and creates a new collection
    mydb["games"].insert_one(game)
# Close the monogoDB connection 
#teams_data.close()
#games_data.close()