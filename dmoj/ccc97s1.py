for i in range(int(input())):
    subjects = []
    verbs = []
    objects = []
    subject_count = int(input())
    verb_count = int(input())
    object_count = int(input())
    for i in range(subject_count):
        subjects.append(input().strip())
    for i in range(verb_count):
        verbs.append(input().strip())
    for i in range(object_count):
        objects.append(input().strip())

    for subject in subjects:
        for verb in verbs:
            for object in objects:
                print("{subject} {verb} {object}.".format(subject=subject, verb=verb, object=object))