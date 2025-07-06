scores={"小明":{"语文":85,"数学":96,"英语":88},
        "小红":{"语文":72,"数学":80,"英语":91},"小亮":{"语文":83,"数学":69,"英语":75}}
max_score=0
top_student=""
for student,subject in scores.items():
    total=sum(subject.values())
    print(f"{student}的总分为{total}")
    if total>max_score :
        max_score=total
        top_student=student
print(f"成绩最高者为{top_student}(总分{max_score})")










