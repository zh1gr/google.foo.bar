def sol(l):
	return sorted(l, key=lambda l:[int(i) for i in l.split('.')])


data = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

print(sol(data))