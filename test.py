f = open('scores/high_score', 'r')
cool = list((f.read()).split('\n'))
def add(a):
    value=a.split(':')
    return value
new=list(map(add, cool))
print(new)