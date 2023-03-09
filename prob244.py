import copy

def h(puzzle):
    score=0
    target="*010010110100101"
    #target="*01010101"
    for i in range(16):
        if i==0:
            if puzzle[0]=='1':
                score+=2
            elif puzzle[0]=='0':
                score+=1
        #elif puzzle[i]=='*':
        #    score+=i//4+i%4
        elif puzzle[i]!=target[i]:
            score+=1

    return score

def h_pattern(puzzle):
    score=0
    target="0101010"
    j=0
    for i in [12, 13, 14, 15, 11, 7, 3]:
        if puzzle[i]!=target[j]:
            score+=1
        j+=1

    return score

def available_moves(x, y, prev_move):
    moves=""
    if x>0 and prev_move!="U":
        moves+="D"
    if x<3 and prev_move!="D":
        moves+="U"
    if y>0 and prev_move!="L":
        moves+="R"
    if y<3 and prev_move!="R":
        moves+="L"
    
    return moves

def solution():
    s="*100110011001100"
    s_2="10011100*"
    t="*010010110100101"

    curr_level=[(s, 0, 0, "", 0, -1, "")]
    next_level=[]
    history=[s]
    for i in range(48):
        while curr_level:
            next_level_capacity=0
            s, x, y, prev_move, g_score, h_score, path=curr_level.pop()
            if h_score==0:
                print("success")
                print("g score = ", g_score)
                print("path = ", path)
                print(s)
            for move in available_moves(x, y, prev_move):
                path_tmp=path+move
                s_tmp=list(s)
                x_tmp=x
                y_tmp=y
                if move=="L":
                    s_tmp[x*4+y], s_tmp[x*4+y+1]=s[x*4+y+1], '*'
                    x_tmp, y_tmp=x, y+1
                elif move=="R":
                    s_tmp[x*4+y], s_tmp[x*4+y-1]=s[x*4+y-1], '*'
                    x_tmp, y_tmp=x, y-1
                elif move=="U":
                    s_tmp[x*4+y], s_tmp[(x+1)*4+y]=s[(x+1)*4+y], '*'
                    x_tmp, y_tmp=x+1, y
                elif move=="D":
                    s_tmp[x*4+y], s_tmp[(x-1)*4+y]=s[(x-1)*4+y], '*'
                    x_tmp, y_tmp=x-1, y
    
                s_tmp="".join(s_tmp)
                if s_tmp not in history:
                    #h_score_tmp=h_pattern(s_tmp)
                    h_score_tmp=h(s_tmp)
                    next_level.append((s_tmp, x_tmp, y_tmp, move, g_score+1, h_score_tmp, path_tmp))
                    history.append(s_tmp)
            
        curr_level=next_level
        next_level=[]
        curr_level=sorted(curr_level, key=lambda d: d[4]+d[5])

    print("History length:", len(history))
    
    #for s in curr_level:
    #    print(s)
    #    print(h(s[0], list(t)))
    #    print(s[0])

solution()
