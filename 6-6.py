def scope_test():
    def do_local():
        s1 = "local    "

    def do_nonlocal():
        nonlocal s2
        s2 = "nonlocal"

    def do_global():
        global s3

        s3 = "global    "

    s0 = s1 = s2 = s3 = "test    "
    do_local()
    print("After local    :", s0, s1, s2, s3)
    do_nonlocal()
    print("After nonlocal :", s0, s1, s2, s3)
    do_global()
    print("After global   :", s0, s1, s2, s3)

  
s0 = s1 = s2 = s3 = "initial "
print("In th global   :", s0, s1, s2, s3)
scope_test()
print("After func call:", s0, s1, s2, s3)