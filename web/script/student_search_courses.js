//filter through array made in client
//doesnt need to connect to db
window.onload = function(){
	
	$('input[type="text"]').keypress(function (e) {
		var code = e.keyCode || e.which;
		if ( code === 13 ){
			$("#searchButton").click();
		}
	});

	document.getElementById("searchButton").onclick = function(){
		search();
	};

	function search(){
		$.get("../../php/student_getCourses.php", function (data){
			var courses = data.split("|"); 
			var query = 
			document.getElementById("searchQuery").value;
			
			//iterate through array
			var arrayLength = courses.length;
			var match = false;
			var ctr = 1;
			for ( var i=0; i<arrayLength; i++){
				//case insensitive
				if ( courses[i].toUpperCase().includes(query.toUpperCase()) ){
					match = true;
				}
				//when counter reaches 4, we have iterated through
				//a course and its corresponding values
				if ( (ctr % 4) === 0 && i !== 0){
					//if match is true, keep the array, set match to false
					if (match){
						match = false;
					//else set the element and prev 3 to null (entire course)
					} else{
						courses[i] = null;
						courses[i-1] = null;
						courses[i-2] = null;
						courses[i-3] = null;
					}
				}
				ctr += 1;
			}

			//if courses[x] exists, we keep it and the next three elements
			//this is an entire lecture, and its corresponding info
			var newArray = [];
			for (var x = 0; x < courses.length-1; x+=4) {
				if (courses[x]) {
			    	newArray.push(courses[x]);
			    	newArray.push(courses[x+1]);
			    	newArray.push(courses[x+2]);
			    	newArray.push(courses[x+3]);
			    }
			}
			courses = newArray;
			//remove current array from html
			//.courseElement is the div class of each individual course
			$('.courseElement').remove();
			//create new array in html
			for (var n = 0; n < courses.length-1; n+=4) {
					var course_code = courses[n].replace(/(\r\n|\n|\r)/gm,"");
					var course_name = courses[n+1].replace(/(\r\n|\n|\r)/gm,"");
					var parallels = courses[n+2].replace(/(\r\n|\n|\r)/gm,"");
					var parallel_id = courses[n+3].replace(/(\r\n|\n|\r)/gm,"");
					$("#div_courselist").append("<div class='courseElement' onclick=\"location.href='course.php#" + course_code + "_" + parallel_id + "';\"><p class='courseName'>" + //generate correct link path
												courses[n] + " " + courses[n + 1] + " </p><p class='parallelName'>" + //generate actual link on page
												courses[n+2] + "</p></div>"); //Display related programmes 
										}
		});
	}
};