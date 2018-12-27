#Muneer Tomeh
#013933567
#CECS 378 Lab Assignment 1
#10/2/2018
import random
import numpy as np

import string


def main():

    firstEncryptedMessage = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    secondEncryptedMessage = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
    thirdEncryptedMessage = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    fourthEncryptedMessage = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    theMatrix = transitionMatrixCreator()

    #Since the first two messages are related to Caesar cipher, utilize the decryption for Caesar accordingly
    print("Decryption Problem 1")
    decrypt(firstEncryptedMessage, theMatrix)
    print()
    print("Decryption Problem 2")
    decrypt(secondEncryptedMessage, theMatrix)

    #Since the last two messagaes are related to simple substitution cipher, utilize the decryption for Simple Substitution cipher accordingly

    print()
    print("Decryption Problem 3")
    metropolis(thirdEncryptedMessage, theMatrix)
    print()
    print("Decryption Problem 4")
    metropolis(fourthEncryptedMessage, theMatrix)




    #ENCRYPTION PART OF THE ASSIGNMENT

    firstRegularMessage = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you"

    secondRegularMessage = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened."
    thirdRegularMessage = "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can"
    print("")
    print("Encryption Problem 1")
    simpleSubstitutionEncryption(firstRegularMessage)
    print("")
    print("Encryption Problem 2")
    simpleSubstitutionEncryption(secondRegularMessage)
    print("")
    print("Encryption Problem 3")
    simpleSubstitutionEncryption(thirdRegularMessage)

    return 0


#This method encrypts a message using the simple substitution cipher method
def simpleSubstitutionEncryption(regularMessage):

    regularMessage = ''.join(regularMessage.split())

    regularMessage = regularMessage.lower()
    print("Regular message: ", regularMessage)

    #Shuffle the alphabets to get a random key
    alphabets = string.ascii_lowercase
    alphabetList = list(alphabets)
    random.shuffle(alphabetList)

    encryptedMessage = ""

    #Traverses the regular message, and then proceceds to encrypt the message given the shared key
    for letter in regularMessage:
        if letter in alphabets:
            letterPosition = string.ascii_lowercase.index(letter)
            encryptedMessage = encryptedMessage + alphabetList[letterPosition]

    #convert the shared key using a list to string conversion
    sharedKey = ''.join(alphabetList)
    print("Encrypted message: ", encryptedMessage)
    print("The key: ", sharedKey)

    print()







#Creates a transition matrix based of bigrams and their occurrence counts in a certain novel
def transitionMatrixCreator():

    transitionMatrix = [[]]

    #Reads the transition probabilities from the text file
    with open("transitionMatrix.txt") as randomFile:

        counter = 0
        summationCounter = 0
        #traverse each line in the file and proceed to remove all whitespaces
        for line in randomFile:
            lineRead = ' '.join(line.split())
            #remove all whitespaces
            splittingLine = lineRead.split(' ')

            interiorCounter = 0

            innerList = []
            #Populate the transition matrix with the bigram mappings
            for component in splittingLine:
                innerList.append(int(component))
                interiorCounter=  interiorCounter+ 1
            summationCounter = summationCounter + interiorCounter
            transitionMatrix.append(innerList)
            counter = counter+1

        #Remove the first list in the transition matrix as it is empty
        transitionMatrix.remove([])

        #Ensure every value in the transition matrix is a percentage
        for i in range(len(transitionMatrix)):
            for j in range(len(transitionMatrix[i])):
                transitionMatrix[i][j] = transitionMatrix[i][j] / summationCounter

        return transitionMatrix




#The Metropolis algorithm that implements the logic behind the decrpytion of the simple substitution cipher
def metropolis(encryptedMessage, transitionMatrix):
    encryptedMessage = ''.join(encryptedMessage.split())
    print("Encrypted message: ", encryptedMessage)
    alphabetMapping = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
                           , 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                       ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
                           , 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]

    #Run the score method for f, which is the current state
    currentScore = metropolisScore(encryptedMessage, transitionMatrix)

    #Does 2000 iterations to obtain the best score and best mapping
    for i in range(2000):
        primeAlphabetMapping = alphabetMapping

        firstRandomValue = random.randint(0, 25)
        secondRandomValue = random.randint(0,25)

        # Create the proposal from f by randomly swapping two letters in the mapping accordingly
        temp = primeAlphabetMapping[1][firstRandomValue]
        primeAlphabetMapping[1][firstRandomValue] = primeAlphabetMapping[1][secondRandomValue]
        primeAlphabetMapping[1][secondRandomValue] = temp

        decipheredMessage = ""

        #Decipher the ciphertext using the alteration of two letters in the alphabet mapping
        for letter in encryptedMessage:
            if letter == primeAlphabetMapping[0][firstRandomValue]:
                decipheredMessage += primeAlphabetMapping[1][firstRandomValue]
            elif letter == primeAlphabetMapping[0][secondRandomValue]:
                decipheredMessage+= primeAlphabetMapping[1][secondRandomValue]
            else:
                decipheredMessage+= letter

        #Calculate the metropolis score of the deciphered message
        newScore = metropolisScore(decipheredMessage, transitionMatrix)

        acceptanceScore = newScore / currentScore

        ##Keep this portion of the algorihtm only for now, might delete this information later at a different time.
        divisionResult = newScore / currentScore
        if newScore > currentScore:
            currentScore = newScore
            alphabetMapping = primeAlphabetMapping

        else:
            randomUniformNumber = random.uniform(0,1)
            if randomUniformNumber <= divisionResult:
                currentScore = newScore
                alphabetMapping = primeAlphabetMapping


    print("This is the final score with the following key ", currentScore, " ", alphabetMapping[1])


    decipheredFinalMessage = ""
    for letter in encryptedMessage:
        letterPosition = string.ascii_lowercase.index(letter)
        decipheredFinalMessage += alphabetMapping[1][letterPosition]


    print("Decrypted Message ", decipheredFinalMessage )


#Calculates the fitness score using probability of bigrams' occurrence from a sample plaintext
def metropolisScore(encryptedMessage, theMatrix):

    probabilityList = []
    summationTotal = 0

    #Traverse through every two letters in the encrypted message
    for i in range((len(encryptedMessage))-1):
        firstLetter = encryptedMessage[i]
        secondLetter = encryptedMessage[i+1]

        firstPosition = string.ascii_lowercase.index(firstLetter)
        secondPosition = string.ascii_lowercase.index(secondLetter)

        #Append to the list if and only if the current value in the matrix is nonzero
        if theMatrix[firstPosition][secondPosition] != 0:
            probabilityList.append(theMatrix[firstPosition][secondPosition])

    #The sum of logarithms in the list is calcualted and returned as the fitness score
    return np.sum((np.array(probabilityList)))



#Calculates the fitness score of the deciphered ciphertext by using the popularity of bigrams from the transition matrix
def fitnessScore(theMessage, theMatrix):
    theMessage = ''.join(theMessage.split())

    sentenceScore = 0

    #Splits the message into an array composed of four letter elements
    someList = ([theMessage[i:i + 2] for i in range(0, len(theMessage), 2)])

    #Traverses each pairing in the created list, and increments to the score of the
    #sentence if the pairing is found in the transition matrix
    for item in someList:
        theItem = item.upper()

        firstLetter= theItem[0]
        secondLetter = theItem[1]

        #Retrieve the positions of the two letters
        firstPosition = string.ascii_uppercase.index(firstLetter)
        secondPosition= string.ascii_uppercase.index(secondLetter)

        if theMatrix[firstPosition][secondPosition]!=0:
            sentenceScore = sentenceScore +theMatrix[firstPosition][secondPosition]

    return sentenceScore






#Decrypts an encrypted message that is associated to the Caesar cipher
def decrypt(encryptedMessage, theMatrix):
    encryptedMessage = ''.join(encryptedMessage.split())

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    print("Encrypted message: ", encryptedMessage)


    keys = []
    scores = []

    #Brute forces all 26 combinations/shifts
    for i in range(26):

        shiftKey = i
        message = " "
        #Attempt to decrypt the message using the following shift key
        for letter in encryptedMessage:
            minimumIndex = alphabets.find(letter)
            locationOfLetterE = alphabets.find('e')
            moduloResult = (minimumIndex - shiftKey) % 26
            message += alphabets[moduloResult]

        #Measure the fitness score of the message per combination/shift
        returnedScore = fitnessScore(message, theMatrix)

        keys.append(message)
        scores.append(returnedScore)

    #Retrieve the encrypted message based on the highest score
    maxThing = scores.index(max(scores))


    print("Decrypted message with key: ", keys[maxThing],  " & ", maxThing)
    print()






main()