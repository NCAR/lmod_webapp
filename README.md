# lmod_webapp
A web application to interactively display Lmod trees

Web application built primarily using Python Flask.

Currently there are multiple txt files in the repository main directory:

References.txt (For any useful or necessary references that have not been inserted in comments in the available code. Will likely contain all necessary references throughout the code as a central file to store such information.)

result_module_output.txt (Currently where the modules are stored after being extracted from the bash terminal. This file is read by the reg_expression.py file to gain the data necessary for the rest of the application.)

Currently there is one bash script in the repository as well:

module_collect.sh (Collects the relevant compiler and module information)

This Flask Application has six different python files:

dict_to_json.py (Manages converting the final output of reg_expression.py to a json to send to the Javascript of the webpage.)

document.py (Holds the configuration and url patterns for the FLASK application. Currently, only two url patterns of note are stored in document.py. The first is "/" and the second is "/json/". The Flask app is ran using commands specified in comments of document.py.)

lists_to_dict_construct.py (Contains the functions necessary to convert the lists containing the content from the target file a hierarchical dictionary that stores sub dictionaries or respective children.)

reg_expression.py (Where the bulk of text processing and organization of content is handled.)

test_js_dict.py (Test code to see what structure could be implemented and accepted as json for the simpletree on the frontend.)

text_cleaner.py (Used at one point to parse the text. Currently unneeded.)

There are multiple JSON files present:

array_dict.json (Example of the format that the jQuery simpletree will accept. Short summary: the data must be contained in lists that contain dictionaries so that the JavaScript can interpret the JSON as the correct JavaScript object.)

dictionary.json (One example if the directories are used to organize the rest of the content.)

dictionary_2.json (One example if the directories are used to organize the rest of the content.)

dictionary_3.json (One example if the directories are used to organize the rest of the content.)

dictionary_3.txt (Example of a structure that cannot be used.)

## Directions
To run this application:
1. export FLASK_APP=document.py
2. flask run

then navigate to the specified url in a web browser to see the webpage to get to the default opage with HTML and CSS. To get the Javascript and Jquery simpletree implementation, add /json/ after the default url.
Ex: DEFAULT_URL/json/

Limitations:
1. The data must be loaded when the page initializes for the simpletree. Data cannot be added after the page has loaded.

2. The data must be loaded within a nested list to dictionary structure. The data will not be displayed otherwise as the simpletree will not be able to traverse said data.
