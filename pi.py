text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

words_list = ("".join(("".join(text.split(","))).split(".")).split())
words_count_list = list(map(str, list(map(len, words_list))))
number = ""
for s in range(len(words_count_list)):
    number += words_count_list[s]
print(number)