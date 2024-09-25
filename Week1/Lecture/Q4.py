top_scorers = [
      ["11 goal(s)", "Sebastien Haller", "Ajax"],
      ["8 goal(s)", "Mohamed Salah", "Liverpool"],
      ["14 goal(s)", "Karim Benzema", "Real Madrid"],
      ["7 goal(s)", "Christopher Nkunku", "Leipzig"],
      ["14 goal(s)", "Robert Lewandowski", "Bayern Munich"]
]

allGoals = []
for sublist in top_scorers:
    curGoal = int(sublist[0].split(" ")[0])
    allGoals.append(curGoal)

maxGoal = max(allGoals)

for sublist in top_scorers:
    curGoal = int(sublist[0].split(" ")[0])
    if curGoal == maxGoal:
        playerName = sublist[1]
        teamName = sublist[2]
        print(playerName, "-", teamName)