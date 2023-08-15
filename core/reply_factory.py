
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)
    if current_question_id is not None:
        session[f"answer_{current_question_id}"] = answer
        return True, ""
    else:
        return False, "No current question ID."

    next_question, next_question_id = get_next_question(current_question_id)

     '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    question_index = current_question_id + 1
    if question_index < len(PYTHON_QUESTION_LIST):
        return PYTHON_QUESTION_LIST[question_index], question_index
    else:
        return None, -1
        final_response = generate_final_response(session)
        bot_responses.append(final_response)
        
total_score = 0
    for question_id, question in enumerate(PYTHON_QUESTION_LIST):
        user_answer = session.get(f"answer_{question_id}")
        if user_answer is not None:
            # Assuming you have a function to evaluate the correctness of the answer
            # and assign a score
            question_score = evaluate_answer(user_answer, question)
            total_score += question_score
    
    final_result = f"Your total score is: {total_score}"
    return final_result



def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    return True, ""


def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    return "dummy question", -1


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''

    return "dummy result"
