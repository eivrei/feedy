<?php
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$id = $_GET["id"];

	if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	//Distinct not needed?
	$sql = "SELECT DISTINCT Lecture.lecture_id, QuizTopic.lecture_id, QuizTopic.topic_id, QuizTopic.topic FROM Lecture 
			INNER JOIN QuizTopic ON Lecture.lecture_id = QuizTopic.lecture_id
			WHERE Lecture.lecture_id='$id'";

	$result = $mysqli->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["topic"]."|".$row["topic_id"]."|"; //note that topic comes first - vital for .js script
		}
	}
	else {
		echo("NO DATA");
	}


	$mysqli->close();
