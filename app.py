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
            return render_template("finalpage.html",errormessage="",listoffactor=app.config['listoffactor'],listofitems=app.config['listofitems'])



@app.route("/createfactors", methods=['GET','POST'])
def addfactors():
    if request.method=='POST':
        if len(app.config['listoffactor'])<5:
            item=request.form.get('factoritems')
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
            factorweight= request.form.getlist('factorweight')
            itemsweight= request.form.getlist('itemsweight')
            factors=listoffactor=app.config['listoffactor']
            items=listofitems=app.config['listofitems']
            print(itemsweight)
            yindex=0
            FINAL_SCORE=[]
            for item in items:
                index=0
                sum=0
                for factor in factors:
                    sum=sum+(int(factorweight[index])*int(itemsweight[yindex]))
                    #print(f'{factor} weight is {factorweight[index]}')
                    index+=1
                    #print(f'{item} score is {itemsweight[yindex]}')
                    yindex+=1
                    
                FINAL_SCORE.append((item,sum))

            print(FINAL_SCORE)



            return render_template("finalpage.html",errormessage="Calculating",listoffactor=app.config['listoffactor'],listofitems=app.config['listofitems'])



@app.route("/finalpage.html")
def finalpage():
    return render_template("finalpage.html",errormessage="",listoffactor=app.config['listoffactor'],listofitems=app.config['listofitems'])





if __name__ == "__main__":
    app.run(debug=True, port=8000)
