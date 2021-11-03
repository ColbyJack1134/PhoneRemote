<?php
	header('Access-Control-Allow-Origin: *');
    header('Access-Control-Request-Headers: *');
	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    	$json = file_get_contents('php://input');
        if(isset($_POST['response'])){
        	file_put_contents('command.txt', '');
        }
        else{
        	file_put_contents('command.txt', $json);
            echo "Success!";
       	}
	}
?>