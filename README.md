# lmod_webapp
A web application to interactively display Lmod trees

Web application built primarily using Python Flask. This web application also makes use of Python's regular expression, json, and copy modules.

Currently there are multiple txt files in the repository main directory:

References.txt (For any useful or necessary references that have not been inserted in comments in the available code. Will likely contain all necessary references throughout the code as a central file to store such information. Update to keep track use of useful or necessary references.)
-> References.txt should be updated to maintain record of any resources or citations that can be used to continue sustain the longevity of the application or allow future users to have access to resources to understand how the application works. While there are references in the comments of the code, allowing the existence of a file that can serve as a central reference point is also helpful.

result_module_output.txt (Currently where the modules are stored after being extracted from the bash terminal. This file is read by the reg_expression.py file to gain the data necessary for the rest of the application.)
-> result_module_output.txt is a text file that was essential for the first and second implementations. Now it can be used to test the code with some modifications to the source code in the regular expression to be able to capture the correct directories/headings. Currently list.out and listcasper.out utilize colons (:) to denote the headings/directories instead of the full glade path.

result_module_output_backup.txt (The text file is a backup of result_module_output.txt in the case of unintended deletion the original file.)

Currently there is one bash script in the repository as well:

module_collect.sh (Collects the relevant compiler and module information)
->module_collect.sh will output a file with the relevant module information. The most recent version was developed using regular expressions provided by Brian Vanderwende. Subject to further modification.

genlist.sh (collects all directory and software components. Provided by Brian Vanderwende. Generates the file list.out. Do not change .out extension to .txt or else it will miss some of the information that is gathered.)

This Flask Application has six different python files:

dict_to_array_dict.py (The Python file is used to generate hierarchical list-dict construct using a pre-made dictionary containing headings/directories as keys and lists of associated content as values. Necessary for the current version of the code to be executed.)

dict_to_json.py (Manages converting the final output of reg_expression.py to a json to send to the Javascript of the webpage.)

document.py (Holds the configuration and url patterns for the FLASK application. Currently, only two url patterns of note are stored in document.py. The first is "/" and the second is "/json/". The Flask app is ran using commands specified in comments of document.py. Running this python file with the proper commands will run the other necessary files that are imported.)

help_additions.py (This code is called in the dict_to_array.py Python file to handle module help information. The module help information is parsed, filtered, manipulated and then inserted into the container of the simpletree to be displayed in a modal. The functions are heavily depndent on one another within this file.)

lists_to_dict_construct.py (Contains the functions necessary to convert the lists containing the content from the target file a hierarchical dictionary that stores sub dictionaries or respective children. Note: Utilizes recursive functions for this process. If altered, please verify the functions are not recursively storing the same dictionary entries over and over.)

reg_expression.py (Where the bulk of text processing and organization of content is handled. Handles a bulk of the initial processing.)

test_js_dict.py (Test code to see what structure could be implemented and accepted as json for the simpletree on the frontend. Can be used for practice runs.)

text_cleaner.py (Used at one point to parse the text. Currently unneeded.)

There are currently three html files present:

view_modules.html (The original HTML file utilized for testing purposes. view_modules.html is the default route for the Flask application.)

json_modules.html (The second HTML file developed. To get to this page json/ must be added to the base URL. Cheyenne is embedded in HTML. The webpage utilizes JavaScript.)

json_casper_modules.html (Third HTML file that is reserved primarily for displaying the Casper software information. Casper is embedded in the HTML tags. The webpage utilizes JavaScript.)

test.html (Unneeded, used for initial experimentation with JavaScript)

There can be multiple JSON files present: (currently deleted)

array_dict.json (Example of the format that the jQuery simpletree will accept. Short summary: the data must be contained in lists that contain dictionaries so that the JavaScript can interpret the JSON as the correct JavaScript object.)

array_dict_list.json (The JSON generated from the lmod_webapp. You can use this file to verify whether the contents are in a proper JSON format. Also allows for checking to see if there are any unnecessary processing details in the code itself.)

There are also two .out files present in the repository.

listcheyenne.out (The software headings/directories and their respective contents that are available on Cheyenne HPC system. This file, and listcasper.out, are the files currently being processed for the web application. To switch the files being processed, simply reload the tab that displays the webpage and specify the alternate file within the terminal. The default route for this file is localhost/json/ using the template json_modules.html.)

listcasper.out (The software headings/directories and their respective contents that are available on the Casper HPC system. This file, along with list.out, are the files currently being processed for the web application. To switch the files being processed, simply reload the tab that displays the webpage and specify the alternate file within the terminal. The default route for this file is localhost/ using the template json_casper_modules.html.)

cheyennehelp.out (The paths for and relevant information regarding the software that is available for Cheyenne. Supplies the content for the modals that appear when clicking on specific software components in the simpleTree.)

casperhelp.out (The paths for and relevant information regarding the software that is available for Casper. Supplies the content for the modals that appear when clicking on specific software components in the simpleTree.)

## Directions
To run this application:
1. export FLASK_APP=document.py
2. flask run
3.

then navigate to the specified url in a web browser to see the webpage to get to the default opage with HTML and CSS. To get the Javascript and Jquery simpletree implementation, add /json/ after the default url.

Ex: DEFAULT_URL/json/

To input the file name, input the base URL and add /json/ after the base URL. Then, when the printed prompt is displayed, enter the name of the file you wish to use. After that, the webpage should fully load. Note: loading will remain indefinite while there is no given input.

The path /casperjson/ works in a similar process to the path /json/, the difference being that /casperjson/ is added to the end of the default url.

Limitations:
1. The data must be loaded when the page initializes for the simpletree. Data cannot be added after the page has loaded.

2. The data must be loaded within a nested list to dictionary structure. The data will not be displayed otherwise as the simpletree will not be able to traverse said data.

3. If the nesting of the dictionaries require extreme depth, the recursive functions can become overwhelmed if there is an extreme quantity of recursive calls.

4. Currently requires a file to already exist with the required information for building the module tree.
Said file can be inputted manually, but if the incorrect file is given, the program will run the specified default file.

5. The file specified must have headings/directories denoted by colons (:) at the end. For examples of such, look into the list.out and the listcasper.out files.

## Debugging:

To see a relatively organized print out of the list-dict construct call the recursive_dict_print_dict() function from lists_to_dict.py at end of the construction of the full list-dict construct or while building it (note there can be a lot of content that will be printed out.) It will print out all the dictionaries in the list-dict construct. Use the printed results to try and find any bugs that may be occurring the code.

If the simpletree is not properly displaying, be sure to check that the correctly formatted JSON object is being transferred to the JavaScript via Flask and Jinja2. The structure be alternating lists to dictionaries, to more lists to dictionaries. Also, the keys should be label, value and children. If the JSON removed from this structure by any means, the simpletree can be affected and not appear. Ususally checking the console errors in a browser such as Google Chrome can help find the issue.

Ensure that a JSON is being transferred to JavaScript. Otherwise, there can be serious errors that emerge as a result of such not being implemented. JavaScript is implemented heavily an required for this web application.

Ensure that the file that is being read has no extra punctuation such as colons, otherwise such punctuation will have to be removed edited out before the Python scripts can successfully run.

The current implementation runs based on an assumption that there are no duplicate directories in the submitted file. If there are, it will cause bugs in the program. Please ensure that in the file given that the directories are not duplicated.

An edit has been made to make the code more robust by distinguishing what will make up the second level of the list-dict structure versus the remaining sub-levels.

Note: simpleTree jQuery was developed by Michael Derntl. It can be used under the permissions of the MIT License.
