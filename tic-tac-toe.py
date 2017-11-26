from tkinter import *
import tkinter.messagebox

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
                                           
      winner(i)

window = Tk()
player = "X"
list= []

def winner(i):
      win = ((0,1,2),
             (3,4,5),
             (6,7,8),
             (0,3,6),
             (1,4,7),
             (2,5,8),
             (0,4,8),
             (2,4,6))
      
      for i in win:
            if(list[i[0]]["text"] == list[i[1]]["text"] == list[i[2]]["text"] == "X"):
                  tkinter.messagebox.showinfo("", "winner is X")
                  quit()
                  return
            
            elif(list[i[0]]["text"] == list[i[1]]["text"] == list[i[2]]["text"] == "O"):
                  tkinter.messagebox.showinfo("", "winner is O")
                  quit()
                  return

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


