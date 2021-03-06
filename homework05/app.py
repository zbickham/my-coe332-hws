import redis
import json
from flask import Flask, request

app = Flask(__name__)

ml_data = {}

@app.route('/data', methods=['POST'])
def load_data(): 
    """
    Opens JSON data and loads it into a dictionary for later use.
    
    Args:
        none
   
   Returns:
        A string that tells the user the data has been loaded.
    """
    global ml_data

    with open('ML_Data_Sample.json', 'r') as f:
               ml_data = json.load(f)
    
    global rd
    rd = redis.Redis(host='10.97.36.98', port = 6379, db =0)
    for d in ml_data['meteorite_landings']:
            rd.set(d['id'],json.dumps(d))
    
    return "Data has been loaded.\n"

@app.route('/data', methods=['GET'])
def load_redis():
    """
    Returns a JSON list of data to the user that contains the loaded information.
    
    Args:
        none
    
    Returns:
        A JSON list of the loaded information.
    """   
    list_of_ml = []
    for x in ml_data['meteorite_landings']:
        list_of_ml.append(json.loads(rd.get(x['id'])))
    return (json.dumps(list_of_ml, indent=1) + '\n')

if __name__ == "__main__":
    x = ml_data
    app.run(debug=True, host = '0.0.0.0')
