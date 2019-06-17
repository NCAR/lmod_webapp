# Thomas Johnson III
# June 17th, 2019
# lists_to_dict_construct.py
# Holds the functions for transforming the lists to dictionary



#def recursive_dict_search(input_dict_containing_lists):

#def recursive_list_search(input_list_containing_dicts):
    #for item in input_list_containing_dicts:
    #    if isinstance(item,dict):

#def dict

#def search_child(str_item,list_of_headings,list_of_lists):
    #if str_item in list_of_headings:

        #build_dict(


def start_build_top_dict(list_of_headings,list_of_lists):
    print("The list of lists:")
    print(list_of_lists)
    top_level_dict = {}
    track_dict_entries_index = 0
    clone_of_headings = list_of_headings.copy()
    clone_of_list_of_lists=list_of_lists.copy()
    clone_of_headings_index=0
    for item_list in clone_of_list_of_lists:
        print("Item List:")
        print(item_list)
        for item in item_list:
            item_dict = {"label": item, "value": str(item + "_value"), "children": "searching"}
            new_item_dict = search_dict_children(item,item_dict,clone_of_headings,clone_of_list_of_lists)
            print()
            top_level_dict[track_dict_entries_index] = new_item_dict
            print("Print new item dict")
            print(new_item_dict)
            track_dict_entries_index+=1
        #clone_of_list_of_lists.pop(clone_of_list_of_lists.index(item_list))
        clone_of_list_of_lists.pop(clone_of_headings_index)
        clone_of_headings.pop(clone_of_headings_index)
        clone_of_headings_index+=1
    return top_level_dict

def search_dict_children(item,item_dict,clone_of_headings,clone_of_list_of_lists):
    search_context = [heading for heading in clone_of_headings if item in heading]
    for heading in search_context:
        print("Printing the item to search heading: ", item)
        print("Printing the heading:")
        print(heading)
        heading_bool = False
        if item in heading:
            sub_dict = build_sub_dict(item,item_dict,clone_of_headings.index(heading),clone_of_list_of_lists,clone_of_headings)
            item_dict["children"] = sub_dict
            heading_bool = True
            print("heading boolean:")
            print(heading_bool)
        else:
            old_item_dict = {"label": item, "value": str(item + "_value")}
            item_dict["children"] = old_item_dict
    return item_dict
#Idea: create a dict where the keys are the headings and the values are the array of associated content!!
#Use the keys to to identify if it is a subdirectory and then use the value lists to iterate through the content smoothly
def build_sub_dict(item_name,item_dict, clone_of_headings_index, clone_of_list_of_lists,clone_of_headings):
    encompassing_dict = {}
    for content_item in clone_of_list_of_lists[clone_of_headings_index]:
        content_item_dict ={"label": content_item, "value": str(content_item + "_value"), "children": "searching"}
        new_content_item_dict = search_dict_children(content_item,content_item_dict,clone_of_headings,clone_of_list_of_lists)
        encompassing_dict = {clone_of_list_of_lists[clone_of_headings_index].index(content_item)}
    item_dict["children"] = new_content_item_dict
    return item_dict
