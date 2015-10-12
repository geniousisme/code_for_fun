## Bit Operation

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
my own way:
a = a^b
b = a^b
a = a^b
```

5. is a integer odd or even?
```python
def is_odd(num):
     return num % 2 == 1

def is_odd(num):
     return (num & 1) == 1
```

6. change positive integer to negative
```python
def negative(num):
     return num * -1

def negative(num):
     return ~num + 1 # so called
```