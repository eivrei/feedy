<?php
	header('Content-type: text/plain; charset=utf-8');
	$db_username = "magnukun_secure";
	$db_password = "YEa2VJXHxmWQ";
	$servername = "mysql.stud.ntnu.no";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$lecture_id = $_GET["lecture"];
	
if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	
	$sql = "SELECT Lecture.lecture_id, Lecture.lectureDate, Lecture.lectureName FROM Lecture
			WHERE lecture_id = '$lecture_id'";
			

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["lectureDate"]."|".$row["lectureName"];
		}
	}
	else {
		echo "NO DATA";
	}


	$conn->close();
?>
