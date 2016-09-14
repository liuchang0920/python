from random import randint
import sys

# use a random number to indecate who goes first
def human_first():
    number = randint(0, 1)
    if number == 0:
        return True
    else:
        return False

# get the input string from user
def get_human_input():
    prompt = "Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X"
    print prompt
    sys.stdout.flush()

    input = raw_input()
    return input


# computer use a relatively wise strategy to draw object, computer uses nim sum when the nim sum result 
# is smaller than one of the heap's objects number, otherwise just random pick one from the first heap
def optimal_computer_move(random_heap):
    xor = 0
    for item in random_heap:
        xor ^= item

    canXOr = False
    for index, item in enumerate(random_heap):
        if item >= xor and xor != 0:
            random_heap[index] -= xor
            print "Player computer took %s objects from heap %s " % (str(xor), str(index+1))
            # print str(index+1)
            sys.stdout.flush()
            canXOr = True
            break

    if not canXOr or xor == 0:
        naive_computer_move(random_heap)
    else:
        display_array(random_heap)


# handle human input and validate if the input is correct; then execute human move
def move(random_heap):
    str = get_human_input()
    split = str.split()
    # print 'split: ', split
    if str is None or len(str) == 0 or len(split) != 2:
        print "Player human that is an invalid move, try again"
        sys.stdout.flush()
        move(random_heap)
    else:
        # try:
        #     heap_num = int(split[1])
        #     element_num = int(split[0])
        # except:
        #     print "Player human that is an invalid move, try again"
        #     sys.stdout.flush()
        #     move(random_heap)
        if not split[1].isdigit() or not split[0].isdigit():
            print "Player human that is an invalid move, try again"
            sys.stdout.flush()
            move(random_heap)
        else:
            heap_num = int(split[1])
            element_num = int(split[0])
            if heap_num > len(random_heap) or element_num > random_heap[heap_num-1] or heap_num <=0 or element_num <= 0:
                print "Player human that is an invalid move, try again"
                sys.stdout.flush()
                move(random_heap)
            else:
                random_heap[heap_num-1] -= element_num
                display_array(random_heap)


# simple way for the computer to draw object from the heaps
def naive_computer_move(random_heap):
    for index, item in enumerate(random_heap):
        if item != 0 :
            random_heap[index] -= 1
            # print "Player computer took 1 objects from heap ", str(index+1)
            print "Player computer took %s objects from heap %s " % (str(1),str(index+1))
            sys.stdout.flush()
            display_array(random_heap)
            break


# decide whether the current player wins or not 
def check_win(array):
    for item in array:
        if item != 0:
            return False

    return True

# use randint function to build random heaps
def build_random_heap():
    num_of_heaps = [3, 5, 7]
    num_of_elements = [9, 11, 13]
    random_heap_number = num_of_heaps[randint(0, len(num_of_heaps)-1)]
    radom_heap = []
    for i in range(random_heap_number):
        radom_heap.append(num_of_elements[randint(0, len(num_of_elements)-1)])
    return radom_heap




# display the information in the heaps
def display_array(array):
    for item in array:
        print item, 
    print ""
    sys.stdout.flush()

# the entrance of the program 
def main():
    random_heap = build_random_heap()
    print "Created", len(random_heap),  "heaps of sizes",
    for item in random_heap:
        print item,
    print ""

    sys.stdout.flush()

    is_human_first = human_first()
    if is_human_first:
        print "Player human goes first"
        sys.stdout.flush()
        while True:
            move(random_heap)
            if check_win(random_heap):
                print "Player human has won"
                sys.stdout.flush()
                return
            else:
                optimal_computer_move(random_heap)
                if check_win(random_heap):
                    print "Player computer has won"
                    sys.stdout.flush()
                    return

    else:
        print "Player computer goes first"
        sys.stdout.flush()
        
        while True:
            optimal_computer_move(random_heap)
            
            if check_win(random_heap):
                print "Player computer has won"
                sys.stdout.flush()
                return
            else:
                move(random_heap)
                if check_win(random_heap):
                    print "Player human has won"
                    sys.stdout.flush()
                    return


if __name__ == '__main__':
    main()