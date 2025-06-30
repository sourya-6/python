tp = (10,30,"hey","sourya")
tp2 =('a','chai',40)
print(tp)
print(tp[1*3])
tp+tp2
# (10, 30, 'hey', 'sourya', 'a', 'chai', 40)
tp
# (10, 30, 'hey', 'sourya')
tp2 = tp+tp2
# (10, 30, 'hey', 'sourya', 'a', 'chai', 40)

"""Checking data type"""
tp =("apple")
type(tp)
# <class 'str'>
tp = ("apple",)
type(tp)
# <class 'tuple'>

"""Converting a Tuple into a list"""
tp = (10,30,"hey","sourya")
li = list(tp)
li[0]=20
# [20, 30, 'hey', 'sourya']