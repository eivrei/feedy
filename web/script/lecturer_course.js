var hash = window.location.hash.substr(1);
hash = hash.split("_");
var course_code =  hash[0];
var parallel_id =  hash[1];

$(document).ready(function() {
	$.get("../../php/lecturer_course.php?course=" + course_code + "_" + parallel_id, function (data) {
		console.log(data);
		var courses = data.split("|"); //length will always be multiple of 3 (course code, -name and programmes)
		courses.pop(); //removes last empty element after split (needed for lecturers with >1 courses in current implementation
		console.log(courses);
		for (var i = 0; i < courses.length-1; i+=4) {
			$("#tb_courselist").append("<tr><td><a href='course.html#" + courses[i] + "_" + courses[i + 3] + "'>" + //generate correct link path
										courses[i] + " " + courses[i + 1] + "</a></td>" + //generate actual link on page
										"<td>" + courses[i+2] + "</td></tr>"); //Display related programmes 

		}
		
	});



});
