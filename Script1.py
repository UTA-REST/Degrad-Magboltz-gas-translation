import sys
'''
This simple script has two uses, the first one is to translate an array in the form of 
	  EIN(1)=-0.0539
      EIN(2)=0.0539
      EIN(3)=-0.0783                                                    
      EIN(4)=0.0783 
      EIN(5)=-0.1126                                                    
      EIN(6)=0.1126
      EIN(7)=-0.1588
      EIN(8)=0.1588                                                     
      EIN(9)=0.3176                                                     
      EIN(10)=0.4764
      EIN(11)=11.5
      EIN(12)=11.63
      EIN(13)=11.88
      EIN(14)=12.13
      EIN(15)=12.38
      EIN(16)=12.50
      EIN(17)=12.63
      EIN(18)=12.88
      EIN(19)=13.13
      EIN(20)=13.38

	  to the form of [-0.0539,0.0539...]

The second use is to translate the DATA array names to their corresponding python names. And grabing them from the npy file (gd file).

     it translates 
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

	  XEN = gd[/gasX/XEN]
	  .
	  .
	  .


	Make sure to change the X value to the corresponding Gas id or name
	Also make sure to remove the DIMENSIoN word from the fortran code input.
'''

for line in sys.stdin:
	# 1st usage.
	line = line.replace('\n','')
	name = line.split('=')[1]
	name = name.replace(' ','')
	if name.find('D')!=-1:
		name = name.replace('D','e')+','
		print(name,end='')
	else:
		name = 'np.float32('+name+'),'
		print(name,end='')

	# uncomment this part to get a list of the Data array names in the gas function. 2nd usage 
'''	for name in l:

		name = name.split('(')[0]
		if name!='':
			print(name+'= gd[\'gas7/'+name+'\']')'''





