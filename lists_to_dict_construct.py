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
        #content_array_popped = clone_of_list_of_lists.pop(clone_of_headings_index)
        #heading_array_popped = clone_of_headings.pop(clone_of_headings_index)
        print("\n\n")
        #print("Content popped: ",content_array_popped, " Heading popped: ", heading_array_popped)
        print("\n\n")
        print("Content left: ",clone_of_list_of_lists)
        print("\n\n\n")
        clone_of_headings_index+=1
        print(top_level_dict)
        recursive_dict_print_dict(top_level_dict)
        #recursive_dict_print(top_level_dict)
    return top_level_dict

def search_dict_children_from_target(item,item_dict,clone_of_headings,clone_of_list_of_lists,target_heading):
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
# search_dict_children is the predecessor of search_dict_children_from_target. It is has multiple bugs
# and was most useful in understanding how to improve its successor
'''
# search_dict_children function was designed to detectif there were any children of a previous dictionary entry.
# The function calls build_sub_dict to build another dictionary within a previous dictionary entry if a child is
# located.
def search_dict_children(item,item_dict,clone_of_headings,clone_of_list_of_lists):
    search_context = next((heading for heading in clone_of_headings if item in heading), None) # Would find the first entry of the occurrence of a substring
    print("Printing Search Context") # Printing to be able to identify the next print statement
    print(search_context) # Prints the search_context value
    #for heading in search_context: # For lop for identifying the  substring for
        #print("Printing the item to search heading: ", item)
        #print("Printing the heading:")
        #print(heading)
        #heading_bool = False
    if search_context == None: # In case search_context yields nothing
        pass
    elif item in search_context and item != item_dict["label"]: #If search_context yields something yet that and the child to be identified is not repeated in the parent dictionary entry
        sub_dict = build_sub_dict(item,item_dict,clone_of_headings.index(heading),clone_of_list_of_lists,clone_of_headings) # Function accepting a string from the content, the current dict being constructed, index of a relevant heading, array of the content, and an array of the headings/directories of said content
        item_dict["children"] = sub_dict # The 
        heading_bool = True
        print("heading boolean:")
        print(heading_bool)
    else:
        old_item_dict = {"label": item, "value": str(item + "_value")}
        item_dict["children"] = old_item_dict
    return item_dict
'''
#Idea: create a dict where the keys are the headings and the values are the array of associated content!!
#Use the keys to to identify if it is a subdirectory and then use the value lists to iterate through the content smoothly
def build_sub_dict(item_name,item_dict, clone_of_headings_index, clone_of_list_of_lists,clone_of_headings):
    encompassing_dict = {}
    for content_item in clone_of_list_of_lists[clone_of_headings_index]:
        content_item_dict ={"label": content_item, "value": str(content_item + "_value")}
        #clone_of_list_of_lists[clone_of_headings_index].remove(content_item)
        if content_item != item_name:
            check_headings_bool, pinpoint_heading = check_headings(content_item,clone_of_headings)
            print("\n content_item = ", content_item," item_name = ", item_name," check_headings_bool = ", check_headings_bool, " pinpoint_heading = ", pinpoint_heading)
            if check_headings_bool == True and pinpoint_heading != None:
                print("print me")
                content_item_dict = search_dict_children_from_target(content_item,content_item_dict,clone_of_headings,clone_of_list_of_lists, pinpoint_heading)
        encompassing_dict[clone_of_list_of_lists[clone_of_headings_index].index(content_item)] =content_item_dict
        #encompassing_dict.update(temp_encompassing_dict)
        print("\n\nEncompassing dict")
        print(encompassing_dict)
    item_dict["children"] = encompassing_dict
    print("\nSub dictionaries:")
    recursive_dict_print(item_dict)
    content_array_popped = clone_of_list_of_lists.pop(clone_of_headings_index)
    heading_array_popped = clone_of_headings.pop(clone_of_headings_index)
    print("\n\n")
    print("Content popped: ",content_array_popped, " Heading popped: ", heading_array_popped)
    print("\n\n")
    print("Content left: ",clone_of_list_of_lists)
    print("\n\n\n")
    return encompassing_dict

def check_headings(target_item, clone_of_headings):
    for heading in clone_of_headings:
        if target_item in heading:
            located_heading = heading
            return True, located_heading
        else:
            continue
    return False, None

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
            print("\n", key,"\n", value)

def recursive_dict_print_dict(item_dictionary):
    for key, value in item_dictionary.items():
        if isinstance(value,dict):
            recursive_dict_print(value)
        else:
            print(item_dictionary)
