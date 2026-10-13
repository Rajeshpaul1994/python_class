from flask import Flask, render_template, request
from file_handler import file_writer

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')
    
@app.route("/student-name-entry", methods=['POST'])
def student_name_entry():
    data = request.form
    name = data['name']
    title = data['title']
    res = file_writer([name,' ',title])
    return res
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    

