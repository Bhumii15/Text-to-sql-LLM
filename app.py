from dotenv import load_dotenv
load_dotenv() #load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#Function to retrive query from the sql database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name New_Student and has the following columns - NAME, CLASS, 
    SECTION,MARKS,ADDRESS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM New_Student ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM New_Student 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

"""
]

#Streamliy App

st.set_page_config(page_title="I can Retrive Any SQL query")
st.header("Gemini App To Retrive SQL Data")

question = st.text_input("Input: ",key="input")

submit = st.button("Ask the question")

#If submit is clicked 
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"stu.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)