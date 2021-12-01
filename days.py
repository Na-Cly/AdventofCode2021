from aoc import aoc
import aocinput
a = aoc()


def day1():
    output = a.day1_1(a.day1_2(aocinput.day1))
    increase = 0
    decrease = 0
    same = 0
    for each in output:
        if each[1] == 1:
            increase += 1
        elif each[1] == -1:
            decrease += 1
        elif each[1] == 0:
            same += 1

    print('Increase: ', increase)
    print('Decrase: ', decrease)
    print('Same: ', same)



if __name__ == '__main__':
    day1()