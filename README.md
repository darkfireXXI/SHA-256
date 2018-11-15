# SHA-256
Building SHA-256 hashing algorithm from scratch

## The Short Cut
Fortunately, you don't have to do this as you can import hashlib and in two lines do all the work:  
text = input()  
digest = hashlib.sha256(('text').encode('utf-8')).hexdigest()

## The Long Cut
Write it from scratch for fun! See Hashing.py

## Choose Function Error
A quick run of the file reveals the script does not produce the correct digests. Using [this video](https://www.youtube.com/watch?v=mbekM2ErHfM) as a reference I was able to find the cause of the error in the Choose Function  
  
f(e,f,g) = (e and f) xor (not e and g)  

written in Python as  
  
ch = (int(e, 2) & int(f, 2)) ^ ((~int(e, 2)) & int(g, 2))  
  
taking e, f, and g as the initial constants in binary and converting them to integers.  

Despite my best efforts I have yet to resolve the issue with this line of code and one can see the error in the Choose Function output here where the h, S1, ch, k(0), w(i) values in binary alongside those correcty output from the video above:
![](https://github.com/darkfireXXI/SHA-256/blob/Image/ChooseFunctionProblem.jpg)
