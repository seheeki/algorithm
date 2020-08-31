
# coding: utf-8

# In[1]:


oxCnt = int(input());


# In[3]:


for i in range(0, oxCnt):
    scrCnt = 1;
    scr = 0;
    answer = input();
    
    for j in range(0, len(answer)):
        if answer[j]=='O':
            scr += scrCnt;
            if (j+1< len(answer)) and answer[j] == answer[j+1]:
                scrCnt+=1;
            else:
                scrCnt = 1;
        else:
            scrCnt = 1;
    print(scr);

