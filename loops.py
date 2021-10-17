counter_external = 0
counter_internal = 0

while counter_external < 5:
    while counter_internal < 6:
        print(counter_external, counter_internal)
        counter_internal+= 1
        if counter_internal >= 3:
            break

    counter_external += 1
    counter_internal = 0
