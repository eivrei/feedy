<?php
    include_once '../includes/functions.php';
	include_once '../includes/db_connect.php';

	sec_session_start();
	$mysqli->set_charset("utf8");
    $quiz_result = json_decode(stripslashes($_POST['quizResult']));
	//var_dump($quiz_result);
   // $topic_id = $form_data[0];
    //$topic = $form_data[1];

    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }
	//generate sql to update numAnswered on keywords
	$keywords_implode = implode(",", $quiz_result->keywords);
	$update_num_Answer = "UPDATE QuizKeyword SET numAnswered = numAnswered + 1 WHERE keyword_id IN ( $keywords_implode )";
	
	//generate sql to add quizAnswers
	//append values in format "(percent,topic_id),"  or ); for last value
	$value_pair_string;
	foreach ($quiz_result->topics as $topic) {
		if (isset($value_pair_string)) {$value_pair_string .=",";}
		$value_pair_string .= "(".$topic->correctPercent.",".$topic->id.")";
	}
	$add_quiz_answers ="INSERT INTO QuizAnswer (correctPercent, topic_id)
	VALUES ".$value_pair_string.";";
	
    $mysqli->query($update_num_Answer);
	$mysqli->query($add_quiz_answers);	

    $mysqli->close();
