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



def check_correct(answer_json):
    #get json answer

def score(answer_json):
    if