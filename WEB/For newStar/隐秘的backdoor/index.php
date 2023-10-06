<?php
error_reporting(0);
highlight_file(__FILE__);
$cmd = $_POST['cmd'];
if(isset($_POST['cmd'])){
    phpinfo();
    die("不要这样！TuT");
} else {
    $cmd = $_POST['cmd'];
    eval($cmd);
}
?>