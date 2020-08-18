from googlesearch import search


def find_posts(department, number, num_results):
    """
    Finds relevant posts to respond to a comment asking about the provided
    class name/number.
    Input:
    department - department prefix of a class
    number - class number
    num_results - the desired number of results to be returned
    """
    results = []
    query = "r/cornell " + department + " " + number + " site:www.reddit.com"
    for j in search(query, tld="co.in", num=num_results, stop=num_results, pause=2):
        results.append(j)
    return results
