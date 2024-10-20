from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Scrollbar Demo")

frame = Frame(window)
frame.pack(padx=10,pady=10)


text_widget = Text(frame,wrap="word",height=10,width=50)
text_widget.pack(side="left")

scrollbar = ttk.Scrollbar(frame,command=text_widget.yview)
scrollbar.pack(side="right",fill=Y)

text_widget.config(yscrollcommand=scrollbar.set)

sample_text = """
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. 
Nulla facilisi. Nam sed sapien libero. Maecenas non scelerisque sem. 
Curabitur vitae laoreet libero. Aliquam erat volutpat. Vivamus placerat 
magna in massa posuere suscipit. Cras luctus metus at gravida dapibus. 
Pellentesque ac tortor vitae risus vulputate lobortis ac eu nunc. 
Suspendisse potenti. Ut ac dui venenatis, varius orci eget, vehicula erat. 
Duis ac dictum dolor. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 

Sed sit amet semper lacus. Aenean luctus, risus id vulputate bibendum, purus velit elementum erat, non pharetra purus ligula eget libero. 
Nam sodales ex nec tellus venenatis, at ullamcorper enim posuere. 
Quisque ut enim eget justo mattis tempus. Duis sit amet libero purus. 
Sed scelerisque euismod neque, a interdum enim iaculis vel.
"""

text_widget.insert(END,sample_text)

window.mainloop()