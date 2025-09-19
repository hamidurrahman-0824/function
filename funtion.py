def fibonacci(t):
    if t <=0:
        return []
    if t == 1:
        return[0]
    if t == 2:
        return [0,1]
    fibo_serie = [0,1]
    if t >2:
        for _ in range(3,t+1):
            fibo_serie.append(fibo_serie[-1] + fibo_serie[-2])
    return fibo_serie
print(fibonacci(6))
def fact(s):
    if s <0 :
        return None
    return 1 if s==0 else s*fact(s-1)
print(fact(9))
def praaim(m):
    if m <=0 or m ==1 or m%2 ==0:
        return None
    if m == 2:
        return True
    for n in range(3,int(m**0.5)+1, 2):
        if m % n == 0:
            return False
    return True
print(praaim(911))