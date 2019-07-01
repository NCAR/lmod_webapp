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
    help_content_info_conteiner = parse_contents_to_container(output_contents)# Calls the function parse_contents_to_container, which begins the next steps in processing the help output that is generated.
    return help_content_info_conteiner

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
    return container_for_help_info # Returns the dictionary that contains all fo the help content

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

# build_container_with_groups_of_arrays() function will build a dictionary of arrays that will be utilized for the purpose of building a dictionary that will keep track of the arrays of content that will later be paired with their paths in the software directory
def build_container_with_groups_of_arrays(all_of_the_contents, container_of_tracking_indices):# the argument all_of_the_contents is a variable pointing to the entire list of content that has been read from the file. The argument container_of_tracking_indices is a ditionary fo the indices that must be tracked to correctly divide up the array based on what content should go where.
    container_of_groupings_of_content = {}# The dictionary pointed to by container_of_groupings_of_content is initialized. This dictionary is used for the purpose of storing each array of content with an enumerated index to later be matched with the correct software directory path
    maximum_iteration = len(container_of_tracking_indices) # Keeps track of the max number of iterations to ensure that the for loop initialized later does not exceed the its limit.
    #counter_of_iteration = 0
    print("Running!")#Print statement used for debuggung. Used to track if this part of the function has ran or not.
    print(all_of_the_contents) #Prints all of the content of the file object in an array to ensure that the array was passed correctly.
    print("\n")
    print("Checking the tracking container.")# Print statement used for debugging by allowing the user to know if there is anything in the container_of_tracking_indices
    print(container_of_tracking_indices)
    for index_position in range(len(container_of_tracking_indices)):#Initializing a for loop that will allow for enumerated keys for storing the arrays of content as values
        if (index_position+2) <= maximum_iteration:# If condition that ensures that the for loop does not run if the numer of usable indices has been exceeded (two indices, the current and the succeeding index, are being used every iteration)
            print("...running for loop to build dictionary of arrays of help content..")# print statement used for debugging. Indicates the code has made it to this point (if statement is valid and not causing bugs)
            #print(all_of_the_contents)# Prints all_of_the_contents, used for debugging purposes.
            first_index_capture = container_of_tracking_indices[index_position]+1 # The beginning index of the new array is stored in first_index_capture
            second_index_capture = container_of_tracking_indices[index_position+1] # The ending index of the new array is stored in second_index_capture
            temporary_container_for_array = {index_position:all_of_the_contents[first_index_capture:second_index_capture]}# The enumerated key is provided by index_position and the array value is the list comprehension of first_index_capture and second_index_capture of the list all_of_the_contents and srored in the ewly initialized dictionary
            container_of_groupings_of_content.update(temporary_container_for_array) # The dictionary container_of_groupings_of_content is updated by the dictionary temporary_container_for_array to store an enumerated key and array of help content values
            index_position += 1 # Increments the index_postion by 1 as a pair of indices is being utilized in the for loop at any given time.
    print("container_of_groupings_of_content")#Prints the contents of the container_of_groupings_of_content dictionary to validate key-values were stored correctly.
    print(container_of_groupings_of_content)
    return container_of_groupings_of_content # Returns the dictionary being pointed to by container_of_groupings_of_content to where the function is called it is called

# build_help_information_containing_dict() function is used to construct a dictionary of the help information that is relevant to the software information tree in the that will be constructed later
def build_help_information_containing_dict(container_possessing_directories, container_possessing_groupings_of_content): #Accepts the arguments: container_possessing_directories, a dictionary that contains the paths of the relevant software in the tree software, and container_possessing_groupings_of_content, a dictionary that contains the lists of associated help content
    help_info_container = {} # Initializes the dictionary that is stored in the variable help_info_container
    max_out_iteration = len(container_possessing_directories)#the variable max_out_iteration stores the maximum iteration that will be reached by the for loop that will be initialized. This ensures the for loop does not exceed that of what is limited.
    print("Printing the directories.")
    print(container_possessing_directories) # Prints the value of the variable container_possessing_directories for debugging putposes, mainly to see if the variable actually stored anything.
    print("Printing the groupings of info.")
    print(container_possessing_groupings_of_content)# Prints the value of container container_possessing_groupings_of_content for debugging purposes, mainly to observe if the variable actually contains anything.
    for iteration in range(max_out_iteration): # Initializes a for loop that uses the enumerates keys of container_possessing_directories and container_possessing_groupings_of_content to pair each software path with its respective help content.
        temp_container_help_info = {container_possessing_directories[iteration]:container_possessing_groupings_of_content[iteration]} #The temporary dictionary temp_container_help_info is utilized to temporarily store each pairing of software path and the assoctated help content.
        help_info_container.update(temp_container_help_info) # Will update the help_info_container dictionary with contents stored in temp_container_help_info
    print("The help container.")
    print(help_info_container)# Will print out the contents of the help_info_container dict to ensure that it has contents to utilize
    print("Regex is being tested:")
    for path in help_info_container:
        temp_array_hold = re.split(".*/.*",path)
        print(temp_array_hold)
    return help_info_container # Return help_info_container to where the build_help_information_containing_dict() function is called



construct_hunting_items("help.out")# Executes the construct_hunting_items() function with the argument hile name "help.out"

#def add_help_information(directory_key, content_target):
