from collections import OrderedDict

if __name__ == '__main__':
    n = int(raw_input())
    item_list = OrderedDict()
    for i in range(0, n):
        x = raw_input().split()
        net_price = 0
        item_name = ""
        if len(x) > 2:
            item_name = x[0] + " " + x[1]
            net_price = int(x[2])
            if item_name in item_list:
                item_list[item_name] += net_price
            else:
                item_list[item_name] = net_price
        else:
            item_name = x[0]
            net_price = int(x[1])
            if item_name in item_list:
                item_list[item_name] += net_price
            else:
                item_list[item_name] = net_price

    for k, v in item_list.items():
        print k, v
