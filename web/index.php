<?php
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';
sec_session_start();
//gets full session name and email for display on account dropdown
getName($mysqli);
getEmail($mysqli);
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Feedy</title>
        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="css/mal.css" rel="stylesheet">
        <link href="css/index.css" rel="stylesheet">
        <link rel="icon" href="img/favicon.ico" type="image/x-icon">
        <script type="text/JavaScript" src="script/sha512.js"></script> 
        <script type="text/JavaScript" src="script/forms.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.1.min.js"></script>
    </head>

    <body>
      <nav class="navbar navbar-inverse navbar-static-top">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-left" href="./">
              <img src="img/FEEDY_logo_eee_small.png" id="feedy_logo" alt="Feedy" />
            </a>
          </div>
          
          <!--account dropdown window and logout function-->
          <?php if (login_check($mysqli)) : ?>

            <div class="collapse navbar-collapse" id="logoutheader">
                <ul class="nav navbar-nav navbar-right">
                  <li class="dropdown">
                    <a href="JavaScript: collapse()" class="dropdown-toggle" data-toggle="dropdown">
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
                                            <a href="includes/logout.php" class="btn btn-primary btn-block btn-sm">Log out</a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="divider top-divider"></li>
                          <li><a href="html/lecturer/courses.php">Your courses<span class="glyphicon glyphicon-education pull-right"></span></a></li>
                        <li class="divider"></li>
                          <li><a href="./">Return to front page<span class="glyphicon glyphicon-home pull-right"></span></a></li>
                  </ul>
                  </li>
                </ul>
              </div>
          <?php endif; ?> 

        </div>
      </nav>
      
      <h1>Welcome to <img src="img/FEEDY_logo_black_small.png" id="intext_logo" alt="FEEDY" />, the smart lecture helper!</h1>

      <div class="container" id="student">
        <h2>Are you a student?</h2>
        <div>
          <a href="html/student/courses.php" class="btn btn-primary btn-lg" role="button" id="sbutton">Click here</a>
        </div>
      </div>
      
      <div class="container">
      <?php 
        //shows login form if not logged in
        if (login_check($mysqli) == false) : ?>
        <form action="includes/process_login.php" class="form-signin" method="post" name=""> 
          <h2 class="form-signin-heading">Are you a lecturer?</h2>
          <label for="inputUsername" class="sr-only">Username</label>
          <input type="text" 
                 name="username" 
                 class="form-control" 
                 placeholder="Username"  autofocus />
          <label for="inputPassword" class="sr-only">Password</label>
          <input type="password" 
                 name="password" 
                 class="form-control" 
                 placeholder="Password" />
          <input type="submit" 
                 value="Log in" id="loginSubmit" 
                 class="btn btn-lg btn-primary btn-block" 
                 onclick="formhash(this.form, this.form.password);" />
        </form>
      <?php endif; ?>

        <?php if (isset($_GET['error'])) : ?>
            <p class="error">Wrong username or password!</p>

        <?php elseif (login_check($mysqli)) : ?>
          <div class="container" id="student">
                  <h2>Are you a lecturer?</h2>
                  <div>
                    <a href="html/lecturer/courses.php" class="btn btn-primary btn-lg" role="button" id="sbutton">Click here</a>
                  </div>
                </div>
        <?php endif; ?>

      <?php if (login_check($mysqli) == false) : ?>
        <p id="register">If you don't have a user, <a href="html/register.php">register</a> here. </p>   
      <?php endif; ?>
      </div> 

    <script src="bootstrap/js/bootstrap.min.js"></script>
    </body>
</html>
