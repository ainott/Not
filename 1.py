def matrix_chain_order(dimensions):

    p = [dimensions[0][0]] + [dim[1] for dim in dimensions]
    n = len(p) - 1
    
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    def construct_optimal_order(s, i, j):
        if i == j:
            return f"Matrix{i}"
        else:
            return f"({construct_optimal_order(s, i, s[i][j])} x {construct_optimal_order(s, s[i][j]+1, j)})"
    
    optimal_order = construct_optimal_order(s, 1, n)
    optimal_cost = m[1][n]
    
    return optimal_order, optimal_cost

# Example usage:
if __name__ == "__main__":
    dimensions = [[10, 20], [20, 65], [65, 45]]
    order, cost = matrix_chain_order(dimensions)
    print(f"The optimal order of matrix multiplication is: {order}")
    print(f"The minimum number of multiplications is: {cost}")
