# seq-unscrambler
Recently I came across a post that was a screenshot of a piece of text in which each word had been partially scrambled. The text was as follows "fi yuo cna raed tihs, yuo hvae a sgtrane mnid too. I cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The phaonmneal pweor of the hmuan mind!". I could unscramble the words in my head without much effort. But this got me thinking, if humans can perform this task then can computers do the same? 
I used a masked language model (Roberta) to reveal the original sentence after the letters in it's words were scrambled.

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
### To run demo using streamlit
```python
PYTHONPATH=. streamlit run streamlit_demo.py
```
