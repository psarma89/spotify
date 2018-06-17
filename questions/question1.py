"""
Question 1 -- sortByStrings(s,t): Sort the letters in the string s by the order they occur in the string t. You can assume t will not have repetitive characters. For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw". For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".
"""

def sort_by_string(s,t):
    """
        Returns the sorted letters in the string 's' by the order they occur in the string 't'
    """

    if len(s) and len(t):
        sorted_char_list = sorted(s, key=lambda char: t.index(char))
        return "".join(sorted_char_list)
    else:
        return "The input strings are not correctly formatted"

if __name__ == '__main__':
    print(sort_by_string("weather", "therapyw"))
    print("--------------------")
    print(sort_by_string("good", "odg"))
