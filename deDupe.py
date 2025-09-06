with open('/Users/sbachta/Workspace/py-random/resources/parse1.txt') as file:
    appFile1 = set(file.read().splitlines())
    with open('/Users/sbachta/Workspace/py-random/resources/parse2.txt') as file:
        appFile2 = set(file.read().splitlines())

print(f'Count of first file: {len(appFile1)}')
print(f'Count of second file: {len(appFile2)}')

deDupe = appFile1.union(appFile2)  # uncomment to remove duplicates between files
# deDupe = appFile1.difference(appFile2)  # uncomment to remove inputs present in the first file from the second file
# deDupe = appFile2.difference(appFile1)  # uncomment to remove inputs present in the second file from the first file
# deDupe = appFile1.intersection(appFile2)  # uncomment to keep only inputs present in both files

with open('/Users/sbachta/Workspace/py-random/resources/deDupe.txt', 'w') as file:
    for line in deDupe:
        file.write(line + '\n')

print(f'Count of deDupe file: {len(deDupe)}')