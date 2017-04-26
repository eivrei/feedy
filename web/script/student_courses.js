$(document).ready(function() {
	$.get("../../php/student_getCourses.php", function (data) {
		var courses = data.split("|"); //length will always be multiple of 3 (course code, -name and programmes)
		courses.pop(); //removes last empty element after split (needed for lecturers with >1 courses in current implementation
		for (var i = 0; i < courses.length-1; i+=4) {
			var course_code = courses[i].replace(/(\r\n|\n|\r)/gm,"");
			var course_name = courses[i+1].replace(/(\r\n|\n|\r)/gm,"");
			var parallels = courses[i+2].replace(/(\r\n|\n|\r)/gm,"");
			var parallel_id = courses[i+3].replace(/(\r\n|\n|\r)/gm,"");
			$("#div_courselist").append("<div class='courseElement' onclick=\"location.href='course.php#" + course_code + "_" + parallel_id + "';\"><p class='courseName'>" + //generate correct link path
										courses[i] + " " + courses[i + 1] + " </p><p class='parallelName'>" + //generate actual link on page
										courses[i+2] + "</p></div>"); //Display related programmes 
										//remember "fake" space

		}
	});



});