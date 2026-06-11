#Homework Project 6

#Part 1: Comma Separated File
file="/Users/filibertomedina/Desktop/CandyList.txt"

#Part 2: Read File
class Candy:
    def __init__(self, name, calories, fat):
        self.name= name
        self.calories= calories
        self.fat= fat

candylist=[]
def main():
    candylist.clear()
    with open(file) as f:
        next(f)
        for line in f:
            words = line.split(',')
            name= words[0]
            calories= words[1]
            fat= words[2]
            candylist.append(Candy(name,calories,fat))
def print_it():
    for candy in candylist:
        print(f"Candy Name: {candy.name}, Calories: {candy.calories}, Fat: {candy.fat}")
main()
print_it()
print('='*50)
#Part 3: Append Line
def update_list():
    with open(file, "a") as f:
        f.write("Skinny-licious Bar, 80, 10\n")
        f.write("Air Candy, 5, 0")
#update_list()
main()
print_it()