
buildings = '123456' #skyscrapers size from 1 to 6
rows = "ABCDEF"

def cross(A:str,B:str)->list:
    return [a+b for a in A for b in B]

# whole grid 
block = cross(rows,buildings)

# column and rows
block_list = ([cross(rows,b)for b in buildings] +
              [cross(r, buildings) for r in rows])

bl = dict((x,[i for i in block_list if x in i])for x in block)

#assigning cell to the respective cells in its row and columns
peers = dict((x, set(sum(bl[x],[]))-set([x]))for x in block)

def test():
    assert len(block) == 36
    assert all(len(bl[a]) == 2 for a in block)
    assert all(len(peers[a]) == 10 for a in block)
    print("passed all the tests")
 
test()