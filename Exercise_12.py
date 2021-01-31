d={'id':4,'name':'abc','age':22,'place':'xyz'}
print("DICTIONARY=",d)
asc=dict(sorted(d.items()))
des=dict(sorted(d.items(),reverse=True))
print("Ascending order=",asc)
print("Descending order=",des)