"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template("form.html")

@app.route('/results')
def show_results():
    """Show resulting message."""
    option1=request.args.get("cheery")
    option2=request.args.get("honest")
    option3=request.args.get("dreary")
    # options=[option1, option2, option3]
    # return render_template("results.html", option1=option1, option2=option2, option3=option3)
    if option1:
        msg="YAY!"
    elif option2:
        msg="HONEST"
    else:
        msg="DREARY"
    # return render_template("results.html", options=options)
    return render_template("results.html", msg=msg)

@app.route('/save-name', methods=["POST"]) #still confused about post method being used and not being used
def save_name():
    """Save name from form."""
    session["name"]=request.form.get("name")

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
