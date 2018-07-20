import questions as MM_Questions 

import tkinter
import tkinter.ttk
import random

available_question_handlers = {}
active_question_text = None
active_question_answer = None

def mm() -> None:
	root_window: tkinter.Tk = create_root_window("Mathemagic")
	home_frame: tkinter.ttk.Frame = create_home_frame(root_window)
	question_frame: tkinter.ttk.Frame = create_question_frame(root_window)

	run_mm(window, home_frame, question_frame)

def run_mm():
	attach_home_frame_event_listeners(home_frame)
	home_frame.tkraise()
	root_window.mainloop()

def create_root_window(title):
	window: tkinter.Tk = tkinter.Tk()
	window.title(title) 
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

def create_home_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	home_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, padx=12, pady=12)
	home_frame.grid(row=0, column=0, sticky="nsew")

	home_frame.grid_rowconfigure(0, weight=1)
	home_frame.grid_rowconfigure(1, weight=1)
	home_frame.grid_rowconfigure(2, weight=1)
	home_frame.grid_rowconfigure(3, weight=1)
	home_frame.grid_columnconfigure(0, weight=1)
	home_frame.grid_columnconfigure(1, weight=1)

	available_question_types = []
	for question_type in MM_Questions.questions_handlers:
		available_question_types.push(tkinter.StringVar())
		checkbox = tkinter.ttk.Checkbox(
								master=home_frame, 
								text=question_type, 
								variable=available_question_types[-1],
								onvalue=question_type,
								offvalue=None
								)
		checkbox.state(["!selected"])
		checkbox.grid

def attach_home_frame_event_listeners():
	start_btn_event_handler = lambda event: _home_frame_start_questions(available_question_handlers)
	start_btn: tkinter.ttk.Button = tkinter.ttk.Button(master=home_frame, text="Start", command=when_start_btn)

def home_frame_start_event_listener(avaiable_question_handlers) -> None:
	attach_question_frame_event_listeners(available_question_handlers)
	question_frame.tkraise()

def create_question_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	question_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, padx=12, pady=12)
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

	go_to_home_event_handler: typing.Callable[[tkinter.Event], None] = lambda event: home_frame.tkraise()
	answer_frame.bind("<Esc>", go_to_home_event_handler)
	
	return question_frame

def _question_frame_event_proceed()
		if not _question_frame_event_proceed.answer_shown:
			_question_frame_event_proceed.answer_shown = False		
		else:
			if _question_frame_event_proceed.answer_shown:
				question_text_box.state(["!disabled"])
				question_text_box.delete("start", "end")	
				answer_text_box.state(["!disabled"])
				answer_text_box.delete("start", "end")	
				answer_text_box.state(["disabled"])
				# show_next_question()
				question_text_box
				_question_frame_event_proceed.answer_shown = False
			else:
				# show_answer()
				_question_frame_event_proceed.answer_shown = True

def _question_frame_generate_question():
	question_type = random.choice(available_question_handlers.keys())
	return available_question_handlers[question_type]()
	
	

if __name__ == "__main__":
	mm()
