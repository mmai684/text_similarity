"""
    Author: My Mai
    Description:

    Development Criteria
    1) Do you count punctuation or only words? - Punctuation either by itself or connected to a word will count as a single word list item
   
    2) Which words should matter in the similarity comparison? - All words up to the length of the shorter text document. We also don't care about capitalization.. Apple and apple are the same word
    3) Do you care about the ordering of words? - We're allowing the user to decide the degree of how much ordering matters.
        They can set the index_dif variable to how many indexes away from the compared index do we want to look for matches.
        Setting index_dif = -1 will ignore ordering
    4) What metric do you use to assign a numerical value to the similarity?
            We're just using a basic calculation:
                Similarity Document Score = Matches / (Length of Longer Text Document)
    5) What type of data structures should be used?
            We're tokenizing the text into lists
            Based on the list length, a dictionary stores the lists and length for loop logic later on
        
"""
def text_similarity(sample_1, sample_2, index_dif):
    #Since we don't care about capitalization, make everything lowercase
    sample_1 = sample_1.lower()
    sample_2 = sample_2.lower()

    #tokenize strings into lists
    sample_1_list = sample_1.split()
    sample_2_list = sample_2.split()

    #determine number of items in each list
    len_1 = len(sample_1_list)
    len_2 = len(sample_2_list)

    #create dictionaries and assign shorter / longer text. If its the same length, we'll just assign the first text as the shorter
    if(len_1 <= len_2):
        text_dict = {
            "shorter_text" : sample_1_list,
            "short_len": len_1,
            "longer_text" : sample_2_list,
            "long_len": len_2
            }
    else:
        text_dict = {
            "shorter_text" : sample_2_list,
            "short_len": len_2,
            "longer_text" : sample_1_list,
            "long_len": len_1
            }
    #if user doesn't care about word ordering and sets index_dif = -1, we'll now set it to take on the length of the longer text input
    if(index_dif ==-1):
        index_dif = text_dict["long_len"]

    match = 0

    #loop through the larger text with each value of the shorter text, if a match is found and is less than index_dif, we'll count it as a match.
    #only account for the first instance a match is made, we don't want to count a match more than once.
    for i in range(text_dict["short_len"]):
       for z in range(text_dict["long_len"]):
            if (text_dict["shorter_text"][i] == text_dict["longer_text"][z] and abs(z-i) < index_dif):
                match+=1
                break

    #Calculate Similarity Score
    match_number = match / text_dict["long_len"]
    #for debugging purposes
    #print("Number of word matches: " + str(match))
    #print(text_dict["long_len"])
    #print("Document Similarity Score: " + str(match_number))
    return match_number
            
