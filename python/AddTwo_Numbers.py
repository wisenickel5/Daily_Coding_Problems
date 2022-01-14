# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def AddTwo_Numbers(l1, l2):
    reversed(l1), reversed(l2)
    
    string1 = [str(num) for num in l1]
    a_string1 = "".join(string1)
    a_Int = int(a_string1)

    string2 = [str(num) for num in l2]
    b_string2 = "".join(string2)
    b_Int = int(b_string2)

    final = a_Int + b_Int
    print(f"{a_Int} + {b_Int} = {final}")

    return final

if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    AddTwo_Numbers(l1, l2)