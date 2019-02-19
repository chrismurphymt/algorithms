#set up array and indices
x = [9,1,7,8,2,5,4,3]
x_sort = sorted(x)
i = 2
j = 4


#1.
index = x_sort.index(x[i])
print(index)

#2.
def probability_of_comparison(x,x_sort,i,j):
    r_i = x_sort.index(x[i])
    r_j = x_sort.index(x[j])
    ans = 2.0/(abs(r_j-r_i)+1)
    return ans

print("prob of compariston: " , probability_of_comparison(x,x_sort,i,j))

#3 2
def total_expected_comparisons(x,x_sort):

    prob = 0.0
    for ii in range(len(x)):
        for jj in range(ii+1, len(x)):

            prob += probability_of_comparison(x,x_sort,ii,jj)

    return prob

print("expected total executions ", total_expected_comparisons(x,x_sort))


#4.
def compute_expected_comarisons(i,j):
    print(i,j)
