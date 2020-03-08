def score_match(subject, query, subject_start, query_start, length):
    score = 0
    # for each base in the match
    for i in range(0,length):
        # first figure out the matching base from both sequences
        subject_base = subject[subject_start + i]
        query_base = query[query_start + i]
        # then adjust the score up or down depending on 
        # whether or not they are the same
        if subject_base == query_base:
            score = score + 1
        else:
            score = score - 1
    return score

def try_all_matches(subject, query, score_limit):
    for subject_start in range(0,len(subject)):
        for query_start in range(0,len(query)):
            for length in range(0,len(query)):
                if (subject_start + length < len(subject) and query_start + length < len(query)):
                    score = score_match(subject, query, subject_start, query_start, length)
                    # only print a line of output if the score is better than some limie
                    if (score >= score_limit):
                        print(subject_start, query_start, length, score)

try_all_matches('one_', 'another_sequencee', 9)