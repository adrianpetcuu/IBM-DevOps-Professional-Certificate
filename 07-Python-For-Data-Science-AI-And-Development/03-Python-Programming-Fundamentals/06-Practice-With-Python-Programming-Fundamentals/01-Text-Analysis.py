# Step 1: Define a string
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Step 2: Define the class and its attributes
class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # You will store the provided 'text' as an instance variable.
    def __init__(self, text):
        self.text = text

# Step 3: Implement a code to format the text in lowercase
class TextAnalzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

# Step 4: Implement a code to count the frequency of all unique words
# Press Shift+Enter to run the code.
class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

# Step 5: Implement a code to count the frequency of a specific word
class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


# Step 1: Create an instance of TextAnalyzer class
analyzed = TextAnalyzer(givenstring)

# Step 2: Call the function that converts the data into lowercase
print("Formatted Text:", analyzed.fmtText)

# Step 3: Call the function that counts the frequency of all unique words from the data
freqMap = analyzed.freqAll()
print(freqMap)

# Step 4: Call the function that counts the frequency of a specific word
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")