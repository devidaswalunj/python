print("python Quiz")

q1=input(""" Q 1)  type() is use for

                    A)address
                    B)datatype
                    C)convert datatype
                    D)none
Enter your answer: """)

q2=input(""" Q 2)  which datatype is mutable in python


                    A)string
                    B)int
                    C)tuple
                    D)list
Enter your answer: """)

q3=input(""" Q 3)  what is the output of the following code 
                                print(type(10.5))

                    A)<class 'int'>
                    B)<class 'float'>
                    C)<class 'bool'>
                    D)<class 'none'>
Enter your answer: """)

q4=input(""" Q 4)  list is  

                    A)mutable
                    B)immutable
                    C)function
                    D)none
Enter your answer: """)

q5=input(""" Q 5)  dictionary is  

                    A)collection of key value pair
                    B)collection of keys
                    C)collection of values
                    D)collection of elements
Enter your answer: """)
q6=input(""" Q 6) Which keyword is used to define a function in Python?
                        A) function
                        B) def
                        C) fun
                        D) define
Enter your answer: """)

q7=input(""" Q 7) recursion means
                        A) function calling itself
                        B) function calling another function
                        C) function calling a variable
                        D) none
Enter your answer: """)

q8=input(""" Q 8) What is the output of the following code?
                                print(type([1, 2, 3]))

                    A) <class 'list'>
                    B) <class 'tuple'>
                    C) <class 'set'>
                    D) <class 'dict'>
Enter your answer: """)

q9=input(""" 
Q 9) What is the output of the following code?
                                print(type((1, 2, 3)))
                                A) <class 'list'>
                                B) <class 'tuple'>
                                C) <class 'set'>
                                D) <class 'dict'>
Enter your answer: """)

q10=input(""" Q 10) What is the output of the following code?
                                print(type({1, 2, 3})) 
                    A) <class 'list'>
                    B) <class 'tuple'>     
                    C) <class 'set'>
                    D) <class 'dict'>
Enter your answer: """)
l1=[]
l1.extend([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10])


l2=["B","D","B","A","A","B","A","A","B","C"]
score=0
for i in range(len(l1)):
    if l1[i].upper()==l2[i]:
        print("Q",i+1,"is correct")
        score+=1
    else:
        print("Q",i+1,"is wrong")
print("Your score is:",score,"/",len(l1))

print("Thank you for playing the quiz!")
# print("correct answers are:",)
# for ans in range(1,len(l2)):
#     for i in l2:
#         print("Q",ans,":",i,end=", ")















