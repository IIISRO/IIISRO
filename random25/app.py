from flask import Flask,render_template
import requests
app = Flask(__name__)
app = Flask(__name__, static_folder='static')

@app.route("/students/")
def students():
    data=requests.get('https://5ffcb43ea77c50001706cab8.mockapi.io/api/v1/students/')
    data_list=data.json()
    return render_template('students.html',students=data_list,bio="I am student at Tech Academy")
@app.route("/students/<int:id>")
def student(id):
    url=f'https://5ffcb43ea77c50001706cab8.mockapi.io/api/v1/students/{id}'
    data=requests.get(url)
    data_list=data.json()
    return render_template('student.html',student=data_list)