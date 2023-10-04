import streamlit as st
import pandas as pd

from cnf.cfg import *
from cnf.cnf import *
from cyk.cyk import *
from streamlit_web.streamlit_web import *

rules = open('rules/rules.txt', 'r').read().splitlines()
start_symbol = "K"
dictionary_cfg = {}
dictionary_cnf = {}

if __name__ == '__main__':
    cfg(dictionary_cfg, rules)
    cnf(dictionary_cfg, dictionary_cnf, start_symbol)
    streamlit_web(st, dictionary_cnf, cyk, pd)
