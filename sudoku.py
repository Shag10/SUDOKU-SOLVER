def sol(sud):
    f=f_empty(sud)
    if not f:
        return True
    else:
        row,col=f
    for i in range(1,10):
        if valid(sud,i,(row,col)):
            sud[row][col]=i
            if sol(sud):
                return True
            sud[row][col]=0
    return False
def valid(sud,n,pos):
    for i in range(len(sud[0])):
        if(sud[pos[0]][i]==n and pos[1]!=i):
            return False
    for i in range(len(sud)):
        if(sud[i][pos[1]]==n and pos[0]!=i):
            return False
    b_x=pos[1]//3
    b_y=pos[0]//3

    for i in range(b_y*3,b_y*3+3):
        for j in range(b_x*3,b_x*3+3):
            if(sud[i][j]==n and (i,j)!=pos):
                return False
    return True
def p_board(sud):
    for i in range(len(sud[0])):
        if i%3==0 and i!=0:
            print("- - - - - - - - - -")
        for j in range(len(sud[0])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==8:
                print(sud[i][j])
            else:
                print(str(sud[i][j])+" ",end="")
def f_empty(sud):
    for i in range(len(sud)):
        for j in range(len(sud[0])):
            if sud[i][j]==0:
                return (i,j)
    return None
board=[
    [4,0,0,0,2,0,0,5,0],
    [3,0,9,8,0,7,6,4,0],
    [0,8,0,0,0,0,0,0,3],
    [0,0,0,0,0,8,5,0,0],
    [7,9,0,5,0,0,0,6,8],
    [8,0,0,2,0,9,0,0,7],
    [0,2,0,6,0,0,0,0,0],
    [6,7,0,0,9,5,0,2,0],
    [5,0,0,4,0,0,7,0,6],
    ]
p_board(board)
sol(board)
print("\nYour answer should be:\n")
p_board(board)
