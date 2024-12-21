
from Textcolor import ColorForText as co
from random import randint,choice
list_win=None
draw_bord=False
def ifwin(X_O_user):
	global list_win
	you_win=False
	wining_cord=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for total in wining_cord:
		sum_is_3=0
		for ind in total:
			sum_is_3+=X_O_user[ind]
		if sum_is_3==3:
			you_win=True
			list_win=total
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
	X_lis_copy=copy_list(X_user)
	O_lis_copy=copy_list(O_user)
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
			
def print_board():
	global list_win,draw_bord
	end=co.Endc
	if draw_bord==True:
		color_bord=co.Yellow
		draw_bord=False
	else:
		color_bord=co.White
	if list_win==None:
		ZeroC=color_bord
		OneC=color_bord
		TwoC=color_bord
		ThreeC=color_bord
		FourC=color_bord
		FiveC=color_bord
		SixC=color_bord
		SevenC=color_bord
		EightC=color_bord
	else:
		if list_win[0]==0 or list_win[1]==0 or list_win[2]==0:
			ZeroC=co.Green
		else:
			ZeroC=co.White
		if list_win[0]==1 or list_win[1]==1 or list_win[2]==1:
			OneC=co.Green
		else:
			OneC=co.White
		if list_win[0]==2 or list_win[1]==2 or list_win[2]==2:
			TwoC=co.Green
		else:
			TwoC=co.White
		if list_win[0]==3 or list_win[1]==3 or list_win[2]==3:
			ThreeC=co.Green
		else:
			ThreeC=co.White
		if list_win[0]==4 or list_win[1]==4 or list_win[2]==4:
			FourC=co.Green
		else:
			FourC=co.White
		if list_win[0]==5 or list_win[1]==5 or list_win[2]==5:
			FiveC=co.Green
		else:
			FiveC=co.White
		if list_win[0]==6 or list_win[1]==6 or list_win[2]==6:
			SixC=co.Green
		else:
			SixC=co.White
		if list_win[0]==7 or list_win[1]==7 or list_win[2]==7:
			SevenC=co.Green
		else:
			SevenC=co.White
		if list_win[0]==8 or list_win[1]==8 or list_win[2]==8:
			EightC=co.Green
		else:
			EightC=co.White
		list_win=None
			
	zero=ZeroC+"X"+end if X_user[0] else (ZeroC+"O"+end if O_user[0] else 0)
	one=OneC+"X"+end if X_user[1] else (OneC+"O"+end if O_user[1] else 1)
	two=TwoC+"X"+end if X_user[2] else (TwoC+"O"+end if O_user[2] else 2)
	three=ThreeC+"X"+end if X_user[3] else (ThreeC+"O"+end if O_user[3] else 3)
	four=FourC+"X"+end if X_user[4] else (FourC+"O"+end if O_user[4] else 4)
	five=FiveC+"X"+end if X_user[5] else (FiveC+"O"+end if O_user[5] else 5)
	six=SixC+"X"+end if X_user[6] else (SixC+"O"+end if O_user[6] else 6)
	seven=SevenC+"X"+end if X_user[7] else (SevenC+"O"+end if O_user[7] else 7)
	eight=EightC+"X"+end if X_user[8] else (EightC+"O"+EightC if O_user[8] else 8)
	color_lines=co.Bold+co.Grey
	line=color_lines+"|"+co.Endc
	print(color_lines+"---|---|---"+co.Endc)
	print(f" {zero} {line} {one} {line} {two} ")
	print(color_lines+"---|---|---"+co.Endc)
	print(f" {three} {line} {four} {line} {five} ")
	print(color_lines+"---|---|---"+co.Endc)
	print(f" {six} {line} {seven} {line} {eight} ")
	print(color_lines+"---|---|---"+co.Endc)
X_user=[0,0,0,0,0,0,0,0,0]
O_user=[0,0,0,0,0,0,0,0,0]
#tern=0
print_board()

toss_list=["h","t"]# this is the toss list wich has Head and Tail using choice function i will choose randomly
toss_won_random_tern=False #if its True taht means now i should choose the input by computer randomly
toss_input=input("Enter (h) for Head or(t) for Tail: ")
random_toss_result=choice(toss_list)
print(random_toss_result)
#the logic is simple if the user wins the toss then he get to choose the input else the computer will randomly genarate an input 
if random_toss_result==toss_input:
	tern=0
else:
	tern=1
	toss_won_random_tern=True
while True:
	X_user_re=[0,0,0,0,0,0,0,0,0]
	O_user_re=[0,0,0,0,0,0,0,0,0]
	stop=False
	if tern==0:
		X_user_tern=int(input("ENTER YOUR POSITION AS INDEX "))
		if O_user[X_user_tern]==1:
			print("already enterd enterd in this position")
		else:
			X_user[X_user_tern]=1
		if ifwin(X_user):
			print("you won X CONGRATULATION;)")
			#print(list_win)
			stop=True
		tern+=1
	else:
		if toss_won_random_tern==True:
			num=randint(0,9)
			toss_won_random_tern=False
		else:
			num=put_by_com()
		print("COMPUTER HAS ENTERD ITS POSITION",num)
		O_user_tern=num
		if O_user_tern==None:
			draw_bord=True
			print("THIS IS A DRAW")
			stop=True
		elif X_user[O_user_tern]==1:
			#if it is already filled
			print("your oponent has already enterd in that position")
		else:
			O_user[O_user_tern]=1
			#put_by_com()
			#print(X_user)
		if ifwin(O_user):
			print("you won O congratuations :)")
			print(list_win)
			stop=True
		tern-=1
	print_board()
	
	if stop==True:
		do_continue=input("do you want continue  ")
		if do_continue=="y" or do_continue=="Y":
			stop=False
			X_user=X_user_re
			O_user=O_user_re
			tern=0
			print_board()
			
			toss_list=["h","t"]# this is the toss list wich has Head and Tail using choice function i will choose randomly
			toss_won_random_tern=False #if its True taht means now i should choose the input by computer randomly
			toss_input=input("Enter (h) for Head or(t) for Tail: ")
			random_toss_result=choice(toss_list)
			print(random_toss_result)
			#the logic is simple if the user wins the toss then he get to choose the input else the computer will randomly genarate an input 
			if random_toss_result==toss_input:
				tern=0
			else:
				tern=1
				toss_won_random_tern=True
		else:
			break
#put_by_com()
