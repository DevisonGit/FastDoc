import os

name = os.getenv('MY_NAME', 'world')
print(f'hello {name} from python')
