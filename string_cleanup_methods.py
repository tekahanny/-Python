# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"

def fancy_cleanup(word):
    return word.strip().replace("g", "z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey  "))
print(fancy_cleanup("       nonsense  "))
print(fancy_cleanup("grade"))
