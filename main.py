from resolution import derive_new_sentences

inp = 'input/'
out = 'output/'

def main(input_file, output_file):
    # Read knowledge base from input file
    with open(inp + input_file, 'r') as f:
        kb = [line.strip().split(' OR ') for line in f]

    # Derive new sentences using resolution rule
    all_sentences, parent_indexes = derive_new_sentences(kb)

    print('All sentences:', all_sentences)
    print('KB:', kb) # the initial knowledge base

    # Remove sentences that are always True
    all_sentences = [s for s in all_sentences if s != ['TRUE']]

    # Write new sentences and parent indexes to output file
    with open(out + output_file, 'w') as f:
        for i, sentence in enumerate(all_sentences):
            #if i >= len(kb):
                f.write(f'[{i}] ' + ' OR '.join(sentence) + '\n')
                f.write('Parents: ' + str(parent_indexes[i]) + '\n')
        f.write('\n\n\n\n' + 'Length of KB: ' + str(len(all_sentences)) + '\n')
        f.write('Num of new sentences: ' + str(len(all_sentences) - len(kb)))


for i in range(1, 7):
    print('Working with input file # ' + str(i) + ':')
    main('input' + str(i) + '.txt', 'output' + str(i) + '.txt')
    print('\n')
