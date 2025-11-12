import sys

def first_number_less_than_10(a):
    # print("function looking for < 10")
    for i in a:
        if i < 10:
            return i 
def first_number_larger_than_100(a):
    # print("function looking for > 100")
    for i in a:
        if i > 100:
            return i

def total_amount_of_numbers_in_the_50s(a):
    # print("In the 50's")
    count = 0
    for i in a:
        if i >= 50 and i < 60:
            count = count + 1
    return count

def total_amount_of_integers(a):
    # print("Total number of integers")
    count = 0
    for i in a:
        if type(i) == int:
            count = count + 1
    return count



def test(given, expected):
    """ Print the result of a test. """
    
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if not expected == given:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)
        print("\tExpected: "+ str(expected))
        print("\tgiven   : "+ str(given))

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("Starting tests")
    #Add your tests here

    #Dr B's tests follow:
    Ronalda = [34, 96, 9, 66, 36, 93, 78, 36, 29, 77, 22, 40]
    answer = first_number_less_than_10(Ronalda)
    test(answer, 9)
    Alia = [0, 39, 56, 41, 97, 40, 96, 44, 68, 59, 95, 10, 97, 97, 34, 94, 94]
    answer = first_number_less_than_10(Alia)
    test(answer, 0)
    Ibby = [93, 55, 39, 87, 55, 20, 89, 41, 39, 4, 79, 87, 88, 12, 77, 51, 71, 23]
    answer = first_number_less_than_10(Ibby)
    test(answer, 4)
    Aida = [90, 92, 2, 84, 90, 79, 29, 56, 19, 28]
    answer = first_number_less_than_10(Aida)
    test(answer, 2)
    Gisella = [93, 44, 1, 38, 56, 35, 54, 31, 34, 83, 86, 31]
    answer = first_number_less_than_10(Gisella)
    test(answer, 1)
    Erinn = [78, 38, 38, 67, 32, 23, 47, 57, 16, 47, 74, 13, 54, 3]
    answer = first_number_less_than_10(Erinn)
    test(answer, 3)
    Mavra = [3, 47, 76, 86, 90, 52, 65, 87, 68, 22, 64, 13, 72, 86, 65]
    answer = first_number_less_than_10(Mavra)
    test(answer, 3)
    Mindy = [16, 83, 92, 68, 45, 74, 97, 37, 82, 9, 47]
    answer = first_number_less_than_10(Mindy)
    test(answer, 9)
    Catina = [41, 48, 77, 63, 73, 60, 44, 13, 2, 16]
    answer = first_number_less_than_10(Catina)
    test(answer, 2)
    Virginie = [28, 12, 54, 14, 68, 77, 95, 33, 55, 32, 84, 98, 51, 7, 92]
    answer = first_number_less_than_10(Virginie)
    test(answer, 7)
    Dana = [42, 44, 3, 70, 50, 89, 28, 58, 0, 0, 93, 43, 10, 47, 14, 159, 68, 11]
    answer = first_number_larger_than_100(Dana)
    test(answer, 159)
    Stephanie = [5, 88, 79, 25, 74, 69, 75, 7, 83, 24, 25, 13, 176, 97, 95, 18]
    answer = first_number_larger_than_100(Stephanie)
    test(answer, 176)
    Augusta = [87, 40, 62, 160, 55, 73, 45, 99, 23, 88, 26, 15, 94, 15, 99, 18]
    answer = first_number_larger_than_100(Augusta)
    test(answer, 160)
    Mariana = [88, 90, 38, 67, 51, 43, 107, 33, 10, 55, 38, 99]
    answer = first_number_larger_than_100(Mariana)
    test(answer, 107)
    Melamie = [44, 192, 34, 56, 93, 34, 82, 69, 17, 97]
    answer = first_number_larger_than_100(Melamie)
    test(answer, 192)
    Katharyn = [90, 80, 105, 1, 72, 95, 85, 14, 16, 55]
    answer = first_number_larger_than_100(Katharyn)
    test(answer, 105)
    TEirtza = [89, 10, 64, 31, 115, 80, 11, 66, 72, 85, 68, 36, 58, 59]
    answer = first_number_larger_than_100(TEirtza)
    test(answer, 115)
    Winifred = [94, 21, 92, 8, 41, 63, 57, 103, 63, 12, 98, 17, 44, 64, 94, 10]
    answer = first_number_larger_than_100(Winifred)
    test(answer, 103)
    Tarrah = [160, 14, 13, 19, 17, 4, 72, 60, 67, 28, 79, 15, 50, 0, 54, 4, 10, 2]
    answer = first_number_larger_than_100(Tarrah)
    test(answer, 160)
    Danit = [25, 13, 47, 13, 81, 18, 62, 17, 27, 44, 3, 63, 57, 166, 38, 54, 27]
    answer = first_number_larger_than_100(Danit)
    test(answer, 166)
    Adorne = [46, 59, 59, 56, 45, 52, 49, 46, 46, 40, 41]
    answer = total_amount_of_numbers_in_the_50s(Adorne)
    test(answer, 4)
    Di = [52, 53, 50, 48, 47, 51, 47, 59, 40, 51, 53, 47, 57, 46]
    answer = total_amount_of_numbers_in_the_50s(Di)
    test(answer, 8)
    Antonie = [46, 57, 49, 59, 58, 50, 41, 47, 57, 58, 59, 56, 47]
    answer = total_amount_of_numbers_in_the_50s(Antonie)
    test(answer, 8)
    Van = [44, 51, 40, 50, 48, 46, 47, 53, 58, 41, 43, 47, 48]
    answer = total_amount_of_numbers_in_the_50s(Van)
    test(answer, 4)
    Vanna = [41, 52, 45, 59, 43, 57, 49, 55, 47, 56, 52, 51, 43]
    answer = total_amount_of_numbers_in_the_50s(Vanna)
    test(answer, 7)
    Vanni = [45, 41, 56, 43, 46, 59, 55, 52, 55, 51, 44, 56, 49, 49, 53, 41]
    answer = total_amount_of_numbers_in_the_50s(Vanni)
    test(answer, 8)
    Eleonora = [57, 51, 48, 51, 51, 56, 42, 43, 52, 55, 58]
    answer = total_amount_of_numbers_in_the_50s(Eleonora)
    test(answer, 8)
    Bobine = [59, 54, 55, 41, 59, 47, 50, 47, 58, 56, 44, 47, 58, 51]
    answer = total_amount_of_numbers_in_the_50s(Bobine)
    test(answer, 9)
    Sadye = [47, 58, 56, 43, 47, 47, 53, 52, 52, 43, 41, 46, 50, 53]
    answer = total_amount_of_numbers_in_the_50s(Sadye)
    test(answer, 7)
    Tammie = [55, 54, 46, 56, 50, 49, 54, 47, 46, 50, 46, 44, 53, 45, 52, 56, 56, 40, 58]
    answer = total_amount_of_numbers_in_the_50s(Tammie)
    test(answer, 11)
    Linda = [13, 94, 'Raquel', 57, 80, 'applauder', 91.68, 95, 'cadge', 54, 37, 15, 39, 17, 71, 'pejoration', 89, 91, 'Abraham', 'oilcloths', 19]
    answer = total_amount_of_integers(Linda)
    test(answer, 14)
    Shirl = [32, 'Plasticine', 'thermometric', 29, 19, 33, 64, 52.51, 14, 88.29, 'levitation', 50, 46.46, 'Donaldson', 8, 0.83, 9, 8.7, 95.3, 24.83, 2, 'bitcoin', 13]
    answer = total_amount_of_integers(Shirl)
    test(answer, 11)
    Danni = [2, 53, 32, 'phalanx', 'callback', 82, 81.25, 78.01, 7, 15, 66.81, 'Politburo', 65, 89.33, 'embower', 'tacker', 62, 89.96, 28.21, 71, 12, 'cloverleaves', 'hogtying', 27, 45.51, 5, 4, 1.04, 92, 82.94, 7.67, 65, 14, 44]
    answer = total_amount_of_integers(Danni)
    test(answer, 17)
    Kally = [20, 11.88, 25, 77, 35, 'oops', 15, 'Hezekiah', 71.44, 'phi', 21, 'argon', 'Ellison', 8, 14, 21, 93, 79, 'merchantmen', 16.52, 77, 'viking', 19, 92, 'assessor', 35.68, 93, 76.2, 63]
    answer = total_amount_of_integers(Kally)
    test(answer, 16)
    Susanna = [53, 15.38, 71.03, 44, 17, 49, 'gurgle', 3, 4, 21, 'flibbertigibbet', 81.8, 80, 72.1, 26.46, 33, 72.48, 61, 58.86, 92]
    answer = total_amount_of_integers(Susanna)
    test(answer, 11)
    Lauree = [15, 'puffiness', 'encipher', 74, 'deformity', 65, 75.22, 34, 25.98, 33, 'phosphorus', 87.9, 'devilry', 6.45, 'beaver', 12.87, 'Short', 50, 'twp', 2, 'viragoes', 'Bulgar', 6, 26, 95, 1]
    answer = total_amount_of_integers(Lauree)
    test(answer, 11)
    Cami = [23, 60.96, 75, 62.62, 71, 58, 99, 'teakettle', 23.88, 'hung', 58.01, 55.92, 33.35, 76, 81, 24.07, 'stream', 98, 51, 29, 22, 'regard', 91, 82, 71.22, 'Hokusai', 92, 53, 48, 63, 'Toyota', 11]
    answer = total_amount_of_integers(Cami)
    test(answer, 18)
    Gloriane = [4, 85, 70, 8, 29, 'whimsy', 1.91, 94, 59, 54, 'lecherousness', 'lofty', 13.96, 'classmate', 14.87, 'yarmulke', 'spotted', 88.32, 78.78, 55, 81.44, 18, 59]
    answer = total_amount_of_integers(Gloriane)
    test(answer, 11)
    Dion = [76, 58, 5, 46, 30, 81, 85, 7.2, 24.2, 86.32, 27.21, 66, 22.17, 43.15, 'brochette', 'RSI', 79, 'actor', 88, 25.97, 'arrogation', 62.46, 75, 'Parliament', 14, 'multipurpose', 26, 54, 19, 'Zhukov', 92]
    answer = total_amount_of_integers(Dion)
    test(answer, 16)
    Maxine = [86, 'movement', 'wry', 44.49, 45.05, 9.56, 54, 75.2, 'cumber', 85, 44, 10, 'tropism', 62, 'lattice', 98, 'Green', 6.45, 99, 87, 84, 89, 'micron', 22.81, 25.01, 90.83, 64.52, 'satyriasis', 53.09, 'bin', 25, 88, 7.83, 33.64, 59, 'Mb', 'bowlegged', 56]
    answer = total_amount_of_integers(Maxine)
    test(answer, 15)
test_suite()
print ("Finished testing")
