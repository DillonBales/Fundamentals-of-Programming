import difflib
import subprocess
from subprocess import PIPE, STDOUT
print ("Starting tests for Ch 05 Assignment 02")
allready_error = False
if allready_error == False:
	the_input='''92.44364434541046'''
	the_answer='''is a(n) A-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A-.' when provided '92.44364434541046' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A-.' (and not one of the other answers) when provided '92.44364434541046' in the following")
		print(stdout)
if allready_error == False:
	the_input='''79.26489513771408'''
	the_answer='''is a(n) C+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C+.' when provided '79.26489513771408' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C+.' (and not one of the other answers) when provided '79.26489513771408' in the following")
		print(stdout)
if allready_error == False:
	the_input='''93.78621737194246'''
	the_answer='''is a(n) A-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A-.' when provided '93.78621737194246' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A-.' (and not one of the other answers) when provided '93.78621737194246' in the following")
		print(stdout)
if allready_error == False:
	the_input='''70.47850957105035'''
	the_answer='''is a(n) C-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C-.' when provided '70.47850957105035' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C-.' (and not one of the other answers) when provided '70.47850957105035' in the following")
		print(stdout)
if allready_error == False:
	the_input='''72.30839126710272'''
	the_answer='''is a(n) C-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C-.' when provided '72.30839126710272' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C-.' (and not one of the other answers) when provided '72.30839126710272' in the following")
		print(stdout)
if allready_error == False:
	the_input='''85.31163095637486'''
	the_answer='''is a(n) B.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B.' when provided '85.31163095637486' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B.' (and not one of the other answers) when provided '85.31163095637486' in the following")
		print(stdout)
if allready_error == False:
	the_input='''84.1280174242955'''
	the_answer='''is a(n) B.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B.' when provided '84.1280174242955' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B.' (and not one of the other answers) when provided '84.1280174242955' in the following")
		print(stdout)
if allready_error == False:
	the_input='''68.67981903721478'''
	the_answer='''is a(n) D+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D+.' when provided '68.67981903721478' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D+.' (and not one of the other answers) when provided '68.67981903721478' in the following")
		print(stdout)
if allready_error == False:
	the_input='''87.37023646869821'''
	the_answer='''is a(n) B+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B+.' when provided '87.37023646869821' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B+.' (and not one of the other answers) when provided '87.37023646869821' in the following")
		print(stdout)
if allready_error == False:
	the_input='''65.11788706391307'''
	the_answer='''is a(n) D.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D.' when provided '65.11788706391307' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D.' (and not one of the other answers) when provided '65.11788706391307' in the following")
		print(stdout)
if allready_error == False:
	the_input='''69.39069620282561'''
	the_answer='''is a(n) D+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D+.' when provided '69.39069620282561' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D+.' (and not one of the other answers) when provided '69.39069620282561' in the following")
		print(stdout)
if allready_error == False:
	the_input='''71.09390909725536'''
	the_answer='''is a(n) C-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C-.' when provided '71.09390909725536' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C-.' (and not one of the other answers) when provided '71.09390909725536' in the following")
		print(stdout)
if allready_error == False:
	the_input='''7.126352222352206'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '7.126352222352206' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '7.126352222352206' in the following")
		print(stdout)
if allready_error == False:
	the_input='''76.3273277665989'''
	the_answer='''is a(n) C.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C.' when provided '76.3273277665989' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C.' (and not one of the other answers) when provided '76.3273277665989' in the following")
		print(stdout)
if allready_error == False:
	the_input='''73.2492139429743'''
	the_answer='''is a(n) C-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C-.' when provided '73.2492139429743' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C-.' (and not one of the other answers) when provided '73.2492139429743' in the following")
		print(stdout)
if allready_error == False:
	the_input='''95.44372298971308'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '95.44372298971308' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '95.44372298971308' in the following")
		print(stdout)
if allready_error == False:
	the_input='''7.826173190523329'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '7.826173190523329' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '7.826173190523329' in the following")
		print(stdout)
if allready_error == False:
	the_input='''67.71945494689778'''
	the_answer='''is a(n) D+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D+.' when provided '67.71945494689778' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D+.' (and not one of the other answers) when provided '67.71945494689778' in the following")
		print(stdout)
if allready_error == False:
	the_input='''64.07524827156742'''
	the_answer='''is a(n) D.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D.' when provided '64.07524827156742' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D.' (and not one of the other answers) when provided '64.07524827156742' in the following")
		print(stdout)
if allready_error == False:
	the_input='''99.14346376118377'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '99.14346376118377' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '99.14346376118377' in the following")
		print(stdout)
if allready_error == False:
	the_input='''35.33418090905598'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '35.33418090905598' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '35.33418090905598' in the following")
		print(stdout)
if allready_error == False:
	the_input='''86.78726268225616'''
	the_answer='''is a(n) B.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B.' when provided '86.78726268225616' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B.' (and not one of the other answers) when provided '86.78726268225616' in the following")
		print(stdout)
if allready_error == False:
	the_input='''82.02600917407881'''
	the_answer='''is a(n) B-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B-.' when provided '82.02600917407881' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B-.' (and not one of the other answers) when provided '82.02600917407881' in the following")
		print(stdout)
if allready_error == False:
	the_input='''78.78469044629455'''
	the_answer='''is a(n) C+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C+.' when provided '78.78469044629455' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C+.' (and not one of the other answers) when provided '78.78469044629455' in the following")
		print(stdout)
if allready_error == False:
	the_input='''98.7862019299834'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '98.7862019299834' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '98.7862019299834' in the following")
		print(stdout)
if allready_error == False:
	the_input='''34.46852155993016'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '34.46852155993016' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '34.46852155993016' in the following")
		print(stdout)
if allready_error == False:
	the_input='''91.02476300325748'''
	the_answer='''is a(n) A-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A-.' when provided '91.02476300325748' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A-.' (and not one of the other answers) when provided '91.02476300325748' in the following")
		print(stdout)
if allready_error == False:
	the_input='''90.89728311719625'''
	the_answer='''is a(n) A-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A-.' when provided '90.89728311719625' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A-.' (and not one of the other answers) when provided '90.89728311719625' in the following")
		print(stdout)
if allready_error == False:
	the_input='''61.21968662367191'''
	the_answer='''is a(n) D-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D-.' when provided '61.21968662367191' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D-.' (and not one of the other answers) when provided '61.21968662367191' in the following")
		print(stdout)
if allready_error == False:
	the_input='''58.93332975610837'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '58.93332975610837' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '58.93332975610837' in the following")
		print(stdout)
if allready_error == False:
	the_input='''74.05802351000034'''
	the_answer='''is a(n) C.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C.' when provided '74.05802351000034' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C.' (and not one of the other answers) when provided '74.05802351000034' in the following")
		print(stdout)
if allready_error == False:
	the_input='''36.61602194472421'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '36.61602194472421' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '36.61602194472421' in the following")
		print(stdout)
if allready_error == False:
	the_input='''75.83731131723926'''
	the_answer='''is a(n) C.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C.' when provided '75.83731131723926' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C.' (and not one of the other answers) when provided '75.83731131723926' in the following")
		print(stdout)
if allready_error == False:
	the_input='''97.8503859264798'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '97.8503859264798' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '97.8503859264798' in the following")
		print(stdout)
if allready_error == False:
	the_input='''89.91373239629326'''
	the_answer='''is a(n) B+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B+.' when provided '89.91373239629326' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B+.' (and not one of the other answers) when provided '89.91373239629326' in the following")
		print(stdout)
if allready_error == False:
	the_input='''80.37995345190379'''
	the_answer='''is a(n) B-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B-.' when provided '80.37995345190379' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B-.' (and not one of the other answers) when provided '80.37995345190379' in the following")
		print(stdout)
if allready_error == False:
	the_input='''77.38295695094543'''
	the_answer='''is a(n) C+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) C+.' when provided '77.38295695094543' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) C+.' (and not one of the other answers) when provided '77.38295695094543' in the following")
		print(stdout)
if allready_error == False:
	the_input='''81.56017320069307'''
	the_answer='''is a(n) B-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B-.' when provided '81.56017320069307' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B-.' (and not one of the other answers) when provided '81.56017320069307' in the following")
		print(stdout)
if allready_error == False:
	the_input='''15.606077631298795'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '15.606077631298795' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '15.606077631298795' in the following")
		print(stdout)
if allready_error == False:
	the_input='''94.07625216669238'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '94.07625216669238' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '94.07625216669238' in the following")
		print(stdout)
if allready_error == False:
	the_input='''96.10085240779816'''
	the_answer='''is a(n) A.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) A.' when provided '96.10085240779816' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) A.' (and not one of the other answers) when provided '96.10085240779816' in the following")
		print(stdout)
if allready_error == False:
	the_input='''66.83176543419144'''
	the_answer='''is a(n) D.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D.' when provided '66.83176543419144' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D.' (and not one of the other answers) when provided '66.83176543419144' in the following")
		print(stdout)
if allready_error == False:
	the_input='''33.144936716733525'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '33.144936716733525' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '33.144936716733525' in the following")
		print(stdout)
if allready_error == False:
	the_input='''38.991835772533335'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '38.991835772533335' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '38.991835772533335' in the following")
		print(stdout)
if allready_error == False:
	the_input='''62.03048941982024'''
	the_answer='''is a(n) D-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D-.' when provided '62.03048941982024' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D-.' (and not one of the other answers) when provided '62.03048941982024' in the following")
		print(stdout)
if allready_error == False:
	the_input='''27.24773250727474'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '27.24773250727474' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '27.24773250727474' in the following")
		print(stdout)
if allready_error == False:
	the_input='''60.81994522834068'''
	the_answer='''is a(n) F.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) F.' when provided '60.81994522834068' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) F.' (and not one of the other answers) when provided '60.81994522834068' in the following")
		print(stdout)
if allready_error == False:
	the_input='''83.81341021678728'''
	the_answer='''is a(n) B-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B-.' when provided '83.81341021678728' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B-.' (and not one of the other answers) when provided '83.81341021678728' in the following")
		print(stdout)
if allready_error == False:
	the_input='''88.52797647029055'''
	the_answer='''is a(n) B+.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) B+.' when provided '88.52797647029055' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) D-.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) B+.' (and not one of the other answers) when provided '88.52797647029055' in the following")
		print(stdout)
if allready_error == False:
	the_input='''63.45173107428305'''
	the_answer='''is a(n) D-.'''
	cmd = subprocess.run(["python", "Ch05_A02_grade_converter.py"], stdout=PIPE, stderr=STDOUT,  input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	merged = stdout.replace('\r','').replace('\n', ' ')
	if (allready_error == False and the_answer not in merged):
		allready_error = True
		print("Expected to find 'is a(n) D-.' when provided '63.45173107428305' in the following")
		print(stdout)
	if (allready_error == False and (
'is a(n) A.'in merged or 'is a(n) A-.'in merged or 'is a(n) B+.'in merged or 'is a(n) B.'in merged or 'is a(n) B-.'in merged or 'is a(n) C+.'in merged or 'is a(n) C.'in merged or 'is a(n) C-.'in merged or 'is a(n) D+.'in merged or 'is a(n) D.'in merged or 'is a(n) F.'in merged or False == True)):
		allready_error = True
		print("I only expected to find 'is a(n) D-.' (and not one of the other answers) when provided '63.45173107428305' in the following")
		print(stdout)
print ("Finished testing - if no errors printed, that means the tests passed successfully")
