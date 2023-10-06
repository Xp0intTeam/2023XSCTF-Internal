<?php
include 'flag.php';
extract($_GET);
if (isset($wsf)) {
    $xmm = trim(file_get_contents($zm));
    if ($xmm == $wsf) {
        if (!empty($xlq)) {
            $xw = trim(file_get_contents($fn));
            if ($xlq === $xw) {

                echo "<p>$flag</p>";
            } else {
                echo '<p>no no no </p>';
            }
        } else 'You cant do that!!';
    } else {
        echo 'hacker!!';
    }
} else {
    highlight_file(__FILE__);
}
?>
