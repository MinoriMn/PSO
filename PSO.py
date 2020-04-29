#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import math


# In[13]:


class PSO:
    # N個体数, omega速度に対する重み, c1 pBest方向に対する重み, c2 gBest方向に対する重み, D入力次元数, up/lo_lim上限, func評価関数
    def __init__(self, N, omega, c1, c2, D, up_lim, lo_lim, func):
        if 0 <= omega and omega < 1:
            print("ωは0≦ω<1の範囲で設定してください")
            return
        if math.isclose(c1 + c2, 2.0 * omega + 2.0):
            print("c1 + c2 = 2ω + 2となるように設定してください")
            return
        
        self.N = N
        self.oemga = omega
        self.c1 = c1
        self.c2 = c2
        self.D = D
        self.up_lim = up_lim
        self.lo_lim = lo_lim
        self.func = func
    
    def init_phase(self, init_func = None):
        # 初期集団生成
        if init_func != None:
            [self.xs, self.vs] = init_func(self.up_lim, self.lo_lim)
        else:
            self.xs = np.array([])
            self.vs = np.array([])
            r_range = [(self.up_lim  - self.lo_lim) / 0.02, (self.up_lim - self.lo_lim) / 0.1] #速度ベクトルの半径の範囲
            for _ in range(N):
                r = random.uniform(*r_range)
                v = np.random.random(self.D) - 0.5
                l = np.linalg.norm(v)
                v = v / l * r
                np.append(self.vs, v.tolist())
                while True:
                    x = np.array([random.uniform(self.lo_lim, self.up_lim), random.uniform(self.lo_lim, self.up_lim)])
                    x_dash = x + v
                    if (x_dash[0] < self.up_lim) and (x_dash[0] > self.lo_lim) and (x_dash[1] < self.up_lim) and (x_dash[1] > self.lo_lim):
                        np.append(self.xs, x.tolist())
                        break
        # 評価値算出
        self.evaluations = [self.func(*x) for x in xs]
        
        #pbest初期化
        self.pb = np.copy(self.xs)
        
        #gbest初期化
        evaluation_min_val = min(self.evaluations)
        evaluation_min_idx = self.evaluations.index(evaluation_min_value)
        self.gb = self.pb[evaluation_min_idx]

    def solution_search_phase(self):
        pb_evaluations = []
        for i in range(self.N):
            #速度更新
            self.vs[i] = self.omega * self.vs[i] + self.c1 * random.random() * (self.pb[i] - self.xs[i]) + self.c2 * random.random() * (self.gb - self.xs[i])
            #位置更新
            self.xs[i] = self.xs[i] + self.vs[i]
            
            self.evaluations[i] = self.func(*self.xs[i])
            pb_evaluations.append(self.func(*self.pb[i]))
            if self.evaluations[i] < pb_evaluations[i]:
                self.pb[i] = self.xs[i]
                
        #gbest更新
        evaluation_min_val = min(pb_evaluations)
        evaluation_min_idx = pb_evaluations.index(evaluation_min_value)
        if pb_evaluations[evaluation_min_idx] < self.func(*self.gb):
            self.gb = self.pb[evaluation_min_idx]


# In[ ]:




