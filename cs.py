l, w = 3, 4
constantsum = l*(w-1)//2

D=[[0 for i in range(l*(w-1)+1)] for j in range(l+1)]
D[0][0]=1
for i in range(l+1):
    for j in range(l*(w-1)+1):
        for k in range(w):
            if j>=k:
                D[i][j]+=D[i-1][j-k]

print(D)


def encode(x):
    c=[0 for i in range(l)] 
    # c is 0-based, which means we use c_0, c_1 ... instead of c_1 , c_2 ...
    s=l*(w-1)//2
    for i in range(l,0,-1):
        for j in range(0,min(w-1,s)+1):
            if x>=D[i-1][s-j]:
                x-=D[i-1][s-j]
            else:
                c[i-1]=j #
                break
        s-=c[i-1]
    return c

print('encode(4) is ',encode(4))

for i in range(D[3][4]):
    print('encode({}) is'.format(i), encode(i))


chain1=[[i] for i in range(w)]
chains=[chain1]

def next_chain(chains):
    new_chains=[]
    for chain in chains:
        t=len(chain)
        k=min(w-1,t-1)
        for j in range(k+1):
            c=[]
            for i in range(t-j):
                c.append(chain[i]+[j])
            for i in range(j+1,w):
                c.append(chain[t-j-1]+[i])
            new_chains.append(c)
    return new_chains
            
def print_chains(chains):
    for chain in chains:
        print(chain)
    print()
print_chains(chains)
for i in range(2,l+1):
    new_chains=next_chain(chains)
    print_chains(new_chains)
    chains=new_chains
