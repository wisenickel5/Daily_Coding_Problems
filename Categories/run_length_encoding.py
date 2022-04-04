'''
Problem completed by Dylan Alexander on 02/10/2022
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a 
single count and character. For example, the string "AAAABBBCCDAA" would 
be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string 
to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
'''

def runLength_Encoding(s: str) -> str:
    result = ""
    if len(s) == 1:
        result = str(1) + s

    elif len(s) > 1:
        counter = 1
        for idx, char in enumerate(s):
            if idx >= 1:
                if char == s[idx - 1]:
                    counter += 1
                elif char != s[idx - 1]:
                    result = result + f"{counter}{s[idx - 1]}"
                    counter = 1
            if idx == len(s) - 1:
                result = result + f"{counter}{s[idx - 1]}"

    return result

if __name__ == "__main__":
    code = "AAAABBBCCDAAB"
    new_code = runLength_Encoding(code)
    print(new_code)