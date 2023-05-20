from flask import Flask, render_template, request



app = Flask(__name__)

app.config['listofitems']=[]
app.config['listoffactor']=[]


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

@app.route("/pageAction", methods=['GET','POST'])
def firstPageActions():
    if request.method=='POST':
        submitType=request.form.get('submitType')
        if submitType=='reset':
            app.config['listofitems']=[]
            app.config['listoffactor']=[]
            return render_template("index.html",errormessage="",listofitems=app.config['listofitems'])
        if submitType=='next':
            return render_template("nextpage.html",errormessage="",listoffactor=app.config['listoffactor'])



@app.route("/nextpage.html")
def nextpage():
    return render_template("nextpage.html",errormessage="",listoffactor=app.config['listoffactor'])

@app.route("/pageAction2", methods=['GET','POST'])
def secondPageActions():
    if request.method=='POST':
        submitType=request.form.get('submitType')
        if submitType=='back':
            return render_template("index.html",errormessage="",listofitems=app.config['listofitems'])
        if submitType=='next':
            return render_template("finalpage.html",errormessage="",listoffactor=app.config['listoffactor'])



@app.route("/createfactors", methods=['GET','POST'])
def addfactors():
    if request.method=='POST':
        if len(app.config['listoffactor'])<5:
            item=request.form.get('factoritems')
            print(app.config['listoffactor'])
            app.config['listoffactor'].append(item)
            return render_template("nextpage.html",errormessage="",listoffactor=app.config['listoffactor'])
        else:
            return render_template("nextpage.html",errormessage="You have added maximum Number of Items, please proceed ahead by click on 'Next'",listoffactor=app.config['listoffactor'])


@app.route("/pageAction3", methods=['GET','POST'])
def finalPageActions():
    if request.method=='POST':
        submitType=request.form.get('submitType')
        if submitType=='back':
            return render_template("nextpage.html",errormessage="",listoffactor=app.config['listoffactor'])
        if submitType=='calculate':
            return render_template("finalpage.html",errormessage="Calculating",listoffactor="")



@app.route("/finalpage.html")
def finalpage():
    return render_template("finalpage.html",errormessage="",listoffactor=app.config['listoffactor'])





if __name__ == "__main__":
    app.run(debug=True, port=8000)
