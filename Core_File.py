```python
#ASCII
def encoder(text):
    encoder_text = ''
    for chr in text:
        if 'a'<=chr<= 'z':
            id_chr = (ord(chr)- ord('a') + 5) % 26 + ord('a')
            encoder_text += chr(id_chr)
        elif 'A'<=chr<= 'Z':
            id_chr = (ord(chr)- ord('A') + 5) % 26 + ord('A')
            encoder_text += chr(id_chr)
        else:
            encoder_text += chr
    return encoder_text

def decoder(text):
    decoder_text = ''
    for chr in text:
        if 'a'<=chr<= 'z':
            id_chr = (ord(chr)-ord('a') - 5) %26 + ord('a')
            decoder_text += chr(id_chr)
        elif 'A'<=chr<= 'Z':
            id_chr = (ord(chr)- ord('A') - 5) % 26 + ord('A')
            decoder_text += chr(id_chr)
        else:
            decoder_text += chr
    return decoder_text

#函数嵌套
def func(n):
    if n == 0:
        return 0
    else:
        return 2*func(n-1)+1
#try:
#    x = int(input('enter an integer'))
#except:
#    print('not an integer')
#else:
#    print(func(x))

#五舍六入问题
x = 4.6
y = int(x)
z = x*10-int(x)*10
#0.6转为二进制 -> 0.59999, 所以先*10，再算小数部分
if z < 0.6*10:
    x_int = y
else:
    x_int = y + 1
#print(x_int)

#单位转化
sec = 5120
sec_to_hour = 3600
h = sec//sec_to_hour
m = sec%sec_to_hour//60
s = sec - h*sec_to_hour - m*60
#print('%dhour%dmin%dsecond'%(h,m,s))

#字符串文本处理
poem = '潮随暗浪雪山倾，远浦渔舟钓月明。桥对寺门松径小，槛当泉眼石波清。迢迢绿树江天晓，霭霭红霞海日晴。遥望四边云接注水碧，峰千点数鸿轻。'
rev_poem =poem[::-1]
rev_poem = rev_poem.replace('，','\n')
rev_poem = rev_poem.replace('。','\n')
#print(rev_poem)

#四玫瑰数
def four_rose_number(number):
    a = number//1000
    b = number//100
    c = number//10
    d = number%10
    if a^4 +b^4 +c^4 + d^4 == number:
        return number
    else:
        return ''
result = []
for n in range(1000,10000):
    detection = 0
    for item in str(n):
        detection += int(item)**4
    if detection == n:
        result.append(n)
#print(result)
#取四位数的每一位可以借用字符串操作，int转str转int

a = [3]
a += [5]
#a += 5, 5 is not iterable
#print(a)

#数列找规律
def f(n):
    up = 2
    down = 1
    add = 0
    for i in range(n):
        add += up/down
        up += down
        down = up-down #
    return add
#print(f'{f(5):.6f}')

#字符串操作
text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''
n_lines = len(text.splitlines())
n_words = len(text.split())
n_char = len(text)
n_spaces = text.count(' ')

#数列迭代
def fibo_list(n):
    ans =[0,1]
    for i in range(2,n):
        item = ans[i-2] + ans[i-1]
        ans.append(item)
    return ans

#进制转化
def inversion(x,k):
    out = ''
    if k == 10:
        return str(x)
    elif k == 16:
        return loop_16(x)
    else:
        return loop_8_2(x,k)
def loop_16(x):
    out = ''
    if x == 0:
        return '0'
    while x >0:
        rem =  x % 16
        if rem<10:
            out = str(rem) + out
        else:
            out = chr(rem-10 + ord('A')) + out
            x //= 16
    return out

def loop_8_2(x,k):
    out = ''
    if x ==0:
        return '0'
    while x>0:
        rem = x%k
        out += str(rem)
        x //= k
    return out

#不用函数：
s =''
N = input('give a number')
while N>0:
    s = str(N%2) + s
    N = int(N/2)
#print(s)

#进制转换从高位到低位，先算出最高位是第几位，逻辑复杂
#从低位到高位取余，最后调转顺序，拼在后面： out = chr + out


#type detection
def type_detect(content):
    if type(content) is float:
        print('%.3f'%content)
    elif type(content) is int:
        if 100 <= content <1000:
            a,b,c = str(content)
            if content == int(a)**3 + int(b)**3 + int(c)**3:
                print(f'{content}是水仙花数')
            else:
                print(f'{content}不是水仙花数')
    elif type(content) is str:
        print(f'{content:*^10}')
    elif type(content) is list:
        print(tuple(content))
    else:
        print('NO PRINT!')
type_detect('python')
#type(x) is -> isinstance(x, type)
#type(True) is int #False
#isinstance(True,int) #True(bool 继承自 int)

#格式化
a = 'python'
b = 'a superlanguage'
#print('{:->10}:{:-<19}'.format(a,b))
#print(f'{a:->10}:{b:-<19}')

#循环求和
total = 0
x_list = []
for i in range(1,201):
    i_list = list(str(i))
    for p in range(len(i_list)):
        if i_list[p]=='3' and i not in x_list:
            total += i
            x_list.append(i)
 
#list operation
#列表运算有加分没有减法，
# pop(i)-索引,返回被删元素；remove(x)-第一个匹配值，返回None
#del ls[i]-index,删指定位置，无返回值

#异常处理关键字: try, except, finally, raise
def divide(a,b):
    try:
        result = a/b
        if result <0:
            raise ValueError('the result cannot be less than zero')
        return result
    except ZeroDivisionError:
        print('the divisor cannot be zero')
        return None
    except ValueError as e:
        print(f'wrong:{e}')
        return None
    except:
        print('undected error')
        return None
    finally:
        print('the operation ends')

#gcd & lcm
import math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b  #这一步不需要考虑a和b的大小关系
        return a
#gcd = math.gcd(a,b)

def lcm(a,b):
    return a*b // gcd(a,b)
#lcm = math.lcm(a,b)

#is_prime
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
```
