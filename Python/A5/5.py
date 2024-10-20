from tkinter import *

candidate1_vote_count = 0
candidate2_vote_count = 0
candidate3_vote_count = 0

def update_Vote():
	global candidate1_vote_count,candidate2_vote_count,candidate3_vote_count
	selected_vote = selected_var.get()


	if selected_vote == 1:
		candidate1_vote_count += 1
	elif selected_vote == 2:
		candidate2_vote_count += 1
	elif selected_vote == 3:
		candidate3_vote_count += 1

	c1_label.config(text=f"Candidate 1 vote : {candidate1_vote_count}")
	c2_label.config(text=f"Candidate 2 vote : {candidate2_vote_count}")
	c3_label.config(text=f"Candidate 3 vote : {candidate3_vote_count}")

window = Tk()
window.title("Vote")
window.geometry("500x500")


selected_var = IntVar(value=1)

c1_radio_btn = Radiobutton(window,text="Candidate 1",value = 1,variable = selected_var)
c2_radio_btn = Radiobutton(window,text="Candidate 2",value = 2,variable = selected_var)
c3_radio_btn = Radiobutton(window,text="Candidate 3",value = 3,variable = selected_var)

c1_radio_btn.pack(anchor='w')
c2_radio_btn.pack(anchor='w')
c3_radio_btn.pack(anchor='w')

vote_btn = Button(window,text="VOTE",command=update_Vote)
vote_btn.pack()

c1_label = Label(window,text=f"Candidate 1 vote : {candidate1_vote_count}")
c2_label = Label(window,text=f"Candidate 2 vote : {candidate2_vote_count}")
c3_label = Label(window,text=f"Candidate 3 vote : {candidate3_vote_count}")

c1_label.pack()
c2_label.pack()
c3_label.pack()

window.mainloop()