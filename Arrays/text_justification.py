"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is 
fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Approach: divide and conquer style
    - functionality to pad words on a single line to match max character length, makesure to pad it with extra space if need to get maxwidth count
    - If the number of spaces on a line does not divide evenly between words,
        the empty slots on the left will be assigned more spaces than the slots on the right?
    - If the number of spaces on a line does not divide evenly between words,
    the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space is inserted between words.
"""
def fullJustify(words:list[str], maxWidth: int):
    # Initialize an empty list to store lines of text, line being constructed and length of current line
    result = [] # list to store lines of text
    line = [] # Current line being constructed
    line_length = 0 # length of current line

    # Iterate through the list of words one by one
    for word in words:
        #for each word we check if adding it to the current line along with 
        #necessary space to achieve maxWidth would exceed the maxWidth.
        if len(word) + line_length + len(line) <= maxWidth:
            # add word to current line
            line.append(word)
            #increment line_lenght by len(word)
            line_length += len(word)
        
        # word can't fit on the current line so we complete current line 
        # and add it to result
        else:
            result.append(justify_line(line, maxWidth))
            # update line list with current word
            line = [word]
            # update current line_length since its a new line now
            line_length = len(word)
    
    # last line, left -justified
    result.append(" ".join(line).ljust(maxWidth))
    return result
def justify_line(line, maxWidth):
    #case when there is only one word
    if len(line) == 1:
        return line[0].ljust(maxWidth)
    
    #case when we have more than one word

    # calculate totalspaces for a given line
    total_spaces = maxWidth - sum(len(word) for word in line)

    #calculate the space space_gaps
    space_gaps = len(line) - 1

    #cal number of spaces to insert between each pair of words
    spaces_between_words = total_spaces // space_gaps

    #calculate extra spaces that couldn't fit evenly as possible
    extra_spaces = total_spaces % space_gaps

    #build the justified line
    #start with the first word in the line
    justified_line = line[0]
    for i in range(1, len(line)):
        spaces = " " * (spaces_between_words + (1 if  extra_spaces > 0 else 0))
        justified_line += spaces + line[i]
        if extra_spaces > 0:
            extra_spaces -= 0
    return justified_line

# TestCase
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

response = fullJustify(words=words, maxWidth=maxWidth)
print(response)
