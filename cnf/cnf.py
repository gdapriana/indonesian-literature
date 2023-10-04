temp_variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
new_right_hand = []
new_left_hand = []


def first_step(dictionary_cfg):
    key = list(dictionary_cfg.keys())
    for i in key:
        for j in key:
            if i in dictionary_cfg[j]:
                dictionary_cfg[j].remove(i)
                dictionary_cfg[j].extend(dictionary_cfg[i])


def second_step(dictionary_cfg, start_symbol):
    if rule_max_length(dictionary_cfg, start_symbol) > 2:
        for j in dictionary_cfg[start_symbol]:
            if len(j.split(' ')) <= 2:
                continue
            else:
                remove_non_terminal(start_symbol, j, dictionary_cfg)


def remove_non_terminal(pin, check_non_term, dictionary_cfg):
    last_check_val = check_non_term.split(' ')
    temp = ''
    index = get_subs_index(new_right_hand, check_non_term)
    if index == -1:
        add_val = ' '.join(last_check_val[0:2])
        new_left_hand.append(temp_variables[len(new_left_hand)])
        new_right_hand.append(add_val)
        temp = check_non_term.replace(add_val, new_left_hand[len(new_left_hand) - 1])
    else:
        temp = check_non_term.replace(new_right_hand[index], new_left_hand[index])
    dictionary_cfg[pin][dictionary_cfg[pin].index(check_non_term)] = temp


def rule_max_length(dictionary_cfg, start_symbol):
    maximize = 0
    for i in dictionary_cfg[start_symbol]:
        if len(i.split(' ')) > maximize:
            maximize = len(i.split(' '))
    return maximize


def get_subs_index(new_rs, check_non_term):
    for i in new_rs:
        if i in check_non_term:
            return new_rs.index(i)
    return -1


def cnf(dictionary_cfg, dictionary_cnf, start_symbol):
    first_step(dictionary_cfg)
    second_step(dictionary_cfg, start_symbol)
    dictionary_cnf.update(dictionary_cfg)
