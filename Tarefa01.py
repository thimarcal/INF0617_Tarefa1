import os, time, string
from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Pool

os.chdir('/Users/thiagom/Documents/Studies/Unicamp/MDC/INF-617/Tarefas/INF0617_Tarefa1')
#print (os.getcwd())

filenames = []
for file in os.listdir('./txt'):
    if file.endswith(".txt"):
        filenames.append(file)

CHARACTERS = list(string.ascii_lowercase) + list(range(0,10))
# print (CHARACTERS)
        
def processar(filename, result): 
    f = open('./txt/'+filename, encoding='utf-8', errors='ignore')
    contents = f.read().lower()
    f.close()
    
    total = []
    for position, character in enumerate(CHARACTERS):
        total.append(contents.count(str(character)))
        #print ("Letra: ", character, "contagem:", total[position])
    result[filename] = CHARACTERS[total.index(max(total))]
    #print ("File:", filename, "Letter", CHARACTERS[total.index(max(total))])

"""
    Processamento Serial
"""
manager = Manager()
resultado_serial = manager.dict()
start_time = time.time()
for filename in filenames:
    processar(filename, resultado_serial)
end_time = time.time()
print("Processamento serial", end_time-start_time)
print(resultado_serial)


"""
    Processamento Paralelo
"""
processes = []
resultado_paralelo = manager.dict()
start_time = time.time()
for filename in filenames:
    p = Process(target=processar, args=(filename,resultado_paralelo))
    processes.append(p)
    p.start()
    
for p in processes:
    p.join()
end_time = time.time()
print("Processamento paralelo", end_time-start_time)
print(resultado_paralelo)


result_pool = manager.dict()
def processar_pool(filename): 
    f = open('./txt/'+filename, encoding='utf-8', errors='ignore')
    contents = f.read().lower()
    f.close()
    
    total = []
    for position, character in enumerate(CHARACTERS):
        total.append(contents.count(str(character)))
        #print ("Letra: ", character, "contagem:", total[position])
    result_pool[filename] = CHARACTERS[total.index(max(total))]

start_time = time.time()   
pool = Pool(processes=16)
pool.map(processar_pool, filenames)
pool.close()
pool.join()
end_time = time.time()

print("Processamento pool", end_time-start_time)
print(result_pool)