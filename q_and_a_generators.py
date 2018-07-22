import typing
import random

Q_AND_A_SIGNATURE: typing.TypeVar = typing.TypeVar(typing.Tuple[str, float])
Q_AND_A_GENERATOR_SIGNATURE: typing.TypeVar = typing.TypeVar(typing.Callable[[None], Q_AND_A_SIGNATURE])

def _ending_in_5_square_2_digit() -> Q_AND_A_SIGNATURE:
	possible_questions: typing.List = [((q * 10) + 5) for q in range(1, 10)] 
	question: str = f"{random.choice(possible_questions)} ** 2"
	answer: float = float(eval(question))
	return (question, answer)

def _addition_2_digit() -> Q_AND_A_SIGNATURE:
	possible_questions: typing.List = range(10, 100)
	question: str = f"{random.choice(possible_questions)} + {random.choice(possible_questions)}"
	answer: float = float(eval(question))
	return (question, answer)

def get_q_type_indexed_generators() -> typing.Dict[str, Q_AND_A_GENERATOR_SIGNATURE]:
	q_type_indexed_q_and_a_generators: typing.Dict[str, Q_AND_A_GENERATOR_SIGNATURE] = {
		"ending in 5 square 2 digit": _ending_in_5_square_2_digit,
		"addition 2 digit": _addition_2_digit,
	}

	return q_type_indexed_q_and_a_generators
