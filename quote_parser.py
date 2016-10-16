with open('quote.txt', 'r') as f:
	content = f.readlines()
f.close()

cpy = []
dups = []
cnt = 0
with open('quote-revised.txt', 'w') as f:
	for c in content:
		if c.strip() == "":
			continue
		tokens = c.split('\t')
		txt = tokens[0].strip()
		if txt in cpy and txt not in dups:
			dups.append(txt)
			cnt += 1
		else:
			cpy.append(txt)
			f.write(tokens[0].strip() + '\t' + tokens[1].strip() + '\t' + tokens[2].strip() + '\t' + tokens[3].strip() + '\n')
f.close()

print len(dups)
print cnt
