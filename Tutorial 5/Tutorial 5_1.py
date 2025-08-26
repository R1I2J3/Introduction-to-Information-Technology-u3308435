name = "Rahman Joy"
name.split()
print("{0:s},{1:s}".format(name.split()[1],name.split()[0]))


tuple1 = ("course", "of", "human", "events", "when", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
alltogether = " ".join(tuple2)
print(alltogether)
