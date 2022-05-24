from flask import Flask, render_template, request
import pandas as pd 
import numpy as np 
import pickle

model = pickle.load(open('ipll.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def intro():
    return render_template('home.html')


@app.route('/predict', methods = ['POST'])
def index():
    predarray = list()
    batteam = list()
    bowlteam = list()

    bat = request.form["battingteam"]
    

    if bat=="Chennai Super Kings":
        batteam = [1,0,0,0,0,0,0,0]
    elif bat=="Delhi Capitals":
        batteam = [0,1,0,0,0,0,0,0]
    elif bat=="Kings XI Punjab":
        batteam = [0,0,1,0,0,0,0,0]
    elif bat=="Kolkata Knight Riders":
        batteam = [0,0,0,1,0,0,0,0]
    elif bat=="Mumbai Indians":
        batteam = [0,0,0,0,1,0,0,0]
    elif bat=="Rajasthan Royals":
        batteam = [0,0,0,0,0,1,0,0]
    elif bat=="Royal Challengers Bangalore":
        batteam = [0,0,0,0,0,0,1,0]
    elif bat=="Sunrisers Hyderabad":
        batteam = [0,0,0,0,0,0,0,1]

    bowl = request.form["bowlingteam"]

    if bowl=="Chennai Super Kings":
        bowlteam = [1,0,0,0,0,0,0,0]
    elif bowl=="Delhi Capitals":
        bowlteam = [0,1,0,0,0,0,0,0]
    elif bowl=="Kings XI Punjab":
        bowlteam = [0,0,1,0,0,0,0,0]
    elif bowl=="Kolkata Knight Riders":
        bowlteam = [0,0,0,1,0,0,0,0]
    elif bowl=="Mumbai Indians":
        bowlteam = [0,0,0,0,1,0,0,0]
    elif bowl=="Rajasthan Royals":
        bowlteam = [0,0,0,0,0,1,0,0]
    elif bowl=="Royal Challengers Bangalore":
        bowlteam = [0,0,0,0,0,0,1,0]
    elif bowl=="Sunrisers Hyderabad":
        bowlteam = [0,0,0,0,0,0,0,1]

    over = float(request.form["overs"])

    run = int(request.form["runs"])

    wicket = int(request.form["wickets"])

    runs5 = int(request.form["runs_in_prev_5"])

    wick5 = int(request.form["wickets_in_prev_5"])

    predarray = batteam + bowlteam + [over, run, wicket, runs5 ,wick5]

    finalscore = np.array([predarray])

    prediction = int(model.predict(finalscore)[0])

    return render_template('result.html', less = prediction-10, more = prediction+10, bats = bat)

if __name__ == "__main__":
    app.run(debug=True)