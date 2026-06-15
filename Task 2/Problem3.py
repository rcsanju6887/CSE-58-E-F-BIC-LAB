def reverse_complement(pattern):

  complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
  
  result = ""

  for nucleotide in pattern : 
        result = complement[nucleotide]+ result

  return result

pattern = input()
print(reverse_complement(pattern))
