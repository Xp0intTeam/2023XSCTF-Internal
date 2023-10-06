<?php
include "config.php";
$id=isset($_GET["id"])?$_GET["id"]:"1";
$sql="select * from images where id='{$id}'";
$result=mysqli_query($con,$sql);
$row=mysqli_fetch_array($result,MYSQLI_ASSOC);
$count=preg_match("/(\.\.)|(config)/i",$row["path"]);
if ($count>0)
{
    die("no no no ");
}

$path="./" . $row["path"];
header("Content-Type: image/jpeg");
readfile($path);