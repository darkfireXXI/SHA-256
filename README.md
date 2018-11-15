# SHA-256
Building SHA-256 hashing algorithm from scratch
[Wiki](https://en.wikipedia.org/wiki/SHA-2)

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

Despite my best efforts I have yet to resolve the issue with this line of code. One can see the error in the Choose Function output here where my h, S1, ch, k(0), w(i) values in binary are displayed alongside those correcty output in the video above:
![](https://github.com/darkfireXXI/SHA-256/blob/Image/ChooseFunctionProblem.jpg)

## Conclusion
Choose Function Error aside the algorithm works as it should. Overall it was a good excercise in coding as it requires a lot of numerical conversions (binary, hex, int) to do various operations and in the process one can understand and appreciate the simplicity/irreversibility of the one way algorithm.
