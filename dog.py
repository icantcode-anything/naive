# -----------------------------------------
# Word Hunt using Naive and KMP Algorithm
# -----------------------------------------

def naive_search(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    n, m = len(text), len(pattern)
    results = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            results.append((i, i + m - 1))
    return results


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    results = []

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            results.append((i - j, i - 1))
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results


# ------------------------
# MAIN PROGRAM
# ------------------------

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

# You can change this line to: results = naive_search(text, pattern)
results = kmp_search(text, pattern)

if results:
    print(f'"{pattern}" word exists!')
    for start, end in results:
        print(f'"{pattern}" word is in the index {start} and ending {end}')
else:
    print(f'"{pattern}" word does NOT exist!')