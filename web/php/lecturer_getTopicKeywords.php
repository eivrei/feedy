<?php
    $db_username = "magnukun_secure";
    $db_password = "YEa2VJXHxmWQ";
    $servername = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($servername, $db_username, $db_password, $db_name);
    $topic_id = $_GET["topic"];

    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }

    $get_topic = "SELECT topic_id, topic FROM QuizTopic WHERE topic_id = '$topic_id'";
    $get_keywords = "SELECT keyword_id, keyword, keywordWeight FROM QuizKeyword WHERE topic_id = '$topic_id'";

    $topics = $conn->query($get_topic);
    session_start();

    if ($topics->num_rows > 0) {
        while($row = $topics->fetch_assoc()) {
            echo $row["topic_id"]."|".$row["topic"];
        }
    }
    else {
        echo "NO DATA|";
    }

    $keywords = $conn->query($get_keywords);

    if ($keywords->num_rows > 0) {
        while($row = $keywords->fetch_assoc()) {
            echo "|".$row["keyword_id"]."|".$row["keyword"]."|".$row["keywordWeight"];
        }
    }
    else {
        echo "NO DATA";
    }

    $conn->close();