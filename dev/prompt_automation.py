from itertools import product

def fill_blank_spaces(sentence, string_lists):
    blank_spaces = sentence.split(" ")
    blank_spaces = [i for i in blank_spaces if i.startswith("__")]
    for i in range(len(blank_spaces)):
        sentence = sentence.replace(blank_spaces[i],"{"+str(i)+"}")
    for element in product(*string_lists):
        yield sentence.format(*element)

# Example usage:
sentence = "The __1__ __2__ __3__ __4__ the __5__"
string_lists = [["cat", "dog"], ["sat", "stood"], ["on", "under"], ["the", "a"], ["mat", "table"]]
result = fill_blank_spaces(sentence, string_lists)
print(list(result))