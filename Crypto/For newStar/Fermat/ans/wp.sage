```python
import libnum
import gmpy2
c = 383052269071505715385426447597196676856924726725478163487677165040606626542840080924029065393943685167200896505822900250494682411209678863720009813992997220773358713797950348313354147839796786462200908428907452080449548989585985103436234778067827406547672616147026309842632519658125941227723665861912785836003661294063297259828689195284280036687908398513165267747288259573388280191403059377374338824475973886240203130725501894468921700924970377424725928891207410
p = 7264567378475393766316470462064630719112846305467513125951873700238924329014777781033538845143365434787519844906892985236426336124932507682572493841285399
N = 437798123078174598319613761875825658493067512637019651515472612621832475078833810510091083993398185830506825646488751300665884159495701386727289892902796636782353039618627937772822062984937753266299423667823571684101962138037247284940818056634463997870665725795236372845178238171252613218559204572128001093968287074149821161941562341679383355930515089185101472087349085252872558393423883916873365081672558534529430248788464012358583949206529395057372875744810521
e=65537
P=pow(p,2)

while True:
    if isPrime(int(P)):
        break
    P=P+1
    
Q=N/P

assert(isPrime(int(P)))
assert(isPrime(int(Q)))

phi=(int(P)-1)*(int(Q)-1)
d=gmpy2.invert(gmpy2.mpz(e),gmpy2.mpz(phi))
m=pow(c,d,N)
print(long_to_bytes(int(m)))
```

