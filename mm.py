# import questions as MM_Questions 

import tkinter
import tkinter.ttk

def mm() -> None:
	mm_window: tkinter.Tk = tkinter.Tk()
	mm_window.title("Mathemagic") 
		
	mm_window.grid_rowconfigure(0, weight=1)
	mm_window.grid_columnconfigure(0, weight=1)

	mm_home_frame: tkinter.ttk.Frame = create_home_frame(mm_window)
	mm_question_frame: tkinter.ttk.Frame = create_question_frame(mm_window)
	
	active_frame: tkinter.ttk.Frame = mm_home_frame
	active_frame.tkraise()

	tkinter.mainloop()

def create_home_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	home_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, padx=12, pady=12)
	home_frame.grid(row=0, column=0, sticky="nsew")

	home_frame.grid_rowconfigure(0, weight=1)
	home_frame.grid_rowconfigure(1, weight=1)
	home_frame.grid_rowconfigure(2, weight=1)
	home_frame.grid_rowconfigure(3, weight=1)
	home_frame.grid_columnconfigure(0, weight=1)
	home_frame.grid_columnconfigure(1, weight=1)

	'''
	for question_type in MM_Questions.questions:
		checkbox: tkinter.ttk.Checkbox(master=home_frame, text=question_type)
		checkbox.state(["!selected"])

	start_btn: tkinter.ttk.Button = tkinter.ttk.Button(master=home_frame, text="Start", command=when_start_btn)

	def when_start_btn_clicked(event: tkinter.Event) -> None:
		if checkbox.instate(["selected"]):
			question_source.add()	

		mm_question_frame.tkraise()

	'''


	return home_frame

def create_question_frame(mm_window: tkinter.Tk) -> tkinter.ttk.Frame:
	question_frame: tkinter.ttk.Frame = tkinter.ttk.Frame(master=mm_window, padx=12, pady=12)
	question_frame.grid(row=0, column=0, sticky="nsew")

	question_frame.grid_rowconfigure(0, weight=1)
	question_frame.grid_rowconfigure(1, weight=1)
	question_frame.grid_columnconfigure(0, weight=1)

	question_text, question_answer = random.choice(list(available_questions.items()))

	question_text: tkinter.ttk.Text = tkinter.ttk.Text(master=question_frame, wrap="word")
	question_text.insert("start", question.question)
	question_text.state(["disabled"])

	answer_text: tkinter.ttk.Text = tkinter.ttk.Text(master=question_frame, wrap="word")
	answer_text.state(["disabled"])

	answer_frame.bind("<Spacebar>", proceed)
	answer_frame.bind("<Esc>", go_to_home)
	
	'''
	def proceed():
		if not proceed.answer_shown:
			proceed.answer_shown = False		
		else:
			if proceed.answer_shown:
				show_next_question()
				proceed.answer_shown = False
			else:
				show_answer()
				proceed.answer_shown = True
				




	'''


	return question_frame


	

if __name__ == "__main__":
	mm()
