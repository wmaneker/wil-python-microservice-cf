
from flask import jsonify
from server import app

@app.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)

@app.route('/answer')
def answer():
    answer = {'The Answer to Life the Universe and Everything': 42}
    return jsonify(answer)