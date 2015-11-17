import goody


def read_fa(file : open) -> {str:{str:str}}:
    result = dict()
    for line in file:
        tokens = line.rstrip('\n').split(';')
        # This is how I did it using only what I know
#         states = dict()
#         for i in range(1, len(tokens), 2):
#             states[tokens[i]] = tokens[i + 1]

        # Using this entry from http://stackoverflow.com/questions/6900955/python-convert-list-to-dictionary
        # Creates new list slices
        # states = dict(zip(tokens[1::2], tokens[2::2]))
        
        # From same entry, using the "grouper" recipe (which is inscrutable to me)
        states = dict(zip(*[iter(tokens[1:])]*2))
        
        result[tokens[0]] = states
    return result

'''
    fa_as_str has a dictionary parameter (representing the FA); 
    it returns a multi-line string (each line is ended by '\n'), which when 
    printed shows the contents of the FA in the appropriate textual 
    form (body is 4 lines; can you do it in 1?).
        even transitions: [('0', 'even'), ('1', 'odd')]
        odd transitions: [('0', 'odd'), ('1', 'even')]
'''
def fa_as_str(fa : {str:{str:str}}) -> str:
    return '\n'.join(['  %s transitions: %s' % (k, str(sorted(v.items()))) for (k,v) in sorted(fa.items())]) + '\n'
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    pass


def interpret(fa_result : [None]) -> str:
    pass

if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
