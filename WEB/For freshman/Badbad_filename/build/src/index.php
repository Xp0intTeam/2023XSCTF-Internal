<?php
error_reporting(0);
include 'flag.php';

if(!isset($_GET['filename'])){
    die("GET me a filename and I'll include it!");
}
$filename = $_GET['filename'];
include 'blacklist.php';

if(strstr($filename,"php")){
    $filename = str_replace("php","",$filename);
    echo("Badboy using 'php', I'll delete it! <br>");
}
if(strstr($filename,"filter")){
    $filename = str_replace("filter","",$filename);
    echo("Badboy using 'filter', I'll delete it! <br>");
}
if(strstr($filename,"base")){
    $filename = str_replace("base","",$filename);
    echo("Badboy using 'base', I'll delete it! <br>");
}
echo("include('" . $filename . "')");
include($filename);

?>