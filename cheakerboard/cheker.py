from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "hello in checkerboard"

@app.route("/<num1>/<num2>")
def chek_board(num1,num2):
    input1=int(num1)
    input2=int(num2)
    return render_template("basic.html", input1=input1, input2=input2)

if __name__ == "__main__":
    app.run(debug = True) 