<?php
include_once '../../includes/db_connect.php';
include_once '../../includes/functions.php';
 
sec_session_start();
if (login_check($mysqli)){
  getName($mysqli);
  getEmail($mysqli);
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- tab info -->
    <title>Feedy</title>
    <link href="../../img/favicon.ico" rel="icon" type="image/x-icon">
    <!-- css -->
    <link href="../../bootstrap/css/bootstrap.min.css" rel="stylesheet">    
    <link href="../../css/mal.css" rel="stylesheet">
    <link href="../../css/course.css" rel="stylesheet">
      <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
	<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.1.min.js"></script>
	<script type="text/javascript" src="../../script/lecturer_preview.js" charset="utf-8"></script>
  </head>
  <?php if (login_check($mysqli)) : ?>


	<body>
    <nav class="navbar navbar-inverse navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-left" href="../../">
            <img src="../../img/FEEDY_logo_eee_small.png" id="feedy_logo" alt="Feedy" />
          </a>
      </div>
      <div class="collapse navbar-collapse" id="logoutheader">
                <ul class="nav navbar-nav navbar-right">
                  <li class="dropdown">
                    <a href ="JavaScript: collapse()" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="glyphicon glyphicon-user"></span> 
                        <?php echo htmlentities($_SESSION['username'])?>
                        <span class="glyphicon glyphicon-chevron-down"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li>
                            <div class="navbar-login">
                                <div class="row">
                                    <div class="col-lg-4">
                                        <p class="text-center">
                                            <span class="glyphicon glyphicon-user icon-size"></span>
                                        </p>
                                    </div>
                                    <div class="col-lg-8">
                                        <p class="text-left king">
                                          <strong>
                                          <?php echo $_SESSION['fullName'];?>
                                          </strong></p>
                                        <p class="text-left small">
                                          <?php echo $_SESSION['email'];?>
                                        </p>
                                        <p class="text-left">
                                            <a href="../../includes/logout.php" class="btn btn-primary btn-block btn-sm">Log out</a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="divider top-divider"></li>
                          <li><a href="courses.php">Your courses<span class="glyphicon glyphicon-education pull-right"></span></a></li>
                        <li class="divider"></li>
                          <li><a href="../../">Return to front page<span class="glyphicon glyphicon-home pull-right"></span></a></li>
                  </ul>
                  </li>
                </ul>
        </div>
      </div>
    </nav>

  <div class="container">

    <a href = "javascript:history.back()" class="btn btn-primary" id="prevPage">
      <span class="glyphicon glyphicon-arrow-left"></span>
      Go back
    </a>

  	<div class="container" id="topics">
  		<h2 id="quiz_name"></h2>
  		<div id="quiz_content"></div>	
  	</div>
  </div>

  <?php else : ?>
    <p>
        <span class="error">You are not authorized to access this page.</span> Please <a href="../../">login</a>.
    </p>
  <?php endif; ?>
  <script src="../../bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>