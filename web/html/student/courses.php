<?php
include_once '../../includes/db_connect.php';
include_once '../../includes/functions.php';
sec_session_start();
//gets full session name and email for display on account dropdown
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
    <link href="../../css/courses.css" rel="stylesheet">    
      <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.1.min.js"></script>
    <script type ="text/javascript" src="../../script/student_search_courses.js"></script>
    <script type="text/javascript" src="../../script/student_courses.js" charset="utf-8"></script>
  </head>

  <body>
    <nav class="navbar navbar-inverse navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-left" href="../../">
            <img src="../../img/FEEDY_logo_eee_small.png" id="feedy_logo" alt="Feedy" />
          </a>
      </div>
      <?php if (login_check($mysqli)) : ?>

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
                          <li><a href="../lecturer/courses.php">Your courses<span class="glyphicon glyphicon-education pull-right"></span></a></li>
                        <li class="divider"></li>
                          <li><a href="../../">Return to front page<span class="glyphicon glyphicon-home pull-right"></span></a></li>
                  </ul>
                  </li>
                </ul>
              </div>
          <?php endif; ?>
      </div>
    </nav>
    
    <div class="container" id="searchbar">

      <a href = "../../" class="btn btn-primary" id="prevPage">
        <span class="glyphicon glyphicon-arrow-left"></span>
        Go back
      </a>    



      <div class="row">
        <div class="col-md-4">
          <form name="search" onsubmit="return false;">
            <div class="input-group" id="adv-search">
              <input type="text" id="searchQuery" 
              class="form-control" 
              placeholder="Search for courses"
              autofocus
              autocomplete="off" />
              <div class="input-group-btn">
                <div class="btn-group" role="group">
                   <submit type="button" id ="searchButton" class="btn btn-primary"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></submit>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>

      <div id="div_courselist">
      </div>
    </div>

    
    <script src="../../bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>