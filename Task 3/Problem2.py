def hamming_distance(s1, s2):
    distance =0
    for i in range(len(s1)):
        if s1[i] !=s2[i]:
            distance +=1
    return distance

def approximate_pattern_matching(pattern, text,d):
   positions =[]
   k = len(pattern)
   for i in range(len(text)- k + 1):
       if hamming_distance(text[i:i+k], pattern)<= d:
              positions.append(i)
   return positions 

pattern = input()
text = input()
d = int(input())

result = approximate_pattern_matching(pattern ,text , d)
print(" ".join(map(str, result)))


