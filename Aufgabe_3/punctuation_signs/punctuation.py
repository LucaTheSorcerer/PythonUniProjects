def point(tut):
    tut.right(90)
    tut.pu()
    tut.fd(70)
    tut.pd()
    tut.dot()
    tut.pu()
    tut.bk(100)
    tut.left(90)
    tut.fd(10)
    tut.pd()

def question_mark(tut):
    tut.right(90)
    tut.pu()
    tut.fd(70)
    tut.pd()
    tut.dot()
    tut.right(180)

    tut.pu()
    tut.fd(30)
    tut.pd()
    tut.fd(30)

    tut.right(90)

    for x in range(180):
        tut.forward(0.5)
        tut.left(1)

    tut.right(180)
    tut.pu()
    tut.fd(30)
    tut.left(90)

    tut.pu()
    tut.fd(60)
    tut.pd()
    tut.left(90)

def exclamation_mark(tut):
    tut.right(90)
    tut.pu()
    tut.fd(70)
    tut.pd()
    tut.dot()
    tut.right(180)

    tut.pu()
    tut.fd(40)
    tut.pd()
    tut.fd(80)

    tut.pu()
    tut.bk(180)
    tut.left(90)
    tut.fd(10)
    tut.pd()

    tut.left(180)
