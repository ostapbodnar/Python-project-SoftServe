number = int(input("Enter number N: "))


def get_deviders(numb):
    # complexity O(sqrt(numb))

    # using set to avoid duplicates of deviders
    deviders = {1}
    # starting from 2 because 1 is always devider of natural number
    for i in range(2, int(numb**0.5) + 2):
        if numb % i == 0:
            deviders.add(numb/i)
            deviders.add(i)
    return deviders


# general complixity of print all "ideal" numbers till number N
# O(n*sqrt(n)) <==> O(n^(3/2))
for i in range(2, number):
    if sum(get_deviders(i)) == i:
        print(i)

# alternative form (cons: print all values after forloop ends)
# print(*(i for i in range(2, number)  if sum(get_deviders(i)) == i ))
