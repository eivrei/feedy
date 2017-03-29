<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8"> 
	</head>
	
	<body>
		
<?php
$target_dir = "../../server/temp/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);



// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 200000000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "pptx") {
    echo "Sorry, only pptx files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
		//execute python program - no data
		

	//$disabled = explode(',', ini_get('disable_functions'));
	//echo !in_array('exec', $disabled);


		//$relpath = "../../server/exec_return_test.py";  
		//$relpath = "/alexanws/PU100/server/exec_return_test.py ";
		//$abspath = realpath($relpath);
		//echo $abspath;
		//echo $relpath;*/
		//echo exec(exec_return_test.py); 
		//echo $test_output;
		//echo exec("whoami");  -- works and returns "alexanws"
		
		
		
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>

	</body>
</html> 	
