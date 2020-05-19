'''
Simple script used to translate somethling like 
      DIMENSION XEN(163),YELM(163),YELT(163),YEPS(163),
     /XVBV4(11),YVBV4(11),XVBV1(11),YVBV1(11),XVBV3(11),YVBV3(11),
     /XVIB5(12),YVIB5(12),XVIB6(12),YVIB6(12),
     /XTR1(12),YTR1(12),XTR2(11),YTR2(11),XTR3(11),YTR3(11),
     /XCF3(37),YCF3(37),XCF2(31),YCF2(31),XCF1(28),YCF1(28),XCF32(25),
     /YCF32(25),XCF0(27),YCF0(27),XC0F(27),YC0F(27),XCF22(25),YCF22(25),
     /XCF(22),YCF(22),XCFF(24),YCFF(24),XCF2F(25),YCF2F(25),
     /XCF3F(26),YCF3F(26),XATT(11),YATT(11),
     /XKSHC(81),YKSHC(81),XKSHF(79),YKSHF(79),IOFFN(46),IOFFION(12)
      DIMENSION Z6T(25),Z9T(25),EBRM(25)

	  to 

	 XEN[163],YELM[163]...

Which makes it eaiser to setup the needed arraies for the gas function. 

Make sure to take the DIMENSION word out of the input first.
'''

import sys
for line in sys.stdin:
	line = line.replace('/','')
	line = line.replace('\n','')
	l = line.split(',')
	line = line.replace('(','[')
	line = line.replace(')',']')
	print(line)


