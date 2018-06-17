"""
Question 2 -- decodeString(s): Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

For s = "4[ab]", the output should be decodeString(s) = "abababab"
For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"
"""

def decode_string(s):
    """
        Returns decoded string based on specifed rules from encoded string
    """

    int_stack, str_stack = [],[]
    temp, result = "", ""

    for i in range(len(s)):
        count = 0

        if s[i].isdigit():
            while s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            i -= 1
            int_stack.append(count)

        elif s[i] == "]":
            temp = ""
            count = 0

            if int_stack:
                count = int_stack[-1]
                int_stack.pop()

            while str_stack and str_stack[-1] != "[":
                temp = str_stack[-1] + temp
                str_stack.pop()

            if str_stack and str_stack[-1] == "[":
                str_stack.pop()

            for j in range(count):
                result += temp

            for j in range(len(result)):
                str_stack.append(result[j])

            result = ""

        elif s[i] == "[":
            if s[i-1].isdigit():
                str_stack.append(s[i])
            else:
                str_stack.append(s[i])
                int_stack.append(1)

        else:
            str_stack.append(s[i])

    while str_stack:
        result = str_stack[-1] + result
        str_stack.pop()

    return result

if __name__ == '__main__':
    print(decode_string("4[ab]"))
    print("--------------------")
    print(decode_string("2[b3[a]]"))
