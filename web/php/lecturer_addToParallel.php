<?php
    include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
    $parallel_and_id = $_GET['parallel_and_id'];
	//echo($parallel_and_id);
	$exploded = explode('_', $parallel_and_id);
	$parallel_id = $exploded[0];
	$lecturer_id = $exploded[1];
    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }
	//generate sql check if lecturer is connected to parallel
	$check_if_added = "SELECT DISTINCT LectureLecturer.lecturer_id, LectureParallel.parallel_id FROM LectureParallel 
						INNER JOIN Lecture ON LectureParallel.lecture_id = Lecture.lecture_id 
						INNER JOIN LectureLecturer ON Lecture.lecture_id = LectureLecturer.lecture_id  
						WHERE LectureParallel.parallel_id = '$parallel_id' AND LectureLecturer.lecturer_id = '$lecturer_id'"; 
	
	$result = $mysqli->query($check_if_added);
	if (mysqli_num_rows($result) > 0) {
		echo("You are already a lecturer in this course!");
	}
	else {
        $add_to_lectures= "INSERT INTO LectureLecturer 
						SELECT lecture_id, '$lecturer_id' FROM LectureParallel 
						WHERE LectureParallel.parallel_id LIKE '".$parallel_id."%'";
        $mysqli->query($add_to_lectures);
        echo("SUCSESS"); //no check on if it actually works
	}	

    $mysqli->close();
