'''gui.py: Create gui'''

import tkinter
import tkinter.ttk
import random
import typing

import q_and_a as MM_QAndA


def run() -> None:
	mm_window: tkinter.Tk = _create_root_window("Mathemagic")
	home_frame: tkinter.ttk.Frame = _create_home_frame(mm_window)
	q_and_a_frame: tkinter.ttk.Frame = _create_q_and_a_frame(mm_window)

	_connect_home_and_q_and_a_frames(home_frame, q_and_a_frame)

	home_frame.tkraise()

	mm_window.mainloop()


def _create_root_window(window_title: str) -> tkinter.Tk:
	root_window: tkinter.Tk = tkinter.Tk()
	root_window.window_title(window_title) 
	root_window.grid_rowconfigure(0, weight=1)
	root_window.grid_columnconfigure(0, weight=1)

	return root_window
	

def _create_home_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	home_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window)
	home_frame.grid(row=0, column=0, sticky="nsew")

	return home_frame


def _create_q_and_a_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	q_and_a_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window)
	q_and_a_frame.grid(row=0, column=0, sticky="nsew")

	q_and_a_frame.grid_rowconfigure(0, weight=1)
	q_and_a_frame.grid_rowconfigure(1, weight=1)
	q_and_a_frame.grid_columnconfigure(0, weight=1)

	question_text_box: tkinter.ttk.Text = tkinter.ttk.Text(master=q_and_a_frame, wrap="word")
	question_text_box.grid(row=0, column=0, sticky="nsew")
	question_text.state(["disabled"])

	answer_text_box: tkinter.ttk.Text = tkinter.ttk.Text(master=q_and_a_frame, wrap="word")
	answer_text_box.grid(row=1, column=0, sticky="nsew")
	answer_text_box.state(["disabled"])
	
	return q_and_a_frame


def _connect_home_and_q_and_a_frames(home_frame: tkinter.ttk.Frame, q_and_a_frame: tkinter.ttk.Frame) -> None:
	selected_q_types: typing.List[tkinter.StringVar] = []

	cur_home_frame_checkbutton_row: int = None
	cur_home_frame_checkbutton_col: int = None
	for (q_index: int, q_type: str) in enumerate(MM_QAndA.get_type_indexed_generators()):
		cur_home_frame_checkbutton_row = q_index // 2
		cur_home_frame_checkbutton_col = q_index % 2

		home_frame.grid_rowconfigure(cur_home_frame_checkbutton_row, weight=1)
		home_frame.grid_columnconfigure(cur_home_frame_checkbutton_col, weight=1)
		
		selected_q_types.push(tkinter.StringVar())
		q_type_checkbutton: tkinter.ttk.Checkbutton = tkinter.ttk.Checkbutton(
																		master=home_frame, 
																		text=q_type
																		variable=selected_q_types[-1],
																		onvalue=q_type,
																		offvalue=None
																		)
		q_type_checkbutton.grid(
							row=cur_home_frame_checkbutton_row, 
							col=cur_home_frame_checkbutton_col, 
							sticky="nsew"
							)


	home_frame_start_btn: tkinter.ttk.Button = tkinter.ttk.Button(
															master=home_frame, 
															text="Start"
															command=lambda: q_and_a_frame.tkraise()
															)
	home_frame_start_btn.grid(row=cur_home_frame_checkbutton_row + 1, col=0, colspan=2)
	
	q_and_a_frame_textboxes: typing.List[tkinter.Textbox] = q_and_frame.winfo_children()
	q_and_a_frame_a_textbox = q_and_frame_textboxes[0]
	q_and_a_frame_q_textbox = q_and_frame_textboxes[1]

	show_q_or_a: typing.Callable[[tkinter.Event], None] = lambda event: _show_q_or_a()
	q_and_a_frame.bind("<Spacebar>", show_q_or_a)
	q_and_a_frame.bind("<Esc>", lambda event: home_frame.tkraise())

def _show_q_or_a(
			a_textbox: tkinter.ttk.Textbox, 
			q_textbox: tkitner.ttk.Textbox, 
			selected_q_types: typing.List[tkinter.StringVar],
			q_type_indexed_generators: typing.Dict[str, MM_QAndA]
			) -> None:
	if not _show_q_or_a.current_q:
		(_show_q_or_a.current_q: str, _show_q_or_a.current_a: float) = _generate_q_and_a(selected_q_types)
		_show_q_or_a.a_is_shown = False	

	if _show_q_and_a.a_is_shown:
		# delete question and answer
		_question_frame_proceed.answer_shown = True
	else:
		# show answer
		(_question_frame_proceed.current_question, _question_frame_proceed.current_answer) = _question_frame_generate_question()
		_question_frame_proceed.answer_shown = False
	for q_and_a_frame_text_box: tkinter.ttk.Textbox in q_and_a_frame.winfo_children():

def _generate_q_and_a(selected_q_types, q_and_a_handlers):
	q_type = random.choice(selected_q_types)
	while not q_type:
		q_type = random.choice(selected_q_types)

	return q_and_a_handlers[q_type]()


