# text_similarity

This is a python application that compares the similarity of two strings.

Similarity is calculated by 

(# of word matches) / (# of total words in larger text)

1 is exact match
0 is not a match

Other considerations:
-punctuation matters
-don't care about capitalization. Apple and apple are the same

Requirements: 
You will need to have docker installed onto your local pc.
You will also need python 3, and the request library if you plan on using flask_sim_api_call.py to post to the flask application

How to run the application:
1) Navigate to where you cloned the repository
2) In the command line, you'll want to create the container with the flask application
3) This can be accomplished in two steps. Creating the docker image, and then running the image in a container
	a) docker build -t text-sim .
    b) docker run -p 5000:5000 text-sim
4) The flask application should be running in the container now. I've created a script that will post to the web application and return a similarity score. Navigate back to the cloned directory and find flask_sim_api_call.py, edit with idle. *Note this is what I used to test it, other tools can be used.
5) Post takes 3 parameters, which can be found in the script. Summary below
	a) string1 - the first string
	b) string2 - the second string
	c) index_dif - this takes an integer value greater than 0 or -1. 
    	a value of 1 will do an exact match
    	a value of 5 will count a match if found within 5 positions from the current index
    	a value of -1 will disregard order and just search to find if a word matches
6) Run the script using F5


Let me know what you think!
