def get_actions(state):
    zero_index = state.index(0)
    actions = []
    if zero_index > 2:
        actions.append('^')
    if zero_index < 6:
        actions.append('v')
    if zero_index % 3 != 0:
        actions.append('<')
    if zero_index % 3 != 2:
        actions.append('>')
    return actions

def get_state(action, state):
    new_state = state.copy()
    zero_index = new_state.index(0)
    if action == '^':
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
    elif action == 'v':
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
    elif action == '<':
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
    elif action == '>':
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
    return new_state

def isgoal(state):
    return state == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def compute_cost(action, state):
    return 1