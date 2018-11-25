"""
Random problem selection

"""
import numpy as np
import copy


def main():
    # building our list of problems and subchapers
    data = [[11, 3, 9, 18, 4, 4, 8],
            [12, 7],
            [8, 2, 3, 2, 3, 11],
            [17, 1, 2, 7],
            [34],
            [16, 17, 4, 4, 4, 6],
            [6, 5, 1],
            [10],
            [9, 4, 6],
            [14, 2, 1, 2],
            [4, 9],
            [20],
            [30, 2, 3, 1],
            [12, 14],
            [8, 7, 5, 3, 3, 4],
            [5, 3, 3, 2, 2],
            [8, 7],
            [17, 10],
            [5, 7, 3, 6],
            [13, 5, 10, 2],
            [5]]
    # Data sanity checks
    ppercent = [0.3, 0.4]
    pperchap = [0] * len(data)
    print("Number of Chapers is " + str(len(data)))
    for chapter in range(len(data)):
        pnumb = sum(data[chapter])
        print("Number of problems in chapter " +
              str(chapter + 1) + " is " + str(pnumb))
        pperchap[chapter] = pnumb
    unselected = probs(ppercent, pperchap, data)
    print(str(listcon(data, unselected)).replace("'", ""))

    return None

# produing the list of the number of problems not selected in each subsection


def probs(ppercent, pperchap, data):
    m = (ppercent[1] - ppercent[0]) / (len(data) - 1)
    b = ppercent[0]
    unselected = copy.deepcopy(data)
    for x in range(len(pperchap)):
        pperchap[x] = int(np.ceil(pperchap[x] * ((m * x) + b)))
    for chapter in range(len(data)):
        index = len(unselected[chapter]) - 1
        for x in range(pperchap[chapter]):
            flag = True
            if index < 0:
                index = len(unselected[chapter]) - 1
            while flag:
                if unselected[chapter][index] > 0:
                    unselected[chapter][index] -= 1
                    index -= 1
                    flag = False
                else:
                    index -= 1
                    if index < 0:
                        index = len(unselected[chapter]) - 1
    return unselected


def listcon(data, unselected):
    final_list = [0]
    for chapter in range(len(data)):
        # Total number of problems before this subsection
        totalupnow = 0
        templist = [0]
        for subsection in range(len(data[chapter])):
            if unselected[chapter][subsection] == 0:
                for numb in range(data[chapter][subsection]):
                    templist.append(totalupnow + 1 + numb)
            else:
                toselect = data[chapter][subsection] - \
                    unselected[chapter][subsection]
                while toselect != 0:
                    X = np.random.beta(4.5, 2.5)
                    numb = np.floor(X * data[chapter][subsection])
                    numbtoadd = int(totalupnow + 1 + int(numb))
                    if numbtoadd not in templist:
                        templist.append(numbtoadd)
                        toselect -= 1
            totalupnow += data[chapter][subsection]
        templist.sort()
        for pnumb in templist:
            if pnumb != 0:
                final_list.append(str(chapter + 1) + '.' + str(pnumb))

    final_list.remove(0)
    return final_list


if __name__ == '__main__':
    main()
