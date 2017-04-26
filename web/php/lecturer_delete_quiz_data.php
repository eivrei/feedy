<?php
    include_once '../includes/db_delete_connect.php';
    include_once '../includes/functions.php';

    sec_session_start();
    $topic_id = $_GET["topic"];

    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }

    $delete_topic_and_keywords = "DELETE FROM QuizTopic WHERE QuizTopic.topic_id = '$topic_id'";
    $mysqli->query($delete_topic_and_keywords);
    if ($mysqli->affected_rows > 0) {
        echo "Data deleted";
    }
    else {
        echo "Something happened during deletion of topics.";
    }

    $mysqli->close();
    