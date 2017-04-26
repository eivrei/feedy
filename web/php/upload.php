<?php
//------------------------------------------------------
$lecture_id = $_POST["lecture_id"];
$course_code = $_POST["course_code"];
$parallel_id = $_POST["parallel_id"];
$target_dir = "../../server/temp/";
$program_dir = escapeshellarg("../../server/quiz_generation_program.py");
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
$nameSplit = explode(".", basename($_FILES["fileToUpload"]["name"]));
$cleanFileName = $nameSplit[0];
$message = "";

// Check if file already exists
if (file_exists($target_file)) {
    $message = "Sorry, file already exists. ";
    $uploadOk = 0;
}

// Check file size
// Because of problems with server, this is done in js-file.
if ($_FILES["fileToUpload"]["size"] > 18000000) {
    $message = "Sorry, your file is too large. Max file size is 20mb.";
    $uploadOk = 0;
}

// Allow certain file formats
 if($imageFileType != "pptx") {
    $message = "Sorry, only pptx files are allowed. ";
    $uploadOk = 0;
}

// if everything is ok, try to upload file
if($uploadOk == 1) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $message = "The quiz '". $cleanFileName. "' has been generated.";
		echo exec("../../../python_env/bin/python3 $program_dir '$cleanFileName' $lecture_id"); //temporary check to see if it works


    } else {
        $message =  "Sorry, there was an error uploading your file.";
    }
}
//------------------------------------------------------ 	*/
?>
<script type="text/javascript">
    var message = "<?php echo $message; ?>";
    alert(message);
    var course_code = <?php echo json_encode($course_code);?>;
    var parallel_id = <?php echo json_encode($parallel_id);?>;
    window.location = "../html/lecturer/course.php#" + course_code + "_" + parallel_id;
</script>