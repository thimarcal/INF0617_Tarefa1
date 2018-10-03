import os, time, string

os.chdir('D:\\Thiago\\Studies\\Unicamp\\MDC\\INF-617\\Tarefas\\INF0617_Tarefa1')
#print (os.getcwd())

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

    print ("File:", filename, "Letter", CHARACTERS[total.index(max(total))])

"""
    Processamento Serial
"""
def proc_serial():

    start_time = time.time()
    for filename in filenames:
        processar(filename)
    end_time = time.time()
    print("Processamento serial", end_time-start_time)


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
    print("Processamento paralelo", end_time-start_time)


def processar_pool(filename):
    f = open('./txt/'+filename, encoding='utf-8', errors='ignore')
    contents = f.read().lower()
    f.close()

    total = []
    for position, character in enumerate(CHARACTERS):
        total.append(contents.count(str(character)))
    print("File", filename, "Max char", CHARACTERS[total.index(max(total))])


def proc_pool():
    start_time = time.time()
    pool = Pool(processes=16)
    pool.map(processar_pool, filenames)
    pool.close()
    pool.join()
    end_time = time.time()

    print("Processamento pool", end_time-start_time)


if __name__ == '__main__':
    from multiprocessing import Process
    from multiprocessing import Pool

    proc_serial()
    proc_paralelo()
    proc_pool()

