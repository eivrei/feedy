<?php

	$db_username = "magnukun_pu100";
	$db_password = "pugruppe100";
	$servername = "mysql.stud.ntnu.no";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);

	if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	$login_username = $_POST["username"];
	$login_password = $_POST["password"];
	
	$page = "../index.html";
	/*
	redirect($page);
	*/
	$sql = "SELECT * FROM Lecturer WHERE Lecturer.Username= '$login_username' AND Lecturer.Password = '$login_password'";
	$userlist = $conn->query($sql);
	
	session_start();
	$_SESSION['login_user'] = "WRONG"; //Dummyvalue for failed login
	
	if ($userlist->num_rows > 0) {
		$_SESSION['login_user']= $login_username; //saved session variable for username - might not be needed
		$row = $userlist->fetch_assoc();
		$username = $row["Username"];
		echo $username;
	}
	else {
		echo "WRONG"; //Value to check in JS-side of login
	}


	$conn->close();
?>
