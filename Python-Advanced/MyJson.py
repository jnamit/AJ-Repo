import json
import pprint

myJsonData ="""{"from": {"id": "8", "name": "Mary Pinter"}, 
                "message": "How ARE you?", 
                "comments": {"count": 0}, 
                "updated_time": "2012-05-01", 
                "created_time": "2012-05-01", 
                "to": {"data": [{"id": "1543", "name": "Honey Pinter"}]},  
                "type": "status", "id": "id_7"}"""

# "to" key's value is a dict containing 1 key "data". Value of "data" key is a list containing only 1 element which is a dict.
#

def getTargetIds(jsonData):
    jsonContent = json.loads(jsonData)
    if 'to' in jsonContent:
        print("'to' key exists at top level in json")
    if 'data' not in jsonContent['to']: # look for 'data' key under 'to' key
        raise ValueError("No data for target")
    else:
        print("found 'data' key under 'to' key")

    if 'data' not in jsonContent: # Lookup does not go down the levels of json. It does a lookup only at the current specified level.
        print("No key 'data' at the top level in json")

    # iterate over each key in the dictionary
    for dest in jsonContent['to']['data']:
        if 'id' not in dest:
            continue
        targetId = dest['id']
        print("to_id:", targetId)

    print("entire 'to' section = ", jsonContent['to']) # you can print or access a subset of json
    # traverse to any key at any depth in json
    print("to_name = ", jsonContent['to']['data'][0]['name']) # [0] is used to reach the 1st element in the list [{"id": "1543", "name": "Honey Pinter"}]
    to_section = jsonContent['to'] # you can assign a subset of json to another variable.
    print("to_section['data'] = ", to_section['data'])

if __name__ == "__main__":
    pprint.pprint(myJsonData)
    getTargetIds(myJsonData)
