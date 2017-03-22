<?php

	$db_username = "magnukun_secure";
	$db_password = "YEa2VJXHxmWQ";
	$servername = "mysql.stud.ntnu.no";
	$db_name = "magnukun_pudb";
	$conn = new mysqli($servername, $db_username, $db_password, $db_name);
	$course_and_parallel = explode("_", $_GET["course"]);
	$course = $course_and_parallel[0];
	$parallel = $course_and_parallel[1];
	
if($conn->connect_error){
		die("Connection failed: " . $conn->connect_error);
	}
	//distinct not needed?
	
	$sql = "SELECT DISTINCT Course.course_code, Course.courseName, Parallel.parallel_id, Lecturer.lecturer_id, Lecture.lecture_id, Lecture.lectureDate FROM Lecturer 
		INNER JOIN LectureLecturer ON Lecturer.lecturer_id = LectureLecturer.lecturer_id 
		INNER JOIN Lecture ON LectureLecturer.lecture_id = Lecture.lecture_id 
		INNER JOIN LectureParallel ON Lecture.lecture_id = LectureParallel.lecture_id 
		INNER JOIN Parallel ON LectureParallel.parallel_id = Parallel.parallel_id 
		INNER JOIN Course ON Parallel.course_code = Course.course_code 
		WHERE Parallel.parallel_id = '$parallel' AND Parallel.course_code = '$course'";

	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			if ('$row["lectureName"]' == "NULL") 
			{
				echo "FOUND NULL";//echo "NULL"."|".$row["lectureDate"]."|".;
			}
			else
			{
				echo $row["lecture_id"]."|".$row["lectureDate"]."|".$row["lectureName"];
			}
			//echo $row["lectureDate"];		
			}
	}
	else {
		echo "NO DATA";
	}


	$conn->close();
?>
