#-*-coding=utf-8-*-
import os
# �г�ĳ���ļ����µ����� case, �����õ��� python
# ���� py �ļ�����һ�κ������һ�� pyc �ĸ���
caselist=os.listdir('F:\\workspace\\hola world\\selenium\\test_case')
for a in caselist:
	s=a.split('.')[1]	# ѡȡ��׺��Ϊ py ���ļ�
	if s=='py':
		# �˴�ִ�� dos �����������浽 log.txt
		os.system('F:\\workspace\\hola world\\selenium\\test_case\\%s 1>>log.txt 2>&1'%a)
