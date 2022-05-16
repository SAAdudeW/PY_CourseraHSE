A1, B1, C1, A2, B2, C2 = int(input()), int(input()), int(input()), \
                         int(input()), int(input()), int(input())
if (A1 <= A2 and ((B1 <= B2 and C1 <= C2) or (B1 <= C2 and C1 <= B2))) \
        or \
        (A1 <= B2 and ((B1 <= A2 and C1 <= C2) or (B1 <= C2 and C1 <= A2))) \
        or \
        (A1 <= C2 and ((B1 <= A2 and C1 <= B2) or (B1 <= B2 and C1 <= A2))):
    print('The first box is smaller than the second one')
elif (A2 <= A1 and ((B2 <= B1 and C2 <= C1) or (B2 <= C1 and C2 <= B1))) \
        or \
        (A2 <= B1 and ((B2 <= A1 and C2 <= C1) or (B2 <= C1 and C2 <= A1))) \
        or \
        (A2 <= C1 and ((B2 <= A1 and C2 <= B1) or (B2 <= B1 and C2 <= A1))):
    print('The first box is larger than the second one')
elif (A1 == A2 and ((B1 == B2 and C1 == C2) or (B1 == C2 and C1 == B2))) \
        or \
        (A1 == B2 and ((B1 == A2 and C1 == C2) or (B1 == C2 and C1 == A2))) \
        or \
        (A1 == C2 and ((B1 == A2 and C1 == B2) or (B1 == B2 and C1 == A2))):
    print('Boxes are equal')
else:
    print('Boxes are incomparable')
