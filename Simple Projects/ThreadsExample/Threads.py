import time
from concurrent.futures import ThreadPoolExecutor



def askuser():
    start=time.time()
    a=input("Enter a number : ")
    print(f"Time taken  = {time.time() - start}")

def complexCal():
    start  = time.time()
    [x**2 for x in range(2000000)]
    print("Time taken for Complex calculation is %s" %(time.time() - start))


start = time.time()
askuser()
complexCal()
print("Time taken for whole program using single threads {}".format(time.time() - start))




start=time.time()
with ThreadPoolExecutor(max_workers=6) as pool:
    pool.submit(complexCal)
    pool.submit(askuser)

print(f"Time taken by 2 thread = {time.time() - start}")


