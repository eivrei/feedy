<?php
	include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
	$course_code = $_GET["course"];

	if($mysqli->connect_error){
		die("Connection failed: " . $mysqli->connect_error);
	}
	
	function checkForParallels($result) {
		// reset the result resource
		if ($result->num_rows > 0) {
			$firstrow = $result->fetch_assoc();
			echo $firstrow["course_code"]."|".$firstrow["course_name"]."|";
			mysqli_data_seek($result, 0);
			while($row = $result->fetch_assoc()) {
				echo $row["programmes"]."|".$row["parallel_id"]."|";
			}
		}
	}
	//Distinct not needed?
	$sql = "SELECT DISTINCT Course.course_code, Course.courseName, Parallel.programmes, Parallel.parallel_id FROM Course 
			INNER JOIN Parallel ON Course.course_code = Parallel.course_code
			WHERE Course.course_code='$course_code'
			ORDER BY Course.course_code ASC";

	$result = $mysqli->query($sql);
	if (mysqli_num_rows($result) > 0)  { 
		checkForParallels($result);
	}
	else {
		//webscrape
		$program_dir = escapeshellarg("../../server/web_scraper.py"); //remember to update
		$return = exec("../../../python_env/bin/python3 $program_dir $course_code");
		$returnSplit = explode(':', $return);
		if ($returnSplit[0] != "There is no information about this course" && $returnSplit[0] != "There was en error writing to the db" ){
			$result2 = $conn->query($sql); //Safeguarding against incorrect seeker info
			checkForParallels($result2);
		}
		else {
			echo $return; //return error message
		}
	}
	$mysqli->close();
