import os


def cfg(dictionary_cfg, rules):
    for i in range(len(rules)):
        left_hand = rules[i].split(' -> ')[0]
        right_hand = set(rules[i].split(' -> ')[1].split(' | '))
        dictionary_cfg.update({left_hand: list(right_hand)})
