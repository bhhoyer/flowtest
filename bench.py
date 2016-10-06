import time

print "How many squares would you like to run?"
#z=input()
z=100000

start = time.time()
for x in range(0, z):
    y = float(x)/1.36592
end = time.time()
elapsed = (end - start)
#print elapsed
if elapsed < 1:
    elapsed=round(elapsed*1000,1)
    u=" msec"
else:
    elapsed=round(elapsed,2)
    u=" seconds"
print "Whew! computed ",z," squares in ",elapsed,u
