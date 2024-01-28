#from flask import Flask, render_template, request
import pandas as pd
import requests as rq
import openai

from flask import Flask, abort, current_app, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



response = {}
score = 0
round_number = 1


def get_question(question_json):
    box_number = question_json['box_number']
    round_number = question_json['round_number']

    if round_number == 1:
        if box_number == 1:
            return "sun"
        elif box_number == 2:
            return "animals"
        elif box_number == 3:
            return "phone"
        else:
            return "puzzle"
    elif round_number == 2:
        if box_number == 1:
            return "mountain"
        elif box_number == 2:
            return "clouds"
        elif box_number == 3:
            return "lightbulb"
        else:
            return "notebook"
    elif round_number == 3:
        if box_number == 1:
            return "moon"
        elif box_number == 2:
            return "robot"
        elif box_number == 3:
            return "astronaut"
        else:
            return "magnet"
    elif round_number == 4:
        if box_number == 1:
            return "scientist"
        elif box_number == 2:
            return "legos"
        elif box_number == 3:
            return "blueprint"
        else:
            return "equation"
    else:
        if box_number == 1:
            return "plant"
        elif box_number == 2:
            return "water"
        elif box_number == 3:
            return "computer"
        else:
            return "calculator"

@app.route('/gpt', methods=['POST'])
def gpt_request():

    question_json = request.get_json()
    # Set your OpenAI GPT-3 API key
    openai.api_key = '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'

    #prompt = "Give me a question about water that elementary school kids should know."
    prompt = "Give me a question about " + get_question(question_json) + "that elementary school kids should know with 4 multiple choice answers (a,b,c,d format) and provide the correct answer at the end."
    # Make a request to the GPT-3 Chat API
    new_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    # Print the generated response
    json_data = new_response['choices'][0]['message']['content']
    #print(json.dumps(json_data, indent=2))

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response
    

@app.route('/correct', methods=['POST'])
def check_correct():
    correct_answer = response.split("Correct Answer:")[1]
    answer_json = request.get_json()
    answer = answer_json['answer']
    if answer in correct_answer:
        score += 100
    display_score()


def display_score():
    
    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(score)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/', methods=['POST'])
def iterate_round():
    get_next_json = request.get_json()
    get_next = get_next_json['next']
    if get_next == "true":
        round += 1
    
    # Create a dictionary with the integer value
    my_dict = {"round": round}

    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(round)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/', methods=['POST'])
def stock_tracker():

    json_data = json.dumps(0)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001, debug = True)

