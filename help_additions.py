# Thomas Johnson III
# 6/27/2019
# help_additions.py
# Extracts and adds the help information to the modules.
# Reference: https://stackoverflow.com/questions/8214932/how-to-check-if-a-value-exists-in-a-dictionary-python
# Reference: https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
import re #Imports the regular expression module from Python's standard library

# list_clean function is utilized to remove empty strings from a list that is the argument of the function
def list_clean(array_with_empty_strings):
    array_with_empty_strings = list(filter(None,array_with_empty_strings))
    print("No more empty strings:") #Prints the list with no empty strings present
    print(array_with_empty_strings)
    print("End...")
    return array_with_empty_strings

# The function construct_hunting_items() initiates the code in the Python file, first reading in another file for the rest of the functions to process
def construct_hunting_items(file_item): #The argument file_item is used to indicate what file should be read by the Python script
    open_target_file = open(file_item,"r")# Opens a file object that is stored in the variable open_target_file
    output_contents = open_target_file.read()# Reads the contents of the file object open_target_file into a variable output_contents
    open_target_file.close() # The file object open_target_file is now closed
    parse_contents_to_container(output_contents)# Calls the function parse_contents_to_container, which begins the next steps in processing the help output that is generated.

# acquiring_all_contents() function takes all the help contents and puts then in their own list through the usage of regular expressions
def acquiring_all_contents(entirety_of_help_contents): # For the function to work, the read contents of the file containing the help information most be provided as an argument to the function
    entirety_of_content_acquired = re.findall("(.*)",entirety_of_help_contents) #Uses the regular expression to parse out all of the contents of the file using Python's regular expression module. The results are then put into lists that capture each line.
    return entirety_of_content_acquired # Returns all of the content of the file. Will be used for later functions.

#parse_contents_to_container() function handles the next steps in processing the help information
def parse_contents_to_container(entirety_of_help_contents): # The argument needed for the function is all of the content of the file after the file has been read.
    target_keys_obtained = re.findall("(%HELP%.+)",entirety_of_help_contents)# regular expression using the unique '%HELP%' string is called. Said string denotes the proper path to the respective software that the help information belongs to.
    print(target_keys_obtained) #Prints the list of directories in order to ensure that they were properly processed.
    unclean_entirety_of_content = acquiring_all_contents(entirety_of_help_contents) #The acquiring_all_contents() function is called here, which will return the all of file's content to the variable entirety_of_content for later usage.
    entirety_of_content =list_clean(unclean_entirety_of_content)# The list_clean() fucntion is called for the purpose of removing the empty strings that will populate the list entirety_of_content.
    tracking_directory_container = construct_a_directory_container(target_keys_obtained) #The costruct_a_directory_container() function is called with the argument target_keys_obtained. The construct_a_directory_container function will return the dictionary of enumerated keys and a directory value for each of those given keys.
    tracking_indices_container = track_container_build(tracking_directory_container,entirety_of_content) #
    container_content_groupings = build_container_with_groups_of_arrays(entirety_of_content, tracking_indices_container)
    container_for_help_info = build_help_information_containing_dict(tracking_directory_container,container_content_groupings)

# The construct_a_directory_container() function is used to build a dictionary from a list.
def construct_a_directory_container(directory_keys_array): #The argument is directory_keys_array, which willprovide a list of the directories to be put into the dictionary
    tracking_directory_obtained = {}# tracking_directory_obtained dicitonary is initialized and will be used to store the contents of the given directories.
    counter_of_iteration = 0 # a variable storing the value of the current iteration. This will be used to generate enumerated keys, each possessing the value of a specific directory.
    for directory_key in directory_keys_array: #Initializing a for loop to begin the inserting the keys (numbers) and values (directories) of the dictionary to teh dictionary.
        temporary_single_item_container = {counter_of_iteration: directory_key} # a new, temporary dictionary called temporary_single_item_container is initialized to store the current value of counter_of_iteration as a key and a directory as the value.
        tracking_directory_obtained.update(temporary_single_item_container) # The tracking_directory_obtained dictionary is updated with the key, value pairing of the temporary_single_item_container
        counter_of_iteration += 1 #The variable counter_of_iteration is incremented so that the next directory will have a new number as a key.
    return tracking_directory_obtained # Returns tracking_directory_obtained to be utilized by the function or script in which it is called.

# track_container_build() function will be used build a dictionary of the relevant indices that will be utilized for picking out the content of each software path.
def track_container_build(container_of_directories, all_of_the_relevant_content): # The argument container_of_directories is a dictionary of the directory paths of the software and all_of_the_relevant_content being a list of all the relevant content of each software directory path
    tracking_indices_container_acquired = {}# Initializes a dictionary that will be used for recording the indices that will make off where the relevant content is
    record_the_key = 0 # used to keep a record of the number that is utilized as the keys for the for the tracking_indices_container_acquired
    for index_count in all_of_the_relevant_content: # For loop that iterates thrugh the content that makes of elements of all_of_the_relevant_content
        print("See index_value for loop populating tracking_indices_container_acquired")# Print statement used for debugging purposes
        print(index_count)
        if index_count in container_of_directories.values(): # If statement that checks whether the value of index_count is in container_of_directories
            temporary_indices_acquired = {record_the_key:all_of_the_relevant_content.index(index_count)}# temporary_indices_acquired dictionary is initialized with the record_the_key and the value being the index of a software directory path
            print("Debugging by checking to make sure only directories are being caught for the track_list")#Print statement that is utilized to for debugging purposes
            print(index_count)
            tracking_indices_container_acquired.update(temporary_indices_acquired) #tracking_indices_container_acquired is updated with the dictionary of temporary_indices_acquired
            record_the_key += 1 #Increments the record_the_key to give a unique enumerated key for each value for the tracking_indices_container_acquired
    temporary_last_addition = {record_the_key: len(all_of_the_relevant_content)} #Adds the final index to the dictionary to make sure to catch the last of the help contents of the  in the list.
    tracking_indices_container_acquired.update(temporary_last_addition)# Makes the fincal update to tracking_indices_container_acquired with the last index to be used to track the contents of the help contents.
    return tracking_indices_container_acquired# Returns the dictionary contained in tracking_indices_container_acquired


def build_container_with_groups_of_arrays(all_of_the_contents, container_of_tracking_indices):
    container_of_groupings_of_content = {}
    maximum_iteration = len(container_of_tracking_indices)
    #counter_of_iteration = 0
    print("Running!")
    print(all_of_the_contents)
    print("\n")
    print("Checking the tracking container.")
    print(container_of_tracking_indices)
    for index_position in range(len(container_of_tracking_indices)):
        if (index_position+2) <= maximum_iteration:
            print("To check if all_of_the_contents is present")
            print(all_of_the_contents)
            first_index_capture = container_of_tracking_indices[index_position]+1
            second_index_capture = container_of_tracking_indices[index_position+1]
            temporary_container_for_array = {index_position:all_of_the_contents[first_index_capture:second_index_capture]}
            container_of_groupings_of_content.update(temporary_container_for_array)
            index_position += 1
    print("container_of_groupings_of_content")
    print(container_of_groupings_of_content)
    return container_of_groupings_of_content

def build_help_information_containing_dict(container_possessing_directories, container_possessing_groupings_of_content):
    help_info_container = {}
    max_out_iteration = len(container_possessing_directories)
    print("Printing the directories.")
    print(container_possessing_directories)
    print("Printing the groupings of info.")
    print(container_possessing_groupings_of_content)
    for iteration in range(max_out_iteration):
        temp_container_help_info = {container_possessing_directories[iteration]:container_possessing_groupings_of_content[iteration]}
        help_info_container.update(temp_container_help_info)
    print("The help container.")
    print(help_info_container)


construct_hunting_items("help.out")

#def add_help_information(directory_key, content_target):
