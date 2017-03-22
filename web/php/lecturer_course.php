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

	$sql = "SELECT Lecture.lectureName, Lecture.lectureDate, Parallel.course_code FROM Parallel
			INNER JOIN LecturerParallel ON Parallel.parallel_id = LecturerParallel.parallel_id
			INNER JOIN Lecturer ON LecturerParallel.lecturer_id = Lecturer.lecturer_id
			INNER JOIN LectureLecturer ON Lecturer.lecturer_id = LectureLecturer.lecturer_id
			INNER JOIN Lecture ON LectureLecturer.lecture_id = Lecture.lecture_id
			WHERE Parallel.parallel_id = '$parallel' AND Parallel.course_code = '$course'";
	$result = $conn->query($sql);
	
	session_start();
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			/*if ('$row["lectureName"]' == "NULL") 
			{
				//echo "NULL"."|".$row["lectureDate"]."|".;
			}
			else
			{
				//echo $row["lectureName"]."|".$row["lectureDate"];
			}*/
			echo $row["lectureName"];		
			}
	}
	else {
		echo "WRONG";
	}


	$conn->close();
?>
