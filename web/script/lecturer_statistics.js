var lecture_id = window.location.hash.substr(1);
var no_data = false;

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
        if (data.replace(/(\r\n|\n|\r)/gm,"") !== "NO DATA") {
            createStatString(data); //if on data length?
        }
        else {
            $("#stats_content").append("<div><br>There are currently no student answers to this quiz.</div>");
            no_data = true;
        }

    });
});

//check if parameter works

function createStatString(statArray) {
    var toAppend="";
    var dataSets = statArray.split("]");
    dataSets.pop();
    var currentSet;
    var name, numAnswers, percentage, spread, alt1, alt2, alt3, alt4;
    var keywords = [];

    //process data into relevant datasets
    for (var i = 0; i < dataSets.length; i++) { //for each [ ] block in stat array
        currentSet = dataSets[i].split(",");
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
                case 4:
                    alt1 = currentSet[j];
                    break;
                case 5:
                    alt2 = currentSet[j];
                    break;
                case 6:
                    alt3 = currentSet[j];
                    break;
                case 7:
                    alt4 = currentSet[j];
                    break;
                default: //happens on j > 7, assumes correct data
                    // console.log(currentSet[j]);
                    keywords.push(currentSet[j]);
            }
        }
        toAppend+=createDataSetString(name, numAnswers, percentage, spread, keywords, alt1, alt2, alt3, alt4);
        // console.log(keywords);
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
        if(data !== "OK" && !no_data){
            alert("Something went wrong. Contact the system administrator.");
        }
        location.reload();
    });
}

