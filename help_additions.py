# Thomas Johnson III
# 6/27/2019
# help_additions.py
# Adds the help information to the modules.
import re
def construct_hunting_items(file_item):
    open_target_file = open(file_item,"r")
    output_contents = open_target_file.read()
    open_target_file.close()
    parse_contents_to_container(output_contents)

def acquiring_all_contents(entirety_of_help_contents):
    entirety_of_content_acquired = re.findall("(.*)",entirety_of_help_contents)
    return entirety_of_content_acquired

def parse_contents_to_container(entirety_of_help_contents):
    target_keys_obtained = re.findall("(%HELP%.+)",entirety_of_help_contents)
    print(target_keys_obtained)
    entirety_of_content = acquiring_all_contents(entirety_of_help_contents)
    tracking_directory_container = construct_a_directory_container(target_keys_obtained)
    tracking_indices_container = track_container_build(tracking_directory_container,entirety_of_content)


def construct_a_directory_container(directory_keys_array):
    tracking_directory_obtained = {}
    for directory_key in directory_keys_array:
        temporary_single_item_container = {directory_key: []}
        tracking_directory_obtained.update(temporary_single_item_container)
    return tracking_directory_obtained

def track_container_build(container_of_directories, all_of_the_relevant_content):
    tracking_indices_container_acquired = {}
    record_the_key = 0
    for index_count in all_of_the_relevant_content: # For loop that iterates thrugh the content that makes of elements of all_of_the_relevant_content
        print("See index_value for loop populating tracking_indices_container_acquired")
        print(index_count)
        if index_count in container_of_directories: # If statement that checks whether the value of index_count is in container_of_directories
            temporary_indices_acquired = {record_the_key:all_of_the_relevant_content.index(index_count)}
            print("Debugging by checking to make sure only directories are being caught for the track_list")
            tracking_indices_container_acquired.update(temporary_indices_acquired)
            record_the_key += 1
    temporary_last_addition = {record_the_key: len(all_of_the_relevant_content)}
    tracking_indices_container_acquired.update(temporary_last_addition)
    return tracking_indices_container_acquired

def build_container_with_groups_of_arrays(all_of_the_contents, container_of_tracking_indices):
    container_of_groupings_of_content = {}
    maximum_iteration = len(container_of_tracking_indices)
    for index_position in range(len(container_of_tracking_indices)):
        if (index_position+2) <= maximum_iteration:
            index_capture = container_of_tracking_indices[index_position]+1
            

construct_hunting_items("help.out")

#def add_help_information(directory_key, content_target):
