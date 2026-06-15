def count_pattern(text, pattern):
    count = 0
    k = len(pattern)
    for i in range(len(text)-k +1):
        if text[i:i+k] == pattern:
            count +=1
           
    return count 
        
text = input()
pattern = input()
print(count_pattern(text,pattern))

