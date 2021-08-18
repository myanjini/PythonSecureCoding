from flask import Flask
from flask import request, send_file, send_from_directory, render_template_string


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        help = request.form['help'] 
        path = '/home/nanjini/PythonSecureCoding/helps/'
        return send_from_directory(path, help, as_attachment=True)

    helps = ['Help-A', 'Help-B', 'Help-C', 'Help-D']
    template = '''
        <form action="/" method="post">
          <select name="help">
          {% for h in helps %}
            <option value="{{h}}" selected>{{h}}</option>"
          {% endfor %}
          </select>
          <input type="submit" value="Help"/>
        </form>
    '''
    return render_template_string(template, helps=helps)

if __name__ == "__main__":
    app.run(debug=True)
