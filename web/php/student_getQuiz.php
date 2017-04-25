<?php
	$servername = "mysql.stud.ntnu.no";
	$db_username = "magnukun_secure";
	$db_password = "YEa2VJXHxmWQ";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$conn->set_charset("utf8");
	$id = $_GET["id"];

	if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	//Distinct not needed?
	$sql = "SELECT DISTINCT Lecture.lecture_id, QuizTopic.lecture_id, QuizTopic.topic_id, QuizTopic.topic FROM Lecture 
			INNER JOIN QuizTopic ON Lecture.lecture_id = QuizTopic.lecture_id
			WHERE Lecture.lecture_id='$id'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["topic"]."|".$row["topic_id"]."|"; //note that topic comes first - vital for .js script
		}
	}
	else {
		echo("NO DATA");
	}


	$conn->close();
?>