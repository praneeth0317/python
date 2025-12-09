
w1 = input("Enter first word: ").lower()
w2 = input("Enter second word: ").lower()

if len(w1) != len(w2):
    print("Not an Anagram")
else:
    used = [False] * len(w2)

    is_anagram = True

    for i in range(len(w1)):
        found = False
        for j in range(len(w2)):
            if (w1[i] == w2[j]) and (not used[j]):
                used[j] = True
                found = True
                break
        if not found:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not an Anagram")
