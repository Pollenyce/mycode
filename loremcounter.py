text = ["Lorem", "ipsum", "dolor", "sit", "amet", "consetetur", "sadipscing", "elitr", "lorem",
        "sed", "lorem", "diam", "nonumy", "eirmod", "tempor", "invidunt", "Lorem", "ut", "labore",
        "et", "dolore", "magna", "aliquyam", "erat", "sed", "diam", "voluptuz", "At", "lorem", 
        "vero", "eos", "et", "accusam", "et", "justo", "duo", "lorem", "dolores", "et", "ea"]

#Dieser Code sorgt dafür, dass gezählt wird wie oft das Wort "Lorem" in dem Text vorkommt. ("Lorem" = es wird +1 dazugezählt)
summe = 0
summe = 0
for wort in text:
    if wort == "lorem":
        summe = summe + 1
    if wort == "Lorem":
        summe = summe + 1

print(summe)

