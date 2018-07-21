import q_and_a as MM_QAndA

import tkinter
import tkinter.ttk
import random

def mm() -> None:
	mm_window: tkinter.Tk = create_root_window("Mathemagic")
		
	q_and_a_handlers = MM_QAndA.get_q_and_a_handlers()
	home_frame: tkinter.ttk.Frame = create_home_frame(mm_window, q_and_a_handlers)
		
	question_frame: tkinter.ttk.Frame = create_question_frame(mm_window)

	connect_home_and_question_frames(mm_window, home_frame, question_frame, q_and_a_handlers)

	home_frame.tkraise()

	root_window.mainloop()

def create_root_window(title):
	window: tkinter.Tk = tkinter.Tk()
	window.title(title) 
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	
def create_home_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	home_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, name="frame_home", padx=12, pady=12)
	home_frame.grid(row=0, column=0, sticky="nsew")

	current_checkbutton_row: int = None
	current_checkbutton_col: int = None
	for (question_index, question_type) in enumerate(MM_Questions.get_question_handlers()):
		current_checkbutton_row = question_index // 2
		current_checkbutton_col = question_index % 2

		home_frame.grid_rowconfigure(current_checkbutton_row, weight=1)
		home_frame.grid_columnconfigure(current_checkbutton_col, weight=1)
		
		tkinter.ttk.Checkbutton(
						master=home_frame, 
						text=question_type,
						name=f"checkbox_{question_type.replace(" ", "_")}"
						) \ 
					.grid(row=current_checkbutton_row, col=current_checkbutton_col, sticky="nsew")

	tkinter.ttk.Button(master=home_frame, name="btn_start", text="Start") \
				.grid(row=current_checkbutton_row + 1, col=0, colspan=2)
	


def create_q_and_a_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	question_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, name="frame_q_and_a", padx=12, pady=12)
	question_frame.grid(row=0, column=0, sticky="nsew")

	question_frame.grid_rowconfigure(0, weight=1)
	question_frame.grid_rowconfigure(1, weight=1)
	question_frame.grid_columnconfigure(0, weight=1)

	question_text_box: tkinter.ttk.Text = tkinter.ttk.Text(master=question_frame, wrap="word")
	question_text_box.grid(row=0, column=1, sticky="nsew")

	question_text, question_answer = _question_frame_generate_question()
	question_text_box.insert("start", question_text)
	question_text.state(["disabled"])

	answer_text_box: tkinter.ttk.Text = tkinter.ttk.Text(master=question_frame, wrap="word")
	question_text_box.grid(row=1, column=1, sticky="nsew")
	answer_text_box.state(["disabled"])
	
	proceed_event_handler: typing.Callable[[tkinter.Event], None] = lambda event: _question_frame_event_proceed() 
	answer_frame.bind("<Spacebar>", proceed_event_handler)

	return question_frame

def connect_home_and_q_and_a_frames(root_window, home_frame, q_and_a_frame, q_and_a_handlers):
	selected_question_types = []
	
	for question_type in q_and_a_handlers:
		selected_question_types.push(tkinter.StringVar())
		root_window.nametowidget(f".frame_home.checkbox{question_type.replace(" ", "_")}") \
				.config(variable=selected_question_types[-1], onvalue=question_type, offvalue=None)
	
	show_q_or_a = lambda event: _show_q_or_a(q_and_a_frame, selected_q_types, q_and_a_handlers)				 
	question_frame.bind("<Spacebar>", show_q_or_a)
	
	root_window.nametowidget(".frame_home.btn_start").configure(command=lambda: question_frame.tkraise())

	question_frame.bind("<Esc>", lambda event: home_frame.tkraise())


def _show_q_or_a()
		if not _question_frame_proceed.current_question:
			(_question_frame_proceed.current_question, _question_frame_proceed.current_answer) = _question_frame_generate_question()
			_question_frame_proceed.answer_shown = False	
		else:	
			if not _question_frame_proceed.answer_shown:
				# show answer
				_question_frame_proceed.answer_shown = True
			else:
				# delete question and answer
				(_question_frame_proceed.current_question, _question_frame_proceed.current_answer) = _question_frame_generate_question()
				_question_frame_proceed.answer_shown = False

def _generate_q_and_a(selected_question_types, q_and_a_handlers):
	question_type = random.choice(selected_question_types)
	while not question_type:
		question_type = random.choice(selected_question_types)

	return q_and_a_handlers[question_type]()
	

if __name__ == "__main__":
	mm()
