from text import courses, mentors, durations
def courses_duration(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [id])
    durations_dict[key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    for duration, ids in durations_dict.items():
        for id in ids:
            return (f'{courses_list[id]["title"]} - {duration} месяцев')
        
        
if __name__ == '__main__':
    courses = courses
    mentors = mentors
    durations = durations
    courses_duration(courses, mentors, durations)
