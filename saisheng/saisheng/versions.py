def compareVersions(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    for v in range(max(len(version1), len(version2))):
        if (v >= len(version1) and int(version2[v]) != 0):
            return -1
        elif v >= len(version2) and int(version1[v]) != 0:
            return 1
        if (v < len(version1) and v < len(version2)):
            if (int(version1[v]) > int(version2[v])):
                return 1
            elif (int(version2[v]) > int(version1[v])):
                return -1
    return 0


print(compareVersions('1.2.0', '1.2'))
