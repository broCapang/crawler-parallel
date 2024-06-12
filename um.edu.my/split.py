def split_file_into_four(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // 4
    remainder = total_lines % 4

    chunks = [chunk_size + (1 if i < remainder else 0) for i in range(4)]

    start = 0
    for i, chunk in enumerate(chunks):
        with open(f'links-umnews-{i+1}.txt', 'w') as out_file:
            for line in lines[start:start+chunk]:
                out_file.write(line)
        start += chunk

split_file_into_four('links-umnews.txt')
