# n=int(input())
# dict={}
# result=[]
# for step in range(n):
#     matrix=tuple(input().strip() for _ in range(8))
#     if matrix in dict:
#         dict[matrix]+=1
#     else:
#         dict[matrix]=1
#     result.append(dict[matrix])
# for i in range(n):
#     print(result[i])



n=int(input())
dic={}
result=[]
for _ in range(n):
    step=tuple(input().strip()for _ in range(8))
    if step in dic:
        dic[step]+=1
    else:
        dic[step]=1
    result.append(dic[step])
for i in range(n):
    print(result[i])
"""
8
********
******pk
*****r*p
p*pQ****
********
**b*B*PP
****qP**
**R***K*
********
******pk
*****r*p
p*pQ****
*b******
****B*PP
****qP**
**R***K*
********
******pk
*****r*p
p*p*****
*b**Q***
****B*PP
****qP**
**R***K*
******k*
******p*
*****r*p
p*p*****
*b**Q***
****B*PP
****qP**
**R***K*
******k*
******p*
*****r*p
p*pQ****
*b******
****B*PP
****qP**
**R***K*
********
******pk
*****r*p
p*pQ****
*b******
****B*PP
****qP**
**R***K*
********
******pk
*****r*p
p*p*****
*b**Q***
****B*PP
****qP**
**R***K*
********
******pk
******rp
p*p*****
*b**Q***
****B*PP
****qP**
**R***K*

1
1
1
1
1
2
2
1
"""

