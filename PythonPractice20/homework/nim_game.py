from random import randint
import sys

def human_first():
    number = randint(0, 1)
    if number == 0:
        return True
    else:
        return False


def get_human_input():
    prompt =  "Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X"
    input = raw_input(prompt)
    print "human enters ", input
    sys.stdout.flush()
    return input



def optimal_computer_move(random_heap):
    xor = 0
    for item in random_heap:
        xor ^= item

    canXOr = False
    for index, item in enumerate(random_heap):
        if item >= xor and xor != 0:
            random_heap[index] -= xor
            print "Player computer took ",xor," objects from heap " + str(index+1)
            sys.stdout.flush()
            canXOr = True
            break

    if not canXOr or xor == 0:
        naive_computer_move(random_heap)
    else:
        display_array(random_heap)
        if check_win(random_heap):
            print "Player computer has won"
            return

        move(random_heap)


def move(random_heap):
    str = get_human_input()
    split = str.split()
    # print 'split: ', split
    if str is None or len(str) == 0 or len(split) != 2:
        print "Player human that is an invalid move, try again"
        sys.stdout.flush()
        move(random_heap)
    else:
        heap_num = int(split[1])
        element_num = int(split[0])
        if heap_num > len(random_heap) or element_num > random_heap[heap_num-1]:
            print "Player human that is an invalid move, try again"
            sys.stdout.flush()
            move(random_heap)
        else:
            random_heap[heap_num-1] -= element_num
            display_array(random_heap)
            if check_win(random_heap):
                print "Player human has won"
                sys.stdout.flush()
                return
            else: optimal_computer_move(random_heap)


def naive_computer_move(random_heap):
    for index, item in enumerate(random_heap):
        if item != 0 :
            random_heap[index] -= 1
            print "Player computer took 1 objects from heap ", str(index+1)
            sys.stdout.flush()
            display_array(random_heap)
            break;

    if check_win(random_heap):
        print "Player computer has won..."
        sys.stdout.flush()
        return

    move(random_heap)


def check_win(array):
    for item in array:
        if item != 0:
            return False

    return True


def build_random_heap():
    num_of_heaps = [3, 5, 7]
    num_of_elements = [9, 11, 13]
    random_heap_number = num_of_heaps[randint(0, len(num_of_heaps)-1)]
    radom_heap = []
    for i in range(random_heap_number):
        radom_heap.append(num_of_elements[randint(0, len(num_of_elements)-1)])
    # print "random heap:",radom_heap
    return radom_heap


# # get random array both for # of heap and # of elements
# def random_num(array):
#     return array[randint(0, len(array)-1)]


def display_array(array):
    for item in array:
        print item, " ",
    print ""
    sys.stdout.flush()


def main():
    random_heap = build_random_heap()
    print "Created", len(random_heap),  "heaps of sizes",
    for item in random_heap:
        print item, " ",
    print ""

    sys.stdout.flush()

    is_human_first = human_first()
    if is_human_first:
        print "Player human goes first"
        sys.stdout.flush()
        move(random_heap)
    else:
        print "Player computer goes first"
        sys.stdout.flush()

        optimal_computer_move(random_heap)


if __name__ == '__main__':
    main()