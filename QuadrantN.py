
# coding: utf-8

# In[8]:


x = int(input());
y = int(input());


# In[9]:


if(x>0 and y>0):
    print(1);
elif(x<0 and y>0):
    print(2);
elif(x<0 and y<0):
    print(3);
else:
    print(4);

