<?php
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$lecture_id = $_GET["lecture"];

	if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	
	$sql = "SELECT Lecture.lecture_id, QuizTopic.topic_id, QuizTopic.topic, QuizKeyword.keyword_id, QuizKeyword.keyword, QuizKeyword.keywordWeight 
			FROM Lecture 
			INNER JOIN QuizTopic ON Lecture.lecture_id = QuizTopic.lecture_id 
			INNER JOIN QuizKeyword ON QuizTopic.topic_id = QuizKeyword.topic_id 
			WHERE Lecture.lecture_id = '$lecture_id'";

	$result = $mysqli->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["topic"]."|".$row["keyword"]."|".$row["keywordWeight"]."|".$row["keyword_id"]."|".$row["topic_id"]."|";
		}
	}
	else {
		echo "NO DATA";
	}


	$mysqli->close();
