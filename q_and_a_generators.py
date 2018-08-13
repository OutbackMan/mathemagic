import typing
import random

Q_AND_A_SIGNATURE: typing.TypeVar = typing.TypeVar(typing.Tuple[str, float])
Q_AND_A_GENERATOR_SIGNATURE: typing.TypeVar = typing.TypeVar(typing.Callable[[None], Q_AND_A_SIGNATURE])

def _ending_in_5_square_2_digit() -> Q_AND_A_SIGNATURE:
	possible_questions: typing.List = [((q * 10) + 5) for q in range(1, 10)] 
	question: str = f"{random.choice(possible_questions)} ** 2"
	answer: float = float(eval(question))
	return (question, answer)

def _multiplication_same_first_add_to_10_2_digit() -> Q_AND_A_SIGNATURE:
    possible_questions: typing.List = range(10, 100)
    first_number: int = random.choice(possible_questions)
    second_number: str = f"{first_number // 10}{10 - (first_number % 10)}"
    question: str = f"{first_number} * {second_number}"
    answer: float = float(eval(question))
    return (question, answer)

def _multiplication_2_digit_with_11() -> Q_AND_A_SIGNATURE:
    possible_questions: typing.List = range(10, 100)
    question: str = f"{random.choice(possible_questions)} * 11"
    answer: float = float(eval(question))
    return (question, answer)

def _addition_2_digit() -> Q_AND_A_SIGNATURE:
    possible_questions: typing.List = range(10, 100)
    question: str = f"{random.choice(possible_questions)} + {random.choice(possible_questions)}"
    answer: float = float(eval(question))
    return (question, answer)

def _addition_3_digit() -> Q_AND_A_SIGNATURE:
    possible_questions: typing.List = range(100, 1000)
    question: str = f"{random.choice(possible_questions)} + {random.choice(possible_questions)}"
    answer: float = float(eval(question))
    return (question, answer)

def _addition_4_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(1000, 10000)
    possible_second: typing.List = range(10, 1000)
    question: str = f"{random.choice(possible_first)} + {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _subtraction_2_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(10, 100)
    first: int = random.choice(possible_first)
    possible_second: typing.List = range(first, 9, -1)
    question: str = f"{first} - {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _subtraction_3_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(100, 1000)
    first: int = random.choice(possible_first)
    possible_second: typing.List = range(first, 99, -1)
    question: str = f"{first} - {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _subtraction_4_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(1000, 10000)
    first: int = random.choice(possible_first)
    possible_second: typing.List = range(100, 1000)
    question: str = f"{first} - {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _multiplication_2_and_1_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(10, 100)
    possible_second: typing.List = range(1, 10)
    question: str = f"{random.choice(possible_first)} * {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _multiplication_3_and_1_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(100, 1000)
    possible_second: typing.List = range(1, 10)
    question: str = f"{random.choice(possible_first)} * {random.choice(possible_second)}"
    answer: float = float(eval(question))
    return (question, answer)

def _square_2_digit() -> Q_AND_A_SIGNATURE:
    possible_first: typing.List = range(10, 100)
    value: int = random.choice(possible_first)
    question: str = f"{value} * {value}"
    answer: float = float(eval(question))
    return (question, answer)

def get_q_type_indexed_generators() -> typing.Dict[str, Q_AND_A_GENERATOR_SIGNATURE]:
	q_type_indexed_generators: typing.Dict[str, Q_AND_A_GENERATOR_SIGNATURE] = {}
	for (identifier, value) in globals().items():
		if callable(value) and value.__module__ == __name__ and identifier != "get_q_type_indexed_generators":
			q_type: str = identifier.split("_", 1)[1].replace("_", " ")
			q_type_indexed_generators[q_type] = value

	return q_type_indexed_generators
