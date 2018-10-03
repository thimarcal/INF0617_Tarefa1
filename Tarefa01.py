import os, time, string

os.chdir('D:\\Thiago\\Studies\\Unicamp\\MDC\\INF-617\\Tarefas\\INF0617_Tarefa1')

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


def proc_pool():
    start_time = time.time()
    pool = Pool(processes=16)
    pool.map(processar, filenames)
    pool.close()
    pool.join()
    end_time = time.time()

    return end_time-start_time


if __name__ == '__main__':
    from multiprocessing import Process
    from multiprocessing import Pool

    print("Processamento Serial", proc_serial())
    print("Processamento Paralelo", proc_paralelo())
    print("Processamento em Pool", proc_pool())

