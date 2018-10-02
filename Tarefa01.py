
# coding: utf-8

# INF-0617 - Big Data
# Tarefa 01 - Contagem de Letras
# Professor: Lucas Wanner
# Alunos: Thiago Gomes Marçal Pereira

# In[4]:


import os, time, string
from multiprocessing import Process

os.chdir('/Users/thiagom/Documents/Studies/Unicamp/MDC/INF-617/Tarefas/01')
print (os.getcwd())


# In[6]:


filenames = []
for file in os.listdir('./txt'):
    if file.endswith(".txt"):
        filenames.append(file)

LETTERS = list(string.ascii_lowercase)
resultado = {}
        
def processar(filename): 
    f = open('./txt/'+filename, encoding='utf-8', errors='ignore')
    contents = f.read().lower()
    f.close()
    
    for position, letter in enumerate(LETTERS):
        contents.count(letter)


# In[ ]:


"""
    Processamento Serial
"""
start_time = time.time()
for filename in filenames:
    processar(filename)
end_time = time.time()
print("Processamento serial", end_time-start_time)


# In[ ]:


"""
    Processamento Paralelo
"""
processes = []
start_time = time.time()
for i in range(1,100):
    p = Process(target=processar, args=(filenames[i],))
    processes.append(p)
    p.start()
    
for p in processes:
    p.join()
end_time = time.time()
print("Processamento paralelo", end_time-start_time)

