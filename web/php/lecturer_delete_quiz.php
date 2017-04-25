<?php
    $db_username = "magnukun_pu100";
    $db_password = "pugruppe100";
    $server_name = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($server_name, $db_username, $db_password, $db_name);
    $lecture_id = $_GET["lecture"];

    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }


    $delete_stats_and_name = "UPDATE Lecture SET lectureStats = NULL, lectureName = NULL 
                              WHERE Lecture.lecture_id = '$lecture_id'";
    $conn->query($delete_stats_and_name);
    if ($conn->affected_rows > 0) {
        echo "Stats deleted|";
    }
    else {
        echo "Something happened during deletion of stats.";
    }

    $delete_topics = "DELETE FROM QuizTopic
                      WHERE QuizTopic.lecture_id = '$lecture_id'";
    $conn->query($delete_topics);
    if ($conn->affected_rows > 0) {
        echo "Topics deleted|";
    }
    else {
        echo "Something happened during deletion of topics.";
    }

    session_start();
    $conn->close();