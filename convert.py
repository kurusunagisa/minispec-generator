import sys
import os

def underline(s):
    i = 0
    while i < len(s):
        j = i
        if s[i] == '-':
            while 1:
                j += 1
                if s[j] == '-' or j == len(s) - 1:
                    break
            if j != len(s) - 1:
                s = s[0:i] + r"\underline{" + s[i+1:j] + "}" + s[j+1:]
            else:
                s = s[0:i] + r"\underline{" + s[i+1:j] + "}" + "\n"
            i = j
        i += 1
    return s

if __name__ == '__main__':
    name = sys.argv[1]
    now = 0
    with open(name,encoding='UTF-8') as f:
        with open(name + "-output.txt",'w',encoding='UTF-8') as g:
            g.write(r"\begin{enumerate}" + '\n')
            now = 0
            current0 = 0
            current1 = 0
            current2 = 0
            current3 = 0
            r = f.readlines()
            for i in r:
                """
                if '...' in i[0:3]:
                    if now > 3:
                        g.write(r"\end{enumerate}" + '\n')
                    if now == 2:
                        g.write(r"\begin{enumerate}[label=" + str(current0) + "." + str(current1) + "." + str(current2)  + "." + r"\arabic*]" + '\n')
                        current3 = 1
                    if now == 1:
                        g.write(r"\begin{enumerate}" + '\n')
                        g.write(r"\begin{enumerate}[label=" + str(current0) + "." + str(current1) + "." + str(current2)  + "." + r"\arabic*]" + '\n')
                        current3 = 0
                    now = 3
                    current3 += 1
                    g.write(r"\item " + i[3:])
                """
                if '..' in i[0:2]:
                    if now == 3:
                        g.write("            " + r"\end{enumerate}" + '\n')
                        current2 += 1
                    if now == 1:
                        g.write("        " + r"\begin{enumerate}[label=" + str(current0) + "." + str(current1) + "." + r"\arabic*]" + '\n')
                        current2 = 0
                    now = 2
                    current2 += 1
                    l = underline(i[2:])
                    g.write("            " + r"\item " + l)
                elif i[0] == '.':
                    if now == 2:
                        g.write("        " + r"\end{enumerate}" + '\n')
                    if now == 0:
                        g.write("    " + r"\begin{enumerate}[label=" + str(current0) + "." + r"\arabic*]"+ '\n')
                        current1 = 0
                    now = 1
                    l = underline(i[1:])
                    g.write("        " + r"\item " + l)
                    current1 += 1
                else:
                    if now == 2:
                        g.write("        " + r"\end{enumerate}" + '\n')
                        g.write("    " + r"\end{enumerate}" + '\n')
                    if now == 1:
                        g.write("    " + r"\end{enumerate}" + '\n')
                    now = 0
                    current0 += 1
                    l = underline(i)
                    g.write("    " + r"\item " + l)
            for i in range(now + 1):
                g.write("    " * (now - i))
                g.write(r"\end{enumerate}" + '\n')