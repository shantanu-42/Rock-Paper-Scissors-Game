from tkinter import *
from PIL import Image,ImageTk
from random import randint

#This is For making a Window 
root=Tk()
root.title('Rock Paper Scissors')
root.configure(background='white')

image = Image.open("scissors.png") 
rotated_image = image.rotate(270)
rotated_image.save("sci_rotated.png")
rotated_image = image.rotate(90)
rotated_image.save("sci1_rotated.png")

image = Image.open("paper.png") 
rotated_image = image.rotate(180)
rotated_image.save("paper_rotated.png")
# rotated_image = image.rotate(270)
# rotated_image.save("paper1_rotated.png")

image = Image.open("rock.png") 
rotated_image = image.rotate(-90)
rotated_image.save("rock_rotated.png")
rotated_image = image.rotate(90)
rotated_image.save("rock1_rotated.png")

rock=ImageTk.PhotoImage(Image.open('rock_rotated.png'))
paper=ImageTk.PhotoImage(Image.open('paper_rotated.png'))
scissors=ImageTk.PhotoImage(Image.open('sci_rotated.png'))
rockpc=ImageTk.PhotoImage(Image.open('rock1_rotated.png'))
paperpc=ImageTk.PhotoImage(Image.open('paper.png'))
scissorspc=ImageTk.PhotoImage(Image.open('sci1_rotated.png'))


user_panel=Label(root,image=rock,bg='white')
user_panel.grid(row=6,column=1)
pc_panel=Label(root,image=rockpc,bg='white')
pc_panel.grid(row=1,column=1)

user_name=Label(root,font=100,text='User',bg='white')
pc_name=Label(root,font=100,text='Computer',bg='white')
user_name.grid(row=6,column=0)
pc_name.grid(row=1,column=0)

user_score=Label(root,text=0,font=200,bg='#215661',fg='white',width=5)
pc_score=Label(root,text=0,font=200,bg='#215661',fg='white',width=5)
text_score=Label(root,text="Match Score:",font=10,bg='white')
text_score.grid(row=3,column=0)
user_score.grid(row=4,column=1)
pc_score.grid(row=3,column=1)

msg=Label(root,font=('bold',17),fg='red',bg='white',text='Welcome to Game !')
msg.grid(row=3,column=2)

rock_button=Button(root,width=17,height=1,text='ROCK',font='bold',bg='grey',fg='white',command= lambda: chooseChoice('rock'))
rock_button.grid(row=7,column=0)
paper_button=Button(root,width=17,font='bold',height=1,text='PAPER',bg='white',fg='black',command= lambda: chooseChoice('paper'))
paper_button.grid(row=7,column=1)
scissors_button=Button(root,width=17,font='bold',height=1,text='SCISSORS',bg='pink',fg='black',command= lambda: chooseChoice('scissors'))
scissors_button.grid(row=7,column=2)

def chooseChoice(x):
    choices=['rock','paper','scissors']
    
    computer_says=choices[randint(0,2)]
    if computer_says=='rock':
        pc_panel.configure(image=rockpc)
    elif computer_says=='paper':
        pc_panel.configure(image=paperpc)
    else:
        pc_panel.configure(image=scissorspc)

    
    if x=='rock':
        user_panel.configure(image=rock)
    elif x=='paper':
        user_panel.configure(image=paper)
    else:
        user_panel.configure(image=scissors)
    
    winner(x,computer_says)


def winner(player,computer):
    if player==computer:
        show_msg('Match Tied !')
    elif player=='rock':
        if computer=='scissors':
            show_msg('YOU WON !')
            update_user_score()
        else:
            show_msg('YOU LOST :(')
            update_comp_score()
    elif player=='paper':
        if computer=='scissors':
            show_msg('YOU LOST :(')
            update_comp_score()
        else:
            show_msg('YOU WON !')
            update_user_score()
    else:
        if computer=='paper':
            show_msg('YOU WON !')
            update_user_score()
        else:
            show_msg('YOU LOST :(')
            update_comp_score()
        
def show_msg(x):
    msg['text']=x

def update_comp_score():
    comp_score=int(pc_score['text'])
    comp_score+=1
    pc_score['text']=str(comp_score)

def update_user_score():
    us_score=int(user_score['text'])
    us_score+=1
    user_score['text']=str(us_score)
    
#This opens the the Window we created
root.mainloop()