#11966 2의 제곱인가
*l,=[2**i for i in range(31)];print('1'if int(input())in l else'0')
#02
print('1'if int(input())in[2**i for i in range(31)]else'0')
#03
print('0'if'1'in bin(int(input()))[3:]else'1')
#04 by hoyasmh
print(int(bin(int(input())).count('1')==1))
