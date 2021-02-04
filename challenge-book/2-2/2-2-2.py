#Saruman's Army P47
N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]


def main():
    # sort[X]
    i = 0
    ans = 0
    while i < N:
        #Sはカバーされていない一番左の点
        s = X[i+1]
        #Sは距離Rを超えるまで右に行く
        while i < N and X[i] <= s + R:
            i = i + 1
        #PはSからRを超えない一番右の点
        p = X[i-1]
        while i < N and X[i] <= p + R:
            i = i + 1
        ans += 1
    
    print(ans)
