# Thomas Johnson III
# June 13th 2019
# test_js_dict.py
# Written to test the effectiveness of restructuring Python dict to better resemble the object the simpleTree of the JQuery app.

import dict_to_json

def test_dict(): #Defines test_dict() function
    overall_dict = {} #The overall_dict will contain everything, for json
    first_level_array = [] #From top to bottom, this is the array that is the value of the
    second_level_dict = {}
    third_level_array = []
    fourth_level_dict = {}
    fifth_level_array = []
    sixth_level_dict = {}
    assign_to_sixth_level_dict(sixth_level_dict)
    assign_to_fifth_level_array(fifth_level_array, sixth_level_dict)
    assign_to_fourth_level_dict(fourth_level_dict,fifth_level_array)
    assign_to_third_level_array(third_level_array,fourth_level_dict)
    assign_to_second_level_dictionary(second_level_dict, third_level_array)
    assign_to_first_level_array(first_level_array, second_level_dict)
    print(first_level_array)
    return first_level_array

def assign_to_sixth_level_dict(input_sixth_level_dict):
    temporary_dict = {"label": "test_label",
                       "value": "test_label"}
    input_sixth_level_dict.update(temporary_dict)

def assign_to_fifth_level_array(input_fifth_level_array,input_sixth_level_dict):
    input_fifth_level_array.append(input_sixth_level_dict)
    print(input_fifth_level_array)

def assign_to_fourth_level_dict(input_fourth_level_dict, input_fifth_level_array):
    temporary_dict = {"label":"test me", "value": "test it","children": input_fifth_level_array}
    input_fourth_level_dict.update(temporary_dict)

def assign_to_third_level_array(input_third_level_array,input_fourth_level_dict):
    input_third_level_array.append(input_fourth_level_dict)
    print(input_third_level_array)

def assign_to_second_level_dictionary(input_second_level_dictionary, input_third_level_array):
    temporary_dictionary = {"label":"Top label", "value":"bottom label",  "children": input_third_level_array}
    input_second_level_dictionary.update(temporary_dictionary)

def assign_to_first_level_array(input_first_level_array,input_second_level_dictionary):
    input_first_level_array.append(input_second_level_dictionary)
    print(input_first_level_array)

def array_dict_to_json(array_dict):
    array_dict_json = dict_to_json.array_dict_to_json(array_dict)
    return array_dict_json

def commence_test():
    test_array_dict = test_dict()
    json_array_dict = array_dict_to_json(test_array_dict)
    return json_array_dict
