# lmod_webapp
A web application to interactively display Lmod trees

Web application built primarily using Python Flask.

This Flask Application depends on five different python files:

dict_to_json.py (Manages converting the final output of reg_expression.py to a json to send to the Javascript of the webpage.)

document.py (Holds the configuration and url patterns for the FLASK application. Currently, only two url patterns of note are stored in document.py. The first is "/" and the second is "/json/". The Flask app is ran using commands specified in comments of document.py.)

reg_expression.py (Where the bulk of text processing and organization of content is handled.)

test_js_dict.py (Test code to see what structure could be implemented and accepted as json for the simpletree on the frontend.)

text_cleaner.py (Used at one point to parse the text. Currently unneeded.)
