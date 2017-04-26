<?php
	header('Content-type: text/plain; charset=utf-8');
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$lecture_id = $_GET["lecture"];
	
if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	
	$sql = "SELECT Lecture.lecture_id, DATE_FORMAT(Lecture.lectureDate, '%Y-%m-%d %H:%i') AS lectureDate, Lecture.lectureName FROM Lecture
			WHERE lecture_id = '$lecture_id'";
			

	$result = $mysqli->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["lectureDate"]."|".$row["lectureName"];
		}
	}
	else {
		echo "NO DATA";
	}


	$mysqli->close();
