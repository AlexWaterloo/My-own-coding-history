def final_grade(mid,mtotal,exam,xtotal):
    g1 =mid/mtotal*100
    print(g1)
    g2 =exam/xtotal*100
    print(g2)
    f_grade=g1*0.5+g2*0.5
    print(f_grade)
    return f_grade
final_grade(30,35,80,83)
