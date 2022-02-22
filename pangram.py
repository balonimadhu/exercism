def is_pangram(sentence):
    input = sentence
    input = input.lower()
    input = set(input)
    alpha = [ ch for ch in input if ord(ch) in range(ord('a'), ord('z')+1)]
    if len(alpha) == 26:
        return True
    else:
        return False 