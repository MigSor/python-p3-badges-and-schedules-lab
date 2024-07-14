def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    creator_list = []
    for name in names:
        creator_list.append(f"Hello, my name is {name}.")
    return creator_list


def assign_rooms(names):
    creator_list_with_room = []
    for index, name in enumerate(names):
        creator_list_with_room.append(
            f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return creator_list_with_room


def printer(names):
    list = batch_badge_creator(names)
    list_2 = assign_rooms(names)
    for item in list:
        print(item)
    for item in list_2:
        print(item)
