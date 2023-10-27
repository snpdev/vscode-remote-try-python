#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

# prompt the user input one of  three options: rock, paper, or scissors.
user_choice = input("Do you choose rock, paper or scissors?")

# print the user's choice
print("user choice: " + user_choice.lower())  



