var hash = window.location.hash.substr(1);
hash = hash.split("_");
var course_code = hash[0];
var parallel_id = hash[1];

$(document).ready(function() {
	$.get("../../php/lecturer_course.php?course=" + course_code + "_" + parallel_id, function (data) {
		if (data !== "NO DATA") {
			$("#course_name").html(course_code + " - Lectures");
			createLectureTable(data); //if on data length?
		}
		else {
		console.log(data);
		}
	});
});

function createButtonString(type, lecture_id) { //remember functions are bound to buttons here
	var buttonString = "";
	//"<button id='" + lecture_id + "' class='btn btn-md btn-primary' type='button'" ; //note: no end >
	switch(type) {
		case "view":
			buttonString += "<button class='viewQuiz btn btn-md-2 btn-primary' type='button' id='viewQuiz'" ; //note: no end >
			buttonString += "value=" + lecture_id + " onclick = view_quiz(this)>View quiz</button>";
			break;
		case "delete":
			buttonString += "<button class='deleteQuiz btn btn-md-2 btn-primary' type='button' id='deleteQuiz'" ; //note: no end >
			buttonString += "value=" +lecture_id + " onclick = delete_quiz(this)>Delete quiz</button>";
			break;
		case "stats":
			buttonString += "<button class='statsQuiz btn btn-md-2 btn-primary' type='button' id='statsQuiz'" ; //note: no end >
			buttonString += "value=" +lecture_id + " onclick = \"window.location = 'statistics.php#" + lecture_id +"'\">View statistics</button>";
			break;
		case "upload":
			buttonString += "<form class='' id='upload_form' action='../../php/upload.php' onsubmit='return upload()' method='post' enctype='multipart/form-data' accept-charset='UTF-8'>" +
								"<div class='col-md-6 col-xs-8'>" +
									"<input type='file' class='uploadField btn btn-default form-control' name='fileToUpload' id='fileUpload' required>" +
								"</div>" +
								"<div class='col-md-6 col-xs-4 button'>" +
									"<input type='submit' value='Generate quiz' class='deleteFile uploadButton btn btn-md-2 btn-primary submitFile' name='submit' id='submitFile'>" +
									"<input type='hidden' name='lecture_id' value='" + lecture_id + "'>" +//gives php access to lecture id
									"<input type='hidden' name='course_code' value='" + course_code + "'>" +//gives php access to course_code
									"<input type='hidden' name='parallel_id' value='" + parallel_id + "'>" +//gives php access to lecture_id
								"</div></form>";
			break;
		default:
			console.log("something went wrong");
	}
	buttonString +=" ";
	//console.log(buttonString);
	return buttonString;
}

function view_quiz(button) {
	var redirectString = "quiz_preview.php#" + button.value + "_" + course_code + "_" + parallel_id;
	window.location = redirectString;
}

function delete_quiz(button) {
    if (confirm("Are you sure?")) {
        $.get("../../php/lecturer_delete_quiz.php?lecture=" + button.value, function (data) {
			data = data.replace(/(\r\n|\n|\r)/gm,"").split("|");
			if (data[0] === "Stats deleted" && data[1] === "Topics deleted"){
				alert("The quiz was successfully deleted");
				location.reload();
			}
        });
    }
}

//creates a table of lectures, not a table of content for one specific lectures
function createLectureTable(data) {
	var lectureContent = data.split("|");
	lectureContent.pop(); //removes final "|"
	var toAppend = "";
	for (var i = 0; i < lectureContent.length; i+=3) { //each iteration makes one complete lecture display with buttons/functionality
		var lecture_id = lectureContent[i].replace(/(\r\n|\n|\r)/gm,"");
		var date = lectureContent[i+1].replace(/(\r\n|\n|\r)/gm,"");
		var name = lectureContent[i+2].replace(/(\r\n|\n|\r)/gm,"");
		toAppend+= "<div class='lectureElement lecture row'>"; //link course name to statistics page
		if (name !== "") { //lectures with names have quizzes already
			toAppend += "<div class='col-md-7 col-xs-12'><p class='lectureInfo' " + lecture_id +"'>" + date + "</p>";
			toAppend += " <i class='lectureName'>" + name + "</i></div>";
			toAppend += " <div class='innerLecture col-md-5 col-xs-12'> " + createButtonString("view",lecture_id); //create view button value = lecture_id
			toAppend += " " + createButtonString("stats",lecture_id);
			toAppend += " " + createButtonString("delete",lecture_id); //create delete button value = lecture_id
		}
		else { //lecture does not have quiz
			toAppend += "<div class='lectureInfo col-md-6 col-xs-8'><p class='dateTime'" + lecture_id +"'>" + date + "</p> </div>";
			toAppend+= " " + createButtonString("upload", lecture_id); //only make var date if this case applies?
			//create upload button value = lecture_id + lecture.date (?)
		}
		toAppend+="</div></div><div class='line lecture'></div>"; //each lecture has its own, nameless div to linebreak break between lectures
	}
		//console.log(toAppend);
		$("#course_content").append(toAppend);
}

function upload() {
    var fileUpload = document.getElementById("fileUpload");
    if (typeof (fileUpload.files) !== "undefined") {
        var size = parseFloat(fileUpload.files[0].size / 1024 / 1024).toFixed(2);
        if (size < 19.5){
        	return true;
		}else{
        	alert("This file is to big. Max file size is 20MB.");
		}
    } else {
        alert("This browser does not support HTML5.");
    }
	return false;
}



