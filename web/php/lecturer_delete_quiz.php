<?php
    include_once '../includes/db_delete_connect.php';
    include_once '../includes/functions.php';

    sec_session_start();
    $lecture_id = $_GET["lecture"];

    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }


    $delete_stats_and_name = "UPDATE Lecture SET lectureStats = NULL, lectureName = NULL 
                              WHERE Lecture.lecture_id = '$lecture_id'";
    $mysqli->query($delete_stats_and_name);
    if ($mysqli->affected_rows > 0) {
        echo "Stats deleted|";
    }
    else {
        echo "Something happened during deletion of stats.";
    }

    $delete_topics = "DELETE FROM QuizTopic
                      WHERE QuizTopic.lecture_id = '$lecture_id'";
    $mysqli->query($delete_topics);
    if ($mysqli->affected_rows > 0) {
        echo "Topics deleted|";
    }
    else {
        echo "Something happened during deletion of topics.";
    }

    $mysqli->close();
    