from TextColor import ColorForText as color
from random import choice,randint

X_player=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#all 16 position for player X on the Board
O_player=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#all 16 position for player O on the Board
winning_pos_arr=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]#all positions in the board where X or O can win
def ifwon(X_or_O_arr):
	"""This function Checks if X or O wins a perticuler position basically 4 O's or 4 X's in row"""
	for win_pos in winning_pos_arr:
		sum_is_4=0
		for ind in win_pos:
			sum_is_4+=X_or_O_arr[ind]
		if sum_is_4==4:
			return True
def copy_list(lis):
	"""Copys a array"""
	li=lis[::]
	return li
	
def ifsum1(O_user,index_lis):
	"""Checks if the sum is 1 in a row"""
	sum_1=0
	for ind in index_lis:
		sum_1+=O_user[ind]
	if sum_1==1:
		return True
	
def ifsum2(X_O_user,index_lis):
	"""Checks if the sum in a row is 2"""
	sum_2=0
	for ind in index_lis:
		sum_2+=X_O_user[ind]
	if sum_2==2:
		return True

def ifsum3(X_O_user,index_lis):
	"""Checks if the sum is 3"""
	sum_3=0
	for ind in index_lis:
		sum_3+=X_O_user[ind]
	if sum_3==3:
		return True
def return_if_0(X_and_O_lis_copy,lis):
	"""it checks which index in a row is empty"""
	index_retu=None
	if X_and_O_lis_copy[lis[0]]==0:
		index_retu=lis[0]
	elif X_and_O_lis_copy[lis[1]]==0:
		index_retu=lis[1]
	elif X_and_O_lis_copy[lis[2]]==0:
		index_retu=lis[2]
	elif X_and_O_lis_copy[lis[3]]==0:
		index_retu=lis[3]
	return index_retu
def check_if_O_can_win():
	"""This will check O the computer has any winning position or not"""
	x_lis_copy=copy_list(X_player)
	o_lis_copy=copy_list(O_player)
	pos_of_O_to_win=None
	for win_pos in winning_pos_arr:
		if ifsum3(o_lis_copy,win_pos):
			if x_lis_copy[win_pos[0]]==1 or x_lis_copy[win_pos[1]]==1 or x_lis_copy[win_pos[2]]==1 or x_lis_copy[win_pos[3]]==1:
				pass
			else:
				pos_of_O_to_win=return_if_0(o_lis_copy,win_pos)
	return pos_of_O_to_win #so if O has any winning postion it will return it else None
def put_by_com():
	x_lis_copy=copy_list(X_player)
	o_lis_copy=copy_list(O_player)
	if x_lis_copy.count(1)==1:
		#Frist i will check if the humam user has entered any position or not then i will itrate through all postion that can win and i will find out the human user has put X then i will check if the computer has put O on that particular position if not i will return rthe empty position using return_if_0
		
		for win_pos in winning_pos_arr:
			if ifsum1(x_lis_copy,win_pos):
				if o_lis_copy[win_pos[0]]==0 and o_lis_copy[win_pos[1]]==0 and o_lis_copy[win_pos[2]]==0 and o_lis_copy[win_pos[3]]==0:
					re_s1=return_if_0(x_lis_copy,win_pos)
					return re_s1
	else:
		re_i_X=None #if X has a wining cordinate
		re_i_O=None #if O has a wining cordinate
		re_i_s1=None #if sum of x lis is 1 
		for win_pos in winning_pos_arr:
			#checking if the computer "O" can win
			win_pos_for_O=check_if_O_can_win()
			if win_pos_for_O!=None:
				re_i_X=win_pos_for_O
			
			elif ifsum3(x_lis_copy,win_pos):
				if o_lis_copy[win_pos[0]]==1 or o_lis_copy[win_pos[1]]==1 or o_lis_copy[win_pos[2]]==1 or o_lis_copy[win_pos[3]]==1:
					pass
				else:
					re_i_O=return_if_0(x_lis_copy,win_pos)
			elif ifsum2(o_lis_copy,win_pos):
				if x_lis_copy[win_pos[0]]==1 or x_lis_copy[win_pos[1]]==1 or x_lis_copy[win_pos[2]]==1 or x_lis_copy[win_pos[3]]==1:
					pass
				else:
					re_i_O=return_if_0(o_lis_copy,win_pos)
			#checking if "X" can win
			elif ifsum2(x_lis_copy,win_pos):
				if o_lis_copy[win_pos[0]]==1 or o_lis_copy[win_pos[1]]==1 or o_lis_copy[win_pos[2]]==1 or o_lis_copy[win_pos[3]]==1:
					pass
				else:
					re_i_X=return_if_0(x_lis_copy,win_pos)
				
			elif ifsum1(x_lis_copy,win_pos):
				if o_lis_copy[win_pos[0]]==0 and o_lis_copy[win_pos[1]]==0 and o_lis_copy[win_pos[2]]==0 and o_lis_copy[win_pos[3]]==0:
					re_i_s1=return_if_0(x_lis_copy,win_pos)
		
		if re_i_O!=None:
			return re_i_O
		elif re_i_X!=None:
			return re_i_X
		else:
			return re_i_s1
					
					

def print_board():
	end=color.Endc
	yellow=color.Yellow
	megenta =color.Magenta 
	zero=yellow+"X"+end if X_player[0] else (megenta+"O"+end if O_player[0] else 0)#its to position a value in 0 index position if X_player of 0 index is 1 that means to put X else O or else tge index itself which in this case is 0
	one=yellow+"X"+end if X_player[1] else (megenta+"O"+end if O_player[1] else 1)
	two=yellow+"X"+end if X_player[2] else (megenta+"O"+end if O_player[2] else 2)
	three=yellow+"X"+end if X_player[3] else (megenta+"O"+end if O_player[3] else 3)
	four=yellow+"X"+end if X_player[4] else (megenta+"O"+end if O_player[4] else 4)
	five=yellow+"X"+end if X_player[5] else (megenta+"O"+end if O_player[5] else 5)
	six=yellow+"X"+end if X_player[6] else (megenta+"O"+end if O_player[6] else 6)
	seven=yellow+"X"+end if X_player[7] else (megenta+"O"+end if O_player[7] else 7)
	eight=yellow+"X"+end if X_player[8] else (megenta+"O"+end if O_player[8] else 8)
	nine=yellow+"X"+end if X_player[9] else (megenta+"O"+end if O_player[9] else 9)
	ten=yellow+" X"+end if X_player[10] else (megenta+" O"+end if O_player[10] else 10)
	ellaven=yellow+"X"+end if X_player[11] else (megenta+"O"+end if O_player[11] else 11)
	twelve=yellow+" X"+end if X_player[12] else (megenta+" O"+end if O_player[12] else 12)
	thirteen=yellow+" X"+end if X_player[13] else (megenta+" O"+end if O_player[13] else 13)
	fourteen=yellow+" X"+end if X_player[14] else (megenta+" O"+end if O_player[14] else 14)
	fifteen=yellow+"X"+end if X_player[15] else (megenta+"O"+end if O_player[15] else 15)
	line="|"
	print("---|---|---|---")
	print(f" {zero} {line} {one} {line} {two} {line} {three}")
	print("---|---|---|---")
	print(f" {four} {line} {five} {line} {six} {line} {seven}")
	print("---|---|---|---")
	print(f" {eight} {line} {nine} {line}{ten} {line} {ellaven}")
	print("---|---|---|---")
	print(f"{twelve} {line}{thirteen} {line}{fourteen} {line} {fifteen}")
def main():
	global tern,computer_frist_tern,O_player,X_player
	run=True
	while run:
		X_player_reset=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		O_player_reset=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		if tern==0:
			x_user_tern=int(input("Enter Your Position as an index: "))
			if O_player[x_user_tern]==1:
				print("Your opponent 'O' has already entered in this postion")
			else:
				X_player[x_user_tern]=1
			if ifwon(X_player):
				print("You Won 'X' Congrats :)")
				run=False
			tern+=1
		else:
			if computer_frist_tern:
				o_user_tern=randint(0,15)
				computer_frist_tern=False
			else:
				o_user_tern=put_by_com()
			print(f"The Computer Has Choosen {o_user_tern}")
			if o_user_tern==None:
				print("its a draw")
				run=False	
			elif X_player[o_user_tern]==1:
				print("Your Opponent 'X' has already entered in this position")
			else:
				O_player[o_user_tern]=1
			if ifwon(O_player):
				print("You Won 'O' Congrats")
				run=False
			tern-=1
		print_board()
		if run==False:
			do_continue=input("Do You Want to play again Yes(y) :")
			if do_continue.lower()=="y":
				run=True
				X_player=X_player_reset
				O_player=O_player_reset
				toss_lis=["h","t"]
				computer_frist_tern=False
				print_board()
				user_toss_choice=input("To choose Heads(h) for Tails(t) :")
				toss_call=choice(toss_lis)
				if user_toss_choice.lower()==toss_call:
					tern=0 #that means the "Human" player had won the toss that means he will put the frist move
					print("You 'X' won the toss")
				else:
					tern=1 #that means computer has won the toss
					computer_frist_tern=True
					print("You 'O' won the toss")
				
				
		
if __name__=="__main__":
	print_board()
	toss_lis=["h","t"]
	user_toss_choice=input("To choose Heads(h) for Tails(t) :")
	toss_call=choice(toss_lis)
	computer_frist_tern=False
	if user_toss_choice.lower()==toss_call:
		tern=0 #that means the "Human" player had won the toss that means he will put the frist move
		print("You 'X' won the toss")
	else:
		tern=1 #that means computer has won the toss
		computer_frist_tern=True
		print("You 'O' won the toss")
	main()

"""
Conclusion of this 4x4 Tic Tac Toe so before making this 4x4 tic tac toe i thought that i was a mess in coding but after making the 4x4 tic tac toe i am super sure im a mess but anyways i hope you can understand the code if not dont worry its not your fault im the MESS

"""

	