'''gui.py: Create gui'''

import tkinter
import random
import typing

import q_and_a_generators as MM_QAndAGenerators


def run() -> None:
	mm_window: tkinter.Tk = _create_root_window("Mathemagic")
	home_frame: tkinter.Frame = _create_home_frame(mm_window)
	q_and_a_frame: tkinter.Frame = _create_q_and_a_frame(mm_window)

	_connect_home_and_q_and_a_frames(home_frame, q_and_a_frame)

	home_frame.tkraise()

	mm_window.mainloop()


def _create_root_window(window_title: str) -> tkinter.Tk:
	root_window: tkinter.Tk = tkinter.Tk()
	root_window.title(window_title) 
	root_window.grid_rowconfigure(0, weight=1)
	root_window.grid_columnconfigure(0, weight=1)

	return root_window
	

def _create_home_frame(mm_window: tkinter.Tk) -> tkinter.Frame:
	home_frame: tkinter.Frame = tkinter.Frame(master=mm_window)
	home_frame.grid(row=0, column=0, sticky="nsew")

	return home_frame


def _create_q_and_a_frame(mm_window: tkinter.Tk) -> tkinter.Frame:
	q_and_a_frame: tkinter.Frame = tkinter.Frame(master=mm_window)
	q_and_a_frame.grid(row=0, column=0, sticky="nsew")

	q_and_a_frame.grid_rowconfigure(0, weight=1)
	q_and_a_frame.grid_rowconfigure(1, weight=1)
	q_and_a_frame.grid_columnconfigure(0, weight=1)

	q_text_box: tkinter.Text = tkinter.Text(master=q_and_a_frame, wrap="word", state="disabled")
	q_text_box.grid(row=0, column=0, sticky="nsew")

	a_text_box: tkinter.Text = tkinter.Text(master=q_and_a_frame, wrap="word", state="disabled")
	a_text_box.grid(row=1, column=0, sticky="nsew")
	
	return q_and_a_frame


def _connect_home_and_q_and_a_frames(home_frame: tkinter.Frame, q_and_a_frame: tkinter.Frame) -> None:
	selected_q_types: typing.List[tkinter.StringVar] = []
	q_type_indexed_q_and_a_generators: typing.Dict[str, MM_QAndAGenerators.Q_AND_A_GENERATOR_SIGNATURE] = MM_QAndAGenerators.get_q_type_indexed_generators()

	cur_home_frame_checkbutton_row: int = 0
	cur_home_frame_checkbutton_col: int = 0
	for (q_index, q_type) in enumerate(q_type_indexed_q_and_a_generators):
		cur_home_frame_checkbutton_row += q_index // 2
		cur_home_frame_checkbutton_col += q_index % 2

		home_frame.grid_rowconfigure(cur_home_frame_checkbutton_row, weight=1)
		home_frame.grid_columnconfigure(cur_home_frame_checkbutton_col, weight=1)
		
		selected_q_types.append(tkinter.StringVar())
		q_type_checkbutton: tkinter.Checkbutton = tkinter.Checkbutton(
																master=home_frame, 
																text=q_type,
																variable=selected_q_types[-1],
																onvalue=q_type,
																offvalue=None
																)
		q_type_checkbutton.grid(
							row=cur_home_frame_checkbutton_row, 
							column=cur_home_frame_checkbutton_col, 
							sticky="nsew"
							)

	home_frame_start_btn: tkinter.Button = tkinter.Button(
													master=home_frame, 
													text="Start",
													command=lambda: _activate_frame(q_and_a_frame)
													)
	home_frame_start_btn.grid(row=cur_home_frame_checkbutton_row + 1, column=0, columnspan=2)
	
	(q_and_a_frame_a_textbox, q_and_a_frame_q_textbox) = q_and_a_frame.winfo_children()

	show_q_or_a: typing.Callable[[tkinter.Event], None] = lambda event: _show_q_or_a(q_and_a_frame_a_textbox, q_and_a_frame_q_textbox, selected_q_types, q_type_indexed_q_and_a_generators)
	q_and_a_frame.bind("<space>", show_q_or_a)
	q_and_a_frame.bind("<Escape>", lambda event: _activate_frame(home_frame)) 

def _activate_frame(frame: tkinter.Frame) -> None:
	frame.tkraise()
	frame.focus_set()

def _show_q_or_a(
			a_textbox: tkinter.Text, 
			q_textbox: tkinter.Text, 
			selected_q_types: typing.List[tkinter.StringVar],
			q_type_indexed_q_and_a_generators: typing.Dict[str, MM_QAndAGenerators.Q_AND_A_GENERATOR_SIGNATURE]
			) -> None:
	print("shi")
	if not _show_q_or_a.current_q:
		(_show_q_or_a.current_q, _show_q_or_a.current_a) = _generate_q_and_a(selected_q_types, q_type_indexed_q_and_a_generators)
		_show_q_or_a.a_is_shown = False	

	if not _show_q_and_a.a_is_shown:
		a_textbox.config(state="normal")	
		a_textbox.delete("start", "end")
		a_textbox.insert(str(_show_q_and_a.current_a))
		a_textbox.config(state="disabled")	
		_show_q_and_a.a_is_shown = True
	else:
		(_show_q_or_a.current_q, _show_q_or_a.current_a) = _generate_q_and_a(selected_q_types, q_type_indexed_q_and_a_generators)

		q_textbox.config(state="normal")	
		q_textbox.delete("start", "end")
		q_textbox.insert(_show_q_and_a.current_q)
		q_textbox.config(state="disabled")	

		a_textbox.config(state="normal")	
		a_textbox.delete("start", "end")
		a_textbox.config(state="disabled")	
		
		_show_q_or_a.a_is_shown = False

def _generate_q_and_a(selected_q_types, q_type_indexed_q_and_a_generators) -> MM_QAndAGenerators.Q_AND_A_SIGNATURE:
	selected_q_type = random.choice(selected_q_types)
	while not selected_q_type:
		selected_q_type = random.choice(selected_q_types)

	return q_type_indexed_q_and_a_generators[selected_q_type]()


