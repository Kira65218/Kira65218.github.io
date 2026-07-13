import random

scores = []
users = ["Roxanne", "Scarlett", "Jocelyn", "Skylar", "Peter", "Oli", "Callum"]
nums = []

def generates():
    for i in range(len(users)):
        scores.append(random.randint(0, 100))
        for i in range(1000):
            nums.append(random.randint(0, 1000))

def linearSearch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
        return -1



def swap(list, i1, i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp

def bubbleSort(scoreList, userlist):
    for i in range(1, len(scoreList)):
        r = i
        while r > 0:
            if scoreList[r] > scoreList[r-1]:
                swap(scores, r, r-1)
                swap(users, r, r-1)
            r -= 1

def main():
    generates()
    bubbleSort(scores, users)
    for i in range(len(scores)):
        print("{} \t {}'s score: \t{}".format(i+1, users[i], scores[i]))
    print(nums)
    print(linearSearch(nums, 500))   

if __name__ == "__main__":
    main()

