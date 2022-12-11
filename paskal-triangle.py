N = 20

def paskal_triangle(N):
    P = []
    for i in range(N):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1] + P[i-1][j]
        P.append(row)
    return   P

# print(paskal_triangle(N))

if __name__ == "__main__":
    text = print(f"Pascal's triangle with depth {N} layers")
    for row in paskal_triangle(N):
        print(row)