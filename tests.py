import encoder_decoder
def test1():
    print("\n********** Test1 **********")
    msg = "abc"
    k = len(msg)
    n = 3
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test2():
    print("\n********** Test2 **********")
    msg = "a"
    k = len(msg)
    n = 2
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test3():
    print("\n********** Test3 **********")
    msg = "a"
    k = len(msg)
    n = 10
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test4():
    print("\n********** Test4 **********")
    msg = "Hello"
    k = len(msg)
    n = 15
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test5():
    print("\n********** Test5 **********")
    msg = "world"
    k = len(msg)
    n = 10
    e = 3
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test6():
    print("\n********** Test6 **********")
    msg = "testing"
    k = len(msg)
    n = 15
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test7():
    print("\n********** Test7 **********")
    msg = "testing"
    k = len(msg)
    n = 20
    e = 6
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test8():
    print("\n********** Test8 **********")
    msg = "abc123"
    k = len(msg)
    n = 8
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test9():
    print("\n********** Test9 **********")
    msg = "python"
    k = len(msg)
    n = 30
    e = 5
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test10():
    print("\n********** Test10 **********")
    msg = "PROJECT"
    k = len(msg)
    n = 30
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test11():
    print("\n********** Test11 **********")
    msg = "example"
    k = len(msg)
    n = 9
    e = 3
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test12():
    print("\n********** Test12 **********")
    msg = "decode"
    k = len(msg)
    n = 7
    e = 1
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test13():
    print("\n********** Test13 **********")
    msg = "cipher"
    k = len(msg)
    n = 6
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test14():
    print("\n********** Test14 **********")
    msg = "encryption"
    k = len(msg)
    n = 11
    e = 4
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test15():
    print("\n********** Test15 **********")
    msg = "security"
    k = len(msg)
    n = 8
    e = 3
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def your_test():
    i = 1
    while 1:
        print(f"********** Test {i} **********\n")
        msg = str(input("Insert the message you wish to test, or exit to stop: "))
        if msg == "exit":
            break
        k = len(msg)
        n = int(input("Insert the \"number of evaluation points\" you want: "))
        e = int(input("Insert the \"number errors\" you want: "))
        eval_pts = [alpha for alpha in range(n)]
        encoder_decoder.run(msg, n, k, e, eval_pts)
        i+=1


if __name__ == "__main__":
    test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    # test12()
    # test13()
    # test14()
    # test15()