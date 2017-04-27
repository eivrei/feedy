<?php
include_once 'db_connect.php';
include_once 'functions.php';
 
sec_session_start(); // Our secure way of starting a PHP session.
 
if (isset($_POST['username'], $_POST['p'])) {
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = $_POST['p']; // The hashed password.
 
    if (login($username, $password, $mysqli) == true) {
        // Login success, point to lecturer/courses evutally
        $_SESSION['username'] = $_POST['username'];
        header('Location: ../html/lecturer/courses.php');
    } else {
        // Login failed
        header('Location: ../index.php?error=1');
    }
} else {
    // The correct POST variables were not sent to this page. 
    echo 'Invalid Request';
}
