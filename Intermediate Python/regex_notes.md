###### REGULAR EXPRESSIONS ######

Regex is a cryptic looking string that describes a search pattern 

Examples of Regex:

1) ^s.+a
2) s[a-t]*$
3) \w{9}

Some parts of a Regex and their meaning:

1) ^ and $ => describes a position

2) \w and [a-t] => describes a set of characters

3) +, * and {n} => describes quantifiers which quantifies the number of occurences of a character

Some regularly used patterns in Regex:

1) ^ matches start of a string i.e ^Nig would match Nigeria

2) $ matches end of string i.e u$ would match Tinubu

3) \d would match a word with a single digit between 0 and 9 i.e
            
            \d ==========> Ronaldo7
            \d\d ========> Messi10
            \d\d\d ======> Omega300

4) \s stands for space would match anything having a space i.e \s would match "Lionel Messi"

5) \w stands for word character and would match any string having lowercase letters, uppercase letters,
digits and underscrore (a-z, A-Z, 0-9 and _). i.e

        \w ==============> Lionel Messi
        ^\w\w ===========> Lionel Messi
        ^\w\w\w\w\w\s ===> Power Rangers


6) *, ?, +, {n} etc are called Regex Quantifiers and are used to specify the number of copies of an expression



###### EXAMPLES

1) [aeiou]{2} would scan a string looking for 2 consecutive follows i.e Lionel Messi, Christiano Ronaldo

2) ^\w{7}$ searches for any string that are exactly 7 consective words; No more, no less i.e Ronaldo, Nigeria

3) If you omit the ^ and $ from the previus example i.e \w{7} would match any word with at least 7 consecutive 
charaters i.e Indaboski Bahose, Christiano Ronaldo





###### CODE SAMPLES

import re  # Importing the regular expressions library


# Matching example
pattern = r"\d+"  # Pattern to find one or more digits
text = "There are 123 apples and 456 oranges."
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']


# Replacing example
pattern = r"apple"  # Pattern to find the word "apple"
replacement = "banana"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: "There are 123 bananas and 456 oranges."

# 