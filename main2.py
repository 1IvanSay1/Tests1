from text import courses, mentors, durations
def connection(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
        mcount_index.append([len(course["mentors"]), index])
    duration_index.sort()
    mcount_index.sort()
    indexes_d = []
    indexes_m = []
    for d in duration_index:
        indexes_d.append(d[1])
    for m in mcount_index:
        indexes_m.append(m[1])
        return ("Связь есть" if d == m else "Связи нет"), (f"Порядок курсов по длительности: {indexes_d}"), (f"Порядок курсов по количеству преподавателей: {indexes_m}")

if __name__ == '__main__':
    courses = courses
    mentors = mentors
    durations = durations
    connection(courses, mentors, durations)