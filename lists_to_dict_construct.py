# Thomas Johnson III
# June 17th, 2019
# lists_to_dict_construct.py
# Holds the functions for transforming the lists to dictionary
# Reference: https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values


#def recursive_dict_search(input_dict_containing_lists):

#def recursive_list_search(input_list_containing_dicts):
    #for item in input_list_containing_dicts:
    #    if isinstance(item,dict):

#def dict

#def search_child(str_item,list_of_headings,list_of_lists):
    #if str_item in list_of_headings:

        #build_dict(

# The function start_build_top_dict initializes the heirarchical dictionary, and then returns said dictionary
def start_build_top_dict(array_of_headings,array_of_lists):# Initiates the entire process
    #print("The list of lists:") #Check if the correct list of lists is being printed.
    #print(list_of_lists)# Prints said list of lists
    top_level_dict = {} # The hierarchical dictionary. Initialized to store each compiler and repsective module
    track_dict_entries_index = 0 # The index of the dictionary
    clone_of_headings = array_of_headings.copy() # Copies the array_of_headings list
    clone_of_list_of_lists=array_of_lists.copy() # Copies the array_of_lists list
    clone_of_headings_index=0 # Tracks the index of clone_of_headings index
    for item_list in clone_of_list_of_lists:
        print("Item List:")
        print(item_list)
        for item in item_list:
            item_dict = {"label": item, "value": str(item + "_value")}
            checked_value, checked_heading = check_for_children(item, clone_of_headings)
            if checked_value == True and checked_heading != None:
                item_dict = search_dict_children_from_target(item,item_dict,clone_of_headings,clone_of_list_of_lists,checked_heading)
            top_level_dict[track_dict_entries_index] = item_dict
            print("Print new item dict")
            print(item_dict)
            track_dict_entries_index+=1
        #clone_of_list_of_lists.pop(clone_of_list_of_lists.index(item_list))
        clone_of_list_of_lists.pop(clone_of_headings_index)
        clone_of_headings.pop(clone_of_headings_index)
        clone_of_headings_index+=1
        print(top_level_dict)
        #recursive_dict_print(top_level_dict)
    return top_level_dict

def search_dict_children_from_target(item,item_dict,clone_of_headings,clone_of_list_of_lists,target_heading):
    search_context = next((heading for heading in clone_of_headings if item in heading), None)
    print("Printing Search Context")
    print(search_context)
    #for heading in search_context:
        #print("Printing the item to search heading: ", item)
        #print("Printing the heading:")
        #print(heading)
        #heading_bool = False
    if item in target_heading:
        sub_dict = build_sub_dict(item,item_dict,clone_of_headings.index(target_heading),clone_of_list_of_lists,clone_of_headings)
        item_dict["children"] = sub_dict
        heading_bool = True
        print("heading boolean:")
        print(heading_bool)
    else:
        old_item_dict = {"label": item, "value": str(item + "_value")}
        item_dict["children"] = old_item_dict
    return item_dict

def search_dict_children(item,item_dict,clone_of_headings,clone_of_list_of_lists):
    search_context = next((heading for heading in clone_of_headings if item in heading), None)
    print("Printing Search Context")
    print(search_context)
    #for heading in search_context:
        #print("Printing the item to search heading: ", item)
        #print("Printing the heading:")
        #print(heading)
        #heading_bool = False
    if search_context == None:
        pass
    elif item in search_context and item != item_dict["label"]:
        sub_dict = build_sub_dict(item,item_dict,clone_of_headings.index(heading),clone_of_list_of_lists,clone_of_headings)
        item_dict["children"] = sub_dict
        heading_bool = True
        print("heading boolean:")
        print(heading_bool)
    else:
        old_item_dict = {"label": item, "value": str(item + "_value")}
        item_dict["children"] = old_item_dict
    return item_dict
#Idea: create a dict where the keys are the headings and the values are the array of associated content!!
#Use the keys to to identify if it is a subdirectory and then use the value lists to iterate through the content smoothly
def build_sub_dict(item_name,item_dict, clone_of_headings_index, clone_of_list_of_lists,clone_of_headings):
    encompassing_dict = {}
    for content_item in clone_of_list_of_lists[clone_of_headings_index]:
        content_item_dict ={"label": content_item, "value": str(content_item + "_value"), "children": "searching"}
        #clone_of_list_of_lists[clone_of_headings_index].remove(content_item)
        if content_item != item_name:
            content_item_dict = search_dict_children(content_item,content_item_dict,clone_of_headings,clone_of_list_of_lists)
        encompassing_dict[clone_of_list_of_lists[clone_of_headings_index].index(content_item)] =content_item_dict
        #encompassing_dict.update(temp_encompassing_dict)
        print("\n\nEncompassing dict")
        print(encompassing_dict)
    item_dict["children"] = encompassing_dict
    print("\nSub dictionaries:")
    recursive_dict_print(item_dict)
    return encompassing_dict

def check_for_children(target_content, clone_of_headings):
    for heading in clone_of_headings:
        if target_content in heading:
            return True, heading
        else:
            continue
    return False, None


def recursive_dict_print(item_dictionary):
    for key, value in item_dictionary.items():
        if isinstance(value,dict):
            recursive_dict_print(value)
        else:
            print(key, value)
