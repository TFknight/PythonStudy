1.txt 是训练集
2.txt 是验证集

CRF_wordtovec.py是取n维向量作为CRF的特征  ,并且将训练集,验证集的特征保存到文本
执行完CRF_wordtovec.py之后,在命令行执行  crf_learn -a MIRA -m 50 -p 20 -f 3 -c 4.0 template 3.txt w2v_model  (将CRF模型保存,训练样本是3.txt)
再在命令号执行 crf_test -m w2v_model 3vali.txt>3vali_result.txt (由CRF得出来的结果)
执行 get_goal.py ,得到最终的准确率
