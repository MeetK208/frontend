from flask import Flask, render_template, request, redirect
from google.cloud import datastore
import os

project_id = "bigquery-demo-340008" 

credentil_json="Python_BigQuery copy.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Python_BigQuery copy.json"

app = Flask(__name__)
datastore_client = datastore.Client()

# The kind for the new entity

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        kind = "Task1" 
        userDetails = request.form
        name = userDetails['name']
        coins = userDetails['coins']
        task_key = datastore_client.key(kind, name)
        task = datastore.Entity(key=task_key)
        task['coins'] = coins
        datastore_client.put(task) 
    return redirect('http://35.184.3.111:80/') 

@app.route('/users')
def users():
    return "Html"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000)
