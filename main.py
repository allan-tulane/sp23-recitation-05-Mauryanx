import random, time
import tabulate


def qsort(a, pivot_fn):
    stack = [(0, len(a) - 1)]
    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = pivot_fn(a[left:right+1])
            i = left
            j = right
            while i <= j:
                while a[i] < pivot:
                    i =i + 1
                while a[j] > pivot:
                    j =j - 1
                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    i = i + 1
                    j = j - 1
            stack.append((left, j))
            stack.append((i, right))
    return a


def ssort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.
    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.
    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key
    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.
    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: a[0]
    qsort_random_pivot = lambda a: random.choice(a)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(lambda a: qsort(a, qsort_fixed_pivot), mylist),
            time_search(lambda a: qsort(a, qsort_random_pivot), mylist),
            time_search(lambda a: ssort(a), mylist),
            time_search(tim_sort, mylist),

        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot','selection sort','time_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_print():
    print_results(compare_sort())


random.seed()
test_print()
