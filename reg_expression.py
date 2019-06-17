# Thomas Hilton Johnson III
# 6/10/2019
# reg_expression.py
# Used to parse portions of the module tree
# Reference: Fernando Wittmann and Amber, https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
#Reference: https://stackabuse.com/using-regex-for-text-manipulation-in-python/
#Reference: https://stackoverflow.com/questions/17949508/python-read-all-text-file-lines-in-loop
#Reference: https://www.regextester.com/15
#https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# Reference: https://www.w3schools.com/python/ref_dictionary_keys.asp
# Refernece: https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python
# Reference: https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
# Reference: https://stackoverflow.com/questions/509211/understanding-slice-notation
# Reference: https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str
# Reference: https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
# Reference: https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
# Reference: https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
import re
import lists_to_dict_construct
# content extract reads a file as an argument to access its content
def content_extract(input_content):
    target_file = open(input_content, "r") #Opens the file and stores the file object to a variable
    target_content = target_file.read() #The target_content variable stores the content of the file
    target_file.close() #Closes the file object
    return target_content # Returns the value of target_content

# text_to_heading_list converts the headings to a list
def text_to_heading_list(input_content):
    heading_acquired = re.findall("(\/glade[\/a-z0-9\.]*)",input_content) #Regular expression that pulls the /glade/ headings form the file content and stores them in a list
    #print(heading_acquired)
    return heading_acquired #Returns the list containing the headings

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
    #print(list_with_empty_strings)

# full_list() function obtains all content from the file
def full_list(input_content):
    full_list_of_content = re.findall(".*/.*",input_content) # Find all content in the file
    #print("This should be all content:")
    #print(full_list_of_content)
    return full_list_of_content #Returns the list containing all of the content
#Prints the lists containing the headings and the list containing all of the content
def print_heading_and_full_content_lists(list_of_headings, full_list_of_content):
    print("All content:")
    #print(full_list_of_content) #Prints a list containing all content
    #print("List of headings:")
    #print(list_of_headings) #Prints a list containing a heading

# Builds the track_list for later usage in the text_to_dict fucntion
def track_list_build(track_list, list_of_headings, full_list_of_content):
    for index_count in full_list_of_content: # For loop that iterates thrugh the content that makes of elements of full_list_of_content
        index_value = index_count # Saves the value of index_count to index_value
        #print("See index_value for loop populating track_list")
        #print(index_value)
        if index_value in list_of_headings: # If statement that checks whether the value of index_value is in list_of_headings
            track_list.append(full_list_of_content.index(index_value)) #Appends the index (numerical index) of any heading in track_list
    track_list.append(len(full_list_of_content))# Appends the end of the list as there is no heading at the ending of the content
    print("Contents of track list:")
    print(track_list)
    print("\n")
    return track_list

# list_of_lists function builds the list_of_lists
def build_lists_of_lists(full_list_of_content, track_list):
    list_of_lists = []
    max_iteration = len(track_list) #Saves the index of the end of the list track_list
    for index_count in range(len(track_list)): # For loop that iterates through the track_list elements
        if (index_count+2) <= max_iteration: # If statement ensuring that the for llop does not excede the number of indices
            index_value = track_list[index_count]+1 #Stores the value of the index after a heading
            print("\n")
            print(index_value)
            second_index_value = track_list[index_count+1]-1 # Stores the value of an index before the next heading
            print(second_index_value)
            list_of_lists.append(list(full_list_of_content[index_value:second_index_value])) # Appends the list of the sliced non heading content
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

# text_to_dict function constructs a dictionary of headings and a list of associated content
def text_to_json_list(list_of_headings, full_list_of_content):
    track_list = [] #Initializes the track_list which will store the indexes of content in between headings
    content_containing_dict = {} #Constructs a dictionary that will use the headings as keys and the lists containing content as the values
    print_heading_and_full_content_lists(list_of_headings, full_list_of_content)
    track_list = track_list_build(track_list, list_of_headings, full_list_of_content)
    list_of_lists = build_lists_of_lists(full_list_of_content, track_list) #Initializes the a list that will contain lists as elements
    heading_list_of_lists_print(list_of_headings, list_of_lists)
    compiled_for_json_list = assign_heading_level_dict(list_of_lists, list_of_headings)
    return compiled_for_json_list
    #content_containing_dict = build_content_containing_dict(content_containing_dict, list_of_lists, list_of_headings)
    #print("\n\n A dictionary containing headings with their respective content:")
    #view_content_containing_dict(content_containing_dict)
    #return content_containing_dict

def text_to_dict(list_of_headings, full_list_of_content):
    track_list = [] #Initializes the track_list which will store the indexes of content in between headings
    content_containing_dict = {} #Constructs a dictionary that will use the headings as keys and the lists containing content as the values
    print_heading_and_full_content_lists(list_of_headings, full_list_of_content)
    track_list = track_list_build(track_list, list_of_headings, full_list_of_content)
    list_of_lists = build_lists_of_lists(full_list_of_content, track_list) #Initializes the a list that will contain lists as elements
    heading_list_of_lists_print(list_of_headings, list_of_lists)
    content_containing_dict = build_content_containing_dict(content_containing_dict, list_of_lists, list_of_headings)
    print("\n\n A dictionary containing headings with their respective content:")
    view_content_containing_dict(content_containing_dict)
    resulting_dict = lists_to_dict_construct.start_build_top_dict(list_of_headings, list_of_lists)
    print("\n\nNow printing the dictionary containing dictionaries:")
    print(resulting_dict)
    print("\n")
    return content_containing_dict

def assign_module_level_dict(list_of_content, heading):#Ignore
    dict_of_heading = {}
    heading_list = []
    for module in list_of_content:
        module_list = []
        description_dict = {"label": str(module +" Description:"), "value": str(module + "descriptionvalue")}
        module_list.append(description_dict)
        module_dict ={"label":str(module), "value": str(module +"_value"), "children": module_list}#, "children": module_list
        heading_list.append(module_dict)
    temp_heading_dict = {"label": heading, "value": heading, "children": heading_list}
    return temp_heading_dict

def assign_heading_level_dict(list_of_lists, list_of_headings):# Ignore
    compiled_list= []
    for data_list, heading_index in zip(list_of_lists, list_of_headings):
        compiled_list.append(assign_module_level_dict(data_list, heading_index))
    return compiled_list



def main():
    stored_content = content_extract("result_module_output.txt")
    stored_heading_content = text_to_heading_list(stored_content)
    stored_module_content = text_to_point(stored_heading_content, stored_content)
    stored_module_content = list_clean(stored_module_content)
    full_content = full_list(stored_content)
    compiled_prep_for_json_list = text_to_json_list(stored_heading_content, full_content)
    return compiled_prep_for_json_list
def main_dict():
    stored_content = content_extract("result_module_output.txt")
    stored_heading_content = text_to_heading_list(stored_content)
    stored_module_content = text_to_point(stored_heading_content, stored_content)
    stored_module_content = list_clean(stored_module_content)
    full_content = full_list(stored_content)
    content_containing_dict = text_to_dict(stored_heading_content, full_content)
    return content_containing_dict
#def test():
#    stored_content = content_extract("result_module_output.txt")
#    stored_heading_content = text_to_heading_list(stored_content)
#    remove_slash(stored_heading_content)
#    print(stored_heading_content)
main()
#test()
