const express = require('express');
const path = require('path');
var fs = require('fs');
const bodyParser = require('body-parser');
var bot = require('./bot')


const app = express();

app.engine('html',require('express-art-template'))

app.use(express.static('public'));
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))


data_path = "data.html";

//主页
app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname, 'public/index.html'));
});


app.post('/do', function(req, res) {
	fs.writeFile('data.html'," 姓名:"+req.body.name+"<br\> 年龄:"+req.body.age+"<br\> 专业:"+req.body.subject+"<br\> 邮箱:"+req.body.mail+"\n",function(error){
		console.log("wriet error")
	});
	bot.visit();
	res.send("<script>alert('提交成功');window.location.href = '/';</script>");
});


app.route('/view')
  .get(function(req, res) {
    res.sendFile(path.join(__dirname, data_path));
  })
  .post(function(req, res) {
	fs.writeFile('data.html'," 姓名:"+req.body.name+"<br\> 年龄:"+req.body.age+"<br\> 专业:"+req.body.subject+"<br\> 邮箱:"+req.body.mail+"\n",function(error){
		console.log("write error")
	});
    res.redirect('/view');
  });

app.listen(80, '0.0.0.0');