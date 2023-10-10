<?php
highlight_file(__FILE__);
echo("Boys and Girls welcome to XSCTF2023!!! Now try to eval eval word~");
echo "<br>";
$xsctf=($_GET['xsctf']);
if(preg_match("/cat|more|less|head|tac|tail|nl|od|vim|uniq|system|proc_open|shell_exec|popen| /i", $xsctf)){
    die('nonononononoooo~');
}else{
    echo("Goodjob! Go on! ");
}

if(isset($_POST['Xp0int'])&&isset($_POST['Sloth'])){
    if($_POST['Xp0int']!==$_POST['Sloth']&& md5($_POST['Xp0int'])===md5($_POST['Sloth'])){
        echo("You succeed!!");
        echo "<br>";
        eval($xsctf);
    }else{
        die("try harderrrr~");
    }
}
?>