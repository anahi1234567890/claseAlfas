word = input("ingresa una palabra\n")
world= list(word)
print ("Es polidromo") if world == list(reversed(world)) else print("No es polidromo")