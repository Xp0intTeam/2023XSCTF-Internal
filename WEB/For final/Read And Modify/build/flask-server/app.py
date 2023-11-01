from flask import Flask, render_template, request, make_response,session
import redis
import os
import random
import string
from main import check

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
# Make a connection of the queue and redis
r = redis.Redis(host='redis', port=6379)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = str(request.form.get('url'))
        resp = check(url)
        return resp
    else:
        resp = make_response(render_template('index.html'))
        if not session.get('userID'):
            user = ''.join((random.choice(string.ascii_letters) for x in range(32)))
            r.mset({str(user + "_isAdmin"): "false"})
            session['userID']=user
        else:
            user = session.get('userID')
            flag = r.get(str(user + "_isAdmin"))
            if flag == b"true":
                session['flag']= str(os.environ['FLAG'])
            else:
                session['flag']= "flag{fake_flag}"
        return resp


if __name__ == "__main__":
    app.run('0.0.0.0')

