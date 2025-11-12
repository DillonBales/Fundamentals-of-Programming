import re
import subprocess

#only_one_error = True
only_one_error = False

allready_error = [False,False,False,False,False,False,False,False]
total_errors=0

def gradeIt(the_input, the_answers):
	global allready_error
	global total_errors
	cmd = subprocess.run(["python", "Midterm.py"], capture_output=True, input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	for i in range(len(the_answers)):
		the_answers[i] = the_answers[i].replace('\r','')

		if (allready_error[i] == False and the_answers[i] not in stdout):
			allready_error[i] = True
			total_errors += 1
			print("")
			print("")
			print("Error with input: ")
			print(the_input, end="")
			print(":")
			print("Unable to find: ")
			print("\t"+the_answers[i])
			print("in the following:")
			print(stdout)
			if(only_one_error):
				print("Tester only prints one error at a time")
				print("  You can change this on line 4 of the tester")
				print("  Change True to False")
				quit()
		if total_errors == 8:
			quit()


print ("Starting tests for Midterm")
the_input = '''Penny
11
906
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Penny we have''',
		'''For a loan amount of $906''',
		'''an interest rate of 10%''',
		'''will be $996.6''']
gradeIt(the_input, the_answers)
the_input = '''Isobel
12
7808
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Isobel we have''',
		'''For a loan amount of $7808''',
		'''an interest rate of 10%''',
		'''will be $8588.8''']
gradeIt(the_input, the_answers)
the_input = '''Charlena
28
7767
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Charlena we have''',
		'''For a loan amount of $7767''',
		'''an interest rate of 10%''',
		'''will be $8543.7''']
gradeIt(the_input, the_answers)
the_input = '''Sybille
29
4954
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Sybille we have''',
		'''For a loan amount of $4954''',
		'''an interest rate of 10%''',
		'''will be $5449.4''']
gradeIt(the_input, the_answers)
the_input = '''Maud
31
6408
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Maud we have''',
		'''For a loan amount of $6408''',
		'''an interest rate of 15%''',
		'''will be $7369.2''']
gradeIt(the_input, the_answers)
the_input = '''Annabella
38
9573
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Annabella we have''',
		'''For a loan amount of $9573''',
		'''an interest rate of 15%''',
		'''will be $11008.95''']
gradeIt(the_input, the_answers)
the_input = '''Nona
16
541
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Nona we have''',
		'''For a loan amount of $541''',
		'''an interest rate of 10%''',
		'''will be $595.1''']
gradeIt(the_input, the_answers)
the_input = '''Anetta
37
1860
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Anetta we have''',
		'''For a loan amount of $1860''',
		'''an interest rate of 15%''',
		'''will be $2139.0''']
gradeIt(the_input, the_answers)
the_input = '''Cammie
18
658
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Cammie we have''',
		'''For a loan amount of $658''',
		'''an interest rate of 10%''',
		'''will be $723.8''']
gradeIt(the_input, the_answers)
the_input = '''Janetta
7
7853
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Janetta we have''',
		'''For a loan amount of $7853''',
		'''an interest rate of 5%''',
		'''will be $8245.65''']
gradeIt(the_input, the_answers)
the_input = '''Charis
40
940
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Charis we have''',
		'''For a loan amount of $940''',
		'''an interest rate of 15%''',
		'''will be $1081.0''']
gradeIt(the_input, the_answers)
the_input = '''Consuelo
27
6015
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Consuelo we have''',
		'''For a loan amount of $6015''',
		'''an interest rate of 10%''',
		'''will be $6616.5''']
gradeIt(the_input, the_answers)
the_input = '''Joanie
13
5048
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Joanie we have''',
		'''For a loan amount of $5048''',
		'''an interest rate of 10%''',
		'''will be $5552.8''']
gradeIt(the_input, the_answers)
the_input = '''Shaina
9
1020
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Shaina we have''',
		'''For a loan amount of $1020''',
		'''an interest rate of 5%''',
		'''will be $1071.0''']
gradeIt(the_input, the_answers)
the_input = '''Romona
39
1952
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Romona we have''',
		'''For a loan amount of $1952''',
		'''an interest rate of 15%''',
		'''will be $2244.8''']
gradeIt(the_input, the_answers)
the_input = '''Lizzy
8
8282
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Lizzy we have''',
		'''For a loan amount of $8282''',
		'''an interest rate of 5%''',
		'''will be $8696.1''']
gradeIt(the_input, the_answers)
the_input = '''Milly
23
8799
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Milly we have''',
		'''For a loan amount of $8799''',
		'''an interest rate of 10%''',
		'''will be $9678.9''']
gradeIt(the_input, the_answers)
the_input = '''Ranice
1
6119
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Ranice we have''',
		'''For a loan amount of $6119''',
		'''an interest rate of 2%''',
		'''will be $6241.38''']
gradeIt(the_input, the_answers)
the_input = '''Michelina
3
4270
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Michelina we have''',
		'''For a loan amount of $4270''',
		'''an interest rate of 2%''',
		'''will be $4355.4''']
gradeIt(the_input, the_answers)
the_input = '''Carmon
14
7122
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Carmon we have''',
		'''For a loan amount of $7122''',
		'''an interest rate of 10%''',
		'''will be $7834.2''']
gradeIt(the_input, the_answers)
the_input = '''Marina
5
8535
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Marina we have''',
		'''For a loan amount of $8535''',
		'''an interest rate of 5%''',
		'''will be $8961.75''']
gradeIt(the_input, the_answers)
the_input = '''Donni
19
6617
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Donni we have''',
		'''For a loan amount of $6617''',
		'''an interest rate of 10%''',
		'''will be $7278.7''']
gradeIt(the_input, the_answers)
the_input = '''Margret
36
5271
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Margret we have''',
		'''For a loan amount of $5271''',
		'''an interest rate of 15%''',
		'''will be $6061.65''']
gradeIt(the_input, the_answers)
the_input = '''Willamina
34
5615
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Willamina we have''',
		'''For a loan amount of $5615''',
		'''an interest rate of 15%''',
		'''will be $6457.25''']
gradeIt(the_input, the_answers)
the_input = '''Sheree
22
5710
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Sheree we have''',
		'''For a loan amount of $5710''',
		'''an interest rate of 10%''',
		'''will be $6281.0''']
gradeIt(the_input, the_answers)
the_input = '''Isa
20
4021
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Isa we have''',
		'''For a loan amount of $4021''',
		'''an interest rate of 10%''',
		'''will be $4423.1''']
gradeIt(the_input, the_answers)
the_input = '''Dedra
35
2660
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Dedra we have''',
		'''For a loan amount of $2660''',
		'''an interest rate of 15%''',
		'''will be $3059.0''']
gradeIt(the_input, the_answers)
the_input = '''Anastasie
17
8964
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Anastasie we have''',
		'''For a loan amount of $8964''',
		'''an interest rate of 10%''',
		'''will be $9860.4''']
gradeIt(the_input, the_answers)
the_input = '''Emmeline
6
5030
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Emmeline we have''',
		'''For a loan amount of $5030''',
		'''an interest rate of 5%''',
		'''will be $5281.5''']
gradeIt(the_input, the_answers)
the_input = '''Stesha
10
3869
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Stesha we have''',
		'''For a loan amount of $3869''',
		'''an interest rate of 10%''',
		'''will be $4255.9''']
gradeIt(the_input, the_answers)
the_input = '''Paulina
2
6901
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Paulina we have''',
		'''For a loan amount of $6901''',
		'''an interest rate of 2%''',
		'''will be $7039.02''']
gradeIt(the_input, the_answers)
the_input = '''Laural
15
8540
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Laural we have''',
		'''For a loan amount of $8540''',
		'''an interest rate of 10%''',
		'''will be $9394.0''']
gradeIt(the_input, the_answers)
the_input = '''Dolly
21
3445
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Dolly we have''',
		'''For a loan amount of $3445''',
		'''an interest rate of 10%''',
		'''will be $3789.5''']
gradeIt(the_input, the_answers)
the_input = '''Florencia
24
5293
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Florencia we have''',
		'''For a loan amount of $5293''',
		'''an interest rate of 10%''',
		'''will be $5822.3''']
gradeIt(the_input, the_answers)
the_input = '''Queenie
4
3141
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Queenie we have''',
		'''For a loan amount of $3141''',
		'''an interest rate of 2%''',
		'''will be $3203.82''']
gradeIt(the_input, the_answers)
the_input = '''Jacquenetta
30
3601
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Jacquenetta we have''',
		'''For a loan amount of $3601''',
		'''an interest rate of 15%''',
		'''will be $4141.15''']
gradeIt(the_input, the_answers)
the_input = '''Dolley
33
8504
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Dolley we have''',
		'''For a loan amount of $8504''',
		'''an interest rate of 15%''',
		'''will be $9779.6''']
gradeIt(the_input, the_answers)
the_input = '''Marie
32
7317
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Marie we have''',
		'''For a loan amount of $7317''',
		'''an interest rate of 15%''',
		'''will be $8414.55''']
gradeIt(the_input, the_answers)
the_input = '''Cher
25
7725
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Cher we have''',
		'''For a loan amount of $7725''',
		'''an interest rate of 10%''',
		'''will be $8497.5''']
gradeIt(the_input, the_answers)
the_input = '''Leesa
26
7251
'''
the_answers = [
		'''Welcome to the Bank''',
		'''your first name''',
		'''number of years''',
		'''amount for your loan''',
		'''For you Leesa we have''',
		'''For a loan amount of $7251''',
		'''an interest rate of 10%''',
		'''will be $7976.1''']
gradeIt(the_input, the_answers)
print ("Finished testing")
