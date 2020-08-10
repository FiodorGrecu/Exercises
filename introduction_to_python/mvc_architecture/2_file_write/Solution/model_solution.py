def create(file_name):
    open(f'{file_name}.txt','w')
    return 

def write(file,content):
    with open(f'{file}.txt','a') as f:
        f.write(content)
    return 

def read(file):
    with open(f'{file}.txt','r') as f:
        data = f.read()
    return data