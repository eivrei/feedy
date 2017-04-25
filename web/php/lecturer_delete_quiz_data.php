<?php
    $db_username = "magnukun_pu100";
    $db_password = "pugruppe100";
    $server_name = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($server_name, $db_username, $db_password, $db_name);
    $topic_id = $_GET["topic"];

    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }

    $delete_topic_and_keywords = "DELETE FROM QuizTopic WHERE QuizTopic.topic_id = '$topic_id'";
    $conn->query($delete_topic_and_keywords);
    if ($conn->affected_rows > 0) {
        echo "Data deleted";
    }
    else {
        echo "Something happened during deletion of topics.";
    }

    session_start();
    $conn->close();