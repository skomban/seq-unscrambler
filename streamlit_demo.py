import streamlit as st

from src.main import SeqUnscrambler
from src.utils import scramble_words


class SeqUnscramblerDemo:

    def __init__(self):
        st.set_page_config(
            page_title="Sequence Unscrambler Demo",
            initial_sidebar_state="expanded",
            layout="wide"
        )
        self.examples = [
            "unscrambling scrambled words",
            "if you can read this you have a strange mind too",
            "this is a simple hack",
            "this uses a language model"

        ]

    @st.cache(show_spinner=False, suppress_st_warning=True, allow_output_mutation=True)
    def load_model(self):
        return SeqUnscrambler()

    def main(self):
        st.title("Sequence Unscrambler")
        st.markdown('A demo for unscrambling scrambled words in a text sequence')

        max_candidates = st.sidebar.number_input(
            label='Max candidates',
            min_value=1,
            max_value=5,
            value=1
        )

        with st.spinner('Loading model..'):
            model = self.load_model()

        input_text = st.selectbox(
            label="Choose an example",
            options=self.examples
        )
        input_text = st.text_input(
            label="Short input text",
            value=input_text
        )

        if (len(input_text.split()) < 15) and (input_text.strip()):
            if st.button("Unscramble"):
                scrambled_text = st.text_input(
                    label='Scrambled input text',
                    value=scramble_words(input_text),
                )

                results = model.analyze(scrambled_text, top_k=max_candidates)
                unscrambled_sentence = results
                st.markdown(f'#### Output:')
                st.write('')

                for sentence, score in unscrambled_sentence:
                    st.success(sentence)
                    st.write('\n')
        else:
            st.warning("Enter text of length less than 10 tokens to continue!!!")


if __name__ == "__main__":
    obj = SeqUnscramblerDemo()
    obj.main()
