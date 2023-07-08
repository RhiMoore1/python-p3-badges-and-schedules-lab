def badge_maker(name):
    return(f"Hello, my name is {name}.")


def batch_badge_creator(names):
    return[f'Hello, my name is {name}.' for name in names]
    

def assign_rooms(names):
    rooms = [1, 2, 3, 4, 5, 6, 7, 8]
    messages = []
    for i, name in enumerate(names):
        if i >= len(rooms):
            break
        messages.append(f"Hello, {name}! You'll be assigned to room {rooms[i]}!")
    return messages



def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for assignment in assignments:
        print(assignment)
    
result = printer(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"])
print(result)