#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
   new_tuple = None
    else:
      new_tuple = sentence[0]
    return (len(sentence), new_tuple)
