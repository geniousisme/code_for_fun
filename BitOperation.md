## Bit Operation

### Author: Chris Hsu

#### 1. X * 2 ^ n
ex.
```python
a = b * 128 (2 ^ 7)
a = b << 7
```

#### 2. X / 2 ^ n
ex.
```python
a = b / 128 (2 ^ 7)
a = b >> 7
```

#### 3. float to int(python doesn't work):
```c
int a;
float b;
a = b >> 0
```

#### 4. exchange two elements:
```python
a ^= b
b ^= a
a ^= b
```

```python
# my own way, eaiser to remember:
a = a^b
b = a^b
a = a^b
```

#### 5. is a integer odd or even?
```python
def is_odd(num):
     return num % 2 == 1

def is_odd(num):
     return (num & 1) == 1
```

#### 6. change positive integer to negative
```python
def negative(num):
     return num * -1

def negative(num):
     return ~num + 1 # so called "complement"
```

#### 7. get remainder of power of two
```python
def remainder(num, pow):
     return num / (2 ** pow)

def remainder(num, pow):
     return num & ((2 ** pow) - 1)
```
#### 8. is number power of two?
```python
def is_two_pow(num):
     return (-num & num) == num

# if return 1 => is power of 2
# else not
```

#### 9. incremental & decremental
```python
def incremental(num):
     return -~num

def decremental(num):
     return ~-num
```

#### 10. same sign or not?
```python
def is_same_sign(a, b):
     return a * b >= 0

def is_same_sign(a, b):
     return a ^ b >= 0
```

### reference:
http://kuoe0.logdown.com/posts/2012/01/26/utlization-of-bitwise-operation
http://edisonx.pixnet.net/blog/post/34033421-%E4%BD%8D%E5%85%83.%E7%A7%BB%E4%BD%8D%E9%81%8B%E7%AE%97%E5%AD%90


## Appendix: How Does Complement Work?
https://randle.wordpress.com/2013/01/29/why-twos-complement-works/
https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8





