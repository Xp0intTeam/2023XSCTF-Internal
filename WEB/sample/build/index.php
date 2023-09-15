<?php
    $flag='flag{82aff90d-1031-48ee-a979-fcccaa655901}';

    header('flag:'.base64_encode($flag));

$html=<<<HTM
<!DOCTYPE html>
<html>
<head>
	<title>Do you find me?</title>
</head>
<body>
	<center>
		<h1>
			Ha Ha Ha, You Must Find Flag, First!
		</h1>
	</center>
</body>
</html>
HTM;
echo $html;