# aba
# lol
# "ab" "a"
# "hell" "eh"
# "lleh" "hell"

def is_palindrome_pair(a, b):
    s = a + b
    for i in range(1, (len(s)/2) + 1):
        if (s[i-1] != s[-i]):
            return False
    return True

# print is_palindrome_pair('ab', 'a')
# print is_palindrome_pair('hell', 'eh')
# print is_palindrome_pair('lleh', 'hell')
# print is_palindrome_pair('lle', 'hell')

# ["a", "ba", "hello", "olleh", "eeh"]
# ["aab", "a", ""]

def check_palindromes(strings):
    for i in range(len(strings)):
        aString = strings[i]
        for j in range(len(strings)):
            bString = strings[j]
            if (is_palindrome_pair(aString, bString) and j != i):
                return True
    return False

# print check_palindromes(["a", "ba", "hello", "olleh", "eeh"])
# # [("a", "ba"), ("hello", "olleh"), ... ]
# print check_palindromes(["aab", "ab", ""])

def find_palindromes(strings):
    palindromes = []
    for i in range(len(strings)):
        aString = strings[i]

        for j in range(len(strings)):
            bString = strings[j]

            if (j != i and is_palindrome_pair(aString, bString)):
                palindromes.append((aString, bString))

    return palindromes

# print find_palindromes(["a", "ba", "hello", "olleh", "eeh"])
# print find_palindromes(["aab", "ab", ""])
# print find_palindromes(["a", "a", "ba", "hello", "olleh", "eeh", "hellol", "eh", "leh"])

def reverse(s):
    return s[::-1]

def make_palindrome_strings(s):
    l = []
    for i in range(1, len(s) + 1):
        l.append(reverse(s[-i:]))
    return l

    # "hello" -> "olleh", "lleh"

print make_palindrome_strings('hello')

# "hellol"     -> "leh"
# "hel" "lol"  -> "leh"

# "olle" "hello" => "ollehello"


# "" "hello" => "olleh"
# "h" "ello" => "olle"

# ======================

# "he" "llo" => "oll"
# "hel" "lo" => "ol"
