# Thomas Johnson III
# 6/19/2019
# dict_to_array_dict.py
# Converts the heading container to array dict
#Reference: https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
#Reference: https://stackoverflow.com/questions/13519644/how-to-solve-dictionary-changed-size-during-iteration-in-python/13519858
#Reference: https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely
#Reference: https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
#reference: https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list
import re
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
            #module_path ="/glade/u/apps/ch/modulefiles/default/" #The root path the first level of subdirectories
            print("Sanity checking...")
            check_label_bool, parent_heading = check_label_in_headings(value_suspect,array_of_headings)# Returns a boolean and a directory that would likely contain the children of a given content dictionary
            print("Sanity checking value_suspect...")
            print(value_suspect)
            print("Printing these hadings for sanity purposes:")
            print(array_of_headings)
            print("\n\n This is the check label and parent heading:")
            print(check_label_bool, parent_heading)
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
        print("Totality of it all in session:") #Prints the entire heading_container_clone which displays all keys (direcories) and arrays of content dictionaries
        print(heading_container_clone)
    print("Totality of it all:") #Prints the entire heading_container_clone which displays all keys (direcories) and arrays of content dictionaries
    print(heading_container_clone)
    full_compiler_container = elminate_superfluous_keys(heading_container_clone,array_of_headings, clone_of_array_of_headings) #Returns the heading container with extra directories eliminated to get rid of the clutter of keys that have already been rearranged in the list-dict hierarchy
    return full_compiler_container#Returns a cleaned up list-dict with no extra keys

#A function responsible for retitling the top level of the list-dict hierarchy
def new_first_level_directories(target_partial_heading_container): #Accepts the dictionaries that will contain the top level directories of the list-dict construct as an argument
    module_path ="/glade/u/apps/ch/modulefiles/default/" # module path for string manipulation
    if target_partial_heading_container["label"] == "compilers": # If statement to catch the compilers directory, then rename it
        target_partial_heading_container["label"] = "Compilers" #Renames said compilers directory
    elif target_partial_heading_container["label"] == "idep": # If statement to catch the compiler independent software dirctory, then rename it
        target_partial_heading_container["label"] = "Compiler Independent" # Renames said compilers independent directory
    else:
        None #None

def elminate_superfluous_keys(heading_container_clone,array_of_headings,clone_of_array_of_headings):# eliminate_superfluous_keys is a function taking the arguments of heading_container_clone,array_of_headings, and clone_of_array_of_headings to get rid of excess directories in the top level of keys in heading_container_clone
    print("The array of headings:")#Prints the directories
    print(array_of_headings)
    for heading in array_of_headings:#For loop to remove any directories matching those in clone_of_array_of_headings to allow clone_of_array_of_headings to be used as a filter for heading_container_clone
        if heading in clone_of_array_of_headings:# Check which directories are shared between both list constructs, and those directories that are shared are are removed from clone_of_array_of_headings
            clone_of_array_of_headings.remove(heading)# Removal of the directory from clone_of_array_of_headings
        else:
            continue #Will continue the for loop when the if statement is not satisfied
    for heading in clone_of_array_of_headings: #For loop using clone_of_array_of_headings to remove the keys that have be rearranged from the first level of the list-dict construct
        heading_container_clone.pop(heading) # The directory is removed from the top level of the heading_conteiner_clone list-dict
    print("Heading container without superfluous keys present:")
    full_compiler_array = [] #A new list full_compiler_array is used to wrap around the the heading_container_clone to complete list-dict construct
    for key in heading_container_clone:#For loop initialized to reconstruct first level of list-dict (Previously the first level was not a list-dict construct nor did it consist of the keys: label, value, children)
        full_compiler_container = {} #The full_compiler_container dictionary is initialized to make a sepaate dictionary for each directory at the first level of the list-dict
        full_compiler_container["label"] = key #The label key is assigned the string the current directory
        full_compiler_container["value"] = str(key + "_value")# The value key is assigned a modified string fo the current dictionary
        full_compiler_container["children"] = heading_container_clone[key] #The children key is assigned the list-dict construct that is currently held by the heading_container_clone's directory (key)
        new_first_level_directories(full_compiler_container)
        full_compiler_array.append(full_compiler_container) # Now each dictionary holding a directory and its content is appended to the full_compiler_array, building a list-dict construct from first level to last level
    print("full_compiler_container is printed here:")
    print(full_compiler_array)#Printing out the full_compiler_array for debugging purposes
    return full_compiler_array #Returns the full_compiler_array as a value to wherever the eliminate_superfluous_keys() function was called

#The move children function handles rearranging the list-dict construct from a one level dictionary to a multi-level list-dict construct
def move_children(heading_container,array_of_headings, parent_heading, item_suspect, location_of_value_suspect):#The arguments are the heading_container containing the relevant directories and their list of contents, An array_of_headings (the directories) to keep track of which directories hav ebeen moved, the parent_heading which is the directory or subdirectory of the current directory that shall be moved to be the "children" of, item_suspect which is the dictionary that is currently in question, and location_of_value_suspect which the location within a list of the item_suspect
    print("Printing item_suspect here:")
    print(item_suspect) #Prints the item_suspect for the purposes of debugging
    item_suspect["children"] = heading_container[parent_heading] #Assigns the directory with the value of parent_heading as the "children" of the item_suspect dictionary
    print("Printing item_suspect with children here:")
    print(item_suspect)#Prints the item_suspect for the purposes of debugging
    print("\n", heading_container)#Prints the heading_container for the purposes of debugging
    print("\nParent Heading here:")
    print(parent_heading)#Prints the parent_heading for the purposes of debugging
    array_of_headings.remove(parent_heading) #Removes the parent_heading that it cannot be utilized again and cause an unending recursive loop
    search_dict_descendants(heading_container,array_of_headings, item_suspect["children"], item_suspect) #Calls search_dict_descendants to ensure that the children of the current directory do not have children themselves
    return item_suspect #Returns item_suspect as a value to were the move_children() function is called

#search_dict_descendants is a function  that is a variation of search_dict_children_from_target() function for searching for the children of directories that deeper than the second level
def search_dict_descendants(heading_container,array_of_headings,item_with_possible_descendants, item_suspect_parent):# Accepts the arguments heading_container (a dictionary of the directories with associated content arrays), a list of the headings to track which directories have been sorted, item_with_possible_descendants is a list containing the associated content of an dictionary of a directory, item_suspect_parent which is the parent dictionary of item_with_possible_descendants
    print("Item with possible descendants:")
    print(item_with_possible_descendants)#Print the array that is being searched for debugging purposes
    for content_container in item_with_possible_descendants:
        print("\nThis point prints content_container and array_of_headings:")
        print(content_container,array_of_headings) # Print the dictionary that is obtained from iterating item_with_possible_descendants and the list of directories for debugging purposes
        parent_sub_heading = check_lineage_label_in_headings(content_container, array_of_headings,item_suspect_parent) #Check the directory to which the current dictionary belongs
        if parent_sub_heading != None: #Will only run the next section if a value other than None is returned.
            location_of_content_container = item_with_possible_descendants.index(content_container) # The location of the dictionary that will be assigned children
            content_container = move_children(heading_container,array_of_headings, parent_sub_heading, content_container, location_of_content_container)# Adds the subdirectory to the children key of the dictionary as the value of the children key
            print("Checking to make sure...")
            print("\nI am printing content_container for debugging purposes:")
            print(content_container)
            print("The missing heading:")
            missing_heading = heading_container.pop(parent_sub_heading) #Identify the key that has been removed from the top level of the head_container construct
            print(missing_heading)
        else:
            continue #Continues the for loop when the if statement is not satisfied


def check_label_in_headings(target_item_dictionary, array_of_headings):# Checks if the heading in question actually has the children of content string
    array_of_top_levels = first_level_obtainment(array_of_headings)
    print("These top levels have been printed:")
    print(array_of_top_levels)
    for heading in array_of_headings:
        print("Checking for any colons:")
        print(target_item_dictionary["label"])
        print("Checking for colon discrepancies:")
        print(heading)
        if target_item_dictionary["label"] +":" == heading: #Checks if the current item when concatenated with the path of the modules is one of the top level directories.
            located_heading = heading #Assigns the heading value to located heading
            return True, located_heading #Returns both values
        else:
            continue# Continues looping otherwise
    return False, None# If not a substring, this is returned

#Function that checks for the parent in the search_dict_descendants() function
def check_lineage_label_in_headings(target_item_content, array_of_headings, parent_of_target_item_content):#Arguments are: target_item_content which is the current dictionary being examined, array_of_headings the list of the directories that have not been sorted, parent_of_target_item_content the parent dictionary of target_item_content
    for target_heading in array_of_headings: #For loop iterating through the list of directories
        if target_item_content["label"] in target_heading:#Continues if the current dictionary's label value is a substring of the current heading
            if parent_of_target_item_content["label"] in target_heading:#Continues if the parent dictionary's label value is a substring of the current heading
                located_target_heading = target_heading#located_target_heading points to the value of target_heading
                print("\nPrint the located_target_heading: ",located_target_heading) #Prints the located_target_heading for debugging purposes
                return located_target_heading #returns the located_target_heading value to where the check_lineage_label_in_headings() function is called
                break
        else:
            continue#Continue to keep the for loop running
    return None

def sub_levels_attainment(array_containing_headings):
    regular_expression_instance = re.compile(".*/.*/.*/.*")
    array_containing_reg_exp = list(filter(regular_expression_instance.match,array_containing_headings))
    print("These are the sub-levels:")
    print(array_containing_reg_exp)
    return array_containing_reg_exp

def first_level_obtainment(array_containing_headings):
    regular_expression_instance = re.compile("[A-z]+:")
    array_containing_reg_exp = list(filter(regular_expression_instance.match,array_containing_headings))
    print("These are the top-levels:")
    print(array_containing_reg_exp)
    return array_containing_reg_exp

def top_levels_attainment(array_containing_headings):
    array_of_top_levels = []
    array_of_sub_levels = sub_levels_attainment(array_containing_headings)
    for heading in array_containing_headings:
        if heading not in array_of_sub_levels:
            array_of_top_levels.append(heading)
    for heading in array_of_top_levels:
        if "\/" in heading:
            array_of_top_levels.remove(heading)
    print("An array of the top levels")
    print(array_of_top_levels)
    return array_of_top_levels
