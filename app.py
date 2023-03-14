from mysql_controller import db_maker
from flask import Flask, send_from_directory
from services import add_task_service, add_todo_service, remove_task_service, remove_todo_service
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ToDoList"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/add_todo/<value>')
def add_todo(value):
    print("calling add_todo")
    try:
        add_todo_service.add_todo(value)
        return "success"
    except:
        return "fail"


@app.route('/delete_todo/<_id>')
def delete_todo(_id):
    print("calling remove_todo")
    try:
        remove_todo_service.remove_todo(_id)
        return "success"
    except:
        return "fail"


@app.route('/add_task/<value>')
def add_task(value):
    print("calling add_task")
    try:
        add_task_service.add_task(value)
        return "success"
    except:
        return "fail"


@app.route('/delete_task/<_id>')
def delete_task(_id):
    print("calling remove_task")
    try:
        remove_task_service.remove_task(_id)
        return "success"
    except:
        return "fail"


if __name__ == "__main__":
    db = db_maker.Create()
    app.run()
