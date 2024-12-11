from flask import Blueprint, render_template, request, jsonify
from .nlp.predict import get_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if user_input:
        response = get_response(user_input)
        return jsonify({"response": response})
    return jsonify({"error": "No message provided"}), 400
