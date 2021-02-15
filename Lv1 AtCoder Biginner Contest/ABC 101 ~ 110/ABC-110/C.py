s,t=[sorted(t.count(s)for s in set(t))for t in[input(),input()]]
print('YNeos'[s!=t::2])