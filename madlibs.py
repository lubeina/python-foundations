print ("Mad libs where libs get mad")
print ("Start below:")

time = input("Enter a number from 1 to 12:")
items = input("Enter a noun (plural):")
name = input("Enter a name:")
scream = input("Enter any sentence:")
action = input("Enter a verb:")

print ("The story then goes... \nIt was "+time+" o'clock when I heard a nock at the door. \nI opened the door and there was a box full of "+items+" with a note saying 'From "+name.title()+".' \nJust as I closed the door I heard a scream '"+scream.upper()+".' \nI froze in place and all I could do was "+action+".")
