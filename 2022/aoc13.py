import ast

def main():
    data = open("input13.txt","r",encoding="utf-8").read()
    signals = data.split("\n\n")
    signal = signals[0]
    
    def depth(l):
        if isinstance(l, list):
            return 1 + max(depth(item) for item in l)
        else:
            return 0
    
    s = 0
        #for signal in signals:
    print(signal)
    s1 = ast.literal_eval(signal.split("\n")[0])
    s2 = ast.literal_eval(signal.split("\n")[1])
    d = depth(s1)

    print(d)
    print(len(s1))
    print(len(s2))
    print(s1[0])
    print(s2[0])
main()