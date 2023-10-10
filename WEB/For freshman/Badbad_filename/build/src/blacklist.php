<?php
if(preg_match("/file/i", $filename)){
    die("Badbad 'file' in the filename ~");
}
if(preg_match("/data/i", $filename)){
    die("Badbad 'data' in the filename ~");
}
if(preg_match("/input/i", $filename)){
    die("Badbad 'input' in the filename ~");
}
?>