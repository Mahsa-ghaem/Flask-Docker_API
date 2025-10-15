from flask import Flask, jsonify
# flask is a library as a python web framework
# Flask is a class, used to create our web application object.
# jsonify is a function that converts python objects (like dictionaries or list ...) into JSON. 

# calls all internal object in the init function of Flask such as routing system, HTTP request handling, error handlerss,....
app = Flask(__name__)

employees = [
    {"id": 1, "name": "Mahsa", "role": "Data Scientist"},
    {"id": 2, "name": "Rusbeh", "role": "AI Engineer"},
    {"id": 3, "name": "Sara", "role": "Software Developer"}
]

# route as a method in Flask, registers a URL and links it to a function.
@app.route('/')
def home():
    return "Simple Employee Data API is running!"

# jsonify is a Flask function that converts python objects into JSON text.
@app.route('/employees')
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:emp_id>')
def get_employee(emp_id):
    employee = next((e for e in employees if e["id"] == emp_id), None)
    return jsonify(employee) if employee else ("Not Found", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

