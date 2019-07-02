#encoding=utf-8
import os
import sys
import jieba
import jieba.posseg as pseg

jieba.load_userdict("sku_dict.txt")

base_sku_file = open('base_sku_20190701.txt')
base_sku_name_map={}
seg_map={}
seg_dict={}
for line in base_sku_file:
    line = line.strip()
    cols = line.split('\t')
    if len(cols)>2:
        sku_name = cols[1]
        if(base_sku_name_map.has_key(sku_name)):
            continue
        base_sku_name_map[sku_name]=1
        words = pseg.cut(sku_name)
        for word,flag in words:
            if(not seg_map.has_key(word)):
                seg_map[word] = []
            seg_map[word].append(sku_name)
            wf = word+"\t"+flag
            if(not seg_dict.has_key(wf)):
                seg_dict[wf] = 0    
            seg_dict[wf] = seg_dict[wf] + 1
            
            #    print word.encode('utf-8'),flag,

print "seg 1 done!"        
#for bsn in base_sku_name_map:
#    print bsn

sku_file = open('cpt_sku_20190630.txt')
sku_name_map={}
seg_map2={}
for line in sku_file:
    line = line.strip()
    cols = line.split('\t')
    i=0
    if len(cols)>6:
        #if(i>20):
        #    continue
        i=i+1
        sku_name = cols[4]
        if(sku_name_map.has_key(sku_name)):
            continue
        sku_name_map[sku_name]=1
        words = pseg.cut(sku_name)
        for word,flag in words:
            if(not seg_map2.has_key(word)):
                seg_map2[word] = []
            seg_map2[word].append(sku_name)
            wf = word+"\t"+flag
            if(not seg_dict.has_key(wf)):
                seg_dict[wf] = 0    
            seg_dict[wf] = seg_dict[wf] + 1
    
sorted_keys = sorted(seg_dict.items(),key=lambda item:item[1],reverse=True)
for key in sorted_keys:
    print key[0].encode('utf-8'),str(key[1])       


print "seg done!"     
