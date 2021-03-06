import random
from class_item import Item
from time import time


def greedy_knapsack(all_items ,number_of_items, capacity):
    # all_items = [Item(random.randint(1, end_range_of_radnomization),
    #                   random.randint(1, end_range_of_radnomization)) for _ in range(number_of_items)]
    all_items.sort(key=lambda x: x.profit, reverse= True)
    items_into_knapsack = []
    remaining_capacity = capacity
    i = 0
    while remaining_capacity > 0:
        if all_items[i].weight <= remaining_capacity:
            items_into_knapsack.append(all_items[i])
            remaining_capacity -= all_items[i].weight
        i += 1
        if i == number_of_items - 1:
            break
    s = 0
    for item in items_into_knapsack:
        s+= item.value
    return (s, items_into_knapsack)

def greedy_const(all_items,number_of_items, capacity):
    items_into_knapsack = []
    remaining_capacity = capacity
    i = 0
    while remaining_capacity > 0:
        if all_items[i].weight <= remaining_capacity:
            items_into_knapsack.append((all_items[i].value, all_items[i].weight))
            remaining_capacity -= all_items[i].weight
        i += 1
        if i == number_of_items - 1:
            break
    s = 0
    for item in items_into_knapsack:
        s+= item.value
    return (s, items_into_knapsack)


def greedy_measure_time_for_const_cap(n, c, end_range, tries):
    s = 0
    r = 0
    for i in range(tries):
        print(f"{n} items {c} capacity {i+1}/{tries} attempt")
        a = [Item(random.randint(1, end_range), random.randint(
        1, end_range)) for _ in range(n)]
        start = time()
        r += greedy_knapsack(a, n, c, r)[0]
        end = time()
        s += end-start
    return (r, s/tries)


def greedy_measure_time_for_const_it(n, c, tries, end_range):
    s = 0
    r = 0
    for i in range(tries):
        print(f"{n} items {c} capacity {i+1}/{tries} attempt")
        all = [Item(random.randint(1, end_range), random.randint(
        1, end_range)) for _ in range(n)]
        start = time()
        r += greedy_const(all, n, c)[0]
        end = time()
        s += end-start
    return (r, s/tries)


if __name__ == "__main__":
    test = int(input("Which would be NOT constant\n1- number of items\n2-Capacity\n"))
    while test != 1 and test != 2:
        test = int(
            input("TYPO\nWhich would be NOT constant\n1- number of items\n2-Capacity\n"))

    if test == 1:
        number_of_items = int(input("START number of items: "))
        capacity = int(input("CONST capacity: "))
    else:
        number_of_items = int(input("CONST Number of items: "))
        capacity = int(input("START capacity: "))


    end_range_of_radnomization = int(
        input("End range of wieghts and values randomization: "))
    steps = int(input("Steps: "))
    step_size = int(input("Step size: "))
    tries = int(input("Tries: "))

    if test == 1:
        end_elements = number_of_items + steps*step_size
        x_axis = []
        for i in range(steps):
            x_axis.append(number_of_items*(i+1))
    else:
        end_elements = capacity + steps*step_size
        x_axis = []
        for i in range(steps):
            x_axis.append(capacity*(i+1))

    if test == 2:
        all_items = [Item(random.randint(1, end_range_of_radnomization),
                        random.randint(1, end_range_of_radnomization))]
        all_items.sort(key=lambda x: x.profit, reverse= True)

    if test == 1:
        print(greedy_knapsack(number_of_items, capacity, end_range_of_radnomization))
    else:
        print(greedy_const(all_items, number_of_items, capacity))

