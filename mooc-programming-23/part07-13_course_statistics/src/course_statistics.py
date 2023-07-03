import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    
    courses = json.loads(data)
    result = []
    
    for course in courses:
        if course['enabled'] == True:
            fullName = course['fullName']
            name = course['name']
            year = course['year']
            exercises = sum(course['exercises'])
            activeCourse = (fullName, name, year, exercises)
            
            result.append(activeCourse)
    
    return result

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()

    course = json.loads(data)
    result = {}

    weeks, students, hours, exercises = 0, 0, 0, 0
    for key, value in course.items():
        if value['students'] > students:
            students = value['students']
        
        hours += value['hour_total']
        exercises += value['exercise_total']
        weeks += 1
    hours_average = hours//students
    exercises_average = exercises//students

    result['weeks'] = weeks
    result['students'] = students
    result['hours'] = hours
    result['hours_average'] = hours_average
    result['exercises'] = exercises
    result['exercises_average'] = exercises_average

    return result
      


if __name__ == "__main__":
    activeCourses = retrieve_all()
    print(activeCourses)
    course_data = retrieve_course("docker2019")
    print(course_data)

    #print in json format
    # print(json.dumps(activeCourses, indent=1))