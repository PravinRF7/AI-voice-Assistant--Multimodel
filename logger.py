import datetime

def writehistory(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logfile = f'{timestamp}_log.txt'
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"{text}\n")
