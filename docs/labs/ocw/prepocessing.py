input = open("dataset/data.dat","r").read().splitlines()
input = [item for item in input if len(item.split()) < 5]
input = "\n".join(input)
open("dataset/data_small.dat", "w").write(input)
output = open("dataset/truth.dat", "r").read().splitlines()
output = [item for item in output if len(item) < 5]
output = "\n".join(output)
open("dataset/truth_small.dat", "w").write(output)
print 0
