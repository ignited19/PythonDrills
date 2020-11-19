class StringOperations(object):

    #=======================================================
    # The purpose of this function is to determine if a
    # string contains all unique characters. The basic
    # attribute to determine if a string contains unique
    # characters is the character count. Luckily with 
    # python, we can use foreach along with the method
    # .count. This negates the need for CharCount array
    # or multiple iterations through the string. I also
    # provided a run down of what characters are duplicated
    # in the string
    #=======================================================
    def UniqueCharCheck():
        ContinueCheckingStr = 1
        

        while (int(ContinueCheckingStr) == 1):

            UserInput = input("Hello! This module's function is check to see if a string contains all unique characters. So lets get started! Please enter a string \n").lower()
            DuplicateChar = {}

            #===================================================
            # Iterate through the user input, checking the char
            # count
            #===================================================
            for Element in UserInput:
                CurrentCharCount = UserInput.count(Element)

                if(CurrentCharCount > 1 ):
                    DuplicateChar[Element] = CurrentCharCount
            
            #===================================================
            # In the instance there are duplicate characters,
            # display the characters to the user.
            #===================================================
            if(len(DuplicateChar)>0):
                print("Okay, so it appears there are some duplicate characters: ")
                
                for Element in DuplicateChar:
                    print(Element)
            
            #====================================================
            # Ask user if they would like to continue entering
            # strings
            #====================================================
            ContinueCheckingStr = input("Would you like to check another string? 1 = Yes \n")

            print(ContinueCheckingStr)

            if(ContinueCheckingStr.isdigit() == False):
                print("Hmm, please enter either 0 or 1")


    #====================================================
    # Check to see if two strings contain more than 1
    # different character
    #====================================================
    def CheckStringDiff ():
        String_A = input("Hello! Lets get started! Please give me the first string to check \n")
        String_B = input("Awesome! Now lets give me the second string to check against the first \n")
 
        
        #Check to see if a character replacement will make the two strings identical 
        def CharReplaceCheck():
            NumberOfDifferences = 0

            #Iterate through both strings to see which characters need replacement
            for i in range(len(String_A)):
                if(String_A[i] != String_B[i]):
                    NumberOfDifferences += 1
            
            print(NumberOfDifferences <= 1)

            return NumberOfDifferences <= 1
            
            
            #Iterate through both strings to see which characters need replacement
            for i in range(len(String_A)):
                if(String_A[i] != String_B[i]):
                    NumberOfDifferences += 1
           
            return NumberOfDifferences <= 1
        
         #====================================================
         # Check to see the amount of character differences 
         # between to strings
         #====================================================
        def InsertCheck():
            StringUpperLimit_A = len(String_A)
            StringUpperLimit_B = len(String_B)
            NumberOfDifferences = 0
            Index_A = 0
            Index_B = 0

            while(Index_A < StringUpperLimit_A and Index_B < StringUpperLimit_B):
                if String_A[Index_A] != String_B[Index_B]:
                    NumberOfDifferences += 1
                    Index_A += 1
                else:
                    Index_A += 1
                    Index_B += 1
            
            
            return NumberOfDifferences <= 1


        #Main for this function. Will determine what sub function to use for the two strings
        if(len(String_A) == len(String_B)):
            Result = CharReplaceCheck()
        elif (len(String_A)-1 == len(String_B) or len(String_A)+1 == len(String_B)):
            Result = InsertCheck()
        else: 
           Result = False

        print("Magic computer, tell us do these two strings containt no more than 1 char difference? " + str(Result))
        

    #================================================
    # Function: Compress strings i.e aabb = a2b2 to
    # view how much a speicific character there is in
    # the string
    #===============================================
    def StringCompression():
        User_Str = input("Lets compress a string! Please enter in a string")
        CharCount = {}
   
        for x in User_Str:
            if x not in CharCount:
                CharCount[x] = User_Str.count(x)
        
        print(CharCount)
            





        





        


