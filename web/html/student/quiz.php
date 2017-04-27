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
	<script type="text/javascript" src="../../script/student_quiz.js" charset="utf-8"></script>
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
                          <li><a href="../lecturer/courses.php">My courses<span class="glyphicon glyphicon-education pull-right"></span></a></li>
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
		<div class="row">
			<div class="col-md-4">
				<div class="input-group" id="adv-search">
					<div class="input-group-btn">
						<div class="btn-group" role="group">
						</div>
					</div>
				</div>
			</div>
		</div>
	
	<h3>Type all keywords related to: <span id="topic-text"></span></h3>
	<div class="input-group">
		<textarea id="answer-input" class="form-control custom-control" maxlength="400" rows="3" style="resize:none"></textarea>
		<span id="send-button" class="input-group-addon btn btn-primary" onclick="topic_answered()">Send</span>
	</div>
	<div class="progress">
		<div class="progress-bar" id="quiz-progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="min-width: 2em;">
			<span id="progress-text"></span>
		</div>
	</div>

    <div class="bs-example">
        <!-- Modal HTML -->
        <!-- see student_quiz.js for details on feedback_modal_onclick(), needs correct hidden value to run -->
        <div id="feedback-modal" class="modal fade">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 id = "modal-title" class="modal-title">You scored less than 20% in one or more topics </h3>
                    </div>
                    <div class="modal-body">
                        <h4> Which of the following apply to the presentation? </h4>
                        <form>
                            <div class="checkbox">
                                <label><input type="checkbox" id="1" value="">Pace is too fast</label>
                            </div>
                            <div class="checkbox">
                                <label><input type="checkbox" id="2" value="">To few/poor examples</label>
                            </div>
                            <div class="checkbox">
                                <label><input type="checkbox" id="3" value="">Unfocused presentation</label>
                            </div>
                            <div class="checkbox">
                                <label><input type="checkbox" id="4" value="">Lacking background info</label>
                            </div>
                            <div class="checkbox">
                                <label><input type="checkbox" value="">None of the above</label>
                            </div>
                            <input type="hidden" id="modal-hidden-input"></input>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" onclick="feedback_modal_onclick()">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="../../bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>