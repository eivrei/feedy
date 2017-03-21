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

	$sql = "SELECT Course.CourseCode, Course.CourseName, Parallel.Programmes FROM Lecturer
			INNER JOIN LecturerParallel ON Lecturer.UserID = LecturerParallel.LecturerID
			INNER JOIN Parallel ON LecturerParallel.ParallelID = Parallel.ParallelID
			INNER JOIN Course ON Parallel.CourseCode = Course.CourseCode
			WHERE Lecturer.Username='$id'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["CourseCode"]."|".$row["CourseName"]."|".$row["Programmes"]."|";
		}
	}
	else {
		print_r($result);
	}


	$conn->close();
?>
