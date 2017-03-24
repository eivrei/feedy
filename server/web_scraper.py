import json
import urllib.request
from datetime import datetime


# The webscraper uses NTNU's sites to extract lecture information for a specific course code
class WebScraper:
    def __init__(self, course_code):
        self.year = str(datetime.now().year)  # Find current year
        self.course_code = course_code.upper()
        self.url = "http://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&" \
                    "p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=cacheLevelPage&" \
                    "p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_courseCode=" + \
                    self.course_code + "&_coursedetailsportlet_WAR_courselistportlet_year=" + self.year + "&year=" + self.year + "&version=1"
        self.response = ""
        self.data = {}
        self.lectures = []

    def run(self):
        try:
            self.response = urllib.request.urlopen(self.url)
            self.data = json.loads(self.response.read())['course']['summarized']
            self.find_schedule()
            self.print_lectures()
        except KeyError:
            print("There is no information about this course")

    # Find all lectures for this course
    def find_schedule(self):
        for event in self.data:
            print(event)
            # FOR = Forelesning, F/Ø = Forelesning/Øving
            if event['acronym'] in ('FOR', "F/Ø"):
                self.lectures.append(Lecture(event['dayNum'], event['from'], event['to'], event['weeks'], event['studyProgramKeys']))

    def print_lectures(self):
        for lecture in self.lectures:
            print(lecture.to_string())


class Lecture:
    def __init__(self, day, from_time, to_time, weeks, programmes):
        self.day = day  # 1 = monday, 2 = tuesday...
        self.from_time = from_time
        self.to_time = to_time
        self.weeks = weeks
        self.programmes = programmes

    def to_string(self):
        return "This lecture is on day " + str(self.day) + " from " + self.from_time + " to " + self.to_time + " the weeks " + \
               ", ".join(week for week in self.weeks) + " for these programmes: " + ", ".join(program for program in self.programmes)

if __name__ == '__main__':
    webScraper = WebScraper(input("Course code: "))
    webScraper.run()
