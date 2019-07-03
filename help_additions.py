# Thomas Johnson III
# 6/27/2019
# help_additions.py
# Extracts and adds the help information to the modules.
# Reference: https://stackoverflow.com/questions/8214932/how-to-check-if-a-value-exists-in-a-dictionary-python
# Reference: https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
# Reference: https://stackoverflow.com/questions/27093319/how-to-add-a-character-to-the-end-of-every-string-in-a-list/27093357
# Reference: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
# Reference: https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
# Reference: https://stackoverflow.com/questions/9483979/is-there-a-difference-between-continue-and-pass-in-a-for-loop-in-python
# Reference: https://stackoverflow.com/questions/27083445/how-to-join-two-string-with-a-new-line-between-them/27083457

import re #Imports the regular expression module from Python's standard library

# list_clean function is utilized to remove empty strings from a list that is the argument of the function
def list_clean(array_with_empty_strings):
    array_with_empty_strings = list(filter(None,array_with_empty_strings))
    #print("No more empty strings:") #Prints the list with no empty strings present
    #print(array_with_empty_strings)
    #print("End...")
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
        #print("See index_value for loop populating tracking_indices_container_acquired")# Print statement used for debugging purposes
        #print(index_count)
        if index_count in container_of_directories.values(): # If statement that checks whether the value of index_count is in container_of_directories
            temporary_indices_acquired = {record_the_key:all_of_the_relevant_content.index(index_count)}# temporary_indices_acquired dictionary is initialized with the record_the_key and the value being the index of a software directory path
            #print("Debugging by checking to make sure only directories are being caught for the track_list")#Print statement that is utilized to for debugging purposes
            #print(index_count)
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
    #print("Running!")#Print statement used for debuggung. Used to track if this part of the function has ran or not.
    #print(all_of_the_contents) #Prints all of the content of the file object in an array to ensure that the array was passed correctly.
    #print("\n")
    #print("Checking the tracking container.")# Print statement used for debugging by allowing the user to know if there is anything in the container_of_tracking_indices
    #print(container_of_tracking_indices)
    for index_position in range(len(container_of_tracking_indices)):#Initializing a for loop that will allow for enumerated keys for storing the arrays of content as values
        if (index_position+2) <= maximum_iteration:# If condition that ensures that the for loop does not run if the numer of usable indices has been exceeded (two indices, the current and the succeeding index, are being used every iteration)
            #print("...running for loop to build dictionary of arrays of help content..")# print statement used for debugging. Indicates the code has made it to this point (if statement is valid and not causing bugs)
            #print(all_of_the_contents)# Prints all_of_the_contents, used for debugging purposes.
            first_index_capture = container_of_tracking_indices[index_position]+1 # The beginning index of the new array is stored in first_index_capture
            second_index_capture = container_of_tracking_indices[index_position+1] # The ending index of the new array is stored in second_index_capture
            content_from_array_to_string = turn_all_of_array_content_to_string(all_of_the_contents[first_index_capture:second_index_capture])
            temporary_container_for_array = {index_position:content_from_array_to_string}# The enumerated key is provided by index_position and the array value is the list comprehension of first_index_capture and second_index_capture of the list all_of_the_contents and srored in the ewly initialized dictionary
            container_of_groupings_of_content.update(temporary_container_for_array) # The dictionary container_of_groupings_of_content is updated by the dictionary temporary_container_for_array to store an enumerated key and array of help content values
            index_position += 1 # Increments the index_postion by 1 as a pair of indices is being utilized in the for loop at any given time.
    #print("container_of_groupings_of_content")#Prints the contents of the container_of_groupings_of_content dictionary to validate key-values were stored correctly.
    #print(container_of_groupings_of_content)
    return container_of_groupings_of_content # Returns the dictionary being pointed to by container_of_groupings_of_content to where the function is called it is called

# build_help_information_containing_dict() function is used to construct a dictionary of the help information that is relevant to the software information tree in the that will be constructed later
def build_help_information_containing_dict(container_possessing_directories, container_possessing_groupings_of_content): #Accepts the arguments: container_possessing_directories, a dictionary that contains the paths of the relevant software in the tree software, and container_possessing_groupings_of_content, a dictionary that contains the lists of associated help content
    help_info_container = {} # Initializes the dictionary that is stored in the variable help_info_container
    max_out_iteration = len(container_possessing_directories)#the variable max_out_iteration stores the maximum iteration that will be reached by the for loop that will be initialized. This ensures the for loop does not exceed that of what is limited.
    #print("Printing the directories.")
    #print(container_possessing_directories) # Prints the value of the variable container_possessing_directories for debugging putposes, mainly to see if the variable actually stored anything.
    #print("Printing the groupings of info.")
    #print(container_possessing_groupings_of_content)# Prints the value of container container_possessing_groupings_of_content for debugging purposes, mainly to observe if the variable actually contains anything.
    for iteration in range(max_out_iteration): # Initializes a for loop that uses the enumerates keys of container_possessing_directories and container_possessing_groupings_of_content to pair each software path with its respective help content.
        clean_directory = re.sub("%HELP% ","",container_possessing_directories[iteration]) # Cleans the "%HELP%" string from the path of the software
        temp_container_help_info = {clean_directory:container_possessing_groupings_of_content[iteration]} #The temporary dictionary temp_container_help_info is utilized to temporarily store each pairing of software path and the assoctated help content.
        help_info_container.update(temp_container_help_info) # Will update the help_info_container dictionary with contents stored in temp_container_help_info
    #print("The help container.")
    #print(help_info_container)# Will print out the contents of the help_info_container dict to ensure that it has contents to utilize
    #print("Regex is being tested:") #Tesing purposes, to be transferred elsewhere.
    for path in help_info_container:# For loop initialized to iterate though the software path keys of the help_info_container
        separate_the_siginificant_parts_of_the_path(path) #Calls the separate_the_significant_parts_of_the_path() function to get an array of the path_items necessary to to correctly store the contents of the module help
    return help_info_container # Return help_info_container to where the build_help_information_containing_dict() function is called

# separate_the_siginificant_parts_of_the_path() fucntion is used to sparate the software path into separate pieces to work with
def separate_the_siginificant_parts_of_the_path(the_path_to_be_partitioned):# The argument the_path_to_be_partitioned is the referring to the key of the help_info_container that has currently been added as an argument
    temp_array_hold = re.split("/",the_path_to_be_partitioned)# The temp_array_hold variable is used to store the result of the split methd using re module of Python
    measure_of_arr = len(temp_array_hold) # Storing the value of the complete size of the array for usage later within the function for modifying the last portion of the path
    temp_array_path_holder = [edited_path + "/" for edited_path in temp_array_hold] #using list comprehension, temp_array_path_holder variable is used to append the forward slash to the end of each string element that is in the list pointed to temp_array_hold
    current_end_index = temp_array_path_holder[measure_of_arr-1] #current_end_index stores the last index of the array so that it can be modified (paths to software do not end with "/")
    new_replacement_index = current_end_index.replace("/","")#new_replacement_index stores a new string that is a modified string of current_end_index
    temp_array_path_holder.remove(current_end_index)#Removes the element that was in the position of the final index of the list
    temp_array_path_holder.append(new_replacement_index)# Replaces the element removed in the previous line with the modified version of that same string
    #print("Observe the elements in the array.")
    #print(temp_array_path_holder) #Print statement used for debugging purposes
    separated_path_items = transform_the_array_of_regex(temp_array_path_holder) # Calls the transform_the_array_of_regex() function to concatenate the elements of the list of path elements so that future lines of code will not have to compensate with specifying two indices to make up one portion of the path
    return separated_path_items # Returns the array formed by the seperated_path_items variable

# transform_the_array_of_regex() is used to piece together the path_items into an easier to utilize list of elements. Otherwise, the elements would be used where they end with the forward slash.
def transform_the_array_of_regex(regex_result_array): # The regex_result_array argument is the list outputted from using the re.split method to generate the elements.
    separated_joined_path_items = [] # Initializes a new list for the purpose of storing the new software path elements
    max_limiter_of_iteration = len(regex_result_array)# Stores the limit that the upcoming for loop can meet before throuwing errors
    iteration_number = 0 #iteration_number is a variable that stores thevalue of the current iteration
    for iteration_number in range(max_limiter_of_iteration): #For loop initialization  using iteration_number and max_limiter_of_iteration
        if (iteration_number+2) <= max_limiter_of_iteration:# If statement that ensures the for loop does not run in excess of the number of elements that are actually present
            if (iteration_number % 2) == 0:# If statement used to make sure the operations within the for loop (which use two indices at a time), does not overlap in the mount of indices used
                #print("Iteration number: ",iteration_number) #Prints the iteration the for loop is on for debugging purposes
                #print("First string element: ", regex_result_array[iteration_number]) # Prints the first element to be used, to debug if the operations are working appropriately
                #print("Second string element:", regex_result_array[iteration_number+1])# Prints the second element to be used, to debug if the operations are working appropriately
                separated_joined_path_items.append(regex_result_array[iteration_number] + regex_result_array[iteration_number+1])# Appends the first and second elements of the current iteration of the for loop together in one string
                #print("Iteration number incremented: ",iteration_number) # Prints the value of the current iteration for the purpose for the purpose of debugging
    #print("Observe the list that was created from joining the regex items together:") #Print statement that displays the path items in a much easier to manipulate state.
    #print(separated_joined_path_items)
    return separated_joined_path_items # Returns the separated_joined_path_items to where the transform_the_array_of_regex() function is called


# attach_help_to_heading_container() function, when executed, it will extract the help module information and return said help module information to be stored in a variable in dict_to_array.py
def attach_help_to_heading_container(container_possessing_help_info, target_directory_key, target_directory_array_of_content, container_of_simple_tree, target_software): #five arguments are accepted here: container_possessing_help_info is a dictionary that stores the paths of the help module information as keys and the help module information itself as values,target_directory_key is the directory from the container_of_simple_tree that the for loop outside this file is currently on, target_directory_array_of_content is the list of content that from container_of_simple_tree that the for loop in dict_to_array.py is currently on, container_of_simple_tree is dictionary directories as keys and lists of software content as values, target_software is the current software that the for loop in dict_to-array.py is currently attempting to build a dictionary for within the for loop
    for help_path,help_contents in container_possessing_help_info.items(): #for loop initialized to iterate the paths to the help information (keys) in the container_possessing_help_info
        vessel_containing_help_path_items = separate_the_siginificant_parts_of_the_path(help_path)
        print("Printing the help_path:")
        print(vessel_containing_help_path_items)
        print("The software target from the simpletree:")
        print(target_software)
        print("this is the directory we are in at the moment:")
        print(target_directory_key)
        print("Printing of the keys:")
        print(container_of_simple_tree.keys())
        if vessel_containing_help_path_items[0] == target_software and vessel_containing_help_path_items[0] +":" not in list(container_possessing_help_info.keys()):
            located_case_of_software = vessel_containing_help_path_items[0]
            compiler_modal_content = container_possessing_help_info[located_case_of_software]
            print("Am I running?")
            return compiler_modal_content
        else:
            pass
        if len(vessel_containing_help_path_items) == 1:
            top_level_software_help_information = vessel_containing_help_path_items[0]
            if top_level_software_help_information in container_of_simple_tree["compilers:"] and top_level_software_help_information == target_software:
                compiler_dependent_modal_content = container_possessing_help_info[top_level_software_help_information]
                print(".....")
                return compiler_dependent_modal_content
            else:
                pass
            if top_level_software_help_information in container_of_simple_tree["idep:"] and top_level_software_help_information == target_software:
                compiler_independent_modal_content = container_possessing_help_info[top_level_software_help_information]
                print("....!")
                return compiler_independent_modal_content
            else:
                pass
        else:
            path_matching_key_in_heading_container = turn_most_of_array_content_to_string(vessel_containing_help_path_items)
            path_matching_key_in_heading_container_colon = character_replacement_with_colon(path_matching_key_in_heading_container)
            pinpoint_software = vessel_containing_help_path_items[(len(vessel_containing_help_path_items)-1)]
            if "cuda" in path_matching_key_in_heading_container_colon:
                print("Viewing the string to observe the target container:")
                print(path_matching_key_in_heading_container_colon)
                print("Directory being looked at:")
                print(target_directory_key)
                print("Looking at the formatting of the software:")
                print(pinpoint_software)
                print("Looking at the formatting of the compared software:")
                print(target_software)
            if path_matching_key_in_heading_container_colon == target_directory_key and pinpoint_software == target_software:
                print("Is the if statement being satisfied?")
                print("\n The help software path for the simpletree: ", path_matching_key_in_heading_container_colon)
                print("\n The directory_key within the simpletree: ", target_directory_key)
                software_help_information = container_possessing_help_info[help_path]
                return software_help_information


def character_replacement_with_colon(inputted_string_for_character_replacement):
    measure_of_the_size_of_the_string = len(inputted_string_for_character_replacement)
    colon_replacement_string = inputted_string_for_character_replacement[:(measure_of_the_size_of_the_string-1)] + ":"
    return colon_replacement_string


def turn_most_of_array_content_to_string(array_that_is_to_be_used_to_craft_a_string):
    total_measure_of_the_array = len(array_that_is_to_be_used_to_craft_a_string)
    new_key_for_locating_help_info_placement = "".join(array_that_is_to_be_used_to_craft_a_string[0:(total_measure_of_the_array-1)])
    retrieved_string = str(new_key_for_locating_help_info_placement)
    return retrieved_string

def turn_all_of_array_content_to_string(a_few_strings_that_are_currently_in_a_list):
    complete_measure_of_the_array = len(a_few_strings_that_are_currently_in_a_list)
    new_content_from_the_array = "\n".join(a_few_strings_that_are_currently_in_a_list[0:complete_measure_of_the_array])
    received_content_string = str(new_content_from_the_array)
    return received_content_string
