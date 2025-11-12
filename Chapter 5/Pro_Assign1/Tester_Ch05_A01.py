import difflib
import subprocess
from subprocess import PIPE, STDOUT
print ("Starting tests for Ch 05 Assignment 01")
allready_error = False
the_input='''Basic
38
No
No
No'''
the_answer='''451.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '451.98' when provided 'Basic 38 No No No' in the following")
	print(stdout)
if (allready_error == False and ('1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '451.98' (and not one of the other totals) when provided 'Basic 38 No No No' in the following")
	print(stdout)
the_input='''Basic
38
No
No
Yes'''
the_answer='''1051.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1051.97' when provided 'Basic 38 No No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1051.97' (and not one of the other totals) when provided 'Basic 38 No No Yes' in the following")
	print(stdout)
the_input='''Basic
38
No
Yes
No'''
the_answer='''576.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '576.98' when provided 'Basic 38 No Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '576.98' (and not one of the other totals) when provided 'Basic 38 No Yes No' in the following")
	print(stdout)
the_input='''Basic
38
No
Yes
Yes'''
the_answer='''1176.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1176.97' when provided 'Basic 38 No Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1176.97' (and not one of the other totals) when provided 'Basic 38 No Yes Yes' in the following")
	print(stdout)
the_input='''Basic
38
Yes
No
No'''
the_answer='''517.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '517.97' when provided 'Basic 38 Yes No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '517.97' (and not one of the other totals) when provided 'Basic 38 Yes No No' in the following")
	print(stdout)
the_input='''Basic
38
Yes
No
Yes'''
the_answer='''1117.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1117.96' when provided 'Basic 38 Yes No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1117.96' (and not one of the other totals) when provided 'Basic 38 Yes No Yes' in the following")
	print(stdout)
the_input='''Basic
38
Yes
Yes
No'''
the_answer='''642.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '642.97' when provided 'Basic 38 Yes Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '642.97' (and not one of the other totals) when provided 'Basic 38 Yes Yes No' in the following")
	print(stdout)
the_input='''Basic
38
Yes
Yes
Yes'''
the_answer='''1242.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1242.96' when provided 'Basic 38 Yes Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1242.96' (and not one of the other totals) when provided 'Basic 38 Yes Yes Yes' in the following")
	print(stdout)
the_input='''Basic
43
No
No
No'''
the_answer='''475.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '475.98' when provided 'Basic 43 No No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '475.98' (and not one of the other totals) when provided 'Basic 43 No No No' in the following")
	print(stdout)
the_input='''Basic
43
No
No
Yes'''
the_answer='''1075.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1075.97' when provided 'Basic 43 No No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1075.97' (and not one of the other totals) when provided 'Basic 43 No No Yes' in the following")
	print(stdout)
the_input='''Basic
43
No
Yes
No'''
the_answer='''600.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '600.98' when provided 'Basic 43 No Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '600.98' (and not one of the other totals) when provided 'Basic 43 No Yes No' in the following")
	print(stdout)
the_input='''Basic
43
No
Yes
Yes'''
the_answer='''1200.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1200.97' when provided 'Basic 43 No Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1200.97' (and not one of the other totals) when provided 'Basic 43 No Yes Yes' in the following")
	print(stdout)
the_input='''Basic
43
Yes
No
No'''
the_answer='''541.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '541.97' when provided 'Basic 43 Yes No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '541.97' (and not one of the other totals) when provided 'Basic 43 Yes No No' in the following")
	print(stdout)
the_input='''Basic
43
Yes
No
Yes'''
the_answer='''1141.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1141.96' when provided 'Basic 43 Yes No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1141.96' (and not one of the other totals) when provided 'Basic 43 Yes No Yes' in the following")
	print(stdout)
the_input='''Basic
43
Yes
Yes
No'''
the_answer='''666.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '666.97' when provided 'Basic 43 Yes Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '666.97' (and not one of the other totals) when provided 'Basic 43 Yes Yes No' in the following")
	print(stdout)
the_input='''Basic
43
Yes
Yes
Yes'''
the_answer='''1266.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1266.96' when provided 'Basic 43 Yes Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1266.96' (and not one of the other totals) when provided 'Basic 43 Yes Yes Yes' in the following")
	print(stdout)
the_input='''Advanced
38
No
No
No'''
the_answer='''851.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '851.98' when provided 'Advanced 38 No No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '851.98' (and not one of the other totals) when provided 'Advanced 38 No No No' in the following")
	print(stdout)
the_input='''Advanced
38
No
No
Yes'''
the_answer='''1451.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1451.97' when provided 'Advanced 38 No No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1451.97' (and not one of the other totals) when provided 'Advanced 38 No No Yes' in the following")
	print(stdout)
the_input='''Advanced
38
No
Yes
No'''
the_answer='''976.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '976.98' when provided 'Advanced 38 No Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '976.98' (and not one of the other totals) when provided 'Advanced 38 No Yes No' in the following")
	print(stdout)
the_input='''Advanced
38
No
Yes
Yes'''
the_answer='''1576.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1576.97' when provided 'Advanced 38 No Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1576.97' (and not one of the other totals) when provided 'Advanced 38 No Yes Yes' in the following")
	print(stdout)
the_input='''Advanced
38
Yes
No
No'''
the_answer='''917.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '917.97' when provided 'Advanced 38 Yes No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '917.97' (and not one of the other totals) when provided 'Advanced 38 Yes No No' in the following")
	print(stdout)
the_input='''Advanced
38
Yes
No
Yes'''
the_answer='''1517.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1517.96' when provided 'Advanced 38 Yes No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1517.96' (and not one of the other totals) when provided 'Advanced 38 Yes No Yes' in the following")
	print(stdout)
the_input='''Advanced
38
Yes
Yes
No'''
the_answer='''1042.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1042.97' when provided 'Advanced 38 Yes Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1042.97' (and not one of the other totals) when provided 'Advanced 38 Yes Yes No' in the following")
	print(stdout)
the_input='''Advanced
38
Yes
Yes
Yes'''
the_answer='''1642.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1642.96' when provided 'Advanced 38 Yes Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1642.96' (and not one of the other totals) when provided 'Advanced 38 Yes Yes Yes' in the following")
	print(stdout)
the_input='''Advanced
43
No
No
No'''
the_answer='''875.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '875.98' when provided 'Advanced 43 No No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '875.98' (and not one of the other totals) when provided 'Advanced 43 No No No' in the following")
	print(stdout)
the_input='''Advanced
43
No
No
Yes'''
the_answer='''1475.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1475.97' when provided 'Advanced 43 No No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1475.97' (and not one of the other totals) when provided 'Advanced 43 No No Yes' in the following")
	print(stdout)
the_input='''Advanced
43
No
Yes
No'''
the_answer='''1000.98'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1000.98' when provided 'Advanced 43 No Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1000.98' (and not one of the other totals) when provided 'Advanced 43 No Yes No' in the following")
	print(stdout)
the_input='''Advanced
43
No
Yes
Yes'''
the_answer='''1600.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1600.97' when provided 'Advanced 43 No Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1600.97' (and not one of the other totals) when provided 'Advanced 43 No Yes Yes' in the following")
	print(stdout)
the_input='''Advanced
43
Yes
No
No'''
the_answer='''941.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '941.97' when provided 'Advanced 43 Yes No No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '1541.96' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '941.97' (and not one of the other totals) when provided 'Advanced 43 Yes No No' in the following")
	print(stdout)
the_input='''Advanced
43
Yes
No
Yes'''
the_answer='''1541.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1541.96' when provided 'Advanced 43 Yes No Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1066.97' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1541.96' (and not one of the other totals) when provided 'Advanced 43 Yes No Yes' in the following")
	print(stdout)
the_input='''Advanced
43
Yes
Yes
No'''
the_answer='''1066.97'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1066.97' when provided 'Advanced 43 Yes Yes No' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1666.96' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1066.97' (and not one of the other totals) when provided 'Advanced 43 Yes Yes No' in the following")
	print(stdout)
the_input='''Advanced
43
Yes
Yes
Yes'''
the_answer='''1666.96'''
the_answer = the_answer.replace('\r','')
cmd = subprocess.run(["python", "Ch05_A01_computer_purchase.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
stdout = cmd.stdout.decode()  # bytes => str
merged = stdout.lower().replace('\r','').replace('\n', ' ')
if (allready_error == False and the_answer.lower().replace('\r','').replace('\n', ' ') not in merged):
	allready_error = True
	print("Error: Expected to find the total of '1666.96' when provided 'Advanced 43 Yes Yes Yes' in the following")
	print(stdout)
if (allready_error == False and ('451.98' in merged or '1051.97' in merged or '576.98' in merged or '1176.97' in merged or '517.97' in merged or '1117.96' in merged or '642.97' in merged or '1242.96' in merged or '475.98' in merged or '1075.97' in merged or '600.98' in merged or '1200.97' in merged or '541.97' in merged or '1141.96' in merged or '666.97' in merged or '1266.96' in merged or '851.98' in merged or '1451.97' in merged or '976.98' in merged or '1576.97' in merged or '917.97' in merged or '1517.96' in merged or '1042.97' in merged or '1642.96' in merged or '875.98' in merged or '1475.97' in merged or '1000.98' in merged or '1600.97' in merged or '941.97' in merged or '1541.96' in merged or '1066.97' in merged or False == True)):
	allready_error = True
	print("I only expected to find the total of '1666.96' (and not one of the other totals) when provided 'Advanced 43 Yes Yes Yes' in the following")
	print(stdout)
print ("Finished testing - if no errors printed, that means the tests passed successfully")
