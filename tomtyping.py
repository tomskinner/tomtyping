# !bin/usr/env/python3.7
'''
Name:- project tomtyper
aim to take a string of normal text and make it horrible to read.
1. Randomly changes the capitalisations in the words. 
2. Insert additional random spaces between words.
3. Include special characters added into words.
4. take a word and scramble the internals of the word. i.e. super becomes speur

################################################
What needs to be done.

Function to find words without specal characters and scramble the internals
:- Still TODO


Additional :- Still TODO
Create a GUI to operate in.
allow text documents to be read and messed with.
allow .docx and other text based documents to be loaded.


'''

import random
from tkinter import *

#Dictionaries and variables
versionnumber = "0.0.2"
colour = "lime"
OutputStr = ''
randomtypelevels = {'capitol':[0, 60, 50, 80, 90],
                    'space2':[0, 30, 10, 40, 70],
                    'specialAdd':[0, 4, 3, 20, 25],
                    'specialreplace':[0, 3, 2, 30, 45],
                    'scrambleWord':[0, 15, 12, 19, 34]
    } # key : [off, normal, with low mod, with med mod, with high mod ]


def randomiser(levelto):
    '''
    TypeORandom will determin the base level of randomness.
    i.e. expect an input from the other functions saying I'm putting letters to capitols expect a high chance of sucsess level i'm adding a special character expect a low chance of sucsess
    
    LvlRandom will apply a modifier (expect a number value 0-4)
    0 = off , 1 = normal, 2 =low,  3 = med, 4 = high
    
    '''
    
    random.seed()
    doit = random.randrange(1, levelto, 1)
    return doit

def Capitol(StringInput, LvlRandom, OutputStr, n):
    '''
    search through the string letter by letter. at each letter run the randomiser and decide if letter needs to be capitalised.
    
    '''
    StringInput[n].isalpha()
    level = randomtypelevels['capitol'][LvlRandom]
    doit = randomiser(levelto=100)
    if doit <= level and StringInput[n].isalpha():
        OutputStr = str(OutputStr) + str(StringInput[n].upper())
    elif doit >= level and StringInput[n].isalpha():
        OutputStr = str(OutputStr) + str(StringInput[n].lower())
    else:
        return str(OutputStr) + str(StringInput[n])
    return str(OutputStr)
    

def mainloop(StringInput, LvlRandom, OutputStr):
    '''
    mainloop provides the ability to reach the different functions used
    '''
    StringLng = len(StringInput)
    n=0
    while n < len(StringInput):
        doit = randomiser(levelto =100)
        if doit <= randomtypelevels['specialreplace'][LvlRandom]:
            OutputStr = SpecReplace(StringInput, LvlRandom, OutputStr, n)
            
        elif doit <= randomtypelevels['specialAdd'][LvlRandom]:
            OutputStr = SpecialAdd(StringInput, LvlRandom, OutputStr, n)
        elif doit <= randomtypelevels['capitol'][LvlRandom]:
            OutputStr = Capitol(StringInput, LvlRandom, OutputStr, n)
        elif doit <= randomtypelevels['space2'][LvlRandom]:
            OutputStr = space2(StringInput, 1, OutputStr, n)
        
        else:
            OutputStr = str(OutputStr) + str(StringInput[n])

        n+=1      
            #'scrambleWord'
        
    outputlabel = Label(outputframe, text = OutputStr, bg= colour)
    outputlabel.grid(row=1, column = 0)
    
def SpecReplace(StringInput, LvlRandom, OutputStr, n):
    # replaces current character in string with a special character found in specialcharpicker()
    doit = randomiser(levelto=30)
    if StringInput[n].isalnum() == True:
        OutputStr = str(OutputStr) + str(specialcharpicker(doit))
    elif StringInput[n].isspace() == True:
        OutputStr = str(OutputStr) + " " + str(specialcharpicker(doit))   
    else:
        return str(OutputStr)
    return str(OutputStr)

def SpecialAdd(StringInput, LvlRandom, OutputStr, n):
    # adds a special character in the string just after current character. this additional character can be found in specialcharpicker()
    doit = randomiser(levelto=30)
    OutputStr = str(OutputStr) + str(StringInput[n]) + str(specialcharpicker(doit))
    return str(OutputStr)

def scrambleWord():
    #TODO
    '''
    
    how I think it will be done.
    ---------------------------
    use split() to find # of words and create a list of those words.
    take a random number between 0 and the amount of words in list.
    then add that number to a counter to keep track position in list.
    (use while loop) 
    the word is then given a chance of being scrambled using the randomiser above a given level.
    the while loop then continues until reached passed the last word.
    
    include a check if the word is less than 3 then skip the scramble pard and continue through the loop.
    
    +++++to find the edges of the word+++++
    use the sum of the length of the words + 1 in the list + 1 for each word of length 0.
    make a 2nd list which contains a list of lengths of each word +1 if word = length 0 then add 2 instead of 1 to that word.
    if the last word take 1 away.
    
    use the length list to find start index of the word
    
    copy the word to a variable
    take the center of the word ane scramble then add the first and last letter back to their original point and return to the same point in the string.
    
    +++++To scramble++++++++
    Still have to think this through.
    
    As the original and the new string may have different lengths and I aim to do this function first.
    
    '''
    print(" I'm going to scramble the word. @ position" + str(n))
    
def space2(StringInput, LvlRandom, OutputStr, n):
    return str(OutputStr) + str(StringInput[n]) + '  '
    

def specialcharpicker(doit):
    specialChar = ['!','£','$','%','^','&','*','|','/','*','-','+','<','>',',','.','#','~','@',1,2,3,4,5,6,7,8,9,0]
    return str(specialChar[doit])

def gotoit(frame):
    StringInput = entrybox.get()
    
    frame.destroy() # doesn't clear the label
    
    outputbox = Label(outputframe, text = "The output is here", bg= colour)
    outputbox.grid(row=0, column = 0, columnspan = 2)
    
    mainloop(StringInput, 1, OutputStr)
    

######################################
root = Tk()
root.title('Toms Typer v.' + str(versionnumber))
#root.iconbitmap('@/home/pi/Documents/Python/GUI/icons/street_warning_transport_icon_148640.xbm')
root.geometry("773x400")
root.configure(background = colour)

mainlabel = Label(root, text = "Get it Scrambled", bg = colour)
mainlabel.grid(row=0, column=0)

btn = Button(root, text = "Scramble", command = lambda: gotoit(outputbox))
btn.grid(row=0, column=1)

entrybox = Entry(root, bg = "#efefef", width=85, font = 'wrap')
entrybox.place(height=50)
entrybox.grid(row = 1, column = 0, ipady = 80, columnspan = 2)

outputframe = Frame(root, bg = colour, width=75, height=50,)
outputframe.grid(row=2, column=0,columnspan = 2)

outputlabel = Label(outputframe, text = "The output is here", bg= colour)
outputlabel.grid(row=0, column = 0, columnspan = 2)

outputbox = Label(outputframe, text = " ", bg= colour, width = 85, height = 40)
outputbox.grid(row=1, column = 0, columnspan = 2)
###########################################################
#StringInput = input("Type in a string to tomtype! \n :=")

root.mainloop()



