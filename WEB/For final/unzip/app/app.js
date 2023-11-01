const createError = require('http-errors');
const express = require('express');
const fs = require('fs');
const fileUpload = require('express-fileupload');
const child_process = require('child_process');

const app = express();

const uploadDir = "./public/upload/"

app.use(express.static('public'));
app.use(fileUpload());

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.post("/upload", async function (req, res, next) {
    if (!req.files || !req.files.file) {
        res.json({error: "非法请求"})
        return
    }
    if (!req.files.file.name.endsWith("zip")) {
        res.json({error: "只允许上传zip文件"})
        return
    }
    let fileName = req.files.file.md5
    let fileData = req.files.file.data
    fs.writeFileSync(uploadDir + fileName, fileData);
    await child_process.exec("unzip " + uploadDir + fileName + " -d " + uploadDir);
    res.json({msg: "解压成功，解压的文件在upload目录"});
})


app.use(function (req, res, next) {
    res.json({error: "page not found"})
});


app.listen(3000, () => {
    console.log("server start")
})
