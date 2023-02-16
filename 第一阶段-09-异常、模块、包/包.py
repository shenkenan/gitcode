# import 第一阶段-my_bao.my_modo1
# import 第一阶段-my_bao.my_modo2

# 第一阶段-my_bao.my_modo1.testb(5, 3)
# 第一阶段-my_bao.my_modo2.testd(10, 2)

# from 第一阶段-my_bao import my_modo1
# from 第一阶段-my_bao import my_modo2
#
# my_modo1.testb(5, 3)
# my_modo2.testc(20, 10)

# from 第一阶段-my_bao.my_modo1 import testa
# from 第一阶段-my_bao.my_modo2 import testc
#
# testc(10, 20)
# testa(2, 3)
# import 第一阶段-my_bao.my_modo1

from my_bao import *
my_modo1.testa()
my_modo2.testd()