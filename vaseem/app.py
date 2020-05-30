
import pandas as pd
from flask import Flask,render_template,request
import os 
from shutil import copyfile
app=Flask(__name__)
wsgi_app=app.wsgi_app
@app.route('/', methods=["GET","POST"])
def vaseem():
    if request.method=="POST":
        file=request.files["file"]
        file.save(os.path.join(r"C:\Users\w10\newproj\vaseem\uploads",file.filename))
        f=open(r"C:\Users\w10\newproj\vaseem\lol.txt","a")
        f.write(request.form.get("company"))
        f.close()
        a=[]
        a.append(request.form.get("Zip"))
        return render_template("index.html",message=a[0])
        srcdf = pd.read_csv(r'C:\Users\w10\newproj\vaseem\uploads\test_dataset.csv')
        destdf = pd.read_csv(r'C:\Users\w10\newproj\vaseem\uploads\dest.csv')
        copyfile(src,dest)
        df=pd.read_excel(r'C:\Users\w10\newproj\vaseem\dest.xlsx',header=None)
        b=[]
        for i in range(len(df.columns)):
            b.append(df[i][0])
        for i in b:
            if request.form.get("fname")==i:
                   for j in range(len(df.columns)):
                          if df[j][0]==i:
                                df[j][0]=="First Name"


    return render_template("index.html",message="Upload")
def akram():
    if request.method =="POST":
        f=open(r"C:\Users\w10\newproj\vaseem\lol.txt","a")
        f.write("NOw the file has more content")
        f.close()

    return 0

  
    return a
if __name__=='__main__':
    import os
    HOST=os.environ.get('SERVER_HOST','localhost')
   
    try:
        PORT=int(os.environ.get('SERVER_HOST','5555'))
    except ValueError:
        PORT=5555
    app.run(HOST,PORT,debug=True)
