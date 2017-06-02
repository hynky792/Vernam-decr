text = input('Insert encrypted text in hex')
keytext = input('Insert plain text contaning key')
text = text.replace(" ","")
cryptline = [text[i:i+2] for i in range(0, len(text), 2)]
x=0
i=-1
n=1
finaltext=''
while(n):
    i+= 1
    finaltext +=  chr(int(cryptline[i],16) ^ ord(keytext[i+x]))
    if i==29:
        x+= 1
        i = -1
        print(finaltext)
        finaltext =""
    if x >= (len(keytext) -29):
        n = 0
input()
