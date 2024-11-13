def sort_lines(input_file, output_file):
    # Open the input file and read all lines
    with open(input_file, 'r') as f: 
     lines = f.readlines()

    # Separate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[:2]
    body = lines[2:]

    # sort the remaining lines by the first character if 0 (case-insensitive)
    sorted_body = sorted(body, key=lambda line: line[0].lower(), reverse=True)

    # you want to sort the file not reversed, just delete the '. reverse = true'
    # combine the header and sorted body 

    sorted_lines = header + sorted_body 

    # write the result to the output file
    with open(output_file, 'w') as f:
       f.writelines(sorted_lines)

# specify input and output file names
input_file = ''
output_file = ''

# call the function to sort lines 
sort_lines(input_file, output_file)

