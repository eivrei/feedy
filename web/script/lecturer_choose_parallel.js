
function searchForCourse() {
	var to_search = document.getElementById("course-search").value;
	//consider text validation/case-insensitivity
	$.get("../../php/lecturer_getParallels.php?course=" + to_search + "_" + lecturer_id, function (data) {
		//PHP tries webscraping on no results by itself
		console.log(data);
		data = data.split("|");
		
		if (data.length > 1) {
			createParallelTable(data);
		}
		else {
		alert(data);
		}
	});
}
//set data = 0 to retrieve data on to_search, otherwise leave out to_search (uses default value)
function createParallelTable(data) {
	//note: two first elements of data are course_code, course_name
	var courses = data;
	courses.pop(); //removes last empty element after split 
	document.getElementById("course_name").innerHTML = data[0], data[1];
	var appendString = "";
	for (var i = 2; i < courses.length-1; i+=2) {
		var parallel = courses[i];
		var parallel_id = courses[i+1];
		appendString+=("<div class='courseElement' onclick='selectParallel()'><p class='courseName'>" + 
									parallel + " </p><p class='parallelName'></div>");
		$("#div_pallellist").html(appendString);
									//remember "fake" space
		
	}
}

function selectParallel() {
	console.log("selected");
}
//------------------- Warning should be displayed anyway?