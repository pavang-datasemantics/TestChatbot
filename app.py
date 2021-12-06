from bot import chatbot
import pyodbc
import textwrap
import datetime
import uuid
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

session_id = uuid.uuid4()

@app.route("/get")
def get_bot_response():

    userText = request.args.get('msg')

    response = str(chatbot.get_response(userText))

    server = 'DESKTOP-KBT39NE\SQLEXPRESS'   ##MS-SQL server name
    database = 'sample1'                    ##enter your database name here

    ##connection
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                        SERVER=' + server + '; \
                        DATABASE=' + database +';\
                        Trusted_Connection=yes;')
    cursor = conn.cursor()
    log = textwrap.dedent("""
                        insert into chat_log(session_id, user_text, user_text_time_stamp, bot_text, bot_text_time_stamp)
                        values(?,?,GETDATE(),?,GETDATE())
                       """)
    cursor.execute(log,session_id,userText,response)
    conn.commit()

    return response

if __name__ == "__main__":
    app.run()