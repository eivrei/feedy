var hash = window.location.hash.substr(1);
hash = hash.split("_");
var course_code =  hash[0];
var parallel_id =  hash[1];

$(document).ready(function() {
	$.get("../../php/lecturer_course.php?course=" + course_code + "_" + parallel_id, function (data) {
		console.log(data);
		if (data != "NO DATA") {
		$("#course_name").html(course_code);
		createLectureTable(data); //if on data length?
		}
		else {
		//console.log(data); //why?
		}

	});	
});

function createButtonString(type, lecture_id, date = "null") { //give date as argument only for type = upload, remember to check if id is needed
	var buttonString = "<button id='" + lecture_id + "' class='btn btn-lg btn-primary btn-block' type='button'" ; //note: no end >
	switch(type) {
		case "view":
			buttonString += "value=" + lecture_id + " onclick = view_quiz(this)>View";
			console.log("create view", buttonString);
			break;
		case "delete":
			buttonString += "value=" +lecture_id + " onclick = delete_quiz(this)>Delete";
			break;
		case "upload": //create full form instead? Copy from hardcoded lecturer/course.html, choose file will be made here as well
			buttonString += "value="+ lecture_id + "_" +date+ " onclick = upload_pptx(this)>Upload placeholder"; //see above
			break;
		default:
			console.log("something went wrong");
	}
	buttonString +="</button>";
	return buttonString;
}

function view_quiz(button) { 
	console.log("in view");
}

function delete_quiz(button) {
	console.log("in delete");
} 

function upload_pptx(button) { //uses form action for upload.php
	console.log("in upload");
}

function createLectureTable(data) { //to be added to document.ready()

	var lectureContent = data.split("|"); //remember to check if pop is needed
	var toAppend = "<div>"; //make divs possibly with id for each
	
	for (var i = 0; i < lectureContent.length; i+=3) { //possibly -1 on length comparison
		var lecture_id = lectureContent[i];
		var date = lectureContent[i+1];
		var name = lectureContent[i+2];
		toAppend+= date; //move furter down?
		if (name != "NULL") { 
			toAppend += " " + name;  
			toAppend += " " + createButtonString("view",lecture_id); //create view button value = lecture_id
			toAppend += " " + createButtonString("delete",lecture_id); //create delete button value = lecture_id
		}
		else {
			toAppend+= " " + createButtonString("upload", lecture_id, date); //only make var date if this case applies?
			//create upload button value = lecture_id + lecture.date (?)
		}
	}
		toAppend += "</div>";
		$("#course_content").append(toAppend);
}



