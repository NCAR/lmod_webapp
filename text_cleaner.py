# Thomas Hilton Johnson III
# text_cleaner.py
# Utilizing regex to clean out unnecessary parts of the text
# Reference: https://stackabuse.com/using-regex-for-text-manipulation-in-python/
# Reference: https://stackoverflow.com/questions/11469228/python-replace-and-overwrite-instead-of-appending/11469328
import re


def dash_cleaner(input_file):
    target_file = open(input_file, "r")
    target_content = target_file.read()
    target_file.close()
    processed_content = re.sub(r"([\-\-]+) | ([\-\-]+)","",target_content)
    target_file = open(input_file, "w")
    target_file.write(processed_content)
    target_file.close()
    
def search_module_cleaner(input_file):
    target_file = open(input_file, "r")
    target_content = target_file.read()
    target_file.close()
    processed_content = re.sub(r"(Where\:)|(D\:.+)|(L\:.+)|(Use .+)","",target_content)
    target_file = open(input_file, "w")
    target_file.write(processed_content)
    target_file.close()
    
dash_cleaner("result_module_output.txt")   
search_module_cleaner("result_module_output.txt") 
