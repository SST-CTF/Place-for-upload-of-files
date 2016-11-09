import fileinput 
from PyDictionary import PyDictionary #not currently in use, for recognizing words in the output
from collections import Counter
print("Loading online dictionary module...")
dictionary = PyDictionary()
print("done")
print("Loading offline english words list...")
words = open('words3.txt')
print("Done!")
print("------------------------------------------")
print("Cipher Tools- SST CTF Team")
mode = input("Which mode to use? bc=brute caesar, dc=decrypt caesar w/ key, ec=encrypt w/ key \n")
inpu = input("input text to act on\n")
inpu = inpu.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
most_common = "etaoinshrdlcumwfgypbvkjxqz"
mostCommonFirstLetters = "toawbcdsfmrhiyeglnpujkqzx"
score = []
if mode == "bc":
    load = ""
    oInpu = []
    mCom = []
    diff = []
    out = []
    for i in range(len(inpu)):
        oInpu.append(ord(inpu[i])-96)
        #print(oInpu[i])
    for i in range(len(most_common)):
        mCom.append(ord(most_common[i])-96)
    oInpu = [i for i in oInpu if i > 0 & i < 26]
    #print(oInpu)
    common = Counter(oInpu)
    mostCommon = common.most_common()
    #print(common)
    #print(mostCommon)
    oMC = [mostCommon[i][0] for i in range(len(mostCommon))]
    for i in range(len(mCom)):
        diff.append(oMC[1]- mCom[i])
        score.append(0)
        #print(diff[i])
        inter = []
        for x in range(len(oInpu)):
            inter.append((oInpu[x]+diff[i]-1)%26+1)
        place = 0;
        place2 = 1;
        out.append(''.join(chr(e+96) for e in inter))
        for z in range(len(out[i])):
            if z != 0:
                place2 = z
                con1 = "ASD"
                con2 = place2-place
                if out[i][place:place2] in words.read():
                    score[i] += 1
                    place = place2
                elif con2 > 15:
                    score[i] += 1
                    place = place2
                
                    
        print("score" + str(score[i]))
        junk = input()
        print(out[i])
        junk = input("next-->")
elif mode == "ec":
    enc = [ord(inpu[i])-96 for i in range(len(inpu))]
    enc = [i for i in enc if i > 0 & i<27]
    shift = input("How much to shift?  ")
    shift = int(shift)
    enc = [i-1+shift for i in enc]
    enc = [i%26+1 for i in enc]
    strEnc = (chr(w+96) for w in enc)
    out = ''.join(strEnc)
    print(out)
elif mode == "dc":
    dec = [ord(inpu[i])-96 for i in range(len(inpu))]
    dec = [i for i in dec if i > 0 & i<27]
    shift = input("What was the shift?  ")
    shift = int(shift)
    dec = [i-1-shift for i in dec]
    dec = [i%26+1 for i in dec]
    strDec = (chr(w+96) for w in dec)
    out = ''.join(strDec)
    print(out)
    

