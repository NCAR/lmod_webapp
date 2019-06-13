# Author: Thomas Hilton Johnson III
# document.py
# For displaying module data retrieved from module_collect.sh
# requires view_modules.html
#Reference: http://flask.pocoo.org/docs/1.0/api/#flask.Flask
#Reference: http://jinja.pocoo.org/docs/2.10/templates/
#Reference: http://flask.pocoo.org/docs/1.0/quickstart/
#Reference: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#Reference: Manan Yadav, https://www.quora.com/What-is-the-right-way-to-read-a-file-and-display-its-content-on-browser-using-flask
#Reference: https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
#Reference: https://stackoverflow.com/questions/32677167/in-a-flask-app-how-to-print-each-item-of-a-list-in-the-new-paragraphs-inside-my
# export FLASK_APP=document.py
# flask run
from flask import Flask
import flask
import reg_expression
import dict_to_json

app = Flask("document")

#def read_content():
#    module_content = open("result_module_output.txt","r")
#    return module_content.read()

@app.route("/")# Default url route for app
def display(): #For rendering the template and sending the necessary data to said template
    dictionary_content = reg_expression.main() # saves the dictionary content of the compilers and the modules
    html_content = dictionary_content #html_content now stores the value of dictionary_content
    return flask.render_template("view_modules.html", text_html = html_content) #Renders the template and passes the data to the webpage

@app.route("/json/")
def display_json_tree():
    dictionary_content = reg_expression.main()
    javascript_content = dict_to_json.dictionary_to_json(dictionary_content)#javascript_content now stores a JSON object of dictionary_content
    return flask.render_template("json_modules.html", tree_content = javascript_content)

if "update_webpage" == "__main__":
    app.run(debug=True)
