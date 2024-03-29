# Thomas Hilton Johnson III
# 6/10/2019
# reg_expression.py
# Used to parse portions of the module tree
# Reference: Fernando Wittmann and Amber, https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
#Reference: https://stackabuse.com/using-regex-for-text-manipulation-in-python/
#Reference: https://stackoverflow.com/questions/17949508/python-read-all-text-file-lines-in-loop
#Reference: https://www.regextester.com/15
#Reference: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# Reference: https://www.w3schools.com/python/ref_dictionary_keys.asp
# Refernece: https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python
# Reference: https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
# Reference: https://stackoverflow.com/questions/509211/understanding-slice-notation
# Reference: https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str
# Reference: https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# Reference: https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
# Reference: https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
#Reference: https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
#Reference: https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
import re
import lists_to_dict_construct
import dict_to_array_dict
# content extract reads a file as an argument to access its content
def content_extract(input_content):
    target_file = open(input_content, "r") #Opens the file and stores the file object to a variable
    target_content = target_file.read() #The target_content variable stores the content of the file
    target_file.close() #Closes the file object
    return target_content # Returns the value of target_content

# text_to_heading_list converts the headings to a list
def text_to_heading_list(input_content):
    heading_acquired = re.findall("(.+\:)",input_content) #Regular expression that pulls the /glade/ headings form the file content and stores them in a list
    print("Here are the headings:")
    #cleaned_heading_acquired = array_clean_colons(heading_acquired)
    print(heading_acquired)
    heading_container ={} #Creates a ditionary to store headings as keys
    for heading in heading_acquired:#Iterates the through the list of directories/headings
        heading_container[heading] = []# Assigns each directory/headings as a key and lists as values
    return heading_acquired,heading_container #Returns the list containing the headings

# Get the non-heading content into a list (May not be needed)
def text_to_point(heading_list, input_content):
    list_of_modules = [] #Initializes a list to store all the non-heading content
    list_of_modules_and_headings = re.findall(".*",input_content) #List containing all the content from the file (headings and non-heading content)
    list_of_modules = remove_list_clones(list_of_modules_and_headings, heading_list) # Uses the remove_list_clones() function to remove the heading content
    #print("List of modules:\n")
    #print(list_of_modules)
    return list_of_modules # Returns a list of only modules

# The remove_list_clones function uses a reference_list argument to remove any similar antries from the primary_list
def remove_list_clones(primary_list, reference_list):
    for index in primary_list: #For loop iterating through primary_list content
        if index in reference_list: #Checks if the current index's value is within the reference_list
            primary_list.remove(index) # Removes the duplicates
        else:
            continue #continue if there are no simialr inentries in the list found
    #print(primary_list)
    return primary_list # Returns the list stored in primary_list

# list_clean function is utilized to remove empty strings from a list that is the argument of the function
def list_clean(list_with_empty_strings):
    for index in list_with_empty_strings: #For loop to iterate through the list that contains empty strings
        #print(index) #Prints the index value
        if index == "": # checks if the index value is an empty string
            list_with_empty_strings.remove(index) # Removes the empty string if found
        else:
            continue #If an empty string is not found, just continue
    print("No more empty strings:") #Prints the list with no empty strings present
    print(list_with_empty_strings)

# The array_clean_colons() function is used to clean out colons from the string elements of a provided list argument
def array_clean_colons(array_with_colons):# The argument can be any list with string elements
    array_without_colons = [] # Inititializes the list that has no colons present
    print(array_with_colons) #Print the list with colons to ensure that the function would need to be ran at this point
    for content_item in array_with_colons:#For loop that iterates every string element to search for strings that have a colon (:) present
        new_content_item = content_item.replace(":","") #A new, colon (:) free string is generated from the previous string
        array_without_colons.append(new_content_item) # The new, colon (:) free string is appended to the list array_without_colons
    print("Array without colons:") # Will print the entire list to allow the user to check and make sure that the list contains no colons whatsoever
    print(array_without_colons)
    return array_without_colons #Returns the entire list that will be absent of colons amongst its string elements


# full_list() function obtains all content from the file
def full_list(input_content):
    full_list_of_content = re.findall(".*",input_content) # Find all content in the file
    print("A full list of content is generated:")
    print(full_list_of_content)
    #print("This should be all content:")
    #print(full_list_of_content)
    return full_list_of_content #Returns the list containing all of the content
#Prints the lists containing the headings and the list containing all of the content
def print_heading_and_full_content_lists(list_of_headings, full_list_of_content):
    print("All relevant content:")
    print(full_list_of_content) #Prints a list containing all content
    #print("List of headings:")
    #print(list_of_headings) #Prints a list containing a heading

# Builds the track_list for later usage in the text_to_dict fucntion
def track_list_build(track_list, list_of_headings, full_list_of_content,heading_container):
    for index_count in full_list_of_content: # For loop that iterates thrugh the content that makes of elements of full_list_of_content
        index_value = index_count # Saves the value of index_count to index_value
        print("See index_value for loop populating track_list")
        print(index_value)# Need to remove semicolons in list.out
        if index_value in list_of_headings: # If statement that checks whether the value of index_value is in list_of_headings
            track_list.append(full_list_of_content.index(index_value)) #Appends the index (numerical index) of any heading in track_list
            print("Debugging by checking to make sure only directories are being caught for the track_list")
            print(full_list_of_content.index(index_value))
    track_list.append(len(full_list_of_content))# Appends the end of the list as there is no heading at the ending of the content
    print("Contents of track list:")
    print(track_list)
    print("\n")
    return track_list

def build_track_container(array_of_indices):
    tracking_container = {}
    number_of_key = 0
    for indices in array_of_indices:
        temporary_container = {number_of_key:indices}
        tracking_container.update(temporary_container)
        number_of_key += 1
    print("This is a tracking_container:")
    print(tracking_container)
    return tracking_container

# list_of_lists function builds the list_of_lists
def build_lists_of_lists(full_list_of_content, track_list):
    list_of_lists = []
    tracking_container = build_track_container(track_list)
    max_iteration = len(tracking_container) #Saves the index of the end of the list track_list
    for index_count in range(len(tracking_container)): # For loop that iterates through the tracking_container elements
        if (index_count+2) <= max_iteration: # If statement ensuring that the for loop does not excede the number of indices
            index_value = tracking_container[index_count]+1 #Stores the value of the index after a heading
            print("\n")
            print(index_value)
            second_index_value = tracking_container[index_count+1] # Stores the value of an index before the next heading
            print(second_index_value)
            print(index_count)
            print("The segmenting of list based on indices")
            print(full_list_of_content[index_value:second_index_value])
            list_of_lists.append(list(full_list_of_content[tracking_container[index_count]+1:tracking_container[index_count+1]])) # Appends the list of the sliced non heading content
            index_count+=1
    print("Array_item of the list_of_lists to observe:")
    for array_item in list_of_lists:
        print("\n", array_item)
    print("Indices of the track_list:")
    for indices in track_list:
        if indices < len(full_list_of_content):
            print(full_list_of_content[indices])
    return list_of_lists

# Prints the headings and the lists stored in list_of_lists
def heading_list_of_lists_print(list_of_headings, list_of_lists):
    print("\n\n\n")
    #print("Presented here is the list of headings:")
    #print(list_of_headings)
    #print("Presented here is a list of the lists of content:")
    #print(list_of_lists)

# Builds the content_containing_dict which is a dictionary containing the headings as keys and the associated content as values
def build_content_containing_dict(content_containing_dict, list_of_lists, list_of_headings):
    list_of_lists_index = 0
    for heading in list_of_headings: #For loop for adding headings and respective content
        #print(type(heading))
        temporary_content_dict = {} #Initializes a temporary dictionary to use
        temporary_content_dict[heading] = list_of_lists[list_of_lists_index] # The heading serves as the key while the cassociated content is the value of said key
        content_containing_dict.update(temporary_content_dict) # Updates content_containing_dict with the key and value of temporary_content_dict
        list_of_lists_index+=1 #Increases the value of list_of_lists_index by 1
    return content_containing_dict

#View the content_containing_dict for error checking
def view_content_containing_dict(content_containing_dict):
    for headings, content in content_containing_dict.items():
        print("\n")
        #print("\nHeading and the Content.")
        #print(headings, content)

#text_to_json_list is cused for constructung a one-level list-dictionary hybrid to be converted to JSON and utilized later
def text_to_json_list(list_of_headings, full_list_of_content):
    track_list = [] #Initializes the track_list which will store the indexes of content in between headings
    content_containing_dict = {} #Constructs a dictionary that will use the headings as keys and the lists containing content as the values
    print_heading_and_full_content_lists(list_of_headings, full_list_of_content) #prints out the heading and full_list_of_content structures for checking purposes
    track_list = track_list_build(track_list, list_of_headings, full_list_of_content) #Builds a list to track the indices of all non-heading/directory content, that list is called track_list
    list_of_lists = build_lists_of_lists(full_list_of_content, track_list) #Initializes the a list that will contain lists as elements
    heading_list_of_lists_print(list_of_headings, list_of_lists) # Prints the heading_list and list_of_lists values for debugging purposes
    compiled_for_json_list = assign_heading_level_dict(list_of_lists, list_of_headings) # used to generate the json list of each heading/directory being separate and having its own respective content
    return compiled_for_json_list #Returns the compiled_for_json_list that is ready to be converted to a JSON
    #content_containing_dict = build_content_containing_dict(content_containing_dict, list_of_lists, list_of_headings)
    #print("\n\n A dictionary containing headings with their respective content:")
    #view_content_containing_dict(content_containing_dict)
    #return content_containing_dict

# text_to_dict function constructs a dictionary of headings and a list of associated content
def text_to_dict(list_of_headings, full_list_of_content,heading_container): #Arguments are an array of the headings, an array of the associated content, and a dictionary of headings as keys and arrays of content as the values
    track_list = [] #Initializes the track_list which will store the indexes of content in between headings
    content_containing_dict = {} #Constructs a dictionary that will use the headings as keys and the lists containing content as the values
    print_heading_and_full_content_lists(list_of_headings, full_list_of_content) # Prints the list_of_headings and full_list_of_content lists for debugging purposes
    track_list = track_list_build(track_list, list_of_headings, full_list_of_content,heading_container) #Builds a list of indices by which only the content of each heading/directory can be found, which can then be used to construct a list containing only the lists of the content.
    list_of_lists = build_lists_of_lists(full_list_of_content, track_list) #Initializes the a list that will contain lists as elements
    heading_list_of_lists_print(list_of_headings, list_of_lists)#Use the heading_list_of_lists_print function to print the list contianing the headings and the list of the associated content for each heading
    content_containing_dict = 0#build_content_containing_dict(content_containing_dict, list_of_lists, list_of_headings) # A dictionary (from the original code's functions) is constructed that stores all the headings/directories as keys and the lists of content as values
    print("\n\n A dictionary containing headings with their respective content:")
    #view_content_containing_dict(content_containing_dict) #the function prints the dictionary, content_containing_dict, printing both keys and their associated values
    #resulting_array_dict = lists_to_dict_construct.start_build_top_dict(list_of_headings, list_of_lists,heading_container) #From second iteration of the code that builds heavily on reg_expression.py's functions to develop a hierachical list-dict construct using list comprehension mainly. This code requires lists_to_dict_construct.py file and its functions to be executed.
    print("\n")
    full_content_vessel = heading_point_to_list(heading_container,list_of_lists,list_of_headings)# From the third version of the code. Reorganizes a pre-designed dictionary of headings/directories as keys and lists of content as values to generate a hierarchical list-dict construct. This code depends heavily on the file dict_to_array_dict.py and its associated functions to be executed.
    return full_content_vessel, content_containing_dict #returns two separate variables full_content_vessel being obtained by the dict_to_array_dict.py code and content_containing_dict being obtained by the original code, both variables are being tilized in the FLASK application

#For calling dict_to_array_dict.py functions for generating a hierarchical list-dict construct
def heading_point_to_list(heading_construct, arrays_of_content,list_of_headings): # The function heading_point_to_list calls on code from the dict_to_array_dict.py and uses its functions to rearrange a dictionary of heading/directory and values of associated lists of content into a hierarchical list-dict construct. Has the arguments heading_construct, arrays_of_content,list_of_headings for building a new dictionary.
    for heading,content in zip(list_of_headings,arrays_of_content):# For loop iterating through the headings/directory, associated lists of content, this constructs a ditionary to avoid using parallel arrays any further
        heading_construct[heading] = content # The list containing headings is to make sure each key is paired with the cuorrect value (value being the list of associated content)
    print("\n Heading dictionary printed")
    for key, value in heading_construct.items():# Iterates the dictionary heading_construct to check the key, value pairs
        print("\n",key,value)
    full_compiler_construct = dict_to_array_dict.value_morph_dict(heading_construct) #The python file dict_to_array_dict.py with function value_morph_dict being called to return a hierarchical list-dict construct to be stored in the variable full_compiler_construct
    return full_compiler_construct # Returns the hierarchical list-dict construct

def assign_module_level_dict(list_of_content, heading):#Ignore, being used for text_to_json_list function for test purposes (arguments are headings and list of associated content)
    dict_of_heading = {} # Creates a dictionary of headings
    heading_list = [] # Creates a list to store the headings (outer wrap of list)
    for module in list_of_content: # A for loop is utilized to iterate for each string of content to construct a a new dictionary to be wrapped in another list
        module_list = []# New list is initialized to store each ditionary of content
        description_dict = {"label": str(module +" Description:"), "value": str(module + "descriptionvalue")}# A dictionary of the description of content with three keys and three separate values to be interpreted by the jQuery simpletree
        module_list.append(description_dict)# Appends the dictionary of content to a list
        module_dict ={"label":str(module), "value": str(module +"_value"), "children": module_list}#module_list is assigned as the valeu of the "children" key. Said key is part of the larger module_dict dictionary. Said dictionary is composed of three keys with three values for each key. The keys are "label", "value", "children"
        heading_list.append(module_dict) # Appends the module dict to the heading_list to be used for constructing a larger list-dict construct.
    temp_heading_dict = {"label": heading, "value": heading, "children": heading_list} # builds the overarching dictionary for the heading/directory to be returned by the function stored in temp_heading_dict
    return temp_heading_dict #Returns the value of temp_heading_dict

def assign_heading_level_dict(list_of_lists, list_of_headings):# Ignore, being used for text_to_json_list function for test purposes (arguments are headings and list of associated content)
    compiled_list= [] #Initializes a list to store the individual dictionaries that will encompass each heading/directory and their respective content
    for data_list, heading_index in zip(list_of_lists, list_of_headings): # Iterates both the headings/directories and lists of associated content for the purpose fo appending to the compiled_list
        compiled_list.append(assign_module_level_dict(data_list, heading_index)) #Appends the dictionary-list content to a larger list-dict construct
    return compiled_list #Returns the value of the variable compiled_list

def assign_name_of_file():
    name_of_file = input("What is the name of your file to submit to the Python scripts? Please type it. ")
    print("The name of the file is: ",name_of_file)
    if (name_of_file == "" or name_of_file == None):
        print("Not a proper file name. Running default file.")
        defaulted_file_name = "list.out"
        return defaulted_file_name
    else:
        return name_of_file

def main():#Initial main function that is the first version of the code implementation
    stored_content = content_extract("result_module_output.txt")# Content extraction to obtain the strings of the content
    stored_heading_content,heading_container = text_to_heading_list(stored_content) #test_to_heading function is called returning the stored_heading content and the heading_container that uses the headings/directories as keys
    stored_module_content = text_to_point(stored_heading_content, stored_content) #The function test_to_point is called to return the content of the extracted content
    stored_module_content = list_clean(stored_module_content)# Cleans the content list of empy strings
    full_content = full_list(stored_content) #Calls the full_list fucntion for the purpose of gaining a list of all content
    compiled_prep_for_json_list = text_to_json_list(stored_heading_content, full_content) #compiled_prep_for_json_list the content is formatted in such a way that would be acceptable as a JSON for the jQuery simpletree
    return compiled_prep_for_json_list #Returns the value for the jQuery simpletree

#Second implementation of the code is prone to breakage.
def main_dict():#Second main fucntion for the second version of the code implementation
    stored_content = content_extract("result_module_output.txt") # Content extraction to obtain the strings of the content
    stored_heading_content,heading_container = text_to_heading_list(stored_content)#test_to_heading function is called returning the stored_heading content and the heading_container that uses the headings/directories as keys
    stored_module_content = text_to_point(stored_heading_content, stored_content)#The function test_to_point is called to return the content of the extracted content
    stored_module_content = list_clean(stored_module_content)# Cleans the content list of empy strings
    full_content = full_list(stored_content)#Calls the full_list fucntion for the purpose of gaining a list of all content
    array_dict_containing_content, content_containing_dict = text_to_dict(stored_heading_content, full_content,heading_container) #returns the array_dict_containing_content as well as content_containing_dict
    return content_containing_dict#Returns the value of view_content_containing_dict

def main_array_dict():#Third main fucntion for the third version of the code implementation
    stored_content = content_extract(assign_name_of_file())# Content extraction to obtain the strings of the content
    stored_heading_content,heading_container = text_to_heading_list(stored_content)#test_to_heading function is called returning the stored_heading content and the heading_container that uses the headings/directories as keys
    stored_module_content = text_to_point(stored_heading_content, stored_content)#The function test_to_point is called to return the content of the extracted content
    stored_module_content = list_clean(stored_module_content)# Cleans the content list of empy strings
    full_content = full_list(stored_content)#Calls the full_list fucntion for the purpose of gaining a list of all content
    full_clean_content = list_clean(full_content)
    print("This is the full_contenttt:", full_clean_content)
    array_dict_containing_content, content_containing_dict = text_to_dict(stored_heading_content, full_content,heading_container)#returns the array_dict_containing_content as well as content_containing_dict
    return array_dict_containing_content #Returns the array_dict_containing_content
#def test():
#    stored_content = content_extract("result_module_output.txt")
#    stored_heading_content = text_to_heading_list(stored_content)
#    remove_slash(stored_heading_content)
#    print(stored_heading_content)

#test()
