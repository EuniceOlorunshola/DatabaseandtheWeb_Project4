# function in python to convert a json output into a response object
from flask import Flask, jsonify
# these are the variables used in python
app = Flask(__name__)
# Define the standings data as a list of dictionaries
standings_baseball_data = [
    {'losses': 3, 'percent': 0.667, 'tcode': 'CHC', 'ties': 0, 'tname': 'Cubs', 'wins': 6},
    {'losses': 3, 'percent': 0.611, 'tcode': 'ARI', 'ties': 1, 'tname': 'Diamondbacks', 'wins': 5},
    {'losses': 5, 'percent': 0.444, 'tcode': 'STL', 'ties': 0, 'tname': 'Cardinals', 'wins': 4},
    {'losses': 5, 'percent': 0.389, 'tcode': 'ATL', 'ties': 1, 'tname': 'Braves', 'wins': 3},
    {'losses': 4, 'percent': 0.375, 'tcode': 'CLE', 'ties': 2, 'tname': 'Indians', 'wins': 2}
  ]
# Define the standings endpoint
@app.route('/baseball/standings/', methods=['GET'])
def get_standings():
    # Return the standings data as a JSON object using jsonify
    return jsonify({'standings': standings_baseball_data})

# Important note: I connected to http://127.0.0.1:5000/baseball/standings/
# it did not work for me when I used localhost

if __name__ == '__main__':
    app.run(debug=True)

# list of games result 
baseball_team_results_data = [
    { "gdate": "2004-03-20", "opponent": "ARI", "result": "WIN", "them": 10, "us": 11 },
    { "gdate": "2004-03-27", "opponent": "STL", "result": "WIN", "them": 7, "us": 9 },
    { "gdate": "2004-03-30", "opponent": "ATL", "result": "LOSS", "them": 10, "us": 5 },
    { "gdate": "2004-04-22", "opponent": "at CLE", "result": "WIN", "them": 4, "us": 7 },
    { "gdate": "2004-04-24", "opponent": "at ARI", "result": "LOSS", "them": 12, "us": 7 },
    { "gdate": "2004-05-01", "opponent": "at STL", "result": "WIN", "them": 0, "us": 10 },
    { "gdate": "2004-05-04", "opponent": "at ATL", "result": "WIN", "them": 8, "us": 10 },
    { "gdate": "2004-05-15", "opponent": "CLE", "result": "WIN", "them": 6, "us": 8 },
    { "gdate": "2004-05-18", "opponent": "ARI", "result": "LOSS", "them": 13, "us": 5 }
]

 

#Define the particualr team location and name
team_location = 'Chicago'
team_name = 'Cubs'

 # Endpoint to get game results for a particular team
@app.route('/baseball/results/<string:tcode>/', methods=['GET'])
def get_game_results(tcode):
    # Filter game results for the given team code
    game_results = [btr for btr in baseball_team_results_data]


    # Sort game results chronologically by game date
    game_results.sort(key=lambda btr: btr["gdate"])

    # Build response JSON object
    json_response = {
        "results": [
            {
                "gdate": btr["gdate"],
                "opponent": btr["opponent"],
                "result": btr["result"],
                "them": btr["them"],
                "us": btr["us"]
            }
            for btr in game_results
        ],
        "tloc": team_location,
        "tname": team_name
    }

    return jsonify(json_response)
#To run the program:
 # I typed the command export FLASK_APP=baseball.py
 # flask run 


#if __name__ == '__main__':
    #app.run(debug=True)