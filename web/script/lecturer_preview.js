var hash = window.location.hash.substr(1);
hash = hash.split("_");
var lecture_id = hash[0];
var course_code = hash[1];
var parallel_id = hash[2];
var delete_topic = true;

$(document).ready(function() {
    document.getElementById("prevPage").href = "course.php#" + course_code + "_" + parallel_id;
	//Retrives and inputs quiz name as page name
	$.get("../../php/lecturer_getStatsHeadinfo.php?lecture=" + lecture_id, function (data){
		var dateAndTime = data.split("|");
		var date = dateAndTime[0];		
		var name = dateAndTime[1];
		var toReplace = ""; //probably unneeded step
		toReplace += date + " <i>" + name + "</i>";
		$("#quiz_name").html(toReplace);
	});
	//retrieves quiz data for lecture and runs functions to format/display content + edit/delete funtionality
	$.get("../../php/lecturer_getPreview.php?lecture=" + lecture_id, function (data) {
		if (data !== "NO DATA") {
			var topics = data.split("|"); 
			topics.pop(); //removes some undefined bullshit that should be tracked down
			createQuizPreview(topics);
			//$("#course_name").html(course_code);
		}
		else {
			//console.log(data); //why?
		}

	});	
});

//both of these need better names
function editQuizData(button) {
    window.location = "edit_topic.php#" + button.value.split("_")[1] + "_" + window.location.hash.substr(1);
}

function deleteQuizData(button) {
	if (delete_topic) {
        if (confirm("Are you sure?")) {
            $.get("../../php/lecturer_delete_quiz_data.php?topic=" + button.value.split("_")[1], function (data) {
                if (data === "Data deleted") {
                    alert("The quiz was successfully deleted");
                    location.reload();
                }
            });
        }
    }
    else {
    	alert("There must be at least 4 topics at all times");
	}
}

function createButtonString(type, topic_id) {
	var buttonString = "<button value='" +type + "_" + topic_id; //note lack of end tag
	
	if (type === "edit") {
		buttonString+="'class='btn btn-sm btn-primary' type='button' onclick = editQuizData(this)>Edit";
	}
	else if (type === "delete") {
		buttonString+="'class='btn btn-sm btn-primary' type='button' onclick = deleteQuizData(this)>Delete";
	}
	else {
		console.log("something went wrong in createButtonString");
	}

	buttonString+= "</button>";
	return buttonString;
}

function createQuizPreview(topics){ 
	var appendString = "";
	var currentTopic = "NULL"; //should not match with db-content
	var topic; //[i]
	var keyword; //[i+1]
	var weight; //[i+2]
	var keyword_id; //[i+3];
	var topic_id; //[i+4]
	var number_of_topics = 0;

	for (var i = 0; i < topics.length;i+=5) { //five returned rows per result from php
		topic = topics[i];
		keyword = topics[i+1];
		weight = topics[i+2];
		keyword_id = topics[i+3];

		if (topic !== currentTopic) {
			number_of_topics ++;
			currentTopic = topic;
			topic_id = topics[i+4]; //places here because it is often not needed
			//new topicstring + 2x buttons
			appendString+="<h3 style=display:inline-block;><span>" + currentTopic + " </span>";
			appendString+= createButtonString("edit", topic_id);
			appendString+=" ";
			appendString+= createButtonString("delete", topic_id);
			appendString+= "</h3>";
            appendString+="<div class='row'>";
            appendString+="<div class='col-md-2 col-xs-5'><h5>Keywords:</h5></div>";
            appendString+="<div class='col-md-2 col-xs-5'><h5>Weight:</h5></div>";
            appendString+= "</div>";
			
		}
		//new keyword string + weight string + 2x buttonstring
		appendString+="<div class='row'>";
		appendString+="<div class='col-md-2 col-xs-5'>" + keyword + "</div>";
		appendString+="<div class='col-md-1 col-xs-5'>" + weight + "</div>";
		//appendString+= createButtonString("edit", keyword_id); //buttons for each keyword
		//appendString+= createButtonString("delete", keyword_id);
		appendString+= "</div>";
	}
	//appendString +="</div>";
	$("#quiz_content").append(appendString);

	if(number_of_topics === 4){
        delete_topic = false;
    }
}


