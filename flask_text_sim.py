from flask import Flask, jsonify, request
#textsim module has our text similarity functio text_similarity
import textsim

app = Flask(__name__)


#creates the web call end point and post method
@app.route('/textsim', methods = ['POST'])
def dashboard():
    #requests for 3 parameters
    sample_1 = request.form.get("string1")
    sample_2 = request.form.get("string2")
    index_dif = request.form.get("index_dif")

    #using the 3 parameters above, text_similarity returns a score
    return jsonify(textsim.text_similarity(sample_1,sample_2,int(index_dif)))

if __name__ == '__main__':
    #allows for the web app to run locally on pc when in container
    app.run(host='0.0.0.0', debug = True, port=5000)
    
