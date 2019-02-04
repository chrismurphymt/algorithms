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
    print("i_sort: ", r_i, " j_sort: ", r_j)
    prob = 0.0
    count = 0

    if r_i >= r_j:
        temp = r_i
        r_i = r_j
        r_j = temp
        print("i_sort: ", r_i, " j_sort: ", r_j)

    for ii in range(r_i,r_j):

        for jj in range(ii+1, r_j):
            ans = abs(jj-ii)+1
            print("ii: ", ii, " jj: ", jj, " ans: ", ans)

            prob += 2/ans
            count += 1


    print("prob: ", (prob/count))



probability_of_comparison(x,x_sort,i,j)


#3 2

#4.
def compute_expected_comarisons(i,j):
    print(i,j)
