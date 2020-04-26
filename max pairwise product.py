
# coding: utf-8

# In[ ]:


def max_pairwise_product2 (a):
        global p,k
        p=a[0]
        k=0
    
        for i in range(len(a)):
            if p<a[i]:
                p=a[i]
                k=i
        #print(p)
        a1=p
        a[k]=a[k-1]
        p=a[0]
        k=0
        for i in range(len(a)):
            if p<a[i]:
                p=a[i]
                k=i
        #print(p)
        a2=p
        ans=a1*a2
        return (ans)

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product2(input_numbers))

