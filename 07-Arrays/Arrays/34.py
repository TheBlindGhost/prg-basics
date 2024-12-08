def identity_matrix(n):
    arr = []

    for i in range (n):
        row = []
        arr.append(row)
        for j in range (n):
            if i == j:
                row.append (1)
            else:
                row.append (0)
            
    
    
    
    
    
    return arr



print(identity_matrix(5))