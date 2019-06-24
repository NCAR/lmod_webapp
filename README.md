# lmod_webapp
A web application to interactively display Lmod trees

Web application built primarily using Python Flask.

Currently there are multiple txt files in the repository main directory:

References.txt (For any useful or necessary references that have not been inserted in comments in the available code. Will likely contain all necessary references throughout the code as a central file to store such information.)

result_module_output.txt (Currently where the modules are stored after being extracted from the bash terminal. This file is read by the reg_expression.py file to gain the data necessary for the rest of the application.)

Currently there is one bash script in the repository as well:

module_collect.sh (Collects the relevant compiler and module information)
->module_collect.sh will output a file with the relevant module information. The most recent version was developed using regular expressions provided by Brian Vanderwende. Subject to further modification.

This Flask Application has six different python files:

dict_to_json.py (Manages converting the final output of reg_expression.py to a json to send to the Javascript of the webpage.)

document.py (Holds the configuration and url patterns for the FLASK application. Currently, only two url patterns of note are stored in document.py. The first is "/" and the second is "/json/". The Flask app is ran using commands specified in comments of document.py.)

lists_to_dict_construct.py (Contains the functions necessary to convert the lists containing the content from the target file a hierarchical dictionary that stores sub dictionaries or respective children. Note: Utilizes recursive functions for this process. If altered, please verify the functions are not recursively storing the same dictionary entries over and over.)

reg_expression.py (Where the bulk of text processing and organization of content is handled.)

test_js_dict.py (Test code to see what structure could be implemented and accepted as json for the simpletree on the frontend.)

text_cleaner.py (Used at one point to parse the text. Currently unneeded.)

dict_to_array_dict.py (The Python file is used to generate hierarchical list-dict construct using a pre-made dictionary containing headings/directories as keys and lists of associated content as values. Necessary for the current version of the code to be executed.)

There are currently three html files present:

view_modules.html (The original HTML file utilized for testing purposes. view_modules.html is the default route for the Flask application.)

json_modules.html (The second HTML file developed. To get to this page json/ must be added to the base URL.)

test.html (Unneeded, used for initial experimentation with JavaScript)

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

3. If the nesting of the dictionaries require extreme depth, the recursive functions can become overwhelmed if there is an extreme quantity of recursive calls.

4. Currently requires a file to already exist with the required information for building the module tree.

Debugging:

To see a relatively organized print out of the list-dict construct call the recursive_dict_print_dict() function from lists_to_dict.py at end of the construction of the full list-dict construct or while building it (note there can be a lot of content that will be printed out.) It will print out all the dictionaries in the list-dict construct. Use the printed results to try and find any bugs that may be occurring the code.

If the simpletree is not properly displaying, be sure to check that the correctly formatted JSON object is being transferred to the JavaScript via Flask and Jinja2. The structure be alternating lists to dictionaries, to more lists to dictionaries. Also, the keys should be label, value and children. If the JSON removed from this structure by any means, the simpletree can be affected and not appear. Ususally checking the console errors in a browser such as Google Chrome can help find the issue.

Ensure that a JSON is being transferred to JavaScript. Otherwise, there can be serious errors that emerge as a result of such not being implemented.
