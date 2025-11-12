
# data is in the format (name, type, description)
def print_names(data):
   print("printing names")
   for row in data:
      print(row[0])

def print_types(data):
   print("printing types")
   for row in data:
      print(row[1])

def print_description(data):
   print("printing descriptions")
   for row in data:
      print(row[2])

def print_wizards(data):
   print("printing wizards with their descriptions")
   for row in data:
      if row[1] == "Wizard":
         print(row[0], row[2])

def create_variables_for_Luna(data):
   for row in data:
      if(row[0] == "Luna Lovegood"):
         name,title,desc = row
         print_wizard(name, title, desc)

def print_wizard(a,b,c):
   print("Name: {0}, Type: {1}, Description: {2}".format(a,b,c))   

def print_things(d):
  # print_names(d)
   # print_types(d)
   # print_description(d)
   # print_wizards(d)
   create_variables_for_Luna(d)

data = (
('''Regulus Arcturus Black''', '''Wizard''', '''Brother of Sirius. Used to be a Death Eater but defected.'''), 
('''Sirius Black''', '''Wizard''', '''Best friend of James Potter and godfather of Harry.'''),      
('''Lavender Brown''', '''Wizard''', '''Killed by a werewolf. She was a gryffindor student who dated Ron. '''), 
('''Cho Chang''', '''Wizard''', '''Ravenclaw student who dated Cedric Diggory and Harry Potter.'''), 
('''Vincent Crabbe Sr.''', '''Wizard''', '''Father of Crabbe and death-eater who escaped Azkaban.'''), 
('''Vincent Crabbe''', '''Wizard''', '''Slytherin student who was best friends with Goyle and followed Draco.'''), 
('''Bartemius "Barty" Crouch Sr.''', '''Wizard''', '''Head of the department of Internation Magical 
Cooperation. Killed by his son.'''), 
('''Bartemius "Barty" Crouch Jr.''', '''Wizard''', '''Death Eater who impersonated Alastor Moody.'''),
('''Fleur Delacour''', '''Wizard''', '''Participated in the Triwizard tournament and married Bill Weasley.'''),
('''Cedric Diggory''', '''Wizard''', '''Participated in the Triwizard tournament and got killed by Voldemort.'''),
('''Alberforth Dumbledore''', '''Wizard''', '''Albus' brother and owner of Hog's Head.'''),
('''Albus Dumbledore''', '''Wizard''', '''Headmaster of Hogwards killed by Snape.'''),
('''Dudley Dursley''', '''Muggle''', '''Muggle son of Vernon and Petunia and first-cousin of Harry.'''),
('''Petunia Dursley''', '''Muggle''', '''Harry's aunt and sister of Lily.'''),
('''Vernon Dursley''', '''Muggle''', '''Harry's muggle uncle.'''),
('''Argus Filch''', '''Squib''', '''Squib caretake of Hogwards.'''),
('''Seamus Finnigan''', '''Wizard''', '''Harry's friend and member of Dumbledore's army.'''),       
('''Nicolas Flamel''', '''Wizard''', '''Creator of the Philosopher's Stone.'''),
('''Cornelius Fudge''', '''Wizard''', '''Minister of Magic that was forced to resign.'''),
('''Goyle Sr.''', '''Wizard''', '''Death Eater and father of Gregory Goyle.'''),
('''Gregory Goyle''', '''Wizard''', '''Best friend of Crabbe. Slytherin student and dies by falling 
into Fiendfyre.'''),
('''Hermione Granger''', '''Wizard''', '''One of Harry's best friend and marries Ron Weasley.'''),  
('''Rubeus Hagrid''', '''Wizard''', '''Half-giant who loves Harry. He was the keeper of Keys and Grounds at Hogwards.'''),
('''Igor Karkaroff''', '''Wizard''', '''Highmaster of Durmstrang and reformed death-eater.'''),     
('''Viktor Krum''', '''Wizard''', '''Participant in the Triwizard tournament. Dated Hermione.'''),  
('''Bellatrix Lestrange''', '''Wizard''', '''Death Eater who was killed by Molly Weasley.'''),      
('''Alice Longbottom''', '''Wizard''', '''Mother of Neville who was tortured by Bellatrix.'''),     
('''Frank Longbottom''', '''Wizard''', '''Father of Neville who was tortured by Bellatrix.'''),     
('''Neville Longbottom''', '''Wizard''', '''Gryffindor student who was a member of Dumbledore's army.'''),
('''Luna Lovegood''', '''Wizard''', '''Ravenclaw student who was a member of Dumbledore's army.'''),
('''Xenophilius Lovegood''', '''Wizard''', '''Father of Luna and editor of The Quibbler.'''),       
('''Remus Lupin''', '''Wizard''', '''Friend of James Potter and werewolf. He married Nymphadora.'''),
('''Draco Malfoy''', '''Wizard''', '''Slytherin student who had many arguments with Harry.'''),     
('''Lucius Malfoy''', '''Wizard''', '''Father of Draco and influential Death-Eater.'''),
('''Narcissa Malfoy''', '''Wizard''', '''Mother of Draco and sister of Bellatrix.'''),
('''Olympe Maxime''', '''Wizard''', '''Half-giantess and headmistress of Beauxbatons.'''),
('''Minerva McGonagall''', '''Wizard''', '''Professor of Transfiguration and head of Gryffindor.'''),
('''Alastor "Mad-Eye" Moody''', '''Wizard''', '''Retired auror and member of the order of the Phoenix. Killed by Voldemort.'''),
('''Peter Pettigrew''', '''Wizard''', '''Betrays James and Lily Potter. Follower of Voldemort.'''), 
('''Harry Potter''', '''Wizard''', '''The boy who lived. Main character of the series.'''),
('''James Potter''', '''Wizard''', '''Father of Harry. Murdered by Voldemort.'''),
('''Lily Potter''', '''Wizard''', '''Mother of Harry. Murdered by Voldemort.'''),
('''Quirinus Quirrell''', '''Wizard''', '''Possessed by Voldemort. Defence against the Dark Arts professor.'''),
('''Tom Riddle Sr.''', '''Muggle''', '''Muggle father of Voldemort who was killed by him.'''),      
('''Mary Riddle''', '''Muggle''', '''Muggle mother of Voldemort who was killed by him.'''),
('''Lord Voldemort''', '''Wizard''', '''The antagonist of the series who murdered many.'''),        
('''Rita Skeeter''', '''Wizard''', '''Reporter at the Daily Prophet.'''),
('''Severus Snape''', '''Wizard''', '''Head of the Slytherin house and saved Harry in many occasions.'''),
('''Nymphadora Tonks''', '''Wizard''', '''Married Remus Lupin and was killed by Bellatrix.'''),     
('''Dolores Janes Umbridge''', '''Wizard''', '''Senior undersecretary to the Ministry of Magic. Eventually sent to Azkaban.'''),
('''Arthur Weasley''', '''Wizard''', '''Father of the Weasleys and member of the Order of the Phoenix.'''),
('''Bill Weasley''', '''Wizard''', '''Oldest son of Arthur and Molly. Husband of Fleur. '''),       
('''Charlie Weasley''', '''Wizard''', '''Second son of Arthur and Molly. Works with dragons in Romania.'''),
('''Fred Weasley''', '''Wizard''', '''Identical twin with George and co-owner of Weasleys' Wizard Wheezes'''),
('''George Weasley''', '''Wizard''', '''Identical twin with Fred and co-owner of Weasleys' Wizard Wheezes'''),
('''Ginny Weasley''', '''Wizard''', '''Marries Harry Potter and only daughter of Molly and Arthur.'''),
('''Molly Weasley''', '''Wizard''', '''Wife of Arthur and mother of the Weasleys. Kills Bellatrix.'''),
('''Percy Weasley''', '''Wizard''', '''Third son of Arthur and Molly. He is a Gryffindor prefect.'''),
('''Ron Weasley''', '''Wizard''', '''Harry's best friend. Marries Hermione.'''),
('''Dobby''', '''Elf''', '''House elf and friend of Harry. He is killed by Bellatrix.'''),
('''Fluffy''', '''Monster''', '''Three-headed dog belonging to Rubeus Hagrid.'''),
('''Hedwig''', '''Owl''', '''Harry's owl.'''),
('''Moaning Myrtle''', '''Ghost''', '''Ghost at Hogwards.'''),
('''Aragog''', '''Acromantula''', '''Acromantula belonging to Rubeus Hagrid.'''),
('''Grawp''', '''Giant''', '''Giant-half brother of Hagrid.''')
)


print_things(data)