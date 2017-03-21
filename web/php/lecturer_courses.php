<?php

	$db_username = "magnukun_pu100";
	$db_password = "pugruppe100";
	$servername = "mysql.stud.ntnu.no";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$id = $_GET["id"]; 
	if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}

	$sql = "SELECT Course.coursecode, Course.coursename, Parallel.programmes FROM Lecturer
			INNER JOIN LecturerParallel ON Lecturer.lecturer_id = LecturerParallel.lecturer_id
			INNER JOIN Parallel ON LecturerParallel.parallel_id = Parallel.parallel_id
			INNER JOIN Course ON Parallel.coursecode = Course.coursecode
			WHERE Lecturer.username='$id'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["coursecode"]."|".$row["coursename"]."|".$row["programmes"]."|";
		}
	}
	else {
		print_r($result);
	}


	$conn->close();
?>
