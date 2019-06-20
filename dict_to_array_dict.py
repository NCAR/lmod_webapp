# Thomas Johnson III
# 6/19/2019
# dict_to_array_dict.py
# Converts the heading container to array dict
#Reference: https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
#Reference: https://stackoverflow.com/questions/13519644/how-to-solve-dictionary-changed-size-during-iteration-in-python/13519858
#Reference: https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely
#Reference: https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary

import copy
def value_morph_dict(heading_container):
    for key, content_array in heading_container.items():
        array_dict_content = []
        for element in content_array:
            element = {"label": element, "value": str(element + "_value")}
            array_dict_content.append(element)
        heading_container[key] = array_dict_content
    print("heading_container with array of dicts:")
    for key, content_array in heading_container.items():
        print("\n",key, content_array)
    full_compiler_container_complete = search_dict_children_from_target(heading_container)
    return full_compiler_container_complete

# search_dict_children_from_target fucntion accepts a string of content, an associated dictionary, a list of headings, a list of lists containing the content, and a heading cotaining the dictionary entry's children
def search_dict_children_from_target(heading_container):
    array_of_headings = list(heading_container.keys())
    clone_of_array_of_headings = array_of_headings.copy()
    heading_container_clone = copy.deepcopy(heading_container)
    for key, value_array_suspect in heading_container_clone.items():
        for value_suspect in value_array_suspect:
            check_label_bool, parent_heading = check_label_in_headings(value_suspect,array_of_headings)
            if check_label_bool == True and parent_heading != None:
                location_of_value_suspect = value_array_suspect.index(value_suspect)
                value_suspect = move_children(heading_container,array_of_headings, parent_heading, value_suspect, location_of_value_suspect)
                print("\n\nPrinting the value_suspect here:")
                print (value_suspect)
                print("\n\nThe full heading_container is printed:")
                print(heading_container)
                print("The missing heading:")
                missing_heading = heading_container.pop(parent_heading)
                print(missing_heading)
            else:
                continue
        print("\nThe resulting heirarchical array-dict object is here:")
        print(key,value_array_suspect)
    print("Totality of it all:")
    print(heading_container_clone)
    full_compiler_container = elminate_superfluous_keys(heading_container_clone,array_of_headings, clone_of_array_of_headings)
    return full_compiler_container

def elminate_superfluous_keys(heading_container_clone,array_of_headings,clone_of_array_of_headings):
    print("The array of headings:")
    print(array_of_headings)
    for heading in array_of_headings:
        if heading in clone_of_array_of_headings:
            clone_of_array_of_headings.remove(heading)
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
    search_dict_descendants(heading_container,array_of_headings, item_suspect["children"])
    return item_suspect

def search_dict_descendants(heading_container,array_of_headings,item_with_possible_descendants):
    print("Item with possible descendants:")
    print(item_with_possible_descendants)
    for content_container in item_with_possible_descendants:
        check_sub_label_bool, parent_sub_heading = check_label_in_headings(content_container, array_of_headings)
        if check_sub_label_bool == True and parent_sub_heading != None:
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
