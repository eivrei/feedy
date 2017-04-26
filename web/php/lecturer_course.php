<?php
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$course_and_parallel = explode("_", $_GET["course"]);
	$course = $course_and_parallel[0];
	$parallel = $course_and_parallel[1];

if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	// Use these example dates for demonstration because all lectures are done for the semester
	$start_date = date('Y-m-d H:i:s', strtotime('2017-03-16 12:15:00'));
	$end_date = date('Y-m-d H:i:s', strtotime('2017-03-30 12:15:00'));

	
	$sql = "SELECT DISTINCT Parallel.parallel_id, Lecturer.lecturer_id, Lecture.lecture_id, DATE_FORMAT(Lecture.lectureDate, '%Y-%m-%d %H:%i') AS lectureDate, Lecture.lectureName FROM Lecturer 
		INNER JOIN LectureLecturer ON Lecturer.lecturer_id = LectureLecturer.lecturer_id 
		INNER JOIN Lecture ON LectureLecturer.lecture_id = Lecture.lecture_id 
		INNER JOIN LectureParallel ON Lecture.lecture_id = LectureParallel.lecture_id 
		INNER JOIN Parallel ON LectureParallel.parallel_id = Parallel.parallel_id 
		INNER JOIN Course ON Parallel.course_code = Course.course_code 
		WHERE Parallel.parallel_id = '$parallel' AND Parallel.course_code = '$course' AND Lecture.lectureDate 
		BETWEEN '$start_date' AND '$end_date'
		GROUP BY Lecture.lecture_id";
	//does not check lecturer id variable - intentional/unneeded?
	$result = $mysqli->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			if ('$row["lectureName"]' == "NULL") 
			{
				echo "FOUND NULL";//echo "NULL"."|".$row["lectureDate"]."|".;
			}
			else
			{
				echo $row["lecture_id"]."|".$row["lectureDate"]."|".$row["lectureName"]."|";
			}
		}
	}
	else {
		echo "NO DATA";
	}
	$mysqli->close();
	