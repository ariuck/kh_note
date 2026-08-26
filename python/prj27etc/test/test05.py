# zip
names = ["홍길동","임꺽정","김철수"]
scores = [100,200,300]
height = [170,180,190]

result = zip(names,scores,height)
for n,s,h in result:
    print(f"{n} / {s} / {h}")

