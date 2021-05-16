from flask import Flask , render_template
app = Flask(__name__)
print(__name__)

@ app.route("/play")
def play_level_1():
    return render_template("index.html")


@ app.route("/play/<int:num>")
def play_level_2(num):
    return render_template("index2.html", times=num)


@ app.route("/play/<int:num>/<color>")
def play_level_3(num, color):
    return render_template("index3.html", times=x, c=color)


@app.errorhandler(404)
def page_not_found(e):
    return "sorry , Try again"


if __name__ == "__main__":
    app.run(debug=True)
