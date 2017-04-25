<?php
    $db_username = "magnukun_pu100";
    $db_password = "pugruppe100";
    $server_name = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($server_name, $db_username, $db_password, $db_name);
    $quiz_result = json_decode(stripslashes($_POST['quizResult']));
	//var_dump($quiz_result);
   // $topic_id = $form_data[0];
    //$topic = $form_data[1];

    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
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
	
	//echo $update_num_Answer;
	//echo $add_quiz_answers;
	
    $conn->query($update_num_Answer);
	$conn->query($add_quiz_answers);	

    $conn->close();
?>