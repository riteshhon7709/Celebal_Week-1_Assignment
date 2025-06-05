def minion_game(string):
    vowels = 'AEIOU'
    kevin = sum(len(string) - i for i in range(len(string)) if string[i] in vowels)
    stuart = sum(len(string) - i for i in range(len(string)) if string[i] not in vowels)

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")

s = input()
minion_game(s)
