title = "Indonesian Literatur"
subtitle = 'The program can be used to produce various types of Indonesian literary texts, such as poems, stories, and dramas. This program can be used to produce creative and interesting Indonesian literature texts.'
github = "https://github.com/icequeenwand/indonesian-literatur"


def welcome(st):
    st.set_page_config(page_title="Indonesian Literatur", page_icon="::tada::", layout="wide", menu_items={
        'About': f"""
        ### Hello World
        {title}
        Made with :heart: by @gedeapriana
        https://github.com/icequeenwand/indonesian-literatur
        """
    })
    st.write(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)
    st.write(f"<p style='text-align: center'>{subtitle}</p>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center;'><a "
             f"href={github}>icequeenwand/indonesian-literatur</a></h2>", unsafe_allow_html=True)
    st.write('')


def streamlit_web(st, dictionary_cnf, cyk, pd):
    welcome(st)
    with st.container():
        st.write('---')
        input_column, rule_column = st.columns(2)
        with input_column:
            string_input = st.text_input(' ', placeholder='Input Indonesian Sentence')
            if len(string_input) == 0:
                st.error('Form tidak boleh kosong!')
            else:
                if cyk(dictionary_cnf, string_input)[0] == 'valid':
                    st.success("The sentence is Valid")
                elif cyk(dictionary_cnf, string_input)[0] == 'invalid':
                    st.error("The sentence is Invalid")
                else:
                    st.warning("The sentence is not Registered")
                st.table(pd.DataFrame(cyk(dictionary_cnf, string_input)[1], columns=string_input.split()))
        with rule_column:
            st.write('### CNF Rules:')
            st.write(dictionary_cnf)
