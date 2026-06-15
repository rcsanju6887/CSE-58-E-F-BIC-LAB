def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)

    for i in range(len(genome) -k +1):
        if genome[i:i+k] == pattern :
            positions.append(i)

    return positions

pattern = input()
genome = input()  

result = pattern_matching(pattern, genome)
print("".join(map(str, result)))


