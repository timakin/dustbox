#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tanimoto係数。 A,Bという2つの集合のアイテムの類似度を示す。
# Cは共通集合を示している。クラスタリングされた集合の類似度を示している。

def tanimoto(a,b):
	c=[v for v in a if v in b]
	return float(len(c))/(len(a)+len(b)+len(c))