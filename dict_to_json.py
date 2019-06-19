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

import json #Imports Python's json library

def dictionary_to_json(input_dictionary):#dictionary_to_json function is used for converting typical Python dictionaries to JSON
    print("Converting dictionary to JSON") # Prints this statement to verify to user that the code is running when the function is called
    with open("dictionary_4.json", "w") as jfile:# Quickly opens a new file to write the JSON to called dictionary_4.json
        json.dump(input_dictionary, jfile) #Writes the JSON to the file
    output_json = json.dump(input_dictionary)# saves the outputted json to a variable for further usage
    print("JSON Ready.")# Print statement to alert the user that the JSON is ready
    print(output_json) #Print the result of the JSON
    return output_json #Return the JSON

def array_dict_to_json(input_dictionary):# array_dict_to_json function is used for converting typical Python list-dictionary constructs to JSON
    print("Converting array/dictionary to JSON") #Signifies that the code of the function is running
    with open("array_dict_list.json", "w") as jfile:#Opens a file titled array_dict_list.json to write the file contents to
        json.dump(input_dictionary, jfile) #Writes the JSON to the file
    output_json = json.dumps(input_dictionary) # Saves the output of the JSON to a variable for further use
    print("JSON Ready.")
    print(output_json)
    return output_json
