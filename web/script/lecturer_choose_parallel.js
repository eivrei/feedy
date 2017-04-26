function searchForCourse() {
	var to_search = document.getElementById("course-search").value;
	//consider text validation/case-insensitivity
	$.get("../../php/lecturer_getParallels.php?course=" + to_search, function (data) {
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
};
//set data = 0 to retrieve data on to_search, otherwise leave out to_search (uses default value)
function createParallelTable(data) {
    //note: two first elements of data are course_code, course_name
    var courses = data;
    courses.pop(); //removes last empty element after split
    document.getElementById("course_name").innerHTML = courses[0] + " " + courses[1];
    var appendString = "";
    for (var i = 2; i < courses.length-1; i+=2) {
        var parallel = courses[i];
        var parallel_id = courses[i+1];
        appendString+=("<div id='"+ parallel_id + "' class='courseElement'  onclick='selectParallel(this)' '><p class='courseName'>" +
        parallel + " </p><p class='parallelName'></div>");
        $("#div_pallellist").html(appendString);
        //remember "fake" space
    }
}

function selectParallel(div) {
    parallel_id = div.id;
    //check if lecturer already added, if so alert
    //else: add to course and alert of sucsess
    $.get("../../php/lecturer_addToParallel.php?parallel_and_id=" + parallel_id + "_" + lecturer_id, function (data) {
        //PHP checks if added already, otherwise adds. Return data reflects this (SUCSESS|error)
        //console.log("in select", data, "end data");
        if (data == "SUCSESS") {
            alert("You are now added to this course");
        }
        else {
            alert(data);
        }
    });
}
//------------------- Warning should be displayed anyway?

