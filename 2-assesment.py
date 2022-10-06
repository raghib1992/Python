# st = 'Print only the words that start with s in this sentence'
# print(st.split())

# sw = [s for s in st.split() if s.startswith("s")]
# print(sw)
# t = ('Jawed', 'Israr', 'Zaman', 'Zaman')
# print(t[2])
# print(t.count('Zaman'))
# print(t.index('Israr'))


st = 'Print every word in this sentence that has an even number of letters'
sb = st.split()

for x in sb:
    if x.__len__() % 2 == 0:
        print("even")

