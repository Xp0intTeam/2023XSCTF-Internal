from flask import Flask
from flask import request
from flask import render_template_string,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    username = request.args.get('name')
    password = request.args.get('password')
    print("登录尝试:{}-{}".format(username,password))
    
    if username != None:
        string = '''alert("{},没买车票不能上车!!!");'''.format(username)
    else:
        string = " "
    
    
    temp = ''' <!DOCTYPE html>
<html>
<head>
    <title>StarRailWay</title>
    <link rel="stylesheet" type="text/css" href="static/1.css">
    <script>
        %s
    </script>
</head>
<body>
    <div class="center-content">
        <form method="GET" action="/">
            <label for="name">用户名:</label>
            <input type="text" id="name" name="name" value="" required><br><br>
            
            <label for="password">&nbsp;密码:&nbsp;&nbsp;</label>
            <input type="password" id="password" name="password" value="" required><br><br>
            
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
''' %(string)
    
    return render_template_string(temp)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0' , port=8080)
