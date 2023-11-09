#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.kodland('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.kodland('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)