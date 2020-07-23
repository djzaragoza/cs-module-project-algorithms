'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    ns = [1,1,2]
    combos = 0
    if n < 3: combos = ns[n]
    else:
        for _ in range(3, n):
            ns.insert(3,ns[0] + ns[1] + ns[2])
            ns.pop(0)
        for n in ns:
            combos += n
    return combos

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    else:
        print('Usage: eating_cookies.py [num_cookies]')