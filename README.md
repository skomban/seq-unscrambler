# seq-unscrambler
Recently I came across a post that was a screenshot of a piece of text in which each word had been partially scrambled. The text was as follows *"fi yuo cna raed tihs, yuo hvae a sgtrane mnid too. I cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The phaonmneal pweor of the hmuan mind!"*. I could unscramble the words in my head without much effort. But this got me thinking, if humans can perform this task then can computers do the same? 
I used a masked language model to reveal the original text after the letters in it's words are scrambled.

## Installation
```python
poetry install
```

## To run
```python
PYTHONPATH=. python src/main.py -t "if you can read this you have a strange mind too" -k 1

args:
    -t text
    -k top k candidates
```
#### Output
    Input text: if you can read this you have a strange mind too
    Scrambled text: fi uoy acn drae hits ouy ehva a eagrnst idmn oot

    Top 1 inferred input texts with log probability scores:

    sentence: if you can read this you have a strange mind too
    score: -40.09420431405306

#### Streamlit
```python
PYTHONPATH=. streamlit run streamlit_demo.py
```
#### Tests
```python
PYTHONPATH=. poetry run pytest --cov src
```
