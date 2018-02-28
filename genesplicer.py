
def printStr(str1, str2, finalStr):
	#DESCRIBE
    print('********************************************')
    print('string 1 - ' + str1 +' 	' + 'string 2 – ' + str2)
    print('shortest string that has both as substring')
    print(finalStr + ' (length ' + str(len(finalStr)) + ')')
    print('********************************************')

def findShortest(str1, str2):
    '''Finds shortest string that contain both str1 and str2 as substrings'''
    c1 = 0
    c2 = 0
    count = len(str1)
    match = False
    addOn = ''
    while(c2 < len(str2)):
        if str2[c2] != str1[c1]:
            if match:
                if str2[c2] == str1[0]:
                    count += 1
                    c1 = 1
                    addOn += str2[c2]
                else:
                    match = False
                    c1 = 0
                    count += 2
                    addOn += str2[c2-1:c2+1]
            else:
                count += 1
                addOn += str2[c2]
            c2 += 1

        elif str2[c2] == str1[c1] or match:
            #if rest of str2 is all in str1
            if str2[c2:] in str1:
                finalStr = addOn + str1
                return finalStr
            #otherwise, keep going 
            match = True    
            c2 += 1
            c1 += 1

    finalStr = addOn + str1
    return finalStr

def checkSubstring(str1, str2):
    #if strings in each other
    if str2 in str1:
        return True

		
def main():
    str1 = input('Input a string representing a snippet of genes').upper()
    str2 = input('Input another string representing a snippet of genes').upper()
    if checkSubstring(str1, str2) or checkSubstring(str2, str1):
        if checkSubstring(str1, str2): finalStr =  str1
        elif checkSubstring(str2, str1): finalStr = str2
    else:
        potenStr1 = findShortest(str1, str2)
        potenStr2 = findShortest(str2, str1)
        if len(potenStr1) < len(potenStr2):
            finalStr = potenStr1
        else:
            finalStr = potenStr2

    printStr(str1, str2, finalStr)

main()
