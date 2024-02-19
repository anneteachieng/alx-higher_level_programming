<<<<<<< HEAD
mport random
=======
#!/usr/bin/python3
import random
>>>>>>> 24af1aaf9c06ea526722a806994a815e85b3f7f3
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
thestring = "Last digit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(f"{thestring} and is greater than 5")
elif lastdigit == 0:
    print(f"{thestring} and is 0")
elif lastdigit < 6:
<<<<<<< HEAD
    print(f"{thestring} and is less than 6 and not 0")
=======
    print(f"{thestring} and is less than 6 and not 0")
>>>>>>> 24af1aaf9c06ea526722a806994a815e85b3f7f3
