#program by : Yhafar
# 2023.03.10
# wrk-05.py    :  python 101 by uncle engineer

student_data = {'อันวา': {'รหัสนักเรียน': '1001','คะแนนเก็บ': 65,'คะแนนสอบ': 24},
'อานัส': {'รหัสนักเรียน': '1004','คะแนนเก็บ': 58,'คะแนนสอบ': 28},
'ชากีร': {'รหัสนักเรียน': '1007','คะแนนเก็บ': 63,'คะแนนสอบ': 25},
'ก็อลบี': {'รหัสนักเรียน': '1025','คะแนนเก็บ': 69,'คะแนนสอบ': 29}}


for std in sorted(student_data):
    print('===='+std+'====') # แสดงชื่อ
    score=student_data[std]['คะแนนเก็บ']+student_data[std]['คะแนนสอบ']
    for s in student_data[std]:
        print(s+f': {student_data[std][s]}')
    print(f'score : {score}')    
    if score>=91 and score<=100:
        print("Your Grade is A1")
    elif score>=81 and score<91:
        print("Your Grade is A2")
    elif score>=71 and score<81:
        print("Your Grade is B1")
    elif score>=61 and score<71:
        print("Your Grade is B2")
    elif score>=51 and score<61:
        print("Your Grade is C1")
    elif score>=41 and score<51:
        print("Your Grade is C2")
    elif score>=33 and score<41:
        print("Your Grade is D")
    elif score>=21 and score<33:
        print("Your Grade is E1")
    elif score>=0 and score<21:
        print("Your Grade is E2")
    else:
        print("Invalid Score!")    
    