def order_bubble_sort(list_ordernate: list) -> list:

    default_while = True

    while default_while:
        default_while = False

        for i in range(len(list_ordernate)-1):
            if list_ordernate[i] > list_ordernate[i+1]:
                list_ordernate[i], list_ordernate[i+1] = list_ordernate[i+1], list_ordernate[i]
                default_while = True

    return list_ordernate


if __name__ == "__main__":
    print(order_bubble_sort([5,3,2,4,7,1,0,6]))