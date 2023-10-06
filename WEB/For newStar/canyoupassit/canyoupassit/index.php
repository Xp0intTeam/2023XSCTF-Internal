<?php
highlight_file(__FILE__);
error_reporting(0);
if ($_POST['a1'] != $_POST['b1'] && md5($_POST['a1'] == md5($_POST['b1']))){
    echo "恭喜你过了第一关!";
} else {
    die("就这?");
}
if ($_POST['key'] == md5($_POST['key'])) {
    echo "恭喜你过了第二关!";
} else {
    die("再看看?");
}
$now = time();
if ($_POST['a2'] != $_POST['b2'] && str_starts_with($_POST['a2'], $now) && str_starts_with($_POST['b2'], $now) && md5($_POST['a2'] === md5($_POST['b2']))){
    echo "恭喜你过了第三关!";
    include "/flag";
} else {
    die("真可惜，就差最后一步了");
}


