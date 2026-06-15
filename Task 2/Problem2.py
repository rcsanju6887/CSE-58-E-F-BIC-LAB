def frequent_words(text, k):
    count_dict = {}

    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        if kmer in count_dict:
            count_dict[kmer] += 1
        else :
            count_dict[kmer] =1

    max_count = max(count_dict.values())

    result =[]
    for kmer , count in count_dict.items():
        if count == max_count:
            result.append(kmer)

    return result
text = input()
k = int(input())

print("".join(frequent_words(text, k)))

