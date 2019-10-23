from itertools import permutations

areas = ["A1", "A2", "A3", "A4", "A5", "A6", "A7"]#, "A8"]
colors = ["green", "yellow", "blue", "orange"]
# colors = ["yellow", "blue", "orange","green"]
# colors = ('orange', 'yellow', 'blue', 'green')

perms = permutations(colors, len(colors))
permsAreas = permutations(areas, len(areas))

neighborPoints = {
    "A1": ["A2", "A4", "A6"],
    "A2": ["A1", "A3", "A4", "A6", "A7"],#, "A8"],
    "A3": ["A2", "A4", "A5", "A7"],#, "A8"],
    "A4": ["A1", "A2", "A3", "A5", "A6", "A7"],
    "A5": ["A3", "A4", "A6"],
    "A6": ["A1", "A2", "A4", "A5"],
    "A7": ["A2", "A3", "A4"],
    #"A8": ["A2", "A3"]
}

totalCombinations = []
finalResult = {}


# for i in range(0, len(areas)):
#     for j in range(0, len(colors)):
#       finalResult[areas[i]] = colors[j]
def getResult(assignedColors, areasList, colorsList):
    global neighborPoints
    for area in areasList:
        # if assignedColors.has_key(area):
        #     continue
        for color in colorsList:
            # print "Checking => area:", area, "color:", color, finalResult, finalResult.has_key(area)
            if assignedColors.has_key(area):
                break
                # if assignedColors[area] != color:
                #     for neighborPoint in neighborPoints[area]:
                #         if assignedColors.has_key(neighborPoint):
                #             continue
                #         else:
                #             assignedColors[neighborPoint] = color
                #             break
            else:
                found = False
                for neighborPoint in neighborPoints[area]:
                    if assignedColors.has_key(neighborPoint):
                        if assignedColors[neighborPoint] == color:
                            # print "area:", area, "neighbour:", neighborPoint, "color:", color
                            found = True
                            break
                if found:
                    continue
                # print "area:", area, "color:", color
                assignedColors[area] = color
                break
    return assignedColors


for permsArea in permsAreas:
    areasList = permsArea
    for per in perms:
        colorsList = per
        print colorsList, areasList
        for i in range(0, len(areasList)):
            for j in range(0, len(colorsList)):
                finalResult[areasList[i]] = colorsList[j]

                finalResult = getResult(finalResult, areasList, colorsList)

                print finalResult
                if len(finalResult) != len(areasList):
                    print "Discarded result:", finalResult
                else:
                    if not finalResult in totalCombinations:
                        totalCombinations.append(finalResult)
                finalResult = {}

print "------------------------------------------------------------------------------------------------"
for combinations in totalCombinations:
    print combinations

print len(totalCombinations)

# print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
# totalCombinations = []
# finalResult = {}
# colors = ['orange', 'yellow', 'green', 'blue']
# areas = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
# for i in range(0, len(areas)):
#     for j in range(0, len(colors)):
#         finalResult[areas[i]] = colors[j]
#         print "#1", finalResult
#
#         finalResult = getResult(finalResult, areas, colors)
#
#         print finalResult
#         if len(finalResult) != len(areas):
#             print "Discarded result:", finalResult
#         else:
#             if not finalResult in totalCombinations:
#                 totalCombinations.append(finalResult)
#         finalResult = {}
#
# for combinations in totalCombinations:
#     print combinations
#
# print len(totalCombinations)
#
