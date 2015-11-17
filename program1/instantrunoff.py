import goody


def read_voter_preferences(file : open):
    result = dict()
    for line in file:
        items = line.rstrip('\n').split(';')
        result[items[0]] = [e for e in items[1:]]
    return result


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    result = ''
    for voter in sorted(d, key=key, reverse=reverse):
        result += '  ' + str(voter[0]) + " -> " + str(d.get(voter[0])) + '\n'
    return result


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    result = dict()
    for choice in vp.values():
        for vote in choice:
            if vote in cie:
                result[vote] = result.get(vote, 0) + 1
                break
    return result


def remaining_candidates(vd : {str:int}) -> {str}:
    result = sorted(vd.items(), key=(lambda t : t[1]))  # sort by lowest count
    return {e[0] for e in result if e[1] != result[0][1]} #compared each to lowest count


def run_election(vp_file : open) -> {str}:
    vp = read_voter_preferences(vp_file)
    candidates = {c for group in vp.values() for c in group}
#    print(candidates)
    print('\nVoter Preferences')
    print(dict_as_str(vp))
    ballot = 1
    while len(vp) > 1:
        print('Vote count on ballot #' + str(ballot) + ' with candidates (alphabetically) = ' + str(candidates))
        print(dict_as_str(evaluate_ballot(vp, candidates)))
        print('Vote count on ballot #' + str(ballot) + ' with candidates (numerically) = ' + str(candidates))
        print(dict_as_str(evaluate_ballot(vp, candidates), key=(lambda t : t[1]), reverse=True))
        vp = remaining_candidates(vp)
    return set(vp[0] if len(vp) == 1 else set()) 
    
if __name__ == '__main__':
    # Write script here
#     file = goody.safe_open('Enter file with voter preferences', 'r', 'Could not open file')
#     winner = run_election(file)
#     if winner == set():
#         print("No winner")
#     else:
#         print("Winner is", winner)
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
