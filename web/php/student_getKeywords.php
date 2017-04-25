<?php
	$servername = "mysql.stud.ntnu.no";
	$db_username = "magnukun_secure";
	$db_password = "YEa2VJXHxmWQ";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$conn->set_charset("utf8");
	$idArray = json_decode(stripslashes($_POST['idArray']));
	$idImplode = implode(',', $idArray);
	
	if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	//Distinct not needed?
	
	$sql = "SELECT DISTINCT QuizTopic.topic_id, QuizKeyword.keyword_id, QuizKeyword.keyword, QuizKeyword.keywordWeight FROM QuizTopic 
			INNER JOIN QuizKeyword ON QuizTopic.topic_id = QuizKeyword.topic_id
			WHERE QuizTopic.topic_id IN ( $idImplode )";
	
	$result = $conn->query($sql);
	session_start();
	
	//keep order of echoed rows as it is, .js depends on it(student_quiz.js)
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["topic_id"]."|".$row["keyword"]."|".$row["keyword_id"]."|".$row["keywordWeight"]."|"; //note that topic comes first - vital for .js script
		}
	}
	else {
		echo("NO DATA");
	}
	$conn->close();
?>