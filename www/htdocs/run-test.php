<?php
$k = $_REQUEST['k'];

if (!empty($k))
{
	// decode
// 	passthru('python ../cgi-bin/decode')

	$k = trim($k);
	passthru('python ../cgi-bin/test/'.$k.'.py');
}

?>