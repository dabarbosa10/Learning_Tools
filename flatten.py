import json

def flatten_json(obj):
    ret = {}

    def flatten(x, flattened_key = ""):
        if type(x) is dict:
            for current_key in x:
                flatten(x[current_key], flattened_key + current_key + '_')

        elif type(x) is list: 
            i=0
            for elem in x: 
                flatten(elem, flattened_key + str(i)+ '_')
                i+=1

        else:
            # x === string, integer, etc.
            ret[flattened_key[:-1]] = x

    flatten(obj)
    return ret




with open('newJson.json', 'r') as file:
     data =json.load(file)
print(data)
print(flatten_json(data))