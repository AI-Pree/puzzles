
buildings = '123456' #skyscrapers size from 1 to 6
rows = "ABCDEF"

def cross(A:str,B:str)->list:
    return [a+b for a in A for b in B]

# whole grid 
block = cross(rows,buildings)

# column and rows
block_list = ([cross(rows,b)for b in buildings] +
              [cross(r, buildings) for r in rows])

#assigning cell to the respective cells in its row and columns
bl = dict((x,[i for i in block_list if x in i])for x in block)

#assigning cell to the respective peers in its row and columns
peers = dict((x, set(sum(bl[x],[]))-set([x]))for x in block)

#the grid for the skyscraper

#assign values
def assign(values,s,d):
    other_values = values[s].replace(d,'')
    if all(eliminate(values,s,d2) for d2 in other_values):
        return values
    else:
        return False

#eliminate values
def eliminate(values,s,d):
    if d not in values[s]:
        return values  #value is already eliminated here
    values[s] = values[s].replace(d,'') #eliminating the possibility of that number

    if len(values[s]) == 0:
        return False #removed last possible value
    
    elif len(values[s]) == 1:
        d2  = values[s]
        if not all(eliminate(values,s2,d2) for s2 in peers[s]):
            return False

    #putting the value if its the only possibility
    for b in bl[s]:
        bplaces = [i for i in b if d in values[i]]
        if len(bplaces) == 0:
            return False
        elif len(bplaces) == 1:
            if not assign(values,bplaces[0],d):
                return False
    return values

#----------some tests-----------------------------#
def test():
    assert len(block) == 36
    assert all(len(bl[a]) == 2 for a in block)
    assert all(len(peers[a]) == 10 for a in block)
    print("passed all the tests")
 
test()