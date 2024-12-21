#from tkinter import Tk
""""So this is a tic-tac-toe 3x3 game that I made a few months ago I thought as I'm sharing my 4x4 tic-tac-toe I should share this as well. And I know this 3x3 tic-tac-toe code doesn't have that many comments so you could unserstand the code  because as I said i coded this a few months ago I didn't used to write comments on my code so yeah and also i pretty much forgot all in tkinter so I don't think so now I would understand that much. But still in this GUI version there are two modes The first one if you are lucky enough you can play it with a friend or whoever other companion you have Or else if you are Mr. Lonely like me you can play it with the AI And btw if you are reading this far then congratulations that's menas You are in the top 87% of the world's population who can read isn't it crazy also after my warning if you want to still read my 3x3 code then read it at your own risk I'm not responsible."""
#to run this code without any errors frist you need to install tkinter (pip install tkinter) 2nd make sure you put the right path of the game code game_gui.py in "diractory_path" variable
from tkinter import Tk,Button,Label,PhotoImage,messagebox,Menu
 
win=Tk()
def play_again():
	pass
X_list=[0,0,0,0,0,0,0,0,0]
O_list=[0,0,0,0,0,0,0,0,0]
dir_path="/storage/emulated/0/TickTackToeAIguiVersion/"
win.configure(bg="black")
win.geometry("680x1440")
my_font=("Helvetica", "8","bold") #font of x and o
Ai_or_Human="2p"
def AI_OR_HUMAN(ai_human):
	global Ai_or_Human
	if ai_human=="Ai":
		Ai_or_Human="Ai"
	else:
		Ai_or_Human="2p"
menubar = Menu(win)

menu_file = Menu(menubar, tearoff=0,bg='yellow') # file

menubar.add_cascade(label="Mode", menu=menu_file) # Top Line

menu_file.add_command(label="2 ON ", command=lambda:AI_OR_HUMAN("Human")) # Item 1 of file
menu_file.add_command(label="Ai", command=lambda:AI_OR_HUMAN("Ai"))
wining_list=None
def ifwin(X_O_user):
	global wining_list
	you_win=False
	wining_cord=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for total in wining_cord:
		sum_is_3=0
		for ind in total:
			sum_is_3+=X_O_user[ind]
		if sum_is_3==3:
			you_win=True
			wining_list=total
			break
	return you_win
	
def ifsum2(X_O_user,index_lis):
	your_win=False
	sum_2=0
	for ind in index_lis:
		sum_2+=X_O_user[ind]
	if sum_2==2:
		#print("yp",index_lis)
		your_win=True
	return your_win
def ifsum1(O_user,index_lis):
	your_win=False
	sum_1=0
	for ind in index_lis:
		sum_1+=O_user[ind]
	if sum_1==1:
		your_win=True
	return your_win
	
def return_if_0(X_and_O_lis_copy,lis):
	index_retu=None
	if X_and_O_lis_copy[lis[0]]==0:
		index_retu=lis[0]
	elif X_and_O_lis_copy[lis[1]]==0:
		index_retu=lis[1]
	elif X_and_O_lis_copy[lis[2]]==0:
		index_retu=lis[2]
	return index_retu
def copy_list(lis):
	li=lis[::]
	return li

def put_by_com():
	X_lis_copy=copy_list(X_list)
	O_lis_copy=copy_list(O_list)
	all_index=[0,1,2,3,4,5,6,7,8]
	wining_cord=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	if X_lis_copy.count(1)==1:
		for lis in wining_cord:
			if ifsum1(X_lis_copy,lis):
				if O_lis_copy[lis[0]]==0 and O_lis_copy[lis[1]]==0 and O_lis_copy[lis[2]]==0:
					re_s1=return_if_0(X_lis_copy,lis)
					return re_s1
	else:
		re_i_X=None #if X has a wining cordinate
		re_i_O=None #if O has a wining cordinate
		re_i_s1=None #if sum of x lis is 1 
		#re_ind=None
		for lis in wining_cord:
			if ifsum2(O_lis_copy,lis):
				#print("O LIST")
				if X_lis_copy[lis[0]]==1 or X_lis_copy[lis[1]]==1 or X_lis_copy[lis[2]]==1:
					pass
				else:
					re_i_O=return_if_0(O_lis_copy,lis)
			elif ifsum2(X_lis_copy,lis):
				#print("X List")
				if O_lis_copy[lis[0]]==1 or O_lis_copy[lis[1]]==1 or O_lis_copy[lis[2]]==1:
					pass
				else:
					re_i_X=return_if_0(X_lis_copy,lis)
				
			elif ifsum1(X_lis_copy,lis):
				if O_lis_copy[lis[0]]==0 and O_lis_copy[lis[1]]==0 and O_lis_copy[lis[2]]==0:
					re_i_s1=return_if_0(X_lis_copy,lis)
					
		if re_i_O!=None:
			return re_i_O
		elif re_i_X!=None:
			return re_i_X
		else:
			return re_i_s1

Button_0=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(0),width=8,height=5)
Button_0.place(x=0,y=350)
Button_1=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(1),height=5,width=8)
Button_1.place(x=240,y=350)
Button_2=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(2),height=5,width=8)
Button_2.place(x=480,y=350)

Button_3=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(3),height=5,width=8)
Button_3.place(x=0,y=580)
Button_4=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(4),height=5,width=8)
Button_4.place(x=240,y=580)
Button_5=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(5),height=5,width=8)
Button_5.place(x=480,y=580)

Button_6=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(6),height=5,width=8)
Button_6.place(x=0,y=820)
Button_7=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(7),height=5,width=8)
Button_7.place(x=240,y=820)
Button_8=Button(win,text=" ",font=my_font,command=lambda:wich_button_cliked(8),height=5,width=8)
Button_8.place(x=480,y=820)


tern=0
diractory_path="/storage/emulated/0/TickTackToeAIguiVersion/"# this is the main path where the game is located you need to change it accoding to where you locate the game_gui.py
def Fill_button(button_num,text_or_bg,X_O_color):
	if button_num==0:
		Button_0[text_or_bg]=X_O_color
	elif button_num==1:
		Button_1[text_or_bg]=X_O_color
	elif button_num==2:
		Button_2[text_or_bg]=X_O_color
	elif button_num==3:
		Button_3[text_or_bg]=X_O_color
	elif button_num==4:
		Button_4[text_or_bg]=X_O_color
	elif button_num==5:
		Button_5[text_or_bg]=X_O_color
	elif button_num==6:
		Button_6[text_or_bg]=X_O_color
	elif button_num==7:
		Button_7[text_or_bg]=X_O_color
	elif button_num==8:
		Button_8[text_or_bg]=X_O_color
def sum_2_lis_8():
	x_lis=sum(X_list)
	o_lis=sum(O_list)
	total=x_lis+o_lis
#	la=Label(win,text=str(total)).pack()
	if total>=8:
		return True
def wich_button_cliked(button_number):
	global tern,yes_or_no,X_list,O_list
	X_user_re=[0,0,0,0,0,0,0,0,0]
	O_user_re=[0,0,0,0,0,0,0,0,0]
	yes_or_no="no"
	you_win=False
	if tern==0:
		if sum_2_lis_8():
			messagebox.showwarning("showwarning", "Its draw")
			yes_or_no=messagebox.askquestion("quit","Do you want to continue",icon="warning")
		elif O_list[button_number]==1:
			#already entered
			messagebox.showwarning("showwarning", "Already entered by O")
		else:
			X_list[button_number]=1
			Fill_button(button_number,"text","X")
			if ifwin(X_list):
				if wining_list!=None:
					for ind in wining_list:
						Fill_button(ind,"bg","green")
				messagebox.showwarning("showwarning", "YOU WON X")
				you_win=True
				yes_or_no=messagebox.askquestion("quit","Do you want to continue",icon="warning")
		tern+=1
		if Ai_or_Human=="Ai" and you_win==False:
			wich_button_cliked(12)
	else:
		if Ai_or_Human=="Ai":
			button_by_ai=put_by_com()
		elif Ai_or_Human=="2p":
			button_by_ai=button_number
		if button_by_ai==None:
			messagebox.showwarning("showwarning", "Its an draw in ai")
			yes_or_no=messagebox.askquestion("quit","Do you want to continue",icon="warning")
		elif X_list[button_by_ai]==1:
			messagebox.showwarning("showwarning", "Already entered by X")
		else:
			O_list[button_by_ai]=1
			Fill_button(button_by_ai,"text","O")
			if ifwin(O_list):
				if wining_list!=None:
					for ind in wining_list:
						Fill_button(ind,"bg","green")
				messagebox.showwarning("showwarning", "YOU WON O")
				yes_or_no=messagebox.askquestion("quit","Do you want to continue",icon="warning")	
		tern-=1
	if yes_or_no=="yes":
		X_list=X_user_re
		O_list=O_user_re
		tern=0
		you_win=False
		for ind in range(0,9):
			Fill_button(ind,"text"," ")
			Fill_button(ind,"bg","white")
	d=str(X_list)
	f=str(O_list)
#	la=Label(win,text=d).pack()
	#la=Label(win,text=f).pack()
win.config(menu=menubar)
win.mainloop()