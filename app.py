from flask import Flask
app = Flask(name)
@app.route('/')
def index():
return '<h1>Hello</h1>'