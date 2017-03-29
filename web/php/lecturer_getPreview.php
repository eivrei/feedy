<?php

	$db_username = "magnukun_secure";
	$db_password = "YEa2VJXHxmWQ";
	$servername = "mysql.stud.ntnu.no";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$lecture_id = $_GET["lecture"];

	if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	
	$sql = "SELECT Lecture.lecture_id, QuizTopic.topic_id, QuizTopic.topic, QuizKeyword.keyword_id, QuizKeyword.keyword, QuizKeyword.keywordWeight 
			FROM Lecture 
			INNER JOIN QuizTopic ON Lecture.lecture_id = QuizTopic.lecture_id 
			INNER JOIN QuizKeyword ON QuizTopic.topic_id = QuizKeyword.topic_id 
			WHERE Lecture.lecture_id = '$lecture_id'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["topic"]."|".$row["keyword"]."|".$row["keywordWeight"]."|".$row["keyword_id"]."|".$row["topic_id"]."|";
		}
	}
	else {
		echo "NO DATA";
	}


	$conn->close();
?>
