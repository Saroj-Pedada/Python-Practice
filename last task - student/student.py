import pandas as pd

df = pd.read_csv("student.csv")
print(df.head())

print(df["name"].head())

df_new = df.drop(["id"],axis=1)
print(df_new.head())

avg_marks = df["mark"].mean()
print(avg_marks)

df_male = df[df["gender"]=="male"]
print(df_male.head())
avg_male = df_male["mark"].mean()
print(avg_male)

df_female = df[df["gender"]=="female"]
print(df_female.head())
avg_female = df_female["mark"].mean()
print(avg_female)

from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/avg")
def avg():
    return "The average marks of the class are: "+str(avg_marks)

@app.route("/avg-male")
def avgmale():
    return "The average marks of males in the class are: "+str(avg_male)

@app.route("/avg-female")
def avgfemale():
    return "The average marks of males in the class are: "+str(avg_female)

@app.route("/")
def index():
    return str(df)

serve(app,port=8080,host='0.0.0.0')