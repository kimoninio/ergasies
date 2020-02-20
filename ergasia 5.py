def split():
    text = open ("file.txt","r")
    text = text.read()
    text = text.split()
    return text

def ay(array ):
    for i in range(len(array)):
        if len(array[i]) > 3:
            array[i] = array[i][1:] + array[i][0] + "ay"
    return array 

filetext = split()
wordsay = ay(filetext)

for i in range (len(wordsay)):
    print(wordsay[i])

