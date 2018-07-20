import typing

# create a TypeVar()
questions: typing.Dict[str, typing.Callable[]] = {}

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

for name in locals():
	if callable(name) and name.__module__ == __name__:
		questions[get_question_type(name)] = name		
