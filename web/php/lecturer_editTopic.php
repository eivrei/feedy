<?php
    $db_username = "magnukun_pu100";
    $db_password = "pugruppe100";
    $server_name = "mysql.stud.ntnu.no";
    $db_name = "magnukun_pudb";
    $conn = new mysqli($server_name, $db_username, $db_password, $db_name);
    $form_data = json_decode($_GET["array"]);
    $topic_id = $form_data[0];
    $topic = $form_data[1];

    if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
    }
    $edit_topic = "UPDATE QuizTopic SET topic = '$topic' WHERE topic_id = '$topic_id'";
    $conn->query($edit_topic);

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
        $conn->query($sql);
    }

    session_start();

    $conn->close();
