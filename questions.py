import typing
import random

# create a TypeVar()
question_handlers: typing.Dict[str, typing.Callable[]] = {}

def question_ending_in_5_square_2_digit() -> typing.Tuple(str, int):
	possible_questions: typing.List = [((q * 10) + 5)) for q in range(1, 10)] 
	question: str = f"{random.choice(possible_questions)} ** 2"
	answer: int = eval(question)
	return (question, answer)

def question_addition_2_digit() -> typing.Tuple(str, int):
	possible_questions: typing.List = range(10, 100)
	question: str = f"{random.choice(possible_questions)} + {random.choice(possible_questions)}"
	answer: int = eval(question)
	return (question, answer)

def _get_question_type(question_handler):
	return question_handler.__name__.split("_", 1)[1].replace("_", " ")

for name in locals():
	if callable(name) and name.__module__ == __name__:
		question_handlers[get_question_type(name)] = name		
