import boto3
from flask import Flask, render_template

app = Flask(__name__)

def listbucket():
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('xxxxxxxxxxx') #replace with your bucket name
    li=[]

    for my_bucket_object in my_bucket.objects.filter(Prefix="home/sarangunasekara/"):
        if my_bucket_object.key !="home/sarangunasekara/":
            li.append(my_bucket_object.key)
    return li

    
@app.route('/')
def homepage():
    try:
        objectlist=listbucket()
        return render_template('home.html', bucketlist=objectlist)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

