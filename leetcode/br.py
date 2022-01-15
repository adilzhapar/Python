# bracket sequence
s = input()

st = []
for i in s:
    if len(st) == 0 and i in '({[':
        st.append(i)
    elif len(st) != 0:
        if i == ')' and st[-1] == '(': st.pop()
        elif i == '}' and st[-1] == '{': st.pop()
        elif i == ']' and st[-1] == '[': st.pop()
        else: st.append(i)
    else: 
        print(False)
        exit(0)
print(len(st) == 0)
