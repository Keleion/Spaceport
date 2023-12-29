from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'id': 1,
    'title': 'New Helpdesk',
    'priority': 'Medium',
    'status': 'Unapproved',
    'start_date': '2023-01-01',
    'due_date': '2023-01-15',
    'description': 'New helpdesk for CBG',
    'progress': '0%',
  },
  {
    'id': 2,
    'title': 'Task Manager App',
    'priority': 'High',
    'status': 'In Progress',
    'start_date': '2023-01-01',
    'due_date': '2023-01-15',
    'description': 'Create app for managing tasks related to chores and projects',
    'progress': '0.5%',
  },
  {
    'id': 3,
    'title': 'Go Study App',
    'priority': 'Low',
    'status': 'Concept',
    'start_date': '2023-01-01',
    'due_date': '2023-01-15',
    'description': 'Create app for logging Go info like problems. Create problems on the fly, or copy the ones you see and save them for later.',
    'progress': '0%',
  }
]

@app.route("/")
def welcome():
  return render_template('home.html',
                        projects=PROJECTS,)

@app.route("/spaceport")
def spaceport():  
  return render_template('spaceport.html',
                        projects=PROJECTS,)

@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)