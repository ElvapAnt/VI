balls = {
    'w': ['w', 'w', 'w', 'w'],
    'y': ['y', 'y', 'y', 'y'],
    'r': ['r', 'r', 'r', 'r'],
    'g': ['g', 'g', 'g', 'g'],
    'b': ['b', 'b', 'b', 'b']
}
start = ['w', 'r', 'y', 'b']
end = ['b', 'g', 'w', 'r']

for color in start:
    balls[color].pop()


def calculate_turns(current_color, target_color, color_order):
    if current_color == target_color:
        return 0
    current_index = color_order.index(current_color)
    target_index = color_order.index(target_color)
    return (target_index - current_index) % len(color_order)


def h(state):
    color_order = list(balls.keys())
    correct_position_bonus = sum(1 for s, e in zip(state, end) if s == e)
    distance = sum(calculate_turns(s, e, color_order) for s, e in zip(state, end))
    # Higher bonus for correct position means lower overall heuristic value
    return distance - correct_position_bonus


# def h(state):
#     score = sum(s != e for s, e in zip(state, end))
#     bonus = sum(1 for s, e in zip(state, end) if s == e)
#     return score - bonus


def generate_states(state):
    new_states = []
    rest_of_colors = list(balls.keys())
    for j, color in enumerate(state):
        i = rest_of_colors.index(color)
        new_state = list(state)
        if i + 1 >= len(rest_of_colors):
            new_state[j] = rest_of_colors[0]
        else:
            new_state[j] = rest_of_colors[i + 1]
        new_states.append(tuple(new_state))
    return new_states


def a_star(start, end):
    found_end = False
    open_set = set()
    open_set.add(tuple(start))
    print(open_set)
    closed_set = set()
    g = {}
    prev_states = {}
    g[tuple(start)] = 0
    prev_states[tuple(start)] = None
    while len(open_set) > 0 and (not found_end):
        state = None
        for next_state in open_set:
            if state is None or g[next_state] + h(next_state) < g[state] + h(state):
                state = next_state
            if state == tuple(end):
                found_end = True
                break
        for next_state in generate_states(state):
            cost = 1
            if next_state not in open_set and next_state not in closed_set:
                open_set.add(next_state)
                prev_states[next_state] = state
                g[next_state] = g[state] + cost
            else:
                if g[next_state] > g[state] + cost:
                    g[next_state] = g[state] + cost
                    prev_states[next_state] = state

                if next_state in closed_set:
                    closed_set.remove(next_state)
                    open_set.add(next_state)
        open_set.remove(state)
        closed_set.add(state)
    path = []
    if found_end:
        prev = tuple(end)
        while prev_states[prev] is not None:
            path.append(prev)
            prev = prev_states[prev]
        path.append(start)
        path.reverse()
    return path


print(a_star(start, end))
