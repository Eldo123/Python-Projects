with open("questions.txt","r") as f1:
    questions=f1.readlines()
    n,m=0,0
    for q in questions:
        m+=1
        print(q[:q.index("=")+1])
        ans=q[q.index("=")+1:q.index("\n")]
        #print(ans)
        with open("answers.txt","r+") as f2:
            f2.read()
            ansin=input()
            #print(ansin)
            f2.write(ansin+"\n")
            if(ansin==ans):
                n+=1
    print("Your score is {}/{}".format(n,m))
