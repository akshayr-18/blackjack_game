#Blackjack game
import random
import string
from os import system, name  

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/         
        
"""
money=1000
bet=0
values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
		
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def cash_out_or_bet():
	global money
	choice2=str(input("Do you want to cash out or place another bet? (Y/N) : "))
	if choice2=='Y' or choice2=='y':
		if money==0:
			print("You don't have enough money for that...")
			quit()
		else:
			play()
	else:
		print(f"You have {money} dollars...!!!")
		quit() 
		
def printall(you_cards,dealer_cards):
	clear()
	global money
	global bet
	print(logo)
	print(f"Player's Money : {money} ")
	print(f"Bet : {bet}")
	print("Dealer's cards are : ",end=" ")
	for i in dealer_cards:
		print(i,end=" ")
	print()
	print("Your cards are: " ,end=" ")
	for i in you_cards:
		print(i,end=" ")
	print()
	
	
	
def house_draws(you_cards,dealer_cards,you_sum2):
	"""Function that allows the dealer to draw cards"""
	global money
	global values
	global bet	
	dealer_cards.append(values[random.randint(0,12)])
	printall(you_cards,dealer_cards)
	dsum=0
	for i in dealer_cards:
		dsum+=i
	if dsum>you_sum2 and dsum<22:
		print("Dealer Wins...!!!")
		cash_out_or_bet()
	elif dsum>21:

		for i in dealer_cards:
			if i==11:
				dealer_cards.remove(11)
				dealer_cards.append(1)
				house_draws(you_cards,dealer_cards,you_sum2)
				

		print("You Win...!!!")
		money+=2*bet
		cash_out_or_bet()
	else:
			house_draws(you_cards,dealer_cards,you_sum2)

	
def draw(you_cards,dealer_cards):
	"""Function that allows the user to draw random cards"""
	global money
	global values
	global bet
	you_cards.append(values[random.randint(0,12)])
	printall(you_cards,dealer_cards)
	you_sum2=0
	for i in you_cards:
			you_sum2+=i
	if you_sum2==21:
			print("BLACKJACK...!!! YOU WIN...!!!")
			money+=2*bet
			cash_out_or_bet()
	elif you_sum2>21:
		for i in you_cards:
			if i==11:
				you_cards.remove(11)
				you_cards.append(1)
				choice4=str(input("Draw or hold? : (D/H)"))
				if choice4=='D':
					draw(you_cards,dealer_cards)
				elif choice4=='H':
					house_draws(you_cards,dealer_cards,you_sum2)
		print("BUST..!! You Lose..!!")
		cash_out_or_bet() 
	else:
		choice5=str(input("Draw or hold? : (D/H)"))
		if choice5=='D':
			draw(you_cards,dealer_cards)
		elif choice5=='H':
			house_draws(you_cards,dealer_cards,you_sum2)

def play():
	"""Function that starts the game"""
	clear()
	print(logo)
	global values
	global money
	global bet
	while money>=0:
		print(f"Player's money : ${money} ")
		bet=int(input("Make your bet! : "))
		while bet>money:
			print("You don't have enough money to make that bet...!")
			bet=int(input("Make your bet! : "))
		money-=bet

		dealer_cards=[]
		you_cards=[] 
		dealer_cards.append(values[random.randint(0,12)])
		you_cards.append(values[random.randint(0,12)])
		you_cards.append(values[random.randint(0,12)])
		print("Dealer's cards are : ",end=" ")
		for i in dealer_cards:
			print(i,end=" ")
		print()
		print("Your cards are: " ,end=" ")
		for i in you_cards:
			print(i,end=" ")
		you_sum=0
		for i in you_cards:
			you_sum+=i
		if you_sum==21:
			print("BLACKJACK...!!! YOU WIN...!!!")
			money+=2*bet
			cash_out_or_bet() 
		if you_sum==22:
			you_cards.clear()
			you_cards.append(1)
			you_cards.append(11)
		choice3=str(input("Draw or hold? : (D/H)"))
		if choice3=='D':
			draw(you_cards,dealer_cards)
		elif choice3=='H':
			house_draws(you_cards,dealer_cards,you_sum)
		
		print()
	print("Oops, you ran out of money... Come back with more...!!")
	quit()
		
def start():
	"""Allows the user to start playing"""
	print(logo)
	choice1=str(input("Do you wish to play BlackJack? (Y/N) : "))
	if choice1=='Y' or choice1=='y':
		play()
	else:
		quit()
start()
