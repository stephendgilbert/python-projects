import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    result = defaultdict(set)
    for line in file:
        nodes = line.rstrip('\n').split(';')
        result[nodes[0]].update(nodes[1])
    return result


def graph_as_str(graph : {str:{str}}) -> str:
#     result = ''
#     for item in sorted(graph.items()):
#         result += '  ' + item[0] + ' -> ' + str(sorted(list(item[1]))) + '\n'
#     return result
    return '\n'.join([('  ' + str(item[0]) + ' -> ' + str(sorted(list(item[1])))) \
                      for item in sorted(graph.items())]) + '\n'
        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    reached = set()
    exploring = [start]
    while len(exploring) > 0:
        node = exploring.pop()
        reached.add(node)
        current = graph.get(node)
        if current != None:
            for destination in current:
                if destination not in reached:
                    exploring.append(destination)
    return reached

if __name__ == '__main__':
    # Write script here
    file = goody.safe_open("Enter file with graph: ", "r", "Could not open that file. Try again.")
    print()
    print('Graph: source -> {destination} edges')
    graph = read_graph(file)
    print(graph_as_str(graph))
    while True:
        starting = prompt.for_string("\nEnter a starting node", \
            is_legal=(lambda x : x == 'quit' or x in graph), \
            error_message = " Illegal: not a source node")
        if (starting == 'quit'): break
        nodes = reachable(graph, starting)
        print("From " + starting + " the reachable nodes are " + str(nodes))
    print()
    # For running batch self-tests
    # what is this?
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
