import os, time, string, sys

#os.chdir('D:\\Thiago\\Studies\\Unicamp\\MDC\\INF-617\\Tarefas\\INF0617_Tarefa1')
os.chdir('/Users/thiagom/Documents/Studies/Unicamp/MDC/INF-617/Tarefas/INF0617_Tarefa1')

if len(sys.argv) == 2: 
    shouldPrint = (str(sys.argv[1]) == True)
else:
    shouldPrint = False

filenames = []
for file in os.listdir('./txt'):
    if file.endswith(".txt"):
        filenames.append(file)

CHARACTERS = list(string.ascii_lowercase) + list(range(0,10))

        
def processar(filename):
    f = open('./txt/'+filename, encoding='utf-8', errors='ignore')
    contents = f.read().lower()
    f.close()
    
    total = []
    for position, character in enumerate(CHARACTERS):
        total.append(contents.count(str(character)))

    if shouldPrint:
        print ("File:", filename, "Letter", CHARACTERS[total.index(max(total))])

"""
    Processamento Serial
"""
def proc_serial():

    start_time = time.time()
    for filename in filenames:
        processar(filename)
    end_time = time.time()
    return end_time-start_time


"""
    Processamento Paralelo
"""
def proc_paralelo():
    processes = []
    start_time = time.time()
    for filename in filenames:
        p = Process(target=processar, args=(filename,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end_time = time.time()
    return end_time-start_time


def proc_pool(processes_number=16):
    start_time = time.time()
    pool = Pool(processes=processes_number)
    pool.map(processar, filenames)
    pool.close()
    pool.join()
    end_time = time.time()

    return end_time-start_time


if __name__ == '__main__':
    from multiprocessing import Process
    from multiprocessing import Pool

    processamento_serial = proc_serial()
    processamento_paralelo = proc_paralelo()
    processamento_pool = proc_pool(16)

    print("Processamento Serial", processamento_serial)
    print("Processamento Paralelo", processamento_paralelo)
    print("Processamento em Pool: ", processamento_pool)

