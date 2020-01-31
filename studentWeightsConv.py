noOfStu = input("Please enter the number of students: ")
noOfStu = int(noOfStu)
weightsLBs = []
weightsKGs = []
for n in range(noOfStu):
        w_lb = float(input("Enter the weight of student in lbs>>"))
        weightsLBs.append(w_lb)

weightsKGs = [weightsLBs[x]*0.453592 for x in range(noOfStu)]

print(weightsKGs)