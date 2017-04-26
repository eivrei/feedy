<?php
include_once '../includes/register.inc.php';
include_once '../includes/functions.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Register</title>
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="../css/mal.css" />
        <link rel="stylesheet" href="../css/register.css" />
        <link rel="icon" href="../img/favicon.ico" type="image/x-icon">
        <script type="text/JavaScript" src="../script/sha512.js"></script> 
        <script type="text/JavaScript" src="../script/forms.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.1.min.js"></script>

    </head>
    <body>
        <nav class="navbar navbar-inverse navbar-static-top">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-left" href="./index.php">
                    <img src="../img/FEEDY_logo_eee_small.png" id="feedy_logo" alt="Feedy" />
                    </a>
                </div>
            </div>
        </nav>

        <!-- Registration form to be output if the POST variables are not
        set or if the registration script caused an error. -->
        <div class="container" id="error">
        <?php
        if (!empty($error_msg)) {
            echo $error_msg;
        }
        ?>
        </div>
        
        <div class="container">
            <h1>Register with us</h1>
            <form action="<?php echo esc_url($_SERVER['REQUEST_URI']); ?>" 
                    method="post"
                    class="form-signin" 
                    name="registration_form">
                    <!-- email -->
                <label for="inputEmail" class="sr-only">E-mail</label>
                <input type="email"
                    name="email"
                    class="form-control"
                    placeholder="E-mail address"
                    id="email" autofocus />
                    <!-- first name -->
                <label for="inputFirstName" class="sr-only">First name </label>
                <input type="text"
                    name="firstName"
                    class="form-control"
                    placeholder="First name"
                    id="firstName" />
                    <!-- Last name -->
                <label for="inputLastName" class="sr-only">Last name</label>
                <input type="text"
                    name="lastName"
                    class="form-control"
                    placeholder="Last name"
                    id="lastName" />
                    <!-- username -->
                <label for="inputUsername" class="sr-only">Username</label>
                <input type="text"
                    name="username"
                    class="form-control"
                    placeholder="Username"
                    id="username" />
                    <!-- password -->
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password"
                    name="password"
                    class="form-control"
                    placeholder="Password"
                    id="password" />
                    <!-- confirm password -->
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password"
                    name="confirmpwd"
                    class="form-control"
                    placeholder="Confirm password"
                    id="confirmpwd" />
                    <!-- Register button -->
                <input type="button" 
                       value="Register"
                       class="btn btn-lg btn-primary btn-block" 
                       onclick="return regformhash(this.form,
                                        this.form.email,
                                        this.form.firstName,
                                        this.form.lastName,
                                        this.form.username,
                                        this.form.password,
                                        this.form.confirmpwd);" />
 
            </form>
        <p id="return_text">Return to the <a href="../index.php">login page</a>.</p>
        </div>

    <script src="../bootstrap/js/bootstrap.min.js"></script>
    </body>
</html>