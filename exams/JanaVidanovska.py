def expand_square(square):
    neighbour_squares = []
    x, y = square
    for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= x < N and 0 <= y < N:
            neighbour_squares.append((x, y))
    return neighbour_squares

def valid(position):
    x,y=position
    if 0<=x<N and 0<=y<N:
        return True
    else: return False
    
def expand_state(state,position):
    x,y=position
    states=state
    neighbours=expand_square(position)
    if valid(position):
        if states[x][y]==0:
            states[x][y]=1
        if states[x][y]==1:
            states[x][y]=0
        for pos in neighbours:
            i,j=pos
            if states[i][j]==0:
                states[i][j]=1
            if states[i][j]==1:
                states[i][j]=0
    return states  
    
state = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
]
position=(0,0)
expand_state(state,position)

//output shto dobivam

[[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]

poentata na igrata e vo matricata poleto ako e 0 da stane 1 i obranto, a isto i negovite sosedi, sosedi se gore dole, levo desno od nego
mene ne mi gi menuva nz zasho
