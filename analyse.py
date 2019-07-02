#encoding=utf-8
import os
import sys
import jieba
import jieba.posseg as pseg

jieba.load_userdict("dict/sku_dict.txt")
jieba.load_userdict("dict/brandname.dict")
jieba.load_userdict("dict/kouwei.dict")
jieba.load_userdict("dict/category_name.dict")

s="sf牌"
print s.find("牌")

base_sku_file = open('base_sku_20190701.txt')
base_sku_name_map={}
seg_map={}
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
    if len(cols)>6:
        sku_name = cols[4]
        if(sku_name_map.has_key(sku_name)):
            continue
        sku_name_map[sku_name]=1
        words = pseg.cut(sku_name)
        for word,flag in words:
            if(not seg_map2.has_key(word)):
                seg_map2[word] = []
            seg_map2[word].append(sku_name)

print "seg done!"     
#for sn in sku_name_map:
#    print sn

def find_lcsubstr(s1, s2): 
	m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)] 
	mmax=0
	p=0
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i]==s2[j]:
				m[i+1][j+1]=m[i][j]+1
				if m[i+1][j+1]>mmax:
					mmax=m[i+1][j+1]
					p=i+1
	return s1[p-mmax:p],mmax

def findCommon(str1,str2):
    #print "compare ",str1," ",str2
    cs,l = find_lcsubstr(str1,str2)
    if(l>=1):
        return 1,cs
    else:
        return 0,cs

handled_sku_map={}
for seg in seg_map2:
    sku_list = seg_map2[seg]
    if(seg_map.has_key(seg)):
        base_sku_list = seg_map[seg]
        for sn in sku_list:
            max_sku_name=""
            max_cnt = -1
            if(handled_sku_map.has_key(sn)):
                continue
            handled_sku_map[sn]=1
            words2 = pseg.cut(sn)
 
            for word2,flag2 in words2:
                print word2.encode('utf-8'),flag2,
            print

            for bsn in base_sku_list:
                #print bsn,sn
                #words = pseg.cut(bsn)
                words2 = pseg.cut(sn)
                print_flag = 0
               
                match_cnt=0
            	for word2,flag2 in words2:
                    words = pseg.cut(bsn)
                    for word,flag in words:
            	    #for word2,flag2 in words2:
                        if word==word2 and flag2.find('n')!=-1 and flag2!='eng' and word.encode('utf-8')!='牌':
                            #print word.encode('utf-8'),flag
                    	    print_flag=1
                        if word==word2:
                            #print word.encode('utf-8')
                            match_cnt=match_cnt+1
                #print match_cnt

                if(print_flag):
                    #print bsn,sn
                    if(match_cnt>max_cnt):
                        max_sku_name=bsn
                        max_cnt = match_cnt 
       	    if(max_cnt>0):    
                print "++++",sn,max_sku_name,str(max_cnt)    

'''
for bsn in base_sku_name_map:
    #print bsn,"++"
    for sn in sku_name_map:
        if(len(bsn)<len(sn)):
            continue
        #flag,cs = findCommon(bsn,sn)
        #if(flag):
            #print bsn,"|",sn
            #print cs
        words = pseg.cut(bsn)
        words2 = pseg.cut(sn)
            #for word,flag in words:
            #    print word.encode('utf-8'),flag,
            #print
            #for word,flag in words2:
            #    print word.encode('utf-8'), flag,
            #print
        common_words_cnt = 0
        for word,flag in words:
            for word2,flag2 in words2:
                #print word.encode('utf-8'),word2.encode('utf-8')
                if(word == word2):
                    common_words_cnt = common_words_cnt + 1
        if(common_words_cnt>1):
            print bsn,sn 
'''     
