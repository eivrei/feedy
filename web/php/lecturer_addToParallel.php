<?php
    $db_username = "magnukun_pu100";
    $db_password = "pugruppe100";
    $server_name = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($server_name, $db_username, $db_password, $db_name);
    $parallel_and_id = $_GET['parallel_and_id'];
	$exploded = explode('_', $parallel_and_id);
	$parallel_id = $exploded[0];
	$lecturer_id = $exploded[1];
    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }
	//generate sql check if lecturer is connected to parallel
	$check_if_added = "SELECT DISTINCT LectureLecturer.lecturer_id, LectureParallel.parallel_id FROM LectureParallel 
						INNER JOIN Lecture ON LectureParallel.lecture_id = Lecture.lecture_id 
						INNER JOIN LectureLecturer ON Lecture.lecture_id = LectureLecturer.lecture_id  
						WHERE LectureParallel.parallel_id = '$parallel_id' AND LectureLecturer.lecturer_id = '$lecturer_id'"; 
	
	$result = $conn->query($check_if_added);
	if (mysqli_num_rows($result) > 0) {
		echo("You are already a lecturer in this course!");
	}
	else {
		$add_to_lectures= "INSERT INTO LectureLecturer 
						SELECT lecture_id, '$lecturer_id' FROM LectureParallel 
						WHERE LectureParallel.parallel_id LIKE '".$parallel_id."%'";
		$conn->query($add_to_lectures);
		echo("SUCSESS"); //no check on if it actually works
	}	

    $conn->close();
?>