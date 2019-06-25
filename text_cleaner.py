# Thomas Hilton Johnson III
# text_cleaner.py
# Utilizing regex to clean out unnecessary parts of the text
# Reference: https://stackabuse.com/using-regex-for-text-manipulation-in-python/
# Reference: https://stackoverflow.com/questions/11469228/python-replace-and-overwrite-instead-of-appending/11469328
# Not necessary for the main implmentation of the code.
import re # Imports the regular expression module of Python


def dash_cleaner(input_file):#dash_cleaner() function takes a file as an argument
    target_file = open(input_file, "r")n# opens the file argument to be read
    target_content = target_file.read() #Stores the content of the file to a variable target_content
    target_file.close()#closes the file that has been opened
    processed_content = re.sub(r"([\-\-]+) | ([\-\-]+)","",target_content) # The variable processed_content is assigned the result of removing excess punctuation - from the text
    target_file = open(input_file, "w")# The file argument is opened to be written
    target_file.write(processed_content)# The file argument has the text of processed_content is written to the file
    target_file.close()# The file is then closed

def search_module_cleaner(input_file):#search_module_cleaner() function takes a file as an argument
    target_file = open(input_file, "r") # The argument file is opened to read its content into the variable target_file
    target_content = target_file.read()# text from the target_file is stored into the variable target_content
    target_file.close()# The file opened with the variable target_file is closed
    processed_content = re.sub(r"(Where\:)|(D\:.+)|(L\:.+)|(Use .+)","",target_content) #Regular expression used to get rid of unneeded lines of text.
    target_file = open(input_file, "w") # target_file used to open the file for writing
    target_file.write(processed_content)# value of the variable processed_content is written to the file
    target_file.close() # The file opened with target_file is now being closed

dash_cleaner("result_module_output.txt") #Calls the function dash_cleaner() with the the file result_module_output.txt as its argument
search_module_cleaner("result_module_output.txt") # Calls the function search_module_cleaner() with the file result_module_output.txt as its argument
