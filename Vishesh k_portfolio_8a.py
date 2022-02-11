name = str(input("What's your name: "))
print("My name is Vishesh...")
print("You will get 5 questions...")
yesorno = str(input("Are you ready or not. To respond yes please write y and to say no write n: ")).lower()
y = "y"
n = "n"
ans1 = "a"
ans4 = "d"
ans2 = "c"
ans3 = "d"

a1L = ans1.lower()
a2L = ans2.lower()
a3L = ans3.lower()
a4L = ans4.lower()
score = 0

def displayq4():
	global answer, ans4, score, a4
	answer = str(input("""Question 4 : Artificial Intelligence is about_____.

a)Playing a game on Computer
b)Making humans intelligent by chips
c)Programming your brain
d)Putting your intelligence in Machine
Ans:-  """)).lower()
	if ans4 == answer:
		score = score + 1
		print("GOOD JOB, THIS IS YOUR SCORE")
		print(score)
	else:
		x = f"Incorrect answer. It was {ans4}"
		print(x)
		print("Your score was")
		print(score)
		
def displayq3():
	global score
	answer = str(input("""Question 3 : The application/applications of Artificial Intelligence is/are

a)Expert Systems
b)Gaming
c)Vision Systems
d)All of the above 
Ans:- """)).lower()
	if a3L == answer:
		score += 1
		print("GOOD JOB, YOU GOT IT CORRECT YOUR SCORE IS ")
		print(score)
		displayq4()
	else:
		print(f'Incorrect Answer.. It Was Actualy {ans3}')
		print(score)
		displayq4()
		
		
def displayq2():
	global score
	answer = str(input("""Question 2 : Who is known as the -Father of AI"?
				a)Fisher Ada
				b)Alan Turing
				c)John McCarthy
				d)Allen Newell
				Ans :- """)).lower()
	if (a2L==answer.lower()):
		score += 1
		print("GOOD JOB, YOU GOT IT CORRECT YOUR SCORE IS ")
		print(score)
		displayq3()
	else:
		print("Incorrect answer.It was ", ans2)
		print(score)
		displayq3()


def displayq1():
	global score
	answer = str(input("""Question 1 : What is the full form of AI?
	a)Artificial intelligence
	b)Aided Intelligence
	c)Both a and b
	d)None of the above
	Ans:- """)).lower()
	if a1L.lower() == answer:
		score += 1
		print("GOOD JOB, YOU GOT IT CORRECT YOUR SCORE IS ")
		print(score)
		displayq2()
	else:
		print("Incorrect answer. It was ", ans1)
		print(score)
		displayq2()


if (yesorno==y):
	print("Ready or not here I come")
	displayq1()
elif (yesorno==n):
	print("Bye Bye", name)
else:
	yesorno = str(input("Are you ready or not. To respond yes please write y and to say no write n: ")).lower()
	if (yesorno==y):
		print("Ready or not here I come")
		displayq1()
	elif (yesorno==n):
		print("Bye Bye", name)
	else:
		print("I guess u are not interested to play")
		print("Bye Bye", name)



			
				
						
