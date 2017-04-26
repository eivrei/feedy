<?php
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$lecture_id = $_GET["lecture"];

	if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	
	$sql = "SELECT Lecture.lectureStats FROM Lecture
			WHERE Lecture.lecture_id = '$lecture_id'";

	$result = $mysqli->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["lectureStats"];
		}
	}
	else {
		echo "NO DATA";
	}


	$mysqli->close();
