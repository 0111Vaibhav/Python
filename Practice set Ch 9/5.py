
# Repeat program 4 for a list of such words to be censored.

words = [
    "donkey",
    "insults",
    "brutal",
    "jeers",
    "battle"
]
with open ("Practice set Ch 9/file.txt") as f :
    content = f.read()
    for word in words:
        content = content.replace(word,"#" * len(word))
with open("Practice set Ch 9/file.txt","w") as f:
    f.write(content)