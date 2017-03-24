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
/* PSEUDOCODE
Retrieve anchors
Give dynamic course name possibly with parallel
createLectureTable(data)

function CreateLectureTable(data) {
	
	while (more lectures) {
		if (hasname) {
		create date field
		create name field
		add take quiz button
		}
		else {
		create date field
		add "no quiz available" text
		}
	}
}

function take_quiz(button) {
	go to take quiz page for correct quiz
}

function createTakeQuizButtonString(lecture_id) {
	construct whole button string (not as separate function?)
	"take quiz"
	link-string to redirect to correct page
}
*/