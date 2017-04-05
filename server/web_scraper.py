import sys
import json
import urllib.request
from datetime import datetime
from db_connector import DbConnector


# The webscraper uses NTNU's sites to extract lecture information for a specific course code
class WebScraper(DbConnector):
    def __init__(self, course_code):
        self.year = str(datetime.now().year)  # Find current year
        self.course_code = course_code.upper()
        self.course_name = ""
        self.url = "http://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&" \
                    "p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=timetable&p_p_cacheability=" \
                   "cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_coursedetailsportlet_WAR_courselistportlet_" \
                   "courseCode=" + self.course_code + "&_coursedetailsportlet_WAR_courselistportlet_year=" + self.year \
                   + "&year=" + self.year + "&version=1"
        self.raw_data = {}  # Data collected from NTNU's websites
        self.lectures = []  # All lectures found by the scraper
        self.lectures_by_parallel = {}  # Sorting all lectures by parallel: {parallel:[lecture, lecture], ...}

    def run(self):
        try:
            self.get_raw_data()
            self.find_lectures()
            if self.lectures:
                self.update_db()
                self.commit()
        except KeyError:
            print("There is no information about this course")
        except Exception as error:
            print("There was en error writing to the db: ", error)
            self.error()
        finally:
            self.close()


    # Find all lectures for this course
    def find_lectures(self):
        for event in self.raw_data:
            # Set course name
            if self.course_name == "":
                self.course_name = event['courseName']

            # FOR = Forelesning, F/Ø = Forelesning/Øving
            if event['acronym'] in ('FOR', "F/Ø"):
                weeks = self.get_all_weeks(event['weeks'])
                for week in weeks:
                    programmes = self.programmes_to_string(event["studyProgramKeys"])
                    lecture = Lecture(str(event['dayNum']), event['from'], event['to'], str(week), self.year, programmes)
                    self.lectures.append(lecture)
                    if programmes in self.lectures_by_parallel:
                        self.lectures_by_parallel[programmes].append(lecture)
                    else:
                        self.lectures_by_parallel[programmes] = [lecture]

    def update_db(self):
        make_course = "INSERT INTO Course VALUES(%s, %s)"
        make_parallel = "INSERT INTO Parallel(programmes, course_code) VALUES(%s, %s)"
        make_lecture = "INSERT INTO Lecture(lectureDate) VALUE(%s)"
        set_lecture_parallel = "INSERT INTO LectureParallel VALUES(%s, %s)"
        self.cursor.execute(make_course, (self.course_code, self.course_name))
        for parallel in self.lectures_by_parallel:
            self.cursor.execute(make_parallel, (parallel, self.course_code))
            parallel_id = self.cursor.lastrowid
            for lecture in self.lectures_by_parallel[parallel]:
                self.cursor.execute(make_lecture, (lecture.datetime,))
                lecture_id = self.cursor.lastrowid
                self.cursor.execute(set_lecture_parallel, (lecture_id, parallel_id))

    def get_raw_data(self):
        # NTNU's website is giving different responses. Run scraper several times to assure we are getting all data
        for i in range(10):
            raw_data = json.loads(urllib.request.urlopen(self.url).read())['course']['summarized']
            if len(raw_data) > len(self.raw_data):
                self.raw_data = raw_data

    @staticmethod
    def get_all_weeks(weeks_list):
        weeks = []
        for element in weeks_list:
            element = element.split("-")
            if len(element) > 1:
                for week_number in range(int(element[0]), int(element[1]) + 1):
                    weeks.append(week_number)
            else:
                weeks.append(int(element[0]))
        return weeks

    @staticmethod
    def programmes_to_string(programmes):
        return ", ".join(program for program in programmes)

    def print_lectures(self):
        for lecture in self.lectures:
            print(lecture.to_string())


class Lecture:
    def __init__(self, day, from_time, to_time, week, year, programmes):
        self.day = day  # 1 = monday, 2 = tuesday...
        self.from_time = from_time
        self.to_time = to_time
        self.week = week
        self.year = year
        self.programmes = programmes
        self.datetime = self.generate_datetime()

    def generate_datetime(self):
        return datetime.strptime(self.year + "-W" + self.week + "-" + self.day + " " + self.from_time,  "%Y-W%W-%w %H:%M")

    def to_string(self):
        return "This lecture is on day " + str(self.day) + " from " + self.from_time + " to " + self.to_time + \
               " the week " + str(self.week) + " for these programmes: " + self.programmes + \
               ". That results in this datetime " + str(self.datetime)

if __name__ == '__main__':
    web_scraper = WebScraper(sys.argv[1])
    web_scraper.run()
