'''The following code should work for answering the Practice Projects in
Automate the Boring Stuff by Al Sweigart and published by No Starch Press'''


import re
import os
import tkinter
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime
import pprint
now = datetime.now()
root = Tk()
root.wm_attributes('-topmost', 1)

print('You will now choose the directory to search for things')

#popup to choose directory with text files in it

'''The tkinter thing is not mentioned yet in the book but it 
causes a popup to occur so you can choose the directory through a GUI as opposed to using ghe command line'''

dirs = tkinter.filedialog.askdirectory()
os.chdir(dirs)
numberofthings = os.listdir(dirs)

#set regular expressions to search for telephone numbers and email addresses

'''These are the phone and email scraping regular expressions from earlier in the book'''

phoneregex = re.compile(r'''(
(\d{3}|\(\d{3}\))?   #area code
(\s|-|\.)?           #seperator
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

#email regex

emailregex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#do the thing
matches = []
res = []
write_file = open('phone_and_email_scan' + str(now) +'.txt','a+')

write_file.write('This is the results of your program as it was run on. ' + str(now) + '\n\n')
for file in numberofthings:
    if file.endswith('.txt'):
        print('The following text document was found and scanned for telephone numbers and email addresses.')
        print(os.path.join(dirs, file))
        write_file.write('\nThe following text document was found and scanned for telephone numbers and email addresses.\n\n')
        write_file.write(os.path.join(dirs, file) +'\n\n')
        txtfile = open(os.path.join(dirs, file), 'r+')
        msg = txtfile.read()
        matches = []
        for groups in phoneregex.findall(msg):
            phonenum = '-'.join([groups[1], groups[3], groups[5]])
            if groups[8] != '':
                phonenum += ' ext ' + groups[8]
            matches.append(phonenum)
            #print(phonenum)
        for groups in emailregex.findall(msg):
            matches.append(groups[0])
        #pprint.pprint(matches)
        res = []
        for i in matches:
            if i not in res:
                res.append(i)
        #pprint.pprint(res)

    #pprint.pprint(res)
    for item in res:
        write_file.write(item + '\n')

'''Notes on the above code, it will read from and save to the same directory chosen by the GUI, 
the variable "dirs" in the top of this code.  Because of this the documents you produce will ALSO be 
scanned for telephone and email addresses, and you will get exponential duplicates.'''







write_file.close()

root.destroy()
os._exit(0)