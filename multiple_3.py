
# coding: utf-8

# In[8]:


x = int(input());
y = int(input());


# In[30]:


thirdY = int(y/100);
secondY = int((y-thirdY*100)/10);
firstY = y-secondY*10-thirdY*100;


# In[32]:


firstR = x*firstY;
secondR = x*secondY;
thirdR = x*thirdY;
result = firstR + secondR*10 + thirdR*100;
print(firstR);
print(secondR);
print(thirdR);
print(result);

