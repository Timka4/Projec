#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form_python():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/', methods=['POST'])
def process_form_discord():
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_discord=button_discord)


if __name__ == "__main__":
    app.run(debug=True)