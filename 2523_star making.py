
# coding: utf-8

# In[87]:


x = int(input());
cnt = x;


# In[88]:


for i in range (0, 2*x-1):
    if i+1>x :
        cnt -= 1;
    else:
        cnt = i;
    for j in range(0, cnt+1):
        print("*", end='');
    print();

