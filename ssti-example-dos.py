from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)
TEMPLATE = '''<html><head><title> Hello {{ person.name }} </title></head><body> Hello FOO </body></html>'''

@app.route('/hello-ssti')
def hello_ssti():
    person = {'name':"world", 'secret':'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='} 
    if request.args.get('name'):
        person['name'] = request.args.get('name')

    template = TEMPLATE.replace("FOO", person['name'])
    return render_template_string(template, person=person)

if __name__ == "__main__":
    app.run(debug=True)
