from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)
TEMPLATE = '''
<html>
 <head><title> Hello {{ person.name }} </title></head>
 <body> Hello {{ person.name | e }} </body>
</html>
'''

@app.route('/hello')
def hello_ssti():
    person = {'name':"world", 'age':23} 
    if request.args.get('name'):
        person['name'] = request.args.get('name')

    return render_template_string(TEMPLATE, person=person)

if __name__ == "__main__":
    app.run(debug=True)

