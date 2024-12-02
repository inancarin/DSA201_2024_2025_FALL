from tv_series import TVSeries

def printMenu():
    menu = """
1. Create a new TV Series, and add to main list
2. Add rating for a TV Series
3. Print average rating for a TV Series
4. Print main list
    """
    print(menu)

def findIndex(mainList, name):
    for idx in range(len(mainList)):
        series = mainList[idx]
        if series.getName() == name:
            return idx
    else:
        return -1

# main
mainList = []

while True:
    printMenu()
    option = input("Select an option: ").lower()
    while option not in ["1", "2", "3", "4", "exit"]:
        option = input("You have selected an invalid option. Enter again: ").lower()
    if option == "exit":
        break
    if option == "1":
        name = input("Enter a TV Series name: ")
        if findIndex(mainList, name) != -1:
            print("This TV Series name had been entered before!")
        else:
            series = TVSeries(name)
            mainList.append(series)
    elif option == "2":
        name = input("Enter a TV Series name: ")
        idx = findIndex(mainList, name)
        if idx == -1:
            print("There is no such TV series!")
        else:
            rating = int(input("Add a rating between 1-5 (you may assume user will enter a valid rating): "))
            mainList[idx].addRating(rating)
    elif option == "3":
        name = input("Enter a TV Series name: ")
        idx = findIndex(mainList, name)
        if idx == -1:
            print("There is no such TV series!")
        else:
            print("The average rating for", name, "is", mainList[idx].averageRating())
    elif option == "4":
        print(mainList)