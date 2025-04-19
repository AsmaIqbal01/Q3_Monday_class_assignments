import time
print("waiting for 2 seconds....:")
time.sleep(2)
print("Done!")

start=time.time()
for i in range(10):
    print("Going through loop! ")

end=time.time()
print(f"time taken: {end - start} seconds")