import random


def run_loop(loops):
    positive = 0
    total = 0
    for i in range(100):
        box1 = [1, 100]
        box2 = [100, 100]
        boxes = [box1, box2]
        box_chosen = boxes[random.randint(0,1)]
        first_bill = box_chosen[random.randint(0,1)]
        box_chosen.remove(first_bill)
        second_bill = box_chosen[0]
        if first_bill == 100 and second_bill == 100:
            positive += 1
            total += 1
        elif first_bill == 100 and second_bill == 1:
            total += 1
    return positive / total


ratio = run_loop(10000000000)
percentage = ratio * 100
print(f"Probability of getting 100 again: {round(percentage,1)}%")
