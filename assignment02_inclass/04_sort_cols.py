def sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter=',', reverse=False):
    # open the input file and read all lines 
    with open(input_file, 'r') as f: 
        lines = f.readlines()

    # separate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[:2]
    body = lines[2:]    

    # sort the body by primary and secondary columns (case-insensitve)
    sorted_body = sorted(
        body, 
        key=lambda line: (
            line.split(delimiter)[primary_index].lower(), # primary sort
            line.split(delimiter)[secondary_index].lower() # secondary sort 
        ),
        reverse=reverse # apply reverse sorting if needed
    )

    # combine the header and sorted body 
    sorted_lines = header + sorted_body 

    # write the result to the output file 
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# specify input and output file names 
input_file = 'names_ages.csv'
output_file = '01_names_ages.csv'

# sort by the first column
sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter=',', reverse=False)