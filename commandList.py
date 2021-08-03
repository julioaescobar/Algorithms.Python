if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(0,N):
        line = input()
        lines = line.split(" ")
        command = lines[0]
        parameters = lines[1:]
        if command !="print":
            command += "("+ ",".join(parameters) +")"
            eval("l."+command)
        else:
            print(l)