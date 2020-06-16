import re
'''
def reverse(x):
    s = str(x)
    result = ''
    if s.startswith('-'):
        s2 = s.replace('-', '')
        for v in s2:
            result = v + result
        result= '-'+result

        print(int(result))
    else:
        for v in s:
            result = v + result
        return int(result)
x =-1420
print(reverse(x)) '''



# def find_func(string):
#     # li = [x for x in string]
#     length = []
#     result = []
#     for i in string:
#         print("starting", i, result, length)
#         if i not in result:
#             print("appending")
#             result.append(i)
#             print(result)
#         elif i in result: 
#             print("checking lenght")
#             length.append(len(result))
#             print(length)
#             result = []
#             result.append(i)
#     length.append(len(result))
#     max_length = max(length)
#     return max_length
#     # total = max(length)
#     # return total
    

# string = "abcdefghcijklmnop"

# print(find_func(string))

# def find(string):
#     length = 0
#     for i in range(len(string)):
#         for j in range(len(string)):
#             substring = string[i:j]
#             if len(list(re.finditer(substring, string))) > 1 and length < len(substring):
#                 length = len(substring)
#     print(length)

# string = "sttrg"
# find(string)

def sam_reverse(num):
    str_num = str(num)
    rev_num =''
    
    for v in str_num:
        rev_num = v + rev_num
    # if rev_num.endswith("-"):
    #     rev_num2 = rev_num.replace("-", "")
    #     rev_num = "-"+ rev_num2

    if rev_num == str(num):
        print(rev_num)
        return True
    else:
        print(rev_num)
        return False

n = 54345
print(sam_reverse(n))