from flask import Flask, render_template, request



app = Flask(__name__)

app.config['listofitems']=[]


@app.route("/")
def mainpage():
    return render_template("index.html",errormessage="",listofitems=app.config['listofitems'])

@app.route("/createitems", methods=['GET','POST'])
def additems():
    if request.method=='POST':
        if len(app.config['listofitems'])<5:
            item=request.form.get('evaluationitems')
            print(app.config['listofitems'])
            app.config['listofitems'].append(item)
            return render_template("index.html",errormessage="",listofitems=app.config['listofitems'])

        else:
            return render_template("index.html",errormessage="You have added maximum Number of Items, please proceed ahead by click on 'Next'",listofitems=app.config['listofitems'])







if __name__ == "__main__":
    app.run(debug=True, port=8000)
