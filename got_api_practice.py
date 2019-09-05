from pprint import pprint
from characters import characters
from houses import houses

#  util fxns
def get_name(character):
    return character["name"]

def find_most_titles(characters):
    ref = 0
    name = ""
    for character in characters:
        if len(character["titles"]) > ref:
            ref = len(character["titles"])
            name = get_name(character)
    return name

def count_characters(characters, filter):
    res = []
    for character in characters:
        if filter(character):
            res.append(character)
    return len(res)

# composable filters
def begin_with_letter(letter, character):
    if character['name'][0] == letter:
        return True
    else:
        return False

def is_attribute(attr, value, character):
    if character[attr] == value:
        return True
    else:
        return False


# composed filters
def start_with_a(character):
    return begin_with_letter("A", character)

def start_with_z(character):
    return begin_with_letter("Z", character)

def is_dead(character):
    return not is_attribute("died", "", character)

def is_valyrian(character):
    return is_attribute("culture", "Valyrian", character)

def is_in_show(character):
    return not is_attribute("tvSeries", [""], character)



##########
# output #
##########

# 1
print("number of characters who's name begins with 'A'")
pprint(
    count_characters(characters, start_with_a)
)

# 2
print("\nnumber of characters who's name begins with 'Z'")
pprint(
    count_characters(characters, start_with_z)
)

# 3
print("\nNumber of dead characters:")
pprint(
    count_characters(characters, is_dead)
)

# 4
print("\nCharacter with the most titles:")
pprint(
    find_most_titles(characters)
)

# 5
print("\nnumber of characters who are Valyrian:")
pprint(
    count_characters(characters, is_valyrian)
)

# 6


# 7
print("\nNumber of characters in show: ")
pprint(
    count_characters(characters, is_in_show)
)