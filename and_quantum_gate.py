#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:53:28 2023

@author: abdullahalshihry
"""

import qiskit as qs

qr = qs.QuantumRegister(3, 'Q')
cr = qs.ClassicalRegister(1, 'c')

def and_gate():
    
    qu0 = [0,1]
    qu1 = [0,1]
    for q0 in qu0:
        qc = qs.QuantumCircuit(qr,cr)
        for q1 in qu1:
            if q0 == 1 and q1 == 1:
                qc.x(qr[0])
                qc.x(qr[1])
                
            elif q0 == 1 and q1 == 0:
                qc.x(qr[0])
                
            elif q0 == 0 and q1 == 1:
                qc.x(qr[1])
            
            
            qc.barrier(qr[0])
            qc.barrier(qr[1])
            qc.ccx(0,1,2)
            qc.measure(2,0)
            qc.draw('mpl')
            
            job1 = qs.execute(qc, qs.Aer.get_backend('aer_simulator'), shots = 1024)
            output1 = job1.result().get_counts()
            print(f"{q0} {q1} : {output1}")
            qc = qs.QuantumCircuit(qr,cr)

and_gate()
    
