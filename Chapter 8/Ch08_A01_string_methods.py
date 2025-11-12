import sys

def paragraph_analysis(a):
    word_count = 0
    e_count = 0

    for word in a.split():
        word_count = word_count + 1
        for i in word:
            if i == "e":
                e_count = e_count + 1
                break
            
    e_percent = str(int(((e_count / word_count) * 100) // 1))

    return f"""Your text contains {word_count} words, of which {e_count} ({e_percent}%) contain(s) an "e"."""


def reverse(a):
    reversed_word = ""
    
    for letter in a:
        reversed_word = letter + reversed_word
    
    return reversed_word


def remove_letter(string, letter):
    removed_word = ""

    for i in string:
        if i != letter:
            removed_word = removed_word + i
    
    return removed_word


def remove_string(string, letter):
    
    new_string = string.replace(letter, "")

    return new_string


already_printed_error = False
def test(did_pass, expected, given):
    global already_printed_error
    """ Print the result of a test. """
    
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        if already_printed_error == False:
            msg = ("Test at line {0} FAILED.".format(linenum))
            print(msg)
            print("\tExpected: "+ str(expected))
            print("\tgiven   : "+ str(given))
            print("Tester only prints a single error - there may be more")
            already_printed_error = True

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("Starting tests")
    #Add your tests here
    
    p = '''There once was a man named Richard '''
    e = '''Your text contains 7 words, of which 3 (42%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)

    p = '''funny'''
    e = '''ynnuf'''
    a = reverse(p)
    test(a == e,e,a)

    p = '''There once was a man named Richard '''
    e = '''Thr onc was a man namd Richard '''
    a = remove_letter(p, 'e')
    test(a == e,e,a)

    p = '''There once was a man named Richard '''
    e = '''There once was a named Richard '''
    a = remove_string(p, 'man ')
    test(a == e,e,a)


    #Dr B's tests follow:
    global already_printed_error
    p = '''Yemenite exerciser atonement hack truncate Maxine Gonzales 
motorway regardless Connemara Bannister Chattanooga weightless helicopter Friedman herniation cab politburo 
secretary contact parish TA cite goldbrick hacienda walnut 
4 solvent adsorb bandeau Odyssey etching '''
    e = '''Your text contains 32 words, of which 20 (62%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''aptness abjuratory conceptualization entombment mannerly Montserrat misguided injection routine Tibet accessibly zone's pulley Orwellian gluten eavesdropped Irrawaddy 
Kafka forenoon Sheffield 
lacquer undergarment unconscionable botanic 
Tuscarora pasteurized kilowatt invasion meritocracy supersede '''
    e = '''Your text contains 30 words, of which 23 (76%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''bobsled Cumberland malice 
Fran transpacific Swanee dicta perceptual documentation caving Eratosthenes Lanai propitiation sailboard darner Riley 
speedway '''
    e = '''Your text contains 17 words, of which 10 (58%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''Cozumel resumption irradiate rood colorize Fields pp economist Thoreau Lyle resole suddenness pompadour overlong bopping 
fathomless dentition Hecate delighted inexplicably gram 
bondsman slapped tagged Onondaga 
croupy VGA Agricola Argos 
'''
    e = '''Your text contains 29 words, of which 18 (62%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''demolish objector sextant Chandigarh joylessness staunch dumbwaiter antivivisectionist 
leastwise Ruthie stateroom 
speculative bear Dixieland phat broadness feet dynamiter piggery popular rpm redye fill's fail forest Bradshaw warship wolfram blaster '''
    e = '''Your text contains 29 words, of which 19 (65%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''Gray truncation imposition loll heroin fictional hemlock Peruvian tentative xerographic Lyme huge accumulation bloc slingshot Pitt Poisson Shackleton ceramics Krishna offshoot foreboding foreknew votary Hauptmann overweening Ahriman '''
    e = '''Your text contains 27 words, of which 12 (44%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''causer Schultz recherche passe colorblindness radiographer imponderable hairsbreadth advise meany consultative Cameroonian pointed 
jalousie downrange compelled consolatory 
cravat frivolous titmice Mencken unease 
Caliban Pickford Americanize certainty Pantheon deckhand Gypsy twirl pinkness responsible hypothermia Godspeed '''
    e = '''Your text contains 34 words, of which 26 (76%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''accolade cross's apposite transitive Shaw integer Macintosh Pacheco eruption WAC pawn doc frizz toerag peninsula Hartford markdown editor wedded rhymester wimple 
Carborundum corporatism briefcase trap borscht shipments westward Austin fence geophysical Pleistocene '''
    e = '''Your text contains 32 words, of which 18 (56%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''Caruso knowing sparred Serbian majesty patronizing Boadicea wouldn't thong dinette 
anchorwoman lay Zomba snowbank tutorship ripen minicab tightener 
frame subsequent symmetrical 
transducer 
seismologist superfluity packaging astern '''
    e = '''Your text contains 26 words, of which 14 (53%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''transcendent 
choreograph nodal hazily pullout then 
whizzbang Kochab tomato innervate tandem Cantor gagged instruction saute 
sec '''
    e = '''Your text contains 16 words, of which 8 (50%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''Khyber thudding interrupter Farrakhan wish tuxedo charlatanism 
timothy bony redcurrant denture schnook furbelow homeostasis finder osier adhesiveness counselor tribeswoman brazier wreak pedagogue slab bare Knievel statehouse type toadded 
meteoric bilge brushstroke terrorize '''
    e = '''Your text contains 32 words, of which 24 (75%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''overlapped ricer dimness fancy theism satisfying cope appreciatory hustler bellwether hatband limo 
Best cardamom modernness backfire 
chyme malocclusion spinster cubist '''
    e = '''Your text contains 20 words, of which 13 (65%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''poop monomaniac housefly equilateral alumina putrescence terrible collision dromedary Castlereagh swigging Omaha salmonellae stringy schoolmistress silkworm bruiser '''
    e = '''Your text contains 17 words, of which 9 (52%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''subprogram Workman Julius backslapping 
cannibalize Epimethius Caspar Haida Berra d 
gratitude complainer Ubangi EDP burn tremor 
weevil preregistration changer plumber preservation tillage '''
    e = '''Your text contains 22 words, of which 12 (54%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''schoolmate yob Vang Axis fringe's parentage clutter bloodhound Denali conceptualize constitutional cleanse innit permutation go 
dessertspoon 
CBC Hanoverian 
tamoxifen capo collateral Saab microphone tonality 
Bennett waltz venerate peculate Arneb '''
    e = '''Your text contains 29 words, of which 17 (58%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''striking negritude Stefan pitchblende sixths Soyuz Dorian Sargent Vienna sect assure numbered officiant GHz Left wrasse cadre sandman chive trouncer gunboat romancer helping murmuring polymer legal Dortmund image 
steersman intrinsic 
nonobligatory hyperthyroid schoolmarm fell '''
    e = '''Your text contains 34 words, of which 21 (61%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''biosphere swanned gregariousness labium irritability Qom traversal mosey superstar prehistoric lovableness decennial scurvy permanent psychodrama Iraqi headscarves Australopithecus amazing Chesapeake okra gormandizer novene WA footpaths prosecution europium Esquire codfish wrestler emirate overrode ovation Klan '''
    e = '''Your text contains 34 words, of which 21 (61%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''muggy subconscious grittiness Addams cornet spatial crotchet slim cultural conquistador bookshelf Gregorio sally multilingualism periwig PM 
pegged indolence embolden practitioner histrionic tutu insightful pumice razz locution '''
    e = '''Your text contains 26 words, of which 11 (42%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''populist daylong pieceworker magnetism Yesenia derisiveness plebby collate network Honduran Edam affinity readability webcam civet Bernoulli Janell ironical garrulous brougham Reginae subscript '''
    e = '''Your text contains 22 words, of which 13 (59%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    p = '''polymorphic litmus Abram IMNSHO Goiania gunwale excellency gorge schmo Dartmoor mezzo expiatory trendsetting retro batten Buber bearing 
'''
    e = '''Your text contains 17 words, of which 10 (58%) contain(s) an "e".'''
    a = paragraph_analysis(p)
    test(a == e,e,a)
    already_printed_error = False
    p = '''dysprosium'''
    e = '''muisorpsyd'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''mayo'''
    e = '''oyam'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''catchphrase'''
    e = '''esarhphctac'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''stroppy'''
    e = '''ypports'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''operation'''
    e = '''noitarepo'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''Bolshevist'''
    e = '''tsivehsloB'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''veritably'''
    e = '''ylbatirev'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''Gestapo'''
    e = '''opatseG'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''sweetening'''
    e = '''gnineteews'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''barker'''
    e = '''rekrab'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''amend'''
    e = '''dnema'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''indulge'''
    e = '''egludni'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''styli'''
    e = '''ilyts'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''indelibly'''
    e = '''ylbiledni'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''Loki'''
    e = '''ikoL'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''eat'''
    e = '''tae'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''char'''
    e = '''rahc'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''babysitter'''
    e = '''rettisybab'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''erythrocyte'''
    e = '''etycorhtyre'''
    a = reverse(p)
    test(a == e,e,a)
    p = '''gentlefolks'''
    e = '''sklofeltneg'''
    a = reverse(p)
    test(a == e,e,a)
    already_printed_error = False
    p = '''Mixtec apish lowbrow Douala sentimental Bessel Francine undercoating Polyphemus iniquitous bred cancellation hosepipe implore gibbet inamorata anomaly whom Ouagadougou manslaughter SIDS patellae inhibition counterattack deterred WWW ragwort lithesome outrage Short Kremlinologist '''
    e = '''Mixtec apish lowbrow Doala sentimental Bessel Francine ndercoating Polyphems iniqitos bred cancellation hosepipe implore gibbet inamorata anomaly whom Oagadogo manslaghter SIDS patellae inhibition conterattack deterred WWW ragwort lithesome otrage Short Kremlinologist '''
    a = remove_letter(p, 'u')
    test(a == e,e,a)
    p = '''icebox aberrant stepsister backstair Oklahoma macerate misalliance chock Caterpillar pylon news backseat aversion fuggy Stromboli dichotomy socialize customarily sapsucker eye Hasidim featherweight dido midshipmen gangsta journeyer fate enthrone honor Leonid cloister snowplow '''
    e = '''icebox aberran sepsiser backsair Oklahoma macerae misalliance chock Caerpillar pylon news backsea aversion fuggy Sromboli dichoomy socialize cusomarily sapsucker eye Hasidim feaherweigh dido midshipmen gangsa journeyer fae enhrone honor Leonid cloiser snowplow '''
    a = remove_letter(p, 't')
    test(a == e,e,a)
    p = '''aural capricious musician divided vast crushing upstroke derivation susceptible encephalitic woody depressurization leaning eradicator autocracy ticker process echinoderm gainful Barclay competences '''
    e = '''aural capricious musician divided vast crushing upstroke derivation susceptible encephalitic woody depressurization leaning eradicator autocracy ticker process echinoderm gainful Barclay competences '''
    a = remove_letter(p, 'q')
    test(a == e,e,a)
    p = '''numerable cockpit Swed preeminent piteousness hybridization leftmost midair Ehrenberg detente despair cellular passably Greeley vendible plagiarize oafishness frosty spiffy upend playacting overweight '''
    e = '''numerable cockpit Swed preeminent piteousness hybridization letmost midair Ehrenberg detente despair cellular passably Greeley vendible plagiarize oaishness rosty spiy upend playacting overweight '''
    a = remove_letter(p, 'f')
    test(a == e,e,a)
    p = '''integument enlist Squibb BPOE satiable bx mopped septuagenarian chosen Latisha ulnar primal shampooer delta factious heppest hind antagonist cropped qty Stimson genitive antidepressant heat wily quail liveryman disconsolate Frye colloquial outgrown span loader '''
    e = '''inegumen enlis Squibb BPOE saiable bx mopped sepuagenarian chosen Laisha ulnar primal shampooer dela facious heppes hind anagonis cropped qy Simson geniive anidepressan hea wily quail liveryman disconsolae Frye colloquial ougrown span loader '''
    a = remove_letter(p, 't')
    test(a == e,e,a)
    p = '''genus janitor beeswax painter dodder duck molter blowup superstitious automatic omnivorousness punishment cortex intern Kommunizma detected mycologist appointment's gnocchi Gareth linens manque Rhine migrant dewiness sensationalism herniate varsity Bose charioteer Gotham '''
    e = '''genus janitor beeswax painter dodder duck molter blowup superstitious automatic omnivorousness punishment cortex intern Kommunizma detected mcologist appointment's gnocchi Gareth linens manque Rhine migrant dewiness sensationalism herniate varsit Bose charioteer Gotham '''
    a = remove_letter(p, 'y')
    test(a == e,e,a)
    p = '''winch simplistically patty puncher peach Schroeder blackball wheat bushmen sealer helpful elate crabwise rakishness curricular telex concubinage sou vincible deflation mensuration paradigm raiser Lie aristocrat bonding '''
    e = '''inch simplistically patty puncher peach Schroeder blackball heat bushmen sealer helpful elate crabise rakishness curricular telex concubinage sou vincible deflation mensuration paradigm raiser Lie aristocrat bonding '''
    a = remove_letter(p, 'w')
    test(a == e,e,a)
    p = '''torpedo illusionist Bede margarita firefly metaphor Cochabamba playschool cornball incommode Rae bawdily Rilke horseless miff auscultation Ga iridium dud imperilment crybaby steno barrister West plectra novelization Northampton acetic Tantalus professional signer lavender '''
    e = '''torpedo illuionit Bede margarita firefly metaphor Cochabamba playchool cornball incommode Rae bawdily Rilke horele miff aucultation Ga iridium dud imperilment crybaby teno barriter Wet plectra novelization Northampton acetic Tantalu profeional igner lavender '''
    a = remove_letter(p, 's')
    test(a == e,e,a)
    p = '''imbecilic bold quorum hundredweight triple advocate shouter Shepard Charlotte enquirer Streisand rope Wurlitzer America Kathy Yangon fledgling sport abundant happy '''
    e = '''imbecilic bold quorum hundredweight triple advocate shouter Shepard Charlotte enquirer Streisand rope Wurlitzer America Kathy Yangon fledgling sport abundant happy '''
    a = remove_letter(p, 'j')
    test(a == e,e,a)
    p = '''sander turgid ornateness Gupta enchant helpmate questioner conjunct malinger wight Winters Bialystok naturalize Swaziland wainscot bronco '''
    e = '''sander turgid ornateness Gupta enhant helpmate questioner onjunt malinger wight Winters Bialystok naturalize Swaziland wainsot brono '''
    a = remove_letter(p, 'c')
    test(a == e,e,a)
    p = '''causality optima browse shoddy snorkeling outbreak icing perplexity school NF deferential Trudy denationalization motorcade caste perchance specialization NBC immunization '''
    e = '''causality optima browse shoddy snoreling outbrea icing perplexity school NF deferential Trudy denationalization motorcade caste perchance specialization NBC immunization '''
    a = remove_letter(p, 'k')
    test(a == e,e,a)
    p = '''monolingual trouser squidgy juridic Balearic Jerrold Shauna Wilma Chinese potion Sophocles backboard Aguilar whaleboat Cavendish serape pension dreamless cloaca Auriga baseline urbanity originality languorous desecration bankroll bravura hoke originator '''
    e = '''monolingual trouser squidg juridic Balearic Jerrold Shauna Wilma Chinese potion Sophocles backboard Aguilar whaleboat Cavendish serape pension dreamless cloaca Auriga baseline urbanit originalit languorous desecration bankroll bravura hoke originator '''
    a = remove_letter(p, 'y')
    test(a == e,e,a)
    p = '''excuse vendor xenophobia locust straightforward flintlock Gwen Omsk apiarist moral Lottie titchy topaz elliptic chewiness innate Eliseo glacier '''
    e = '''excuse vedor xeophobia locust straightforward flitlock Gwe Omsk apiarist moral Lottie titchy topaz elliptic chewiess iate Eliseo glacier '''
    a = remove_letter(p, 'n')
    test(a == e,e,a)
    p = '''dissipate checkout interesting Beelzebub angelic humanities irreconcilable nourishment nihilism timezone Trevor casual when rile hearten '''
    e = '''dissipate checkout iterestig Beelzebub agelic humaities irrecocilable ourishmet ihilism timezoe Trevor casual whe rile hearte '''
    a = remove_letter(p, 'n')
    test(a == e,e,a)
    p = '''pelt Titus Mann pyromania Morse ultralight muralist telepathy warhead theorist limelight extension praline especial nobody cupping emotion furrier decaffeinate essential Sarto timorous Grendel '''
    e = '''pelt Titus Mann pyroania Morse ultralight uralist telepathy warhead theorist lielight extension praline especial nobody cupping eotion furrier decaffeinate essential Sarto tiorous Grendel '''
    a = remove_letter(p, 'm')
    test(a == e,e,a)
    p = '''requited sullied windblown tan interceptor parasite misspelling optics blister lope cigarette segregationist ovenproof intrusiveness inviolably McPherson imaginable measure '''
    e = '''requited sullied windblown tan interceptor parasite misspelling optics blister lope cigarette segregationist oenproof intrusieness iniolably McPherson imaginable measure '''
    a = remove_letter(p, 'v')
    test(a == e,e,a)
    p = '''encore worldview canter Argentina intrepid burglarproof admirer crackly cauterize crunchiness donation eutectic goddammit JV professed symposium councilmen cosmetologist Ashcroft jackrabbit stander paperweight pleasure Polanski buttonwood inventory Val woefuller lecherousness berths wigwagging printout closemouthed '''
    e = '''encore orldvie canter Argentina intrepid burglarproof admirer crackly cauterize crunchiness donation eutectic goddammit JV professed symposium councilmen cosmetologist Ashcroft jackrabbit stander papereight pleasure Polanski buttonood inventory Val oefuller lecherousness berths igagging printout closemouthed '''
    a = remove_letter(p, 'w')
    test(a == e,e,a)
    p = '''wireless importation siesta Aurelio elodea Sung Bronte lite Carboniferous sleepiness ref extermination cowpox farming certitude SAM normality advantageous too oxymoron navigate pillow panoply sunlamp they'll crisscross intensification austral la microsecond fang affliction forte advent '''
    e = '''wireless importation siesta Aurelio elodea Sung Bronte lite Carbonierous sleepiness re extermination cowpox arming certitude SAM normality advantageous too oxymoron navigate pillow panoply sunlamp they'll crisscross intensiication austral la microsecond ang aliction orte advent '''
    a = remove_letter(p, 'f')
    test(a == e,e,a)
    p = '''collect's Set likableness grandmother Asmara Cole Hohenlohe Bluetooth flashcard acquaint nightingale Shevardnadze impenitence leaper biting smiling Medan White sheen distraction americium tearjerker woodcutter durably absurdity scale Gus infinitive symbiotically diurnal ceca knead salesman rosebush '''
    e = '''collect's Set likableess gradmother Asmara Cole Hohelohe Bluetooth flashcard acquait ightigale Shevardadze impeitece leaper bitig smilig Meda White shee distractio americium tearjerker woodcutter durably absurdity scale Gus ifiitive symbiotically diural ceca kead salesma rosebush '''
    a = remove_letter(p, 'n')
    test(a == e,e,a)
    p = '''Linnaeus fattest snippy snorer inkblot prostitution SOB Mo meddler tire's externalize transmissible alternator bitumen biennium equity musicale philosophical '''
    e = '''Linnaeu fattet nippy norer inkblot protitution SOB Mo meddler tire' externalize tranmiible alternator bitumen biennium equity muicale philoophical '''
    a = remove_letter(p, 's')
    test(a == e,e,a)
    already_printed_error = False
    p = '''foregoes Menuhin televangelism Doctorow carnation crewel Shasta Prensa bedfellow ukulele detestation l tuneup cerebellar Yaounde humus adjustment Shasta CPR Shasta Ostwald anesthetize feverishness Shasta sax miniaturization prohibitory commonalty Shasta liaison '''
    e = '''foregoes Menuhin televangelism Doctorow carnation crewel  Prensa bedfellow ukulele detestation l tuneup cerebellar Yaounde humus adjustment  CPR  Ostwald anesthetize feverishness  sax miniaturization prohibitory commonalty  liaison '''
    a = remove_string(p, 'Shasta')
    test(a == e,e,a)
    p = '''Giannini umbilical quadriceps kvetch cogitate vulvae Noyce inciter ratification xxvii ratification commandment fuel's respectable artifact Walloon Rhone luxuriation measly anapest carhop spook chimney Theosophy sadomasochist '''
    e = '''Giannini umbilical quadriceps kvetch cogitate vulvae Noyce inciter  xxvii  commandment fuel's respectable artifact Walloon Rhone luxuriation measly anapest carhop spook chimney Theosophy sadomasochist '''
    a = remove_string(p, 'ratification')
    test(a == e,e,a)
    p = '''catalog cheerfuller schedule's sportsmen paternalistic plectrum affably Ecclesiastes trichinosis interrogative wodge duster sonorous rubato instinctive define '''
    e = '''catalog cheerfuller schedule's sportsmen paternalistic plectrum affably Ecclesiastes trichinosis interrogative wodge duster sonorous rubato instinctive define '''
    a = remove_string(p, 'handle')
    test(a == e,e,a)
    p = '''Crater Odom refined Chirico cretinism contractible Sepoy burial Crater Basho Crater finisher Chiclets Miller miscreant yodeler crest impecunious expertness limbo adrenaline effluvium shipmate Crater Crater greasily '''
    e = ''' Odom refined Chirico cretinism contractible Sepoy burial  Basho  finisher Chiclets Miller miscreant yodeler crest impecunious expertness limbo adrenaline effluvium shipmate   greasily '''
    a = remove_string(p, 'Crater')
    test(a == e,e,a)
    p = '''deferral Delmer profaneness gooey narcotic Rb wasteful federation deb Delacroix puffy beating retroactive Pfc underpinning campground commune edifice judicious faraway exorbitance shooting hexameter anion cedar '''
    e = '''deferral Delmer profaneness  narcotic Rb wasteful federation deb Delacroix puffy beating retroactive Pfc underpinning campground commune edifice judicious faraway exorbitance shooting hexameter anion cedar '''
    a = remove_string(p, 'gooey')
    test(a == e,e,a)
    p = '''hireling Lorelei gigabyte progenitor magistracy nonexplosive prophet anticlockwise evidence condition's bromine aisle falter Mesabi Collin certificate vegetarianism '''
    e = '''hireling Lorelei gigabyte progenitor magistracy nonexplosive prophet anticlockwise evidence condition's bromine aisle falter Mesabi Collin certificate vegetarianism '''
    a = remove_string(p, 'residency')
    test(a == e,e,a)
    p = '''downtrodden IRA Burbank cruciform propensity ringlet bewail pressing foamy grating desiccant windily Rios Eltanin compete thorax expediences Haber embankment relegate gerbil honcho Woods Arcadian Dobro xxiv asymmetrical embraceable hatchery government '''
    e = '''downtrodden IRA Burbank cruciform propensity ringlet bewail pressing foamy  desiccant windily Rios Eltanin compete thorax expediences Haber embankment relegate gerbil honcho Woods Arcadian Dobro xxiv asymmetrical embraceable hatchery government '''
    a = remove_string(p, 'grating')
    test(a == e,e,a)
    p = '''uncaring Switzerland Terence platinum fibulae advisement mordant Richards barney citrus Khayyam cantor imbrication flavor antenatal solder advisement spectacular encystment vibraphone omit outcropping plimsoll advisement '''
    e = '''uncaring Switzerland Terence platinum fibulae  mordant Richards barney citrus Khayyam cantor imbrication flavor antenatal solder  spectacular encystment vibraphone omit outcropping plimsoll  '''
    a = remove_string(p, 'advisement')
    test(a == e,e,a)
    p = '''Mariano Hanukkah vassal hick Katherine forewomen tom organic leftover member boonies helluva adulterer spit McCain '''
    e = '''Mariano Hanukkah vassal hick  forewomen tom organic leftover member boonies helluva adulterer spit McCain '''
    a = remove_string(p, 'Katherine')
    test(a == e,e,a)
    p = '''improvisational software shoplift obstetric dominate Tupi dock Ruchbah crock lurch valueless coldblooded convector avowal abalone chronicle receptacle funny necessary Phanerozoic megapixel Goteborg craftiness ponderousness lamppost churchwarden analyze snugger insure asinine enjoyably '''
    e = '''improvisational software shoplift obstetric dominate Tupi dock Ruchbah crock lurch valueless coldblooded convector  abalone chronicle receptacle funny necessary Phanerozoic megapixel Goteborg craftiness ponderousness lamppost churchwarden analyze snugger insure asinine enjoyably '''
    a = remove_string(p, 'avowal')
    test(a == e,e,a)
    p = '''Deon sandpit culminate biog beaker Bayonne waistline Comanche sainthood expelling indefeasibly medico whiskey Musial chocoholic repairmen marred homesickness speechlessness participate isthmian '''
    e = '''Deon sandpit culminate biog beaker Bayonne waistline Comanche sainthood expelling indefeasibly medico whiskey Musial chocoholic repairmen  homesickness speechlessness participate isthmian '''
    a = remove_string(p, 'marred')
    test(a == e,e,a)
    p = '''injurious Bethune Cthulhu departmentalize Innsbruck highball masturbatory prophylaxes phoneme playgoer buttress earldom injurious Eichmann sickish less bark's clearance achoo gymkhana efferent Tammy deejay cure's N'Djamena Wolf instead vigilante eponymous haiku intestacy acre '''
    e = ''' Bethune Cthulhu departmentalize Innsbruck highball masturbatory prophylaxes phoneme playgoer buttress earldom  Eichmann sickish less bark's clearance achoo gymkhana efferent Tammy deejay cure's N'Djamena Wolf instead vigilante eponymous haiku intestacy acre '''
    a = remove_string(p, 'injurious')
    test(a == e,e,a)
    p = '''oldster loftily nondiscriminatory umpire respirator taxonomic felon aromatic Mingus faff parietal fatherland trollop swig Epiphany creativeness Epiphany hospice demijohn Madge coon flywheel trapping acceptability zoophytic scorbutic '''
    e = '''oldster loftily nondiscriminatory umpire respirator taxonomic felon aromatic Mingus faff parietal fatherland trollop swig  creativeness  hospice demijohn Madge coon flywheel trapping acceptability zoophytic scorbutic '''
    a = remove_string(p, 'Epiphany')
    test(a == e,e,a)
    p = '''overstrict strum inspect florist solubility inspect wholegrain Vanderbilt spoilsport airily inspect coronary marketable material Dubrovnik weaponless allergy Amelia lemming speech rejuvenation shiv aggressive composedly trainee Donovan Olson puristic '''
    e = '''overstrict strum  florist solubility  wholegrain Vanderbilt spoilsport airily  coronary marketable material Dubrovnik weaponless allergy Amelia lemming speech rejuvenation shiv aggressive composedly trainee Donovan Olson puristic '''
    a = remove_string(p, 'inspect')
    test(a == e,e,a)
    p = '''department fastidiousness body Corfu handbag bedded Kiel millionth Vince florescence humbleness whipped cynical bollocks calumet cologne '''
    e = '''department fastidiousness body  handbag bedded Kiel millionth Vince florescence humbleness whipped cynical bollocks calumet cologne '''
    a = remove_string(p, 'Corfu')
    test(a == e,e,a)
    p = '''evoke Anacin malpractice Selma n retrofit retrofit Ontarian malevolent overfed nontraditional pike servicing Wendy's guided '''
    e = '''evoke Anacin malpractice Selma n   Ontarian malevolent overfed nontraditional pike servicing Wendy's guided '''
    a = remove_string(p, 'retrofit')
    test(a == e,e,a)
    p = '''Monterrey sleighs nondramatic scrub workings splodge Judy okay pocketknives Herculaneum Adriatic okay Voltaire okay lithograph freedmen candidness creep repercussion Edwardo hematite I'm '''
    e = '''Monterrey sleighs nondramatic scrub workings splodge Judy  pocketknives Herculaneum Adriatic  Voltaire  lithograph freedmen candidness creep repercussion Edwardo hematite I'm '''
    a = remove_string(p, 'okay')
    test(a == e,e,a)
    p = '''6 employable repetitive hying Howrah nonathletic Lorrie Valarie Republicanism Hollywood bacchanalian Balaton Custer neuritic Tyree tornadoes count astronaut dinosaur palatinate pureeing angiosperm premonitory Tertiary Glenn California selfishness '''
    e = '''6 employable repetitive hying Howrah nonathletic Lorrie Valarie Republicanism Hollywood bacchanalian  Custer neuritic Tyree tornadoes count astronaut dinosaur palatinate pureeing angiosperm premonitory Tertiary Glenn California selfishness '''
    a = remove_string(p, 'Balaton')
    test(a == e,e,a)
    p = '''nunnery BBQ chambray Palmer Sept four pureness Payne aquatic glance Humvee Mediterranean diacritical Faberge Wolverhampton Lethe tingly Humvee nonbreakable fender Aristotle tetanus carcass sadistic Zoroastrianism helpless hide fucker om '''
    e = '''nunnery BBQ chambray Palmer Sept four pureness Payne aquatic glance  Mediterranean diacritical Faberge Wolverhampton Lethe tingly  nonbreakable fender Aristotle tetanus carcass sadistic Zoroastrianism helpless hide fucker om '''
    a = remove_string(p, 'Humvee')
    test(a == e,e,a)
    p = '''Porfirio Peace Kahlua pipsqueak Sheppard resentment plainclothes healthfulness laminate boll jumpiness enclosure understaffed Cherry Sikkimese magnum opulence Pythias Ricardo amniocenteses Tirane promotional underskirt ballot miscommunication scheduled imputation initialized inalienably hegemony forgoes '''
    e = '''Porfirio Peace Kahlua pipsqueak Sheppard resentment plainclothes healthfulness laminate boll jumpiness enclosure understaffed Cherry Sikkimese magnum opulence Pythias Ricardo amniocenteses Tirane promotional underskirt ballot  scheduled imputation initialized inalienably hegemony forgoes '''
    a = remove_string(p, 'miscommunication')
    test(a == e,e,a)

    print("Ending tests")


test_suite()