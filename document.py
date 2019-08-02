# Author: Thomas Hilton Johnson III
# document.py
# For displaying module data retrieved from module_collect.sh
# requires view_modules.html and json_modules.html
#Reference: http://flask.pocoo.org/docs/1.0/api/#flask.Flask
#Reference: http://jinja.pocoo.org/docs/2.10/templates/
#Reference: http://flask.pocoo.org/docs/1.0/quickstart/
#Reference: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#Reference: Manan Yadav, https://www.quora.com/What-is-the-right-way-to-read-a-file-and-display-its-content-on-browser-using-flask
#Reference: https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
#Reference: https://stackoverflow.com/questions/32677167/in-a-flask-app-how-to-print-each-item-of-a-list-in-the-new-paragraphs-inside-my
# Reference: https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app
# export FLASK_APP=document.py
# flask run
from flask import Flask #Importing the flask module, which is necessary for a Flask app
import flask
import reg_expression # Imports reg_expression.py to allow reg_expression.py's functions to be utilized. Necessary for the app.
import dict_to_json # Imports dict_to_json.py to allow dict_to_json.py's functions to be utilized.
app = Flask("document") #Name of the Flask app

# Code will be ran when the page is loading. If there is any printed information in the Terminal,
# feel free to read said information for the purpose of ensuring that the code is running correctly.

#@app.route("/")# Default url route for app
#def display(): #For rendering the template and sending the necessary data to said template
#    dictionary_content = reg_expression.main_dict() # saves the dictionary content of the compilers and the modules
#    html_content = dictionary_content #html_content now stores the value of dictionary_content
#    return flask.render_template("view_modules.html", text_html = html_content) #Renders the template and passes the data to the webpage

@app.route("/cheyennejson/")# Add json/ to default  URL route to go to json_modules.html
def display_json_tree():#Function initialized to display the webpage that will in turn render the jQuery simpletree
    #dictionary_content = reg_expression.main()
    javascript_content = dict_to_json.array_dict_to_json(reg_expression.cheyenne_array_dict())# converts the list-dictionary construct returned by main_array_dict() from the file reg_expression to be converted to JSON by the array_dict_to_json function from the dict_to_json Python file
    #javascript_content = test_js_dict.commence_test()#dict_to_json.dictionary_to_json(dictionary_content)#javascript_content now stores a JSON object of dictionary_content
    return flask.render_template("json_modules.html", tree_content = javascript_content)#Renders the HTML file and passes the javascript_content variable to be utilized by Jinja2 or JavaScript

@app.route("/casperjson/")# Add casperjson/ to default  URL route to go to json_modules.html
def display_json_casper_tree():#Function initialized to display the webpage that will in turn render the jQuery simpletree
    #dictionary_content = reg_expression.main()
    javascript_content = dict_to_json.array_dict_to_json(reg_expression.casper_array_dict())# converts the list-dictionary construct returned by main_array_dict() from the file reg_expression to be converted to JSON by the array_dict_to_json function from the dict_to_json Python file
    #javascript_content = test_js_dict.commence_test()#dict_to_json.dictionary_to_json(dictionary_content)#javascript_content now stores a JSON object of dictionary_content
    return flask.render_template("json_casper_modules.html", tree_content = javascript_content)#Renders the HTML file and passes the javascript_content variable to be utilized by Jinja2 or JavaScript

if "update_webpage" == "__main__":
    app.run(debug=True) #For opening debugging options
