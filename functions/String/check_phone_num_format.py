def solution(S):
    pnum = S.split('-') 
    if len(pnum) != 3: 
        return False
    else:
        if len(pnum[0]) != 3:
            return False
        if len(pnum[1]) != 3:
            return False
        if len(pnum[2]) != 4:
            return False
        if pnum[0].isdecimal() and pnum[1].isdecimal() and pnum[2].isdecimal(): 
            return True
     return False
