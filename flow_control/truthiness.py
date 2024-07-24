print(3 and 'foo')   # last evaluated op: 'foo'
print('foo' and 3)   # last evaluated op: 3
print(0 and 'foo')   # last evaluated op: 0
print('foo' and 0)   # last evaluated op: 0

print(3 or 'foo')    # last evaluated op: 3
print('foo' or 3)    # last evaluated op: 'foo'
print(0 or 'foo')    # last evaluated op: 'foo'
print('foo' or 0)    # last evaluated op: 'foo'
print('' or 0)       # last evaluated op: 0
print(None or [])    # last evaluated op: []