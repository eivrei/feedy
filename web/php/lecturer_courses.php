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
	$sql = "SELECT DISTINCT Course.course_code, Course.courseName, Parallel.programmes, Parallel.parallel_id FROM Lecturer 
			INNER JOIN LectureLecturer ON Lecturer.lecturer_id = LectureLecturer.lecturer_id 
			INNER JOIN Lecture ON LectureLecturer.lecture_id = Lecture.lecture_id 
			INNER JOIN LectureParallel ON Lecture.lecture_id = LectureParallel.lecture_id 
			INNER JOIN Parallel ON LectureParallel.parallel_id = Parallel.parallel_id 
			INNER JOIN Course ON Parallel.course_code = Course.course_code 
			WHERE Lecturer.username='$id'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo $row["course_code"]."|".$row["courseName"]."|".$row["programmes"]."|".$row["parallel_id"]."|";
		}
	}
	else {
		print_r($result);
	}


	$conn->close();
?>
