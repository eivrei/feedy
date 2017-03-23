$(document).ready(function() {
	$.get("../../php/student_getCourses.php", function (data) {
		console.log(data);
		var courses = data.split("|"); //length will always be multiple of 3 (course code, -name and programmes)
		courses.pop(); //removes last empty element after split (needed for lecturers with >1 courses in current implementation
		console.log(courses);
		for (var i = 0; i < courses.length-1; i+=4) {
			var course_code = courses[i];
			var course_name = courses[i+1]
			var parallels = courses[i+2];
			var parallel_id = courses[i+3];
			$("#tb_courselist").append("<tr><td><a href='course.html#" + course_code + "_" + parallel_id + "'>" + //generate correct link path
										courses[i] + " " + courses[i + 1] + "</a></td>" + //generate actual link on page
										"<td>" + courses[i+2] + "</td></tr>"); //Display related programmes 

		}
	});



});