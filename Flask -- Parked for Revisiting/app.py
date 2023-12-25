from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1>Hey there Adarsh, Welcome...!</h1>"

@app.route("/task")
def task():
    return "Task is to learn some Flask related concepts"

@app.route("/topic")
def get_topic():
    return "Topic being covered is 'API'"

@app.route("/table")
def html_tab():
    with open("D:\Github\PWSkills-Data-Science-Masters\Flask\html_sample_table.txt") as fh:
        tab = fh.read()
    
    return tab

@app.route("/user/<user_name>")
def user_accessing_page(user_name):
    return "Your username is: {}".format(user_name)


# to test below code open browser and hit- "http://192.168.29.192:5000/dig0axn2/user_input?q=OpenAI"
@app.route("/<user_name>/user_input")
def get_user_request(user_name):
    usr_input = request.args.get("q")

    return "User '{}' queried for : <b>{}</b>".format(user_name, usr_input)

##############################################################################
############################## MAIN START HERE ###############################
##############################################################################

if __name__ == "__main__":
    app.run(host = "0.0.0.0")