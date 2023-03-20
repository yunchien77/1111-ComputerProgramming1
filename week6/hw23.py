"""
公元年分非4的倍數，為平年(normal year)。
公元年分為4的倍數但非100的倍數，為閏年(leap year)。
公元年分為100的倍數但非400的倍數，為平年。
公元年分為400的倍數為閏年。

例如N = 5時：
輸入為：
5
1987
1988
1990
1991
1992

輸出為：
1987 is normal year.
1988 is leap year.
1990 is normal year.
1991 is normal year.
1992 is leap year.
----------------------------------------------------------------------------

輸入說明:
第一行輸入N個年份 (1 <= N <= 10)。
接下來N行，每行皆輸入年份Y (1 <= Y <= 10000)。

輸出說明:
依照輸入的N值，輸入N個年份，並且根據輸入的年份，判斷閏年或是平年。

"""

n = int(input())
year_list = []
for i in range(n):
    year = int(input())
    year_list.append(year)

for i in year_list:
    if (i % 4 != 0):
        print(i, 'is normal year.')
    elif (i % 4 == 0) and (i % 100 != 0):
        print(i, 'is leap year.')
    elif (i % 100 == 0) and (i % 400 != 0):
        print(i, 'is normal year.')
    elif (i % 400 == 0):
        print(i, 'is leap year.')
        