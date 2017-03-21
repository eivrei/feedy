var username = getCookie("Username");

$(document).ready(function() {
	$.get("../../php/lecturer_courses.php?id=" + username, function (data) {
	//console.log(data);
		console.log(data);
		var courses = data.split("|"); //length will always be multiple of 3 (course code, -name and programmes)
		courses.pop(); //removes last empty element after split (needed for lecturers with >1 courses in current implementation
		console.log(courses);
		for (var i = 0; i < courses.length-1; i+=3) {
			$("#tb_courselist").append("<tr><td><a href='course.html#" + courses[i] + "'>" + //generate correct link path
										courses[i] + " " + courses[i + 1] + "</a></td>" + //generate actual link on page
										"<td>" + courses[i+2] + "</td></tr>"); //Display related programmes 

		}
		
	});



});


		/*$("#tr_course_code").append("<td>" + courses[i] + "</td>");
		$("#tr_courseName").append("<td>" + courses[i+1] + "</td>");
		$("#tr_programmes").append("<td>" + courses[i+2] + "</td>");*/