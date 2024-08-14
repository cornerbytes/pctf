from flask import Flask, render_template, request
import subprocess, os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        except_char = ["$",";", "|", "&", "/", "{", "}","\\"]
        text = request.form.get("text")
        if not any(char in text for char in except_char):
            result = fig(text)
            return render_template("index.html", res=result)
        else:
            return render_template("index.html", res="")

def fig(text):
    cmd = "/bin/sh -c \"figlet " + text + "\""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return result

if __name__ == "__main__":
    app.run("0.0.0.0", port=1080)

