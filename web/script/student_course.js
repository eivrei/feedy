var hash = window.location.hash.substr(1);
hash = hash.split("_");
var course_code =  hash[0];
var parallel_id =  hash[1];

$(document).ready(function() {
	$.get("../../php/student_getCourse.php?course=" + course_code + "_" + parallel_id, function (data) {
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

function take_quiz(button) {
	console.log("in take quiz");
}

function createTakeQuizButtonString(lecture_id) {

	var buttonString = "<button id='" + lecture_id + "' class='btn btn-md btn-primary' type='button'" ; //note: no end >
	buttonString += "value=" + lecture_id + " onclick = take_quiz(this)>Take quiz";
	buttonString +="</button>";
	console.log(buttonString);
	return buttonString;
}

function createLectureTable(data) { 

	var lectureContent = data.split("|"); //remember to check if pop is needed
	lectureContent.pop();
	var toAppend = "<div><span>"; //make divs possibly with id for each
	
	for (var i = 0; i < lectureContent.length; i+=3) { //possibly -1 on length comparison
		var lecture_id = lectureContent[i];
		var date = lectureContent[i+1];
		var name = lectureContent[i+2];
		console.log("name =" ,name);
		toAppend+= "<a href='statistics.html#" + lecture_id +"'>" + date + "</a>"; //link course name to statistics page
		if (name != "NULL") { 
			toAppend += " <i>" + name + "</i></span>";  
			toAppend += " " + createTakeQuizButtonString(lecture_id); //create view button value = lecture_id
		}
		toAppend+="</div>";
	}
		//toAppend += "</br>";
		console.log(toAppend);
		$("#course_content").append(toAppend);
}
