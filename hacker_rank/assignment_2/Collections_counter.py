from collections import Counter

if __name__ == '__main__':
    num_of_shoes = int(raw_input())
    shoe_sizes = map(int, raw_input().split())
    num_of_customers = int(raw_input())
    shoe_sizes = Counter(shoe_sizes)
    money_earned = 0
    for i in range(0, num_of_customers):
        purchase = map(int, raw_input().split())
        if shoe_sizes[purchase[0]] != 0:
            shoe_sizes[purchase[0]] += -1
            money_earned += purchase[1]
    print money_earned