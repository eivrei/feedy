var lecture_id = window.location.hash.substr(1);

$(document).ready(function() {
	$.get("../../php/lecturer_getStatsHeadinfo.php?lecture=" + lecture_id, function (data){
		var dateAndTime = data.split("|");
		var date = dateAndTime[0];		
		var name = dateAndTime[1];
		var toReplace = ""; //probably unneeded step
		toReplace += date + " <i>" + name + "</i>";
		$("#lecture_name").html(toReplace);
	});

	
	$.get("../../php/lecturer_getStatistics.php?lecture=" + lecture_id, function (data) {
		
		if (data != "NO DATA") {
			//var statArray = data.split("|"); 
			createStatString(data); //if on data length?
		}
		else {
			console.log(data); //why?
		}

	});	
});

//check if parameter works

function createStatString(statArray) {
	toAppend="";
	var dataSets = statArray.split("]");
	dataSets.pop();
	var currentSet;
	var name, numAnswers, percentage, spread;
	var keywords = [];
	
	//process data into relevant datasets
	for (var i = 0; i < dataSets.length; i++) { //for each [ ] block in stat array
		currentSet = dataSets[i].split(",");
		name = "";
		numAnswers = 0;
		percentage = 0;
		spread = 0;
		keywords = [];
		for (var j = 0; j < currentSet.length; j++) { //for each comma-separeted element in currentSet
			switch(j) {
				case 0:
					name = currentSet[j].replace(/(\r\n|\n|\r)/gm,"");
					name = name.substr(1);
					break;
				case 1:
					numAnswers = currentSet[j];
					break;
				case 2:
					percentage = currentSet[j];
					break;
				case 3:
					spread = currentSet[j];
					break;
				default: //happens on j > 3, assumes correct data
					keywords.push(currentSet[j]);
			}
		}
		toAppend+=createDataSetString(name, numAnswers, percentage, spread, keywords);
	}
	$("#stats_content").append(toAppend);
}

//for later: Make arguments an array instead?
function createDataSetString(name, numAnswers, percentage, spread, keywords, alt1, alt2, alt3, alt4) {
	var dataSetString = "";
	dataSetString += "<h3>" + name + "</h3>";
	dataSetString += "<ul>";
	dataSetString += "<li><b>Answers: </b>" + numAnswers + "</li>";
	dataSetString += "<li><b>Average correctness percentage: </b>" + percentage + "</li>";
	dataSetString += "<li><b>Spread: </b>" + spread + "</li>";
	dataSetString +="<li><b>Keywords found in < 20% of answers: </b>";
	keywords.forEach(function (item, index) {
		dataSetString += item;
		if (index !== keywords.length - 1){
			dataSetString += ", ";
		}
	});
	dataSetString += "</li>";
	dataSetString += "<li><b>Lower percentage students say: </b>";
    dataSetString += "<ul>";
    dataSetString += "<li><b>Pace is too fast: </b>" + alt1 + "</li>";
    dataSetString += "<li><b>Too few/poor examples: </b>" + alt2 + "</li>";
    dataSetString += "<li><b>Unfocused presentation: </b>" + alt3 + "</li>";
    dataSetString += "<li><b>Lacking background info: </b>" + alt4 + "</li>";
    dataSetString += "</ul>";
	dataSetString += "</ul>";
	return dataSetString;
}

function generateStatistics() {
    $.get("../../php/lecturer_generateStatistics.php?lecture=" + lecture_id, function (data) {
        if (data === "There are no answers to this lectureOK"){
            alert("There are no answers to this lecture");
        }else if (data !== "OK"){
            alert("Something went wrong. Contact the system administrator.");
        }
		location.reload();
    });
}
