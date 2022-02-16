import random

n = input(" How many cycles do you want? ")
infected = 1
population = input(" What do you want the total population to be? ")

for n in range(0, int(n)):
    randinfec = random.randint(0,3)
    newfecs = int(infected) + int(infected)*int(randinfec)
    infected = int(population) - (int(population) - int(newfecs))
    if infected>int(population):
        print("Everyone has been infected.")
        break

    print(infected, "No. of people infected: ", randinfec)
