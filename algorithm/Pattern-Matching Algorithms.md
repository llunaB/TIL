# Pattern-Matching Algorithms

## Brute Force

<img src="Pattern-Matching Algorithms.assets/image-20210817112349370.png">

```python
T = input()
P = input()

def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)   # introduce convinient notations
    for i in range(n-m+1):  # try every potential stating index within T
        k = 0               # an index into pattern P
        while k < m and T[i+k] == P[k]: # kth character of P matches
            k += 1
        if k == m:          # if we reached the end of pattern,
            return i        # substring T[i:i+m] matches P
    return -1               # failed to find a match string with any i   
 
# 주석 없이
def find_brute(T, P):
    n, m = len(T), len(P)   
    for i in range(n-m+1):
        k = 0               
        while k < m and T[i+k] == P[k]: 
            k += 1
        if k == m:          
            return i        
    return -1     
```

