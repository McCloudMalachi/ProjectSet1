#Programmer: Malachi McCloud
#Food and Gas Price Calculator

#Take user input to store invariables for the number of people and days
people=int(input("Enter the number of people:"))#People
days=int(input("Enter the number of days:"))#Days

#Establish our loop itteration Variable
i=0

#Create a new empty arry for both costFood and costGas
costFood = [None] * days
costGas = [None] * days

totCostFood= 0
totCostGas= 0
#Establish a loop for taking input for every day

while i<days:#Creates a loop which checks to ensure our loop iteration is lower than the amount of days
    print("Enter the amounts of gas and food for Day:",(i+1))#Creates a prompt for the day the user is entering the data for
    costFood[i]=float(input("Enter the cost of food for the day:"))
    costGas[i]=float(input("Enter the cost of gas for the day:"))

    #Create calculations for our food and gas variables to have total amounts
    totCostFood = totCostFood + costFood[i]
    totCostGas = totCostGas + costGas[i]
    i+=1#Run our loop through the amount of iterations or days

#Print our cost
print("Total cost of food: ", totCostFood ,"$")
print("Total cost of gas: ", totCostGas ,"$")

#Print cost of our trip
print("Total cost of trip: ", totCostFood+totCostGas ,"$")
#Create a print statement with our total per person by using the people variable from above and dividing the cost by the amount of them
print("Each person's split of the total cost for the trip is", (totCostFood+totCostGas)/people)
