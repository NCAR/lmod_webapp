# Thomas Johnson III
# 6/19/2019
# dict_to_array_dict.py
# Converts the heading container to array dict
#Reference: https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
#Reference: https://stackoverflow.com/questions/13519644/how-to-solve-dictionary-changed-size-during-iteration-in-python/13519858
#Reference: https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely
#Reference: https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary

import copy #Imports the copy module of Python for the purpose of making deep copies to maniulate dictionaries in this code
def value_morph_dict(heading_container):# Function value_morph_dict function accepts a dictionary argument. Executes the remainder of the code in this Python file.
    for key, content_array in heading_container.items():# Iterates through the dictionary
        array_dict_content = [] #Initializes an outer list to wrap around the dictionaries that will be formed
        for element in content_array:# For every indicidual piece of content, a dictionary eill be formed with keys and values
            element = {"label": element, "value": str(element + "_value")}# Ditionary template for the dictionaries that will be formed
            array_dict_content.append(element)# Appends the dictionary to the list arra_dict_content to keep dictionaries of all content contained and managed
        heading_container[key] = array_dict_content #Now each dictionary will store all of dicitonaries contianing the content
    print("heading_container with array of dicts:")# Print statement for debugging purposes
    for key, content_array in heading_container.items():#For loop and print statement to track the initial organization of each piece of content
        print("\n",key, content_array)
    full_compiler_container_complete = search_dict_children_from_target(heading_container) #Returns the complete list-dict construct to be stored in a variable for further usage
    return full_compiler_container_complete#Returns the list-dict construct to reg_expression.py

# search_dict_children_from_target fucntion has an argument of heading_container, will search for children of the given dictionary
def search_dict_children_from_target(heading_container): # The function argument is already a heaing_container
    array_of_headings = list(heading_container.keys()) # Creates a list of headings for tracking purposes
    clone_of_array_of_headings = array_of_headings.copy()# Clones the array_of_headings
    heading_container_clone = copy.deepcopy(heading_container)# Create a clone of the heading_container completely
    for key, value_array_suspect in heading_container_clone.items():# For loop iterating through the directories and arrays of content in the heading_conteiner_clone dictionary
        for value_suspect in value_array_suspect:# For loop iterating through the individual values of the array of content dictionary
            check_label_bool, parent_heading = check_label_in_headings(value_suspect,array_of_headings)# Returns a boolean and a directory that would likely contain the children of a given content dictionary
            if check_label_bool == True and parent_heading != None: #Checks to make sure theat the boolean is True and a value for parent_heading is provided, otherwise no children were found
                location_of_value_suspect = value_array_suspect.index(value_suspect) #Tracks the content dictionary in the array that contains them
                value_suspect = move_children(heading_container,array_of_headings, parent_heading, value_suspect, location_of_value_suspect)#Function that moves content dictionary array that has the children of said content dictionary, takes the overall structure, the headings that are remaining to utilize, the heading of the children, the content dictionary that has children, and the location of the content dictionary in the array of content dictionaries
                print("\n\nPrinting the value_suspect here:") #Print statement that will be used for debugging purposes (tracking the current content dictionary being examined)
                print (value_suspect)
                print("\n\nThe full heading_container is printed:")#Print statement that will be used for debugging purposes (tracking the heading_container as it goes through changes)
                print(heading_container)
                print("The missing heading:")#Print statement that will be used for debugging purposes (tracking the directories that remain to be utilized for the purpose of tracking the children of dictionaries, which one has been removed)
                missing_heading = heading_container.pop(parent_heading)#Removes a directory from the keys of the heading_container
                print(missing_heading)
            else:
                continue
        print("\nThe resulting heirarchical array-dict object is here:") #Further debugging (Track the rearrangement of list-dict construct)
        print(key,value_array_suspect)
    print("Totality of it all:") #Prints the entire heading_container_clone which displays all keys (direcories) and arrays of content dictionaries
    print(heading_container_clone)
    full_compiler_container = elminate_superfluous_keys(heading_container_clone,array_of_headings, clone_of_array_of_headings) #Returns the heading container with extra directories eliminated to get rid of the clutter
    return full_compiler_container

def elminate_superfluous_keys(heading_container_clone,array_of_headings,clone_of_array_of_headings):# eliminate_superfluous_keys is a function taking the arguments of heading_container_clone,array_of_headings, and clone_of_array_of_headings to get rid of excess directories in the top level of keys in heading_container_clone
    print("The array of headings:")#Prints the directories
    print(array_of_headings)
    for heading in array_of_headings:#For loop to remove any directories matching those in clone_of_array_of_headings to allow clone_of_array_of_headings to be used as a filter for heading_container_clone
        if heading in clone_of_array_of_headings:
            clone_of_array_of_headings.remove(heading)#Removal of the directory
        else:
            continue
    for heading in clone_of_array_of_headings:
        heading_container_clone.pop(heading)
    print("Heading container without superfluous keys present:")
    full_compiler_array = []
    for key in heading_container_clone:
        full_compiler_container = {}
        full_compiler_container["label"] = key
        full_compiler_container["value"] = str(key + "_value")
        full_compiler_container["children"] = heading_container_clone[key]
        full_compiler_array.append(full_compiler_container)
    print("full_compiler_container is printed here:")
    print(full_compiler_array)
    return full_compiler_array

def move_children(heading_container,array_of_headings, parent_heading, item_suspect, location_of_value_suspect):
    print("Printing item_suspect here:")
    print(item_suspect)
    item_suspect["children"] = heading_container[parent_heading]
    print("Printing item_suspect with children here:")
    print(item_suspect)
    print("\n", heading_container)
    print("\nParent Heading here:")
    print(parent_heading)
    array_of_headings.remove(parent_heading)
    search_dict_descendants(heading_container,array_of_headings, item_suspect["children"], item_suspect)
    return item_suspect

def search_dict_descendants(heading_container,array_of_headings,item_with_possible_descendants, item_suspect_parent):
    print("Item with possible descendants:")
    print(item_with_possible_descendants)
    for content_container in item_with_possible_descendants:
        print("\nThis point prints content_contianer and array_of_headings:")
        print(content_container,array_of_headings)
        parent_sub_heading = check_lineage_label_in_headings(content_container, array_of_headings,item_suspect_parent)
        if parent_sub_heading != None:
            location_of_content_container = item_with_possible_descendants.index(content_container)
            content_container = move_children(heading_container,array_of_headings, parent_sub_heading, content_container, location_of_content_container)
            print("The missing heading:")
            missing_heading = heading_container.pop(parent_sub_heading)
            print(missing_heading)
        else:
            continue

def check_label_in_headings(target_item_dictionary, array_of_headings):# Checks if the heading in question actually has the children of content string
    for heading in array_of_headings: # For loop for going through the headings
        if target_item_dictionary["label"] in heading: #Checks id target_item is a substring of the heading
            located_heading = heading #Assigns the heading value to located heading
            return True, located_heading #Returns both values
        else:
            continue# Continues looping otherwise
    return False, None# If not a substring, this is returned

def check_lineage_label_in_headings(target_item_content, array_of_headings, parent_of_target_item_content):
    for target_heading in array_of_headings:
        if target_item_content["label"] in target_heading:
            if parent_of_target_item_content["label"] in target_heading:
                located_target_heading = target_heading
                print("\nPrint the located_target_heading: ",located_target_heading)
                return located_target_heading
        else:
            continue
        return None
