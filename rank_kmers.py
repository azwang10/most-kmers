# generates the whole genome as a string
seq = open('sequence.txt', 'r')
seq_str = seq.read().replace('\n','')
seq_str = seq_str[68:]

#builds a hash table of all 6-mer combinations
bases = ['A', 'T', 'C', 'G']
hash_table = []
to_append = ''
for i in bases:
    for j in bases:
        for k in bases:
            for l in bases:
                for m in bases:
                    for n in bases:
                        hash_table.append([i + j + k + l + m + n, 0])

#for a given 6-mer finds its index within the hash table
def get_index_in_hash(seq_str):
    total = 0
    seq_str = seq_str[::-1]
    count = 0
    bases = ['A', 'T', 'C', 'G']
    for i in seq_str:
        total += bases.index(i) * (4 ** count)
        count += 1
    return total

#adds all 6-mers to the corresponding count in the hash table
for i in range(len(seq_str) - 5):
    kmer = seq_str[i:i+6]
    index = get_index_in_hash(kmer)
    hash_table[index][1] += 1
    print(i)

#a selection sort for the list in table format
def selSort(table):
    for i in range(len(table)):
        smallest = table[i][1]
        for k in range(i + 1, len(table)):
            if table[k][1] < table[i][1]:
                temp = table[k]
                table[k] = table[i]
                table[i] = temp
    return table

#sorts the table and outputs a csv of the counts of all the 6-mers
hash_table = selSort(hash_table)
output = open('ranked.csv', 'w')
output.write('6-mer,count\n')
for i in hash_table:
    output.write(i[0] + ',' + str(i[1]) + '\n')
