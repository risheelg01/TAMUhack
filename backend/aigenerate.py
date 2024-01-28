import openai
import json
json_reponse = {}
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


def gpt_request(question_json):

    question_json = request.get_json()
    # Set your OpenAI GPT-3 API key
    openai.api_key = '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'

    #prompt = "Give me a question about water that elementary school kids should know."
    prompt = "Give me a question and the answer about " + get_question(question_json) + "that elementary school kids should know with multiple choice answers."
    # Make a request to the GPT-3 Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "Give me a question and the answer about water that elementary school kids should know with multiple choice answers."}
        ]
    )

    # Print the generated response
    json_response = response['choices'][0]['message']['content']
    print(json.dumps(json_response, indent=2))

def check_correct():
    correct_answer = json_reponse['choices'][0]['message']['content']['correct_answer']
    answer_json = request.get_json()
    answer = answer_json['answer']
    if correct_answer == answer:
        score += 100

def display_score():
    
    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(score)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


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

    
