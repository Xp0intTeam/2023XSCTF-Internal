<?php
header('Content-Type: text/html; charset=utf-8');
error_reporting(0);
if (!is_dir("uploads")) {
    mkdir("uploads", 0777, true);
}
if (isset($_POST['submit'])) {
    $ext_arr = array('jpg', 'png', 'gif');
    $file_name = $_FILES['upload_file']['name'];
    $temp_file = $_FILES['upload_file']['tmp_name'];
    $file_ext = substr($file_name, strrpos($file_name, ".") + 1);
    $upload_file = 'uploads' . '/' . $file_name;
    if (move_uploaded_file($temp_file, $upload_file)) {
        $msg = $upload_file.'上传成功！'.'</br>';
        if (in_array($file_ext, $ext_arr)) {
            $img_path = 'uploads' . '/' . md5(time()) . "." . $file_ext;
        } else {
        $msg.='你想干嘛？嗨客';
            $img_path = 'uploads' . '/' . md5(time()) . "." . 'jpg';
	}
	sleep(1);
        rename($upload_file, $img_path);
        $is_upload = true;
        $msg =$msg. $img_path;
    } else {
	$msg=$temp_file.'/'.$upload_file;
        $msg .= '上传出错！';
    }
}
?>
<!DOCTYPE html>
<html lang="en" class="no-js">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Upload</title>
    <link rel="stylesheet" type="text/css" href="css/normalize.css" />
    <link rel="stylesheet" type="text/css" href="css/demo.css" />
    <!--必要样式-->
    <link rel="stylesheet" type="text/css" href="css/component.css" />
    <!--[if IE]>
<script src="js/html5.js"></script>
<![endif]-->
</head>

<body>
    <div class="container demo-1">
        <div class="content">
            <div id="large-header" class="large-header">
                <canvas id="demo-canvas"></canvas>
                <div class="logo_box">
                    <h3>XSCTF</h3>
                    <form enctype="multipart/form-data" method="post">
                        <input class="input_file" style="cursor: pointer;" type="file" name="upload_file" />
                        <input class="button" style="color:white; background:#0096e6; line-height: 20px; text-align: center; font-size: 20px; border-radius: 50px;margin:10px;" type="submit" name="submit" value="上传" />
                    </form>
                    <div id="msg">
                        <?php
                        if ($msg != null) {
                            echo "提示：" . $msg;
                        }
                        ?>
                    </div>

                </div>
            </div>
        </div>
    </div><!-- /container -->
    <script src="js/TweenLite.min.js"></script>
    <script src="js/EasePack.min.js"></script>
    <script src="js/rAF.js"></script>
    <script src="js/demo-1.js"></script>
</body>

</html>
