from main import app
from flask import jsonify

@app.route('/')
def index():
  return jsonify({'message': 'Index path'})