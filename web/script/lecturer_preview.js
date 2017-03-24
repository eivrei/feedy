var lecture_id = window.location.hash.substr(1);

$(document).ready(function() {
	//new $.get for quiz name? Probably just adds confusion if sent from getPreview
	$.get("../../php/lecturer_getStatsHeadinfo.php?lecture=" + lecture_id, function (data){
		console.log(data);
		var dateAndTime = data.split("|");
		var date = dateAndTime[0];		
		var name = dateAndTime[1];
		var toReplace = ""; //probably unneeded step
		toReplace += date + " <i>" + name + "</i>";
		$("#quiz_name").html(toReplace);
	});

	$.get("../../php/lecturer_getPreview.php?lecture=" + lecture_id, function (data) {
		console.log(data);
		
		if (data != "NO DATA") {
			var topics = data.split("|"); 
			topics.pop(); //removes some undefined bullshit that should be tracked down
			createQuizPreview(topics);
			//$("#course_name").html(course_code);
			//createQuizPreview(data); //if on data length?
		}
		else {
			//console.log(data); //why?
		}

	});	
});

/* PSEUDOCODE
format data topic -> related keywords + weight
append sequentially? Might avoid empty page/whole page popping
(if not sequential add)
for each topic {
	make topic header string
	make topic header edit/delete string ON SAME LINE AS TOPIC HEADER STRING
	for each topic keyword {
		make topic keyword + weight string
		make edit/delete buttonstring ON SAME LINE AS TOPIC KEYWORD + WEIGHT STRING
		append to header string? NEEDS NEW DIV/LINEBREAK/SOMETHING
	}
	append to appendString
}
append appendString to html
*/

//both of these need better names
function editQuiz(button) {
	console.log("in edit");
}

function deleteQuiz(button) {
	console.log("in delete");
}

function createButtonString(type, id) {
	var buttonString = "<button value='" +type + "_" + id + "'class='btn btn-sm btn-primary' type='button'"; //note lack of end tag
	
	if (type == "edit") {
		buttonString+="onclick = editQuiz(this)>Edit";
	}
	else if (type == "delete") {
		buttonString+="onclick = deleteQuiz(this)>Delete";
	}
	else {
		console.log("something went wrong in createButtonString");
	}

	buttonString+= "</button>";
	return buttonString;
}

function createQuizPreview(topics){ 
	var appendString = "";
	var currentTopic = "NULL" //should not match with db-content
	var topic; //[i]
	var keyword; //[i+1]
	var weight; //[i+2]
	var topic_id; //[i+3]
	var keyword_id; //[i+4];
	
	for (var i = 0; i < topics.length;i+=5) { //five returned rows per result from php
		topic = topics[i];
		keyword = topics[i+1];
		weight = topics[i+2];
		keyword_id = topics[i+3];

		if (topic != currentTopic) {
			currentTopic = topic;
			topic_id = topics[i+4]; //places here because it is often not needed
			//new topicstring + 2x buttons
			appendString+="<span><h3 style=display:inline-block;>" + currentTopic + "</h3></span>";
			appendString+= createButtonString("edit", topic_id);
			appendString+= createButtonString("delete", topic_id);
			
		}
		//new keyword string + weight string + 2x buttonstring
		appendString+="<div><span>" + keyword + ": weight " + weight + "</span>";
		appendString+= createButtonString("edit", keyword_id);
		appendString+= createButtonString("delete", keyword_id);
		appendString+= "</div>";
	}
	//appendString +="</div>";
	console.log("appendstring: ", appendString);
	$("#quiz_content").append(appendString);
}


