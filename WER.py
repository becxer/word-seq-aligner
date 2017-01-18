i#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def WER(ref, trg):
    ref = unicode(ref)
    trg = unicode(trg)
    lref = len(ref)
    ltrg = len(trg)
    dp = [[0 for j in range(ltrg)] for i in range(lref)]
    if ref[0] != trg[0]: dp[0][0] = 1
    for i in range(lref):
        for j in range(ltrg):
            min_edit = 999999999
            if j > 0 and dp[i][j-1] < min_edit:
                min_edit = dp[i][j-1]
            if i > 0 and dp[i-1][j] < min_edit:
                min_edit = dp[i-1][j]
            if i > 0 and j > 0 and dp[i-1][j-1] < min_edit:
                min_edit = dp[i-1][j-1]
            if i != 0 and j != 0:
                dp[i][j] = min_edit
            if ref[i] != trg[j]:
                dp[i][j] += 1
    return float(dp[lref-1][ltrg-1]) / float(lref)

if len(sys.argv) < 3:
    print("Usage : WER.py reference.txt target.txt")
    sys.exit()

arr_ref = open(sys.argv[1]).read().strip().split("\n")
arr_trg = open(sys.argv[2]).read().strip().split("\n")
if len(arr_ref) != len(arr_trg):
    print("Error : Reference and Target are not parallel")
    sys.exit()

total_ = 0
for idx in range(len(arr_ref)):
    _refer = arr_ref[idx]
    _trg = arr_trg[idx]
    wer_one = WER(_refer,_trg)
    total_ += wer_one
    print(str(_refer) + "\n" + str(_trg) + "\t" + "| WER : " + str(wer_one))

print("-----------------------------------------------------------")
print("Average  WER : " + str(float(total_) / float(len(arr_ref))))
