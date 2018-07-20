import questions as MM_Questions 

import tkinter
import tkinter.ttk
import random

selected_question_types = []

def mm() -> None:
	root_window: tkinter.Tk = create_root_window("Mathemagic")
	home_frame: tkinter.ttk.Frame = create_home_frame(root_window)
	question_frame: tkinter.ttk.Frame = create_question_frame(root_window)

	connect_home_and_question_frames(home_frame, question_frame)

	home_frame.tkraise()

	root_window.mainloop()

def create_root_window(title):
	window: tkinter.Tk = tkinter.Tk()
	window.title(title) 
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	
def create_home_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	home_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, name="home", padx=12, pady=12)
	home_frame.grid(row=0, column=0, sticky="nsew")

	current_checkbutton_row: int = None
	current_checkbutton_col: int = None
	global selected_question_types
	for (question_index, question_type) in enumerate(MM_Questions.get_question_handlers()):
		current_checkbutton_row = question_index // 2
		current_checkbutton_col = question_index % 2

		home_frame.grid_rowconfigure(current_checkbutton_row, weight=1)
		home_frame.grid_columnconfigure(current_checkbutton_col, weight=1)
		
		selected_question_types.push(tkinter.StringVar())
		tkinter.ttk.Checkbutton(
						master=home_frame, 
						text=question_type, 
						variable=selected_question_types[-1],
						onvalue=question_type,
						offvalue=None
						) \ 
					.grid(row=current_checkbutton_row, col=current_checkbutton_col, sticky="nsew")

	tkinter.ttk.Button(master=home_frame, name="start", text="Start") \
				.grid(row=current_checkbutton_row + 1, col=0, colspan=2)
	


def create_question_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	question_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, name="question", padx=12, pady=12)
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

def connect_home_and_question_frames(root_window, home_frame, question_frame):
	root_window.nametowidget(".home.start").configure(command=lambda: question_frame.tkraise())

	question_frame.bind("<Esc>", lambda event: home_frame.tkraise())


def _question_frame_proceed()
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

def _question_frame_generate_question():
	question_type = random.choice(selected_question_types)
	while not question_type:
		question_type = random.choice(selected_question_types)

	return MM_Questions.question_handlers[question_type]()
	

if __name__ == "__main__":
	mm()
