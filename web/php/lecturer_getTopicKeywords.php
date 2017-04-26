<?php
    include_once '../includes/functions.php';
    include_once '../includes/db_connect.php';

    sec_session_start();
    $mysqli->set_charset("utf8");
    $topic_id = $_GET["topic"];

    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }

    $get_topic = "SELECT topic_id, topic FROM QuizTopic WHERE topic_id = '$topic_id'";
    $get_keywords = "SELECT keyword_id, keyword, keywordWeight FROM QuizKeyword WHERE topic_id = '$topic_id'";

    $topics = $mysqli->query($get_topic);
    session_start();

    if ($topics->num_rows > 0) {
        while($row = $topics->fetch_assoc()) {
            echo $row["topic_id"]."|".$row["topic"];
        }
    }
    else {
        echo "NO DATA|";
    }

    $keywords = $mysqli->query($get_keywords);

    if ($keywords->num_rows > 0) {
        while($row = $keywords->fetch_assoc()) {
            echo "|".$row["keyword_id"]."|".$row["keyword"]."|".$row["keywordWeight"];
        }
    }
    else {
        echo "NO DATA";
    }

    $mysqli->close();
    