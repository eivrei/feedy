<?php
include_once '../includes/db_connect.php';
include_once '../includes/functions.php';
 
sec_session_start();
 
if (login_check($mysqli) == true) {
    $logged = 'in';
} else {
    $logged = 'out';
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Feedy</title>
        <link rel="stylesheet" href="styles/main.css">
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="../css/mal.css" rel="stylesheet">
        <link href="../css/success.css" rel="stylesheet">
        <link rel="icon" href="../img/favicon.ico" type="image/x-icon">
        <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.1.min.js"></script>

    </head>
    <body>
      <nav class="navbar navbar-inverse navbar-static-top">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-left" href="../">
              <img src="../img/FEEDY_logo_eee_small.png" id="feedy_logo" alt="Feedy" />
            </a>
          </div>
          <?php if (login_check($mysqli) == true) {
            echo '<div class="collapse navbar-collapse" id="logoutheader">
                    <ul class="nav navbar-nav navbar-right">
                      <li><a href="includes/logout.php">Log out</a></li></ul>
                  </div>'; }?> 
        </div>
      </nav>
      
      <div class="container">
      	<h3>Registration successful! Click the <a href="../"><img src="../img/FEEDY_logo_black_small.png" alt="FEEDY" id="intext_logo" /></a> logo to return to the login page. </h3>
      </div>

    <script src="bootstrap/js/bootstrap.min.js"></script>
    </body>
</html>
