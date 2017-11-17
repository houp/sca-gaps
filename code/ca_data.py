
elementary_neighborhoods = ['000', '001', '010', '011', '100', '101', '110', '111']

grouped_configurations = {1: [[0, 0, 0, 0, 0, 0, 0, 0]],
                          # one 1
                          2: [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0, 0, 0, 0]],
                          # two 1 dis 0
                          3: [[1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 1, 1]],
                          # two 1 dis 1
                          4: [[1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
                              [0, 0, 0, 1, 0, 1, 0, 0],
                              [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0],
                              [0, 1, 0, 0, 0, 0, 0, 1]],
                          # two 1 dis 2
                          5: [[1, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0],
                              [0, 0, 1, 0, 0, 0, 0, 1]],
                          # two 1 dis 3
                          6: [[1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0],
                              [0, 0, 0, 1, 0, 0, 0, 1]],
                          # three one dis 0,0,5
                          7: [[1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0],
                              [0, 0, 0, 1, 1, 1, 0, 0],
                              [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 1],
                              [1, 1, 0, 0, 0, 0, 0, 1]],
                          # three one dis 0,1,4
                          8: [[1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0],
                              [0, 0, 0, 1, 1, 0, 1, 0],
                              [0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1],
                              [1, 0, 1, 0, 0, 0, 0, 1]],
                          # three one dis 0,2,3
                          9: [[1, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0],
                              [0, 0, 0, 1, 1, 0, 0, 1],
                              [1, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1],
                              [1, 0, 0, 1, 0, 0, 0, 1]],

                          31: [[1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0, 1],
                               [1, 0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0],
                               [0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1]],

                          32: [[0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 0],
                               [0, 1, 1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 0, 0, 1],
                               [1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0]],
                          # tree one dis 1,1,3
                          10: [[1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0],
                               [0, 0, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0],
                               [0, 1, 0, 1, 0, 0, 0, 1]],
                          # three one dis 1,2,2
                          11: [[1, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1],
                               [1, 0, 0, 1, 0, 1, 0, 0],
                               [0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0],
                               [0, 1, 0, 0, 1, 0, 0, 1]],
                          # four one dis 0,0,0,4
                          12: [[1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0],
                               [0, 0, 0, 1, 1, 1, 1, 0],
                               [0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1],
                               [1, 1, 1, 0, 0, 0, 0, 1]],
                          # four one dis 0,0,1,3
                          13: [[1, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0],
                               [0, 0, 0, 1, 1, 1, 0, 1],
                               [1, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 1],
                               [1, 1, 0, 1, 0, 0, 0, 1]],

                          # four one dis 0,1,0,3
                          14: [[1, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0],
                               [0, 0, 0, 1, 1, 0, 1, 1],
                               [1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1],
                               [1, 0, 1, 1, 0, 0, 0, 1]],
                          # four one dis 0,0,2,2
                          15: [[1, 1, 1, 0, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1],
                               [1, 0, 0, 1, 1, 1, 0, 0],
                               [0, 1, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1, 1],
                               [1, 1, 0, 0, 1, 0, 0, 1]],
                          # four one dis 0,2,0,2
                          16: [[1, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1],
                               [1, 0, 0, 1, 1, 0, 0, 1]],
                          # four one dis 1,1,1,1
                          17: [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]],

                          18: [[1, 1, 1, 1, 1, 1, 1, 1]],
                          # one 0
                          19: [[1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1],
                               [1, 1, 1, 1, 0, 1, 1, 1],
                               [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1],
                               [0, 1, 1, 1, 1, 1, 1, 1]],
                          # two 0 dis 1
                          20: [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1, 1],
                               [1, 1, 0, 0, 1, 1, 1, 1],
                               [1, 1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1],
                               [1, 1, 1, 1, 1, 1, 0, 0]],
                          # two 0 dis 0
                          21: [[0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1, 1, 1],
                               [1, 1, 1, 0, 1, 0, 1, 1],
                               [1, 1, 1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1],
                               [1, 0, 1, 1, 1, 1, 1, 0]],
                          # two 0 dis 2
                          22: [[0, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1, 1],
                               [1, 1, 1, 0, 1, 1, 0, 1],
                               [1, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1],
                               [1, 1, 0, 1, 1, 1, 1, 0]],
                          # two 0 dis 3
                          23: [[0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1],
                               [1, 1, 1, 0, 1, 1, 1, 0]],
                          # three one dis 1,1,5
                          24: [[0, 0, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1],
                               [1, 1, 1, 0, 0, 0, 1, 1],
                               [1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0],
                               [0, 0, 1, 1, 1, 1, 1, 0]],
                          # three one dis 1,0,4
                          25: [[0, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 1],
                               [1, 1, 1, 0, 0, 1, 0, 1],
                               [1, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 0],
                               [0, 1, 0, 1, 1, 1, 1, 0]],
                          # three one dis 1,2,3
                          26: [[0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1],
                               [1, 1, 1, 0, 0, 1, 1, 0],
                               [0, 1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0],
                               [0, 1, 1, 0, 1, 1, 1, 0]],
                          # tree one dis 0,0,3
                          27: [[0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1],
                               [1, 1, 1, 0, 1, 0, 1, 0],
                               [0, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1],
                               [1, 0, 1, 0, 1, 1, 1, 0]],
                          # three one dis 0,2,2
                          28: [[0, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 0],
                               [0, 1, 1, 0, 1, 0, 1, 1],
                               [1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1, 0, 1],
                               [1, 0, 1, 1, 0, 1, 1, 0]],
                          29: [[1, 0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0, 0],
                               [0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 1],
                               [1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1]],
                          30: [[0, 1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 0, 1, 1],
                               [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1, 0],
                               [0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0]],
                          33: [[0, 0, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1],
                               [1, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0, 0],
                               [0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 0]],
                          34: [[0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 1, 0, 1, 0],
                               [0, 1, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1],
                               [1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1, 0]],
                          35: [[0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 1],
                               [1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1],
                               [1, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0]],
                          36: [[0, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1],
                               [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1],
                               [1, 1, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0]],
                          }


def findGroupForBlock(block):
    for k in grouped_configurations:
        if block in grouped_configurations[k]:
            return k


wolfram_classification = {
    '1': [0, 8, 32, 40, 64, 96, 128, 136, 160, 168, 192, 224, 234, 235, 238, 239, 248,
          249, 250, 251, 252, 253, 254, 255],
    '2': [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21,
          23, 24, 25, 26, 27, 28, 29, 31, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44,
          46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 61, 62, 63, 65, 66,
          67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
          87, 88, 91, 92, 93, 94, 95, 97, 98, 99, 100, 103, 104, 107, 108, 109, 111, 112,
          113, 114, 115, 116, 117, 118, 119, 121, 123, 125, 127, 130, 131, 132,
          133, 134, 138, 139, 140, 141, 142, 143, 144, 145, 148, 152, 154, 155, 156, 157,
          158, 159, 162, 163, 164, 166, 167, 170, 171, 172, 173, 174, 175, 176, 177,
          178, 179, 180, 181, 184, 185, 186, 187, 188, 189, 190, 191, 194, 196, 197,
          198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
          213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 226, 227, 228, 229,
          230, 231, 232, 233, 236, 237, 240, 241, 242, 243, 244, 245, 246, 247],

    '3': [18, 22, 30, 45, 54, 60, 75, 86, 89, 90, 101, 102, 105, 122, 126, 129,
          135, 146, 149, 150, 151, 153, 161, 165, 182, 183, 195],

    '4': [41, 106, 110, 120, 124, 137, 147, 169, 193, 225]
}


def getWolframClassForRule(rule):
    for c in wolfram_classification:
        if rule in wolfram_classification[c]:
            return c
    return 0


def countDiff(dd):
    result = 0
    for d in dd:
        result = result + len(dd[d])
    return result


def isUnique(dd):
    a = []
    for d in dd:
        for v in dd[d]:
            if v not in a:
                a.append(v)
            else:
                print("Not unique " + str(d) + " " + str(v))
                return False
    print(len(a))
    return True


similarRulesDict = {
    0: [0, 255],
    1: [1, 127],
    2: [2, 16, 191, 247],
    3: [3, 17, 63, 119],
    4: [4, 223],
    5: [5, 95],
    6: [6, 20, 159, 215],
    7: [7, 21, 31, 87],
    8: [8, 64, 239, 253],
    9: [9, 65, 111, 125],
    10: [10, 80, 175, 245],
    11: [11, 47, 81, 117],
    12: [12, 68, 207, 221],
    13: [13, 69, 79, 93],
    14: [14, 84, 143, 213],
    15: [15, 85],
    18: [18, 183],
    19: [19, 55],
    22: [22, 151],
    23: [23],
    24: [24, 66, 189, 231],
    25: [25, 61, 67, 103],
    26: [26, 82, 167, 181],
    27: [27, 39, 53, 83],
    28: [28, 70, 157, 199],
    29: [29, 71],
    30: [30, 86, 135, 149],
    32: [32, 251],
    33: [33, 123],
    34: [34, 48, 187, 243],
    35: [35, 49, 59, 115],
    36: [36, 219],
    37: [37, 91],
    38: [38, 52, 155, 211],
    40: [40, 96, 235, 249],
    41: [41, 97, 107, 121],
    42: [42, 112, 171, 241],
    43: [43, 113],
    44: [44, 100, 203, 217],
    45: [45, 75, 89, 101],
    46: [46, 116, 139, 209],
    50: [50, 179],
    51: [51],
    54: [54, 147],
    56: [56, 98, 185, 227],
    57: [57, 99],
    58: [58, 114, 163, 177],
    60: [60, 102, 153, 195],
    62: [131, 62, 145, 118],
    72: [72, 237],
    73: [73, 109],
    74: [74, 88, 173, 229],
    76: [76, 205],
    77: [77],
    78: [78, 92, 141, 197],
    90: [90, 165],
    94: [94, 133],
    104: [104, 233],
    105: [105],
    106: [106, 120, 169, 225],
    108: [108, 201],
    110: [137, 110, 124, 193],
    128: [128, 254],
    129: [129, 126],
    130: [130, 144, 190, 246],
    132: [132, 222],
    134: [134, 148, 158, 214],
    136: [136, 192, 238, 252],
    138: [138, 174, 208, 244],
    140: [140, 196, 206, 220],
    142: [142, 212],
    146: [146, 182],
    150: [150],
    152: [152, 188, 194, 230],
    154: [154, 166, 180, 210],
    156: [156, 198],
    160: [160, 250],
    161: [161, 122],
    162: [162, 176, 186, 242],
    164: [164, 218],
    168: [168, 224, 234, 248],
    170: [170, 240],
    172: [172, 202, 216, 228],
    178: [178],
    184: [184, 226],
    200: [200, 236],
    204: [204],
    232: [232]
}

def checkIfSimilarRulesDictIsCorrect():
    r = [i for i in range(256)]
    count = 0
    for k in similarRulesDict.keys():
        for rule in similarRulesDict[k]:
            if rule in r:
                r.remove(rule)
                count += 1
            else:
                print("RULE: " + str(rule))
                break
    return len(r) == 0 and count == 256

my_classification = {
    'jednopunktowy' : [0, 8, 32, 36, 40, 64, 72, 96, 104, 128, 136, 160, 164, 168, 192, 224,
           218, 219, 233, 234, 235, 237, 238, 239, 248, 249, 250, 251, 252, 253, 254, 255],
    'jednostajny' : [15, 25, 26, 30, 39, 42, 45, 51, 53, 54, 60, 67,
                      73, 75, 85, 86, 89, 90, 101, 102, 105, 106, 109, 112,
                     120, 135, 137, 147, 149, 150, 153, 154, 165, 166, 169, 170, 180,
                     193, 195, 204, 208, 210, 225, 240],
    '111' : [91, 111, 125, 151, 155, 159, 173, 175, 182, 183, 187, 188, 189, 190, 191, 202, 203, 206, 207, 211,
             215, 216, 217, 220, 222, 223, 230, 231, 236, 245, 246, 247],
    '000' : [2, 4, 6, 9, 10, 12, 16, 18, 20, 22, 24, 37, 38, 44, 52, 66, 68, 74, 80, 88, 100, 130,
             132, 134, 140, 144, 146, 148, 152, 172, 194, 200, 228],
    '111 i 000' : [1, 3, 7, 17, 19, 21, 23, 31, 33, 55, 63, 65, 87, 119, 122, 123, 126, 127, 129, 161, 232],
    '010 i 101' : [13, 28, 29, 50, 56, 57, 69, 70, 71, 77, 78, 79, 92, 93, 94, 98, 99, 133, 141, 156, 157, 178,
                   179, 184, 185, 197, 198, 199, 226, 227],
    '001=011=100=110' : [11, 14, 43, 47, 81, 84, 113, 117, 142, 143, 212, 213],

    'inne' : [5, 27, 34, 35, 41, 46, 48, 49, 58, 59, 61, 62, 76, 82, 83, 95, 97, 103, 107, 108, 110, 114,
              115, 116, 118, 121, 124, 131, 138, 139, 145, 158, 162, 163, 167, 171, 174, 176, 177, 181, 186,
              196, 201, 205, 209, 214, 221, 229, 241, 242, 243, 244]
}



def get_my_class_for_rule(rule):
    for c in my_classification:
        if rule in my_classification[c]:
            return c
    return "NIE MA!"
