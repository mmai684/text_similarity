import requests

#web app parameters
#takes 2 strings and returns a similarity score
#index_dif - specifies how many index positions from current search position to look for a match
    #index dif accounts for ordering of words
    #a value of 1 is exact match. You can specify any number > 0. If ordering doesn't matter, set index_dif = -1

parameters = {
    "string1":"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
    "string2":"The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.",
    "index_dif": 5
    }

#post request
request = requests.post("http://localhost:5000/textsim", parameters)

#stores requst output in a json object
json_obj = request.json()

#output to console the score
print("Document Similarity Score: " + str(json_obj))
