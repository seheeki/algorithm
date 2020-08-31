
# coding: utf-8

# In[25]:


cnt = 0;
x = input(); 


# In[26]:


y = -1;
x2 = x;
str1 = 0;


# In[27]:


while int(x)!=int(y):
    cnt+=1;
    str1 = 0;
    for i in range(0, len(x2)):
        str1 += int(x2[i]);
    
    str2 = str(str1);
    y = x2[-1] + str2[-1]
    x2 = y;


# In[28]:


print(cnt);

