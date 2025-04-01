from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = request.form.get("expression", "")

    button = request.form.get("button", "")

    if button == "C":
        expression = ""
    elif button == "=":
        try:
            expression = str(eval(expression))
        except ZeroDivisionError:
            expression = "Error: Division by zero"
        except:
            expression = "Error"
    elif button:
        expression += button

    return render_template("calculator.html", expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
