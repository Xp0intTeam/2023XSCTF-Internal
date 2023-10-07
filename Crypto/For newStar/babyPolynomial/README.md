- **题目名称：** babyPolynomial
- **题目类型：** Crypto
- **题目难度：**简单
- **出题人：** =w=
- **考点：**

1. 拉格朗日插值的简单应用

- **描述：** 您认识这种多项式吗？
- **flag：** flag{f5115f27-bb41-49c0-b84d-97cc2d8024b921a83029-8dd0-4f9e-a723-c9c9641e456a}
- **Writeup：**

## 题目代码解析
对于 $i\in [1,n]$

get_coeff 函数的功能为：给定一组数 $x_i=ID_i$，构造它们的**拉格朗日插值基函数$f_i(x)$**，并将多项式的系数全部返回

$\begin{aligned}f_i(x)&=\prod_{j=1,j\neq i}^n\frac{x-x_j}{x_i-x_j}=\sum_{j=0}^{n-1}a_{i,j}x^j modp \end{aligned}$

对于基函数，易得出如下性质

$\left.f_i(x_j)=\left\{\begin{matrix}1&i=j\\0&i\neq j\end{matrix}\right.\right.$

然后计算一组 $Q_i$ 作为输出，此处需注意公式下标

$Q_i=\sum^n_{j=1}a_{j,i-1}A_j$

task1 和 task2 的目标都是求出 $A_1$，区别在于给出的 $ID$ 的数量，task1 全给了，task2 只给了一个 $ID_1$，如果你能直接解出 task2，那你肯定能解出 task1，反过来就不一定咯

## 题解
对于 task1，由于给了所有的 $ID$，那可以照葫芦画瓢把所有的多项式系数 $a_{i,j}$ 算出来，接着对于 $A$ 的计算就可以变成解线性方程组，刚好10个未知数，10个式子，写成下面的矩阵形式，sage 跑一下就解出来了

$$
\begin{pmatrix}
 a_{1,0} & a_{2,0} & ... & a_{n,0}\\
 a_{1,1} & a_{2,1} & ... & a_{n,1}\\
 ... & ... & ... & ..\\
 a_{1,n-1} & a_{2,n-1} & ... & a_{n,n-1}
\end{pmatrix}
\begin{pmatrix}
 A_1\\
 A_2\\
 ... \\
 A_n
\end{pmatrix}
=
\begin{pmatrix}
 Q_1\\
 Q_2\\
 ... \\
 Q_n
\end{pmatrix}
$$

对于 task2，没有那么多关系给你构造方程组了。值得注意的是，我们还没有用到基函数的性质，重点就在这里。仔细体会下面的式子就能解出来了，从下往上看是推出式子的思路，从上往下看是证明 $Q=A_i$ 的过程，这个做法不需要再计算多项式系数，而且只需要一个 $x_i =ID_i$ 就能拿到对应的 $A_i$

$$
\begin{aligned}
    Q &= Q_1+x_iQ_2+x_i^2Q_3+...+x_i^{n-1}Q_n \\
      &= (a_{1,0}A_1+a_{2,0}A_2+...+a_{n,0}A_n) \\
      &+ x_i(a_{1,1}A_1 a_{2,1}A_2+...+a_{n,1}A_n)+...\\&+x_i^{n-1}(a_{1,n-1}A_1 +a_{2,n-1}A_2+...+a_{n,n-1}A_n)  \\
      &= (a_{1,0}+a_{1,1}x_i+a_{1,2}x_i^2+...+a_{1,n-1}x_i^{n-1})A_1 \\
      &+ (a_{2,0}+a_{2,1}x_i+a_{2,2}x_i^2+...+a_{2,n-1}x_i^{n-1})A_2+... \\&+(a_{n,0}+a_{n,1}x_i+a_{n,2}x_i^2+...+a_{n,n-1}x_i^{n-1})A_n\\
      &= f_1(x_i)A_1+f_2(x_i)A_2+...+f_n(x_i)A_n\\
      &=A_i
\end{aligned}
$$


```python
from Crypto.Util.number import *

IDs_1 = []
IDs_2 = []
p1 = 
p2 = 
Q1 = []
Q2 = []

def get_coeff(IDs, p):
    a = []
    R.<x> = Zmod(p)[]
    for x_i in IDs: 
        f_i = 1
        for x_j in IDs:
            if x_j != x_i:
                f_i *= (x-x_j)/(x_i-x_j)
        a.append(f_i.coefficients(sparse=False))
    return a

def solve(Q, IDs, p):
    n = len(IDs)
    if(n!=1):
        a = get_coeff(IDs, p)
        A = matrix(Zmod(p),n,n,a).transpose()
        B = matrix(Zmod(p),n,Q)
        X = A.solve_right(B)
        return int(X[0][0])
    x = IDs[0]
    Q_prime = 0
    for i in range(10):
        Q_prime += pow(x,i,p)*Q[i]%p
    return int(Q_prime)

res1 = solve(Q1, IDs_1, p1)
res2 = solve(Q2, [IDs_2[0]], p2)

res = b"flag{" + long_to_bytes(res1)+long_to_bytes(res2) + b"}"
print(res)
```
