def data_input():
    lessonNo = input()
    lesson = [lessonNo]
    lessonHr = int(input())
    for i in range(lessonHr):
        lessonTime = input()
        lesson.append(lessonTime)
    return lesson

def check(lesson1, lesson2):
    set1 = set(lesson1)
    set2 = set(lesson2)
    checked = list(set1.intersection(set2))
    for i in range(len(checked)):
        print(lesson1[0],"and",lesson2[0],"conflict on",checked[i])

L1 = data_input()
L2 = data_input()
L3 = data_input()

checked_lessons = check(L1,L2)
checked_lessons = check(L1,L3)
checked_lessons = check(L2,L3)