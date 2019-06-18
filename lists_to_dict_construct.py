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
    clone_of_array_of_arrays=array_of_lists.copy() # Copies the array_of_lists list
    clone_of_headings_index=0 # Tracks the index of clone_of_headings index
    for item_list in clone_of_array_of_arrays:# Outer for loop iterating through all the contentin the clone_of_array_of_arrays variable
        print("Item List:")# Used to track the item_list print value
        print(item_list)
        for item in item_list:#Inner for loop iterating through the individual entries of each list within the list containing lists of content
            item_dict = {"label": item, "value": str(item + "_value")} # The current dictionary entry, stored in item_dict
            checked_value, checked_heading = check_for_children(item, clone_of_headings) # Calls check_for_children to determine if the current content string is will have children, returning a boolean value and the directory that will contain the associated children
            if checked_value == True and checked_heading != None: # If statement that verifies if the values returned from check_for_children would indicate the dictionary entry will have children
                item_dict = search_dict_children_from_target(item,item_dict,clone_of_headings,clone_of_array_of_arrays,checked_heading) # Current dictionary is assigned the result of search_dict_children_from_target to gain the children of said dictionary entry
            top_level_dict[track_dict_entries_index] = item_dict #Stores the dictionary entry into a larger dictionary
            print("Print new item dict")# Print contents of dictionary entry
            print(item_dict)
            track_dict_entries_index+=1 # For enumerating the dictionary entries
        #clone_of_array_of_arrays.pop(clone_of_array_of_arrays.index(item_list))
        #content_array_popped = clone_of_array_of_arrays.pop(clone_of_headings_index)
        #heading_array_popped = clone_of_headings.pop(clone_of_headings_index)
        print("\n\n")
        #print("Content popped: ",content_array_popped, " Heading popped: ", heading_array_popped)
        print("\n\n")
        print("Content left: ",clone_of_array_of_arrays)
        print("\n\n\n")
        clone_of_headings_index+=1 # Increment clone_of_headings_index
        print(top_level_dict)
        recursive_dict_print_dict(top_level_dict) #Print sub dictionaries
        #recursive_dict_print(top_level_dict)
    return top_level_dict# Returns the value of top_level_dict


# search_dict_children_from_target fucntion accepts a string of content, an associated dictionary, a list of headings, a list of lists containing the content, and a heading cotaining the dictionary entry's children
def search_dict_children_from_target(item,item_dict,clone_of_headings,clone_of_list_of_lists,target_heading):
    if item in target_heading: # If tstatement checking to snsure that the content substring is a part of the string of the target_heading that was passed in the arguments
        sub_dict = build_sub_dict(item,item_dict,clone_of_headings.index(target_heading),clone_of_list_of_lists,clone_of_headings) # Another dictionary is created containing the children of the previous dictionary through the build_sub_dict function
        item_dict["children"] = sub_dict # The value of sub_dict is assigned as the children of item_dict
    else:
        old_item_dict = {"label": item, "value": str(item + "_value")} #Creates this dictionary entry if no children are found
        item_dict["children"] = old_item_dict #old_item_dict assigned to item_dict to be returned
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
        item_dict["children"] = sub_dict # The current dictionary entry being processed is assigned the result of build_sub_dict as the children of the current dictonary entry
        heading_bool = True # heading_bool is to track if there was a heading_bool value present
        print("heading boolean:")#printing for heading_bool
        print(heading_bool)
    else:
        old_item_dict = {"label": item, "value": str(item + "_value")} #If none of the previous entries are satisfied, this dictionary entry is sent back.
        item_dict["children"] = old_item_dict
    return item_dict # Returns the dictionary entry
'''
#Idea: create a dict where the keys are the headings and the values are the array of associated content!!
#Use the keys to to identify if it is a subdirectory and then use the value lists to iterate through the content smoothly
# build_sub_dict accepts a content string, the associated content string's dictonary entry, the index of associated directory in the headings array, the array of lists containing lists of content, and an array of the headings/directories
def build_sub_dict(item_name,item_dict, clone_of_headings_index, clone_of_list_of_lists,clone_of_headings):
    encompassing_dict = {} #encompassing_dict will contain all the children dictionaries
    for content_item in clone_of_list_of_lists[clone_of_headings_index]:# iterates through the content strings that are part of the associated heading/directory
        content_item_dict ={"label": content_item, "value": str(content_item + "_value")} #This dictionary entry is the defualt if no children dictionary entries are present
        #clone_of_list_of_lists[clone_of_headings_index].remove(content_item)
        if content_item != item_name: # If the content string is the same as the dictionary label value, the code will not run to avoid duplicates
            check_headings_bool, pinpoint_heading = check_headings(content_item,clone_of_headings)# The function check_headings returns a boolean and an associated heading that contains children dictionaries
            print("\n content_item = ", content_item," item_name = ", item_name," check_headings_bool = ", check_headings_bool, " pinpoint_heading = ", pinpoint_heading)# Print statement to determine if there are errors or bugs
            if check_headings_bool == True and pinpoint_heading != None:# If statement to determine if the there will be child dictionaries of current content string
                content_item_dict = search_dict_children_from_target(content_item,content_item_dict,clone_of_headings,clone_of_list_of_lists, pinpoint_heading) #Searches for any child dictionaries of the current content string
        encompassing_dict[clone_of_list_of_lists[clone_of_headings_index].index(content_item)] = content_item_dict #Puts the new child dictionary into the encompassing dictionary
        #encompassing_dict.update(temp_encompassing_dict)
        print("\n\nEncompassing dict")
        print(encompassing_dict)
    item_dict["children"] = encompassing_dict #Assigns encompassing_dict as the child of item_dict
    print("\nSub dictionaries:")
    recursive_dict_print(item_dict)
    content_array_popped = clone_of_list_of_lists.pop(clone_of_headings_index) #Pops the used content array in the function (Where the child's content came from)
    heading_array_popped = clone_of_headings.pop(clone_of_headings_index) #Pops the used heading/directory of the child dictionary
    print("\n\n")
    print("Content popped: ",content_array_popped, " Heading popped: ", heading_array_popped)
    print("\n\n")
    print("Content left: ",clone_of_list_of_lists)
    print("\n\n\n")
    return encompassing_dict # returns the encompassing_dict

def check_headings(target_item, clone_of_headings):# Checks if the heading in question actually has the children of content string
    for heading in clone_of_headings: # For loop for going through the headings
        if target_item in heading: #Checks id target_item is a substring of the heading
            located_heading = heading #Assigns the heading value to located heading
            return True, located_heading #Returns both values
        else:
            continue# Continues looping otherwise
    return False, None# If not a substring, this is returned

def check_for_children(target_content, clone_of_headings): #Checks for where the children are in regard to the headings
    for heading in clone_of_headings:#For loop looping through the headings
        if target_content in heading:# If statement checking if the target_content is a substring of of the heading
            return True, heading # Return the True value and heading value
        else:
            continue#continue if not satisfying if statement
    return False, None# If not satisfying the if-else statement above, return these values

# Reference: https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values
def recursive_dict_print(item_dictionary):# Prints the sub_dictionaries recursively
    for key, value in item_dictionary.items():#Loop through keys and values
        if isinstance(value,dict):#When the value is a dictionary itself
            recursive_dict_print(value)# recursively call the function to go through the nested dictionaries
        else:
            print("\n", key,"\n", value) # Print s the key and value

def recursive_dict_print_dict(item_dictionary):# Prints the sub_dictionaries recursively
    for key, value in item_dictionary.items():#Loop through keys and values
        if isinstance(value,dict):#When the value is a dictionary itself
            recursive_dict_print_dict(value)# recursively call the function to go through the nested dictionaries
        else:
            print(item_dictionary) #Prints the dictionary
