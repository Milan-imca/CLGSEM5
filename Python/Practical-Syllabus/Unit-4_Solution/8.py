# Create  a  GUI Application  to  display  Movie  Chooser  using check box control.
from tkinter import *

window = Tk()
window.title("Movie Chooser")

movies = ["Radhe Shyam","RRR","Taqdeer","DJ"]
movie_vars = {}


def show_selected_movies():
  selected_movies = [movie for movie,var in movie_vars.items() if var.get()]
  if selected_movies:
    # result_label.config(text="Selected Movies: " + ", ".join(selected_movies))
    result_label.config(text="Selected movies : " + " , ".join(selected_movies))
  else:
    result_label.config(text="No movies selected")

for movie in movies:
  var = IntVar()
  checkbox = Checkbutton(
    window,
    text=movie,
    variable=var,
    command=show_selected_movies
  )
  checkbox.pack(anchor='w')
  movie_vars[movie] = var



result_label = Label(
  window,
  text="Selected Movies : ",
  # font=("Arial",16)
  )
result_label.pack(pady=10)


window.mainloop()
