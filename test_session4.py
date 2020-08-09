# -*- coding: utf-8 -*-
"""
@author: Malay Patel
"""
import pytest
import random
import string
import session4
import os
import inspect
import re
import cmath

def test_tc02_1_Qualean_object():
    '''test -1<q<1, test data:0'''
    q=session4.Qualean(0)
    assert (q.value == 0), f"Your code returned wrong Qualean for 0,\n{q}"

def test_tc02_2_Qualean_object():
    '''test -1<q<1, test data:1,-1'''
    for input in [1,-1]:
        q=session4.Qualean(input)
        assert (q.value <= 1 and q.value >= -1), f"Your code returned wrong Qualean for {input},\n{q}"
        
def test_tc02_3_Qualean_object():
    '''test input is in [-1,0,1],test data:0.1'''
    with pytest.raises(ValueError):
        session4.Qualean(0.1)
def test_tc02_4_Qualean_object():
    '''test input is in [-1,0,1],data:-2'''        
    with pytest.raises(ValueError):
        session4.Qualean(-2)
def test_tc02_5_Qualean_object():
    '''test input is in [-1,0,1],data:3'''        
    with pytest.raises(ValueError):
        session4.Qualean(3)
def test_tc02_6_Qualean_object():
    '''test input is in [-1,0,1],data:'x'''        
    with pytest.raises(ValueError):
        session4.Qualean('x') 
def test_tc02_7_Qualean_object():
    '''test input is in [-1,0,1],data:1+2j'''        
    with pytest.raises(ValueError):
        session4.Qualean(1+2j)

def test_tc03_1_and():
    '''test q1 and q2 returns q1 if q1 is false'''
    q1=session4.Qualean(0)
    q2=session4.Qualean(1)
    assert(q1.__and__(q2)==0),f"q1 and q2 retruned incorrect value for q1 = 0"
def test_tc03_2_and():
    '''test q1 and q2 returns q2 if q1 is True'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert(q1.__and__(q2)==q2.value),f"q1 and q2 retruned incorrect value for q1 = {q1.value}"
def test_tc03_3_and():
    '''test q1 and n returns n if q1 is True,n is int'''
    q1=session4.Qualean(1)
    n=256
    assert(q1.__and__(n)==n),f"q1 and q2 retruned incorrect value for q1 = {q1.value} and q2 = {n}"
def test_tc03_4_and():
    '''test q1 and n returns n if q1 is True,n is complex'''
    q1=session4.Qualean(1)
    n=1+2j
    assert(q1.__and__(n)==n),f"q1 and q2 retruned incorrect value for q1 = {q1.value} and n = {n}"
def test_tc03_5_and():
    '''test q1 and n returns n_str if q1 is True,n_str is string'''
    q1=session4.Qualean(1)
    n_string="This is string"
    assert(q1.__and__(n_string)==n_string),f"q1 and q2 retruned incorrect value for q1 = {q1.value} and n_string = {n_string}"        

def test_tc04_1_or():
    '''test q1 or q2 returns q1 if q1 is True'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert(q1.__or__(q2)==q1.value),f"q1 or q2 retruned incorrect value for q1 = {q1}"
def test_tc04_2_or():
    '''test q1 or q2 returns q2 if q1 is false'''
    q1=session4.Qualean(0)
    q2=session4.Qualean(1)
    assert(q1.__or__(q2)==q2.value),f"q1 or q2 retruned incorrect value for q1 = {q1.value}"
def test_tc04_3_or():
    '''test q1 or n returns n if q1 is False,n is int'''
    q1=session4.Qualean(0)
    n=256
    assert(q1.__or__(n)==n),f"q1 or n retruned incorrect value for q1 = {q1.value} and q2 = {n}"
def test_tc04_4_or():
    '''test q1 or n returns n if q1 is False,n is complex'''
    q1=session4.Qualean(0)
    n=1+2j
    assert(q1.__or__(n)==n),f"q1 or n retruned incorrect value for q1 = {q1.value} and n = {n}"
def test_tc04_5_or():
    '''test q1 or n returns n_str if q1 is True,n_str is string'''
    q1=session4.Qualean(0)
    n_string="This is string"
    assert(q1.__or__(n_string)==n_string),f"q1 and q2 retruned incorrect value for q1 = {q1.value} and n_string = {n_string}"

def test_tc05_1_add():
    '''test q1+q2,test data q1 and q2 are Qualean'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    q3=q1+q2
    assert(q3.value==(q1.value+q2.value))
def test_tc05_2_add():
    '''test q1+n, n is int'''
    q1=session4.Qualean(1)
    n=125
    q3=q1+n
    assert(q3.value==(q1.value+n))
def test_tc05_3_add():
    '''test q1+n, n is float'''
    q1=session4.Qualean(1)
    n=2.5
    q3=q1+n
    assert(q3.value==(q1.value+n))
def test_tc05_4_add():
    '''test q1+n, n is complex'''
    q1=session4.Qualean(1)
    n=1+2j
    q3=q1+n
    assert(q3==(q1.value+n))
def test_tc05_5_add():
    '''test q + q + q ... 100 times = 100 * q'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(0)
    for i in range(100):
        q2=q1+q2
    assert(cmath.isclose(q2.value,q1.value*100,rel_tol=1e-10)),f"q1={q1.value} q2={q2.value}"
    
def test_tc06_1_mul():
    '''test q1*q2,test data q1,q2 are Qualean'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    q3=q1*q2
    assert(cmath.isclose(q3.value,q1.value*q2.value,rel_tol=1e-10,abs_tol=1e-10)),f"Multiplication of q1 and q2 is incorrect"
def test_tc06_2_mul():
    '''test q1*n,n is integer'''
    q1=session4.Qualean(1)
    n=2
    q3=q1*n
    assert(cmath.isclose(q3.value,q1.value*n,rel_tol=1e-10)),f"Multiplication of q1 and n is incorrect"
def test_tc06_3_mul():
    '''test q1*n,n is float'''
    q1=session4.Qualean(1)
    n=6.234
    q3=q1*n
    assert(cmath.isclose(q3.value,q1.value*n,rel_tol=1e-10)),f"Multiplication of q1 and n is incorrect"
def test_tc06_4_mul():
    '''test q1*n,n is complex'''
    q1=session4.Qualean(1)
    n=5+6j
    assert(cmath.isclose(q1*n,q1.value*n,rel_tol=1e-10)),f"Multiplication of q1 and n is incorrect"
    
def test_tc07_1_eq():
    '''test q1==q2,q1 and q2 are equal'''
    q1=session4.Qualean(0)
    q2=session4.Qualean(0)
    assert(q1==q2),f"Equality test Failed!"
def test_tc07_2_eq():
    '''test q1==q2,q1 and q2 are equal'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert(not(q1==q2)),f"Equality test Failed!"

def test_tc08_1_ge():
    '''test q1>=q2'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert((q1>=q2) == (q1.value>=q2.value)),f"ge test Failed!"
def test_tc09_1_le():
    '''test q1<=q2'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert((q1<=q2) == (q1.value<=q2.value)),f"le test Failed!"
def test_tc10_1_gt():
    '''test q1>q2'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert((q1>q2) == (q1.value>q2.value)),f"gt test Failed!"
def test_tc11_1_lt():
    '''test q1<=q2'''
    q1=session4.Qualean(1)
    q2=session4.Qualean(1)
    assert((q1<q2) == (q1.value<q2.value)),f"lt test Failed!"
def test_tc12_1_float():
    '''test __float__'''
    q1=session4.Qualean(1)
    assert(float(q1)==q1.value),f"__float__ returned incorrect value!"
def test_tc13_1_inversign():
    q1=session4.Qualean(1)
    assert(q1.__invertsign__()==(-q1.value)),f"__invertsign__ returned incorrect value!"
def test_tc14_1_sqrt():
    q1=session4.Qualean(1)
    q1_sqrt=q1.__sqrt__()
    if q1.value>=0:
        assert(cmath.isclose(q1_sqrt.value,cmath.sqrt(q1.value),rel_tol=1e-10)),f"Square root is incorrect!"
    else:
        assert(cmath.isclose(q1_sqrt,cmath.sqrt(q1.value),rel_tol=1e-10)),f"Square root is incorrect!"
def test_tc15_1_bool():
    q1=session4.Qualean(0)
    assert(bool(q1)==False),f"Bool is incorrect!"
def test_tc15_2_bool():
    q1=session4.Qualean(1)
    if q1.value!=0:
        assert(bool(q1)==True),f"Bool is incorrect!"
    else:
        assert(bool(q1)==False),f"Bool is incorrect!"