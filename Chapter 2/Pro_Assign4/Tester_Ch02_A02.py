import difflib
import subprocess
from subprocess import PIPE, STDOUT

allready_error = False
def perform(the_input, the_answer):
	global allready_error
	if (allready_error == True):
		return

	the_answer = the_answer.replace('\r','')
	cmd = subprocess.run(["python", "Ch02_A02_Story.py"], stdout=PIPE, stderr=STDOUT, input=the_input.encode())
	stdout = cmd.stdout.decode()  # bytes => str
	stdout = stdout.replace('\r','')
	try:
		startOfString = stdout.index('It was the one')
		short = stdout[startOfString::]
		if (the_answer.lower().replace('\n', '') not in stdout.lower().replace('\r','').replace('\n', '')):
			allready_error = True
			print("This doesn't seem to match exactly")
			print("")
			print('expected')
			print(the_answer)
			print()
			print('received')
			print(short)
			print("Here is a printout in an attempt to help you find what doesn't match")
			print("")
			for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, the_answer, short).get_opcodes():
				if tag != "equal":
					print (f'{the_answer[i1:i2]!r:>6} <--> {short[j1:j2]!r} somewhere close to the letters --{the_answer[i1-10:i2+10]}--')
	except ValueError as e:
		allready_error = True
		print ("It looks like you either have a syntax error or didn't start your story with the correct words")
		print("Check this carefully")
		print(stdout)

print ("Starting tests for Ch 02 Assignment 02")

the_input='''Beverlie's College
sloppiest
mapper
Nordic
binomial
vagarious
noun
torrential
tragedy
chromatin
bx
788
dadoes
versus
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Beverlie's College. The library was full of sloppiest students all glued to their books and mapper deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) Nordic. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like binomial. I began to vagarious noun.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my torrential was so exhausted that I decided to crash at tragedy. I was awoken 5 hours later by a not so friendly chromatin who was gnawing on my notes.
"bx! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 788 years and am actually a(n) dadoes.
"Oh well," I sighed. "At least I'll always be smarter than versus."
'''
perform(the_input, the_answer)
the_input='''Gabbey's College
wrapped
proponent
it
Porfirio
cab
temperate
maladaptive
Seder
pita
Damascus
7838
genteelness
Zara
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Gabbey's College. The library was full of wrapped students all glued to their books and proponent deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) it. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like Porfirio. I began to cab temperate.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my maladaptive was so exhausted that I decided to crash at Seder. I was awoken 5 hours later by a not so friendly pita who was gnawing on my notes.
"Damascus! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 7838 years and am actually a(n) genteelness.
"Oh well," I sighed. "At least I'll always be smarter than Zara."
'''
perform(the_input, the_answer)
the_input='''Adelaida's College
particularism
tapioca
burial
nymphomaniac
radioman
desperate
evaporative
creepiness
brain
scrivener
7373
Isiah
Cayuse
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Adelaida's College. The library was full of particularism students all glued to their books and tapioca deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) burial. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like nymphomaniac. I began to radioman desperate.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my evaporative was so exhausted that I decided to crash at creepiness. I was awoken 5 hours later by a not so friendly brain who was gnawing on my notes.
"scrivener! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 7373 years and am actually a(n) Isiah.
"Oh well," I sighed. "At least I'll always be smarter than Cayuse."
'''
perform(the_input, the_answer)
the_input='''Jesselyn's College
strobic
solvable
probosces
Gilead
landfall
remembrance
dandified
astrophysicist
archery
cit
6997
geosyncline
mandarin
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Jesselyn's College. The library was full of strobic students all glued to their books and solvable deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) probosces. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like Gilead. I began to landfall remembrance.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my dandified was so exhausted that I decided to crash at astrophysicist. I was awoken 5 hours later by a not so friendly archery who was gnawing on my notes.
"cit! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 6997 years and am actually a(n) geosyncline.
"Oh well," I sighed. "At least I'll always be smarter than mandarin."
'''
perform(the_input, the_answer)
the_input='''Ediva's College
plumular
desalinate
doubtless
Permian
climatic
across
fiendish
hdqrs
hiya
glob
8164
antecedent
wild
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Ediva's College. The library was full of plumular students all glued to their books and desalinate deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) doubtless. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like Permian. I began to climatic across.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my fiendish was so exhausted that I decided to crash at hdqrs. I was awoken 5 hours later by a not so friendly hiya who was gnawing on my notes.
"glob! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 8164 years and am actually a(n) antecedent.
"Oh well," I sighed. "At least I'll always be smarter than wild."
'''
perform(the_input, the_answer)
the_input='''Reba's College
reniform
synthetic
Lubbock
savoriness
taunter
tentacle
red
quanta
roadwork
watertight
7277
mystification
Pamirs
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Reba's College. The library was full of reniform students all glued to their books and synthetic deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) Lubbock. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like savoriness. I began to taunter tentacle.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my red was so exhausted that I decided to crash at quanta. I was awoken 5 hours later by a not so friendly roadwork who was gnawing on my notes.
"watertight! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 7277 years and am actually a(n) mystification.
"Oh well," I sighed. "At least I'll always be smarter than Pamirs."
'''
perform(the_input, the_answer)
the_input='''Anitra's College
stormproof
archduke
Cousteau
nickelodeon
skimp
Gujarati
tardier
wanderlust
nowt
ogler
2922
finesse
Cedric
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Anitra's College. The library was full of stormproof students all glued to their books and archduke deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) Cousteau. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like nickelodeon. I began to skimp Gujarati.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my tardier was so exhausted that I decided to crash at wanderlust. I was awoken 5 hours later by a not so friendly nowt who was gnawing on my notes.
"ogler! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 2922 years and am actually a(n) finesse.
"Oh well," I sighed. "At least I'll always be smarter than Cedric."
'''
perform(the_input, the_answer)
the_input='''Lorilee's College
kitsch
revolution
Keller
gym
rattletrap
titlist
clinking
Havel
nerve
goodhearted
8606
capitalism
kissoff
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Lorilee's College. The library was full of kitsch students all glued to their books and revolution deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) Keller. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like gym. I began to rattletrap titlist.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my clinking was so exhausted that I decided to crash at Havel. I was awoken 5 hours later by a not so friendly nerve who was gnawing on my notes.
"goodhearted! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 8606 years and am actually a(n) capitalism.
"Oh well," I sighed. "At least I'll always be smarter than kissoff."
'''
perform(the_input, the_answer)
the_input='''Sibelle's College
anastomotic
haphazardness
crosspiece
wanderings
mite
Chi
cinereous
extraterritoriality
unguent
glossily
8146
bewildering
excoriation
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Sibelle's College. The library was full of anastomotic students all glued to their books and haphazardness deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) crosspiece. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like wanderings. I began to mite Chi.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my cinereous was so exhausted that I decided to crash at extraterritoriality. I was awoken 5 hours later by a not so friendly unguent who was gnawing on my notes.
"glossily! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 8146 years and am actually a(n) bewildering.
"Oh well," I sighed. "At least I'll always be smarter than excoriation."
'''
perform(the_input, the_answer)
the_input='''Aurore's College
heinous
synopses
deodorant
ibis
Boulez
pylorus
enticing
counterexample
Alpheratz
hoary
8179
Stacey
justify
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Aurore's College. The library was full of heinous students all glued to their books and synopses deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) deodorant. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like ibis. I began to Boulez pylorus.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my enticing was so exhausted that I decided to crash at counterexample. I was awoken 5 hours later by a not so friendly Alpheratz who was gnawing on my notes.
"hoary! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 8179 years and am actually a(n) Stacey.
"Oh well," I sighed. "At least I'll always be smarter than justify."
'''
perform(the_input, the_answer)
the_input='''Wilhelmina's College
top
Bearnaise
snoopy
advocacy
thankful
thing
unpraised
conflation
uninviting
mayfly
2559
chrome
macho
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Wilhelmina's College. The library was full of top students all glued to their books and Bearnaise deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) snoopy. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like advocacy. I began to thankful thing.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my unpraised was so exhausted that I decided to crash at conflation. I was awoken 5 hours later by a not so friendly uninviting who was gnawing on my notes.
"mayfly! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 2559 years and am actually a(n) chrome.
"Oh well," I sighed. "At least I'll always be smarter than macho."
'''
perform(the_input, the_answer)
the_input='''Kettie's College
unscriptural
bactericidal
backup
roger
dozen
illness
ocherous
serendipity
cruciform
hawthorn
2548
fertile
Chantilly
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Kettie's College. The library was full of unscriptural students all glued to their books and bactericidal deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) backup. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like roger. I began to dozen illness.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my ocherous was so exhausted that I decided to crash at serendipity. I was awoken 5 hours later by a not so friendly cruciform who was gnawing on my notes.
"hawthorn! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 2548 years and am actually a(n) fertile.
"Oh well," I sighed. "At least I'll always be smarter than Chantilly."
'''
perform(the_input, the_answer)
the_input='''Bunny's College
inconsolable
primula
stucco
hummingbird
bye
tetrahedron
trochoid
have
Limousin
Onondaga
3797
SPCA
tradeswoman
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Bunny's College. The library was full of inconsolable students all glued to their books and primula deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) stucco. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like hummingbird. I began to bye tetrahedron.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my trochoid was so exhausted that I decided to crash at have. I was awoken 5 hours later by a not so friendly Limousin who was gnawing on my notes.
"Onondaga! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 3797 years and am actually a(n) SPCA.
"Oh well," I sighed. "At least I'll always be smarter than tradeswoman."
'''
perform(the_input, the_answer)
the_input='''Emiline's College
arrased
manageability
august
afflict
Wozniak
faction
droll
reader
Amazon
hoist
2636
Kendall
holiday
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Emiline's College. The library was full of arrased students all glued to their books and manageability deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) august. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like afflict. I began to Wozniak faction.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my droll was so exhausted that I decided to crash at reader. I was awoken 5 hours later by a not so friendly Amazon who was gnawing on my notes.
"hoist! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 2636 years and am actually a(n) Kendall.
"Oh well," I sighed. "At least I'll always be smarter than holiday."
'''
perform(the_input, the_answer)
the_input='''Celene's College
fancy-free
naysayer
overdrew
Utah
whereabouts
blowzy
obstinate
whorehouse
tortuousness
Hawks
3975
Mnemosyne
Kurd
'''
the_answer='''It was the one night everybody dreads, the night before finals week, at Celene's College. The library was full of fancy-free students all glued to their books and naysayer deep in energy drink cans and empty coffee cups. One desperate student even had the guts to sneak in a(n) overdrew. As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like Utah. I began to whereabouts blowzy.
Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, but my obstinate was so exhausted that I decided to crash at whorehouse. I was awoken 5 hours later by a not so friendly tortuousness who was gnawing on my notes.
"Hawks! I'm late for my first final!" I yelled. I ran to class as fast as I could, but when I got there and saw no one in class, I realized that my first final was actually a week ago and it was not Monday at all. In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for 3975 years and am actually a(n) Mnemosyne.
"Oh well," I sighed. "At least I'll always be smarter than Kurd."
'''
perform(the_input, the_answer)
print ("Finished testing - if no errors printed, that means the tests passed successfully")
