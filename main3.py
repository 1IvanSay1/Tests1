from text import courses, mentors, durations
def count(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    for course in courses_list:
        all_list = []
        all_list.extend(mentors[0] + mentors[1] + mentors[2] + mentors[3])
        all_list_str = ', '.join(all_list)
        all_names_list = all_list_str.split(' ')
        name = all_names_list[0::2]
        name.sort(key=len)
        unique_names = set(name)
        same_name_list = []
        for a in unique_names:
            count_a = 0
            for b in course["mentors"]:
                if a in b:
                    count_a += 1
                    if count_a > 1 and a not in same_name_list:
                        same_name_list.append(a)
    same_name_list_res = []
    for i in same_name_list:
        for j in course["mentors"]:
            if i in j:
                same_name_list_res.append(j)
                same_name_list_res.sort()
    return (f"На курсе {course['title']} есть тёзки: {', '.join(same_name_list_res)}")

if __name__ == '__main__':
    courses = courses
    mentors = mentors
    durations = durations
    count(courses, mentors, durations)