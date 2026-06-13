def maze(grid,path,i,j,n):
    if(i==n and j==n):
        print(path)
        return
    if(i+1<=n and grid[i+1][j]==1):
        maze(grid,i+1,j,n)
    if(j+1<-n and grid[i][j+1]==1):
        maze(grid,i,j+1,n)
    grid = [[1,2]]

