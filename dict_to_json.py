# Thomas Hilton Johnson III
# dict_to_json.py
# June 12th, 2019
# Python 3
# Converts python dictionary to json for usage elsewhere
# will be used with document.py so that flask app can
# hopefully store the values in a JavaScript object to
# used with the jQuery plugin
# Reference: https://www.w3schools.com/python/python_json.asp
# Reference: https://stackoverflow.com/questions/15617164/parsing-json-giving-unexpected-token-o-error
# reference: https://stackoverflow.com/questions/15617164/parsing-json-giving-unexpected-token-o-error
# Reference: https://stackoverflow.com/questions/4933217/print-json-parsed-object

import json

def dictionary_to_json(input_dictionary):
    print("Converting dictionary to JSON")
    with open("dictionary_3.txt", "w") as jfile:
        json.dump(input_dictionary, jfile)
    output_json = json.dumps(input_dictionary)
    print("JSON Ready.")
    print(output_json)
    return output_json

def array_dict_to_json(input_dictionary):
    print("Converting array/dictionary to JSON")
    with open("array_dict.json", "w") as jfile:
        json.dump(input_dictionary, jfile)
    output_json = json.dumps(input_dictionary)
    print("JSON Ready.")
    print(output_json)
    return output_json
