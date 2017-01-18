#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# @author becxer
# @email becxer87@gmail.com
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def space_2(char):
    if char == ' ': return '  '
    else : return char

def ErrorDistance(ref, trg):
    ref = '#' + ref
    trg = '#' + trg
    lref = len(ref)
    ltrg = len(trg)
    dp = [[0 for j in range(lref)] for i in range(ltrg)]
    dpf = [[ None for j in range(lref)] for i in range(ltrg)]
    for i in range(ltrg):
        for j in range(lref):
            min_edit = 999999999
            if j > 0 and dp[i][j-1] < min_edit and ref[j] != trg[i]:
                dpf[i][j] = 'I'
                min_edit = dp[i][j-1]
            if i > 0 and dp[i-1][j] < min_edit and ref[j] != trg[i]:
                dpf[i][j] = 'D'
                min_edit = dp[i-1][j]
            if i > 0 and j > 0 and (dp[i-1][j-1] < min_edit or ref[j] == trg[i]):
                dpf[i][j] = 'S'
                min_edit = dp[i-1][j-1]
            if i != 0 or j != 0:
                dp[i][j] = min_edit
            if ref[j] != trg[i]:
                dp[i][j] += 1
    fromer = dpf[ltrg-1][lref-1]
    alref = ''
    altrg = ''
    rdx = lref-1
    tdx = ltrg-1
    while(fromer != None):
        if fromer == 'S':
            alref = space_2(ref[rdx]) + alref
            altrg = space_2(trg[tdx]) + altrg
            rdx -= 1 ; tdx -= 1
        elif fromer == 'D' :
            alref = '  ' + alref
            altrg = space_2(trg[tdx]) + altrg
            tdx -= 1
        elif fromer == 'I' :
            alref = space_2(ref[rdx]) + alref
            altrg = '  ' + altrg
            rdx -= 1
        fromer = dpf[tdx][rdx]
    return dp[ltrg-1][lref-1], alref, altrg

if len(sys.argv) < 3:
    print("Usage : WER.py reference.txt target.txt")
    sys.exit()

arr_ref = open(sys.argv[1]).read().split("\n") ; arr_ref.pop()
arr_trg = open(sys.argv[2]).read().split("\n") ; arr_trg.pop()
if len(arr_ref) != len(arr_trg):
    print("Error : Reference and Target are not parallel")
    sys.exit()

total_wer = 0
total_dist = 0
total_same = 0
for idx in range(len(arr_ref)):
    print ("----------------------------------------------------")
    _refer = unicode(arr_ref[idx]).strip()
    _trg = unicode(arr_trg[idx]).strip()
    dist, al_ref, al_trg = ErrorDistance(_refer,_trg)
    wer = float(dist) / float(len(_refer))
    print ('REF : ' + str(al_ref) + " (" + str(len(_refer)) + ")")
    print ('TRG : ' + str(al_trg) + " (" + str(len(_trg)) + ")")
    print ('ED : ' + str(dist))
    print ('WER : ' + str(wer))
    if dist == 0 : total_same += 1
    total_dist += dist
    total_wer += wer

print("===========================================================")
print("Average ED : " + str(float(total_dist) / float(len(arr_ref))))
print("Average WER : " + str(float(total_wer) / float(len(arr_ref))))
print("Average ERR : " + str((float(len(arr_ref)) - float(total_same)) / float(len(arr_ref))))
