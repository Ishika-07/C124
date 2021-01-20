from flask import Flask, jsonify, request

app = Flask(__name__)

task = [
    {
        'id': 1,
        'name':'Raju',
        'contact':"9987644456",
        'done': False
    },
    {
        'id': 2,
        'name':'Rahul',
        'contact':"9876543222",
        'done': False
    }
]

@app.route("/add_task", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({"status":"error", "message":"Please provide the data"}, 400)
    t={
        'id': task[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json['contact'],
        'done': False
     }
    task.append(t)
    return  jsonify({"status":"Success", "message":"Task added successfully"})

if(__name__ == "__main__"):
    app.run(debug = True)
