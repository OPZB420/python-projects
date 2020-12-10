## Replace substrings in a string

things = "tree, box, chair, lamp, \n" \
         "desk, cat, dog, grass, \n" \
         "pig, box, lamp, shelf"
print(things)
print()

old_item = input("old item: ")
new_item = input("new item : ")
len_old_item = len(old_item)

i = things.find(old_item)
while i > 0:
    before = things[:i]
    after = things[i+len_old_item :]
    things = before + new_item + after
    i = things.find(old_item)
    
print()
print(things)