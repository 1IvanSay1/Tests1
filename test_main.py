from text import courses, mentors, durations
import pytest
from main1 import courses_duration
from main2 import connection
from main3 import count
from yandex import create_folder


def test_courses_duration():
    result = courses_duration(courses, mentors, durations)
    expectation = 'Python-разработчик с нуля - 12 месяцев'
    assert result == expectation

def test_connection():
    result = connection(courses, mentors, durations)
    expectation = ('Связи нет', 'Порядок курсов по длительности: [2, 0, 1, 3]', 'Порядок курсов по количеству преподавателей: [2]')
    assert result == expectation

def test_count():
    result = count(courses, mentors, durations)
    expectation = 'На курсе Frontend-разработчик с нуля есть тёзки: Александр Беспоясов, Александр Фитискин, Александр Шлейко'
    assert result == expectation

def test_create_folder():
    path = 'New'
    result = create_folder(path)
    expectation = '<Response [201]>'
    assert result == expectation