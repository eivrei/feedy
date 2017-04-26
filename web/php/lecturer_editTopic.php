<?php
    include_once '../includes/db_delete_connect.php';
    include_once '../includes/functions.php';

    sec_session_start();
    $form_data = json_decode($_GET["array"]);
    $topic_id = $form_data[0];
    $topic = $form_data[1];

    if($mysqli->connect_error){
        die("Connection failed: " . $mysqli->connect_error);
    }
    $edit_topic = "UPDATE QuizTopic SET topic = '$topic' WHERE topic_id = '$topic_id'";
    $mysqli->query($edit_topic);

    for ($i = 2; $i <= count($form_data) - 4; $i+= 4) {
        $sql = "";
        $keyword_id = $form_data[$i];
        $keyword = $form_data[$i + 1];
        $weight = $form_data[$i + 2];
        $checkbox = $form_data[$i + 3];
        if($checkbox == "1"){
            echo "|delete ".$keyword." ".$keyword_id;
            $sql = "DELETE FROM QuizKeyword WHERE keyword_id = '$keyword_id'";
        }
        else{
            echo "|update ".$keyword;
            $sql = "UPDATE QuizKeyword SET keyword = '$keyword', keywordWeight = '$weight' WHERE keyword_id = '$keyword_id'";
        }
        echo $sql;
        $mysqli->query($sql);
    }

    $mysqli->close();
