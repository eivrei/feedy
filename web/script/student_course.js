var hash = window.location.hash.substr(1);
hash = hash.split("_");
var course_code =  hash[0];
var parallel_id =  hash[1];

$(document).ready(function() {
	$.get("../../php/student_getCourse.php?course=" + course_code + "_" + parallel_id, function (data) {
		if (data !== "NO DATA") {
		$("#course_name").html(course_code);
		createLectureTable(data); //if on data length?
		}
		else {
		//console.log(data); //why?
		}

	});	
});

function take_quiz(button) {
	var redirectString = "quiz.php#" + button.value;
	window.location = redirectString;
}

function createTakeQuizButtonString(lecture_id) {
	var buttonString = "<button class='takeQuiz btn btn-md-2 btn-primary' type='button'" ; //note: no end >
	buttonString += "value=" + lecture_id + " onclick = take_quiz(this)>Take quiz";
	buttonString +="</button></span>";
	return buttonString;
}

function createLectureTable(data) { 
	var lectureContent = data.split("|"); //remember to check if pop is needed
	lectureContent.pop();
	var toAppend = ""; //make divs possibly with id for each
	
	for (var i = 0; i < lectureContent.length; i+=3) { //possibly -1 on length comparison
		var lecture_id = lectureContent[i];
		var date = lectureContent[i+1];
		var name = lectureContent[i+2];
		toAppend+= "<div class='lectureElement lecture row'><div class='col-md-7 col-xs-12'><p class='lectureInfo' " + lecture_id +"'>" + date + "</p>"; //link course name to statistics page
		if (name !== "") { //lectures with names have quizzes already
			toAppend += " <i class='lectureName'>" + name + "</i></div>";
			toAppend += " <div class='innerLecture col-md-5 col-xs-12'> "; //create view button value = lecture_id
			toAppend += " " + createTakeQuizButtonString(lecture_id); //create view button value = lecture_id
		}
		toAppend+="</div></div><div class='line lecture'></div>";
	}
		//toAppend += "</br>";
		$("#course_content").append(toAppend);
}
