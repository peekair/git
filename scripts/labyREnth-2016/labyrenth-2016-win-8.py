#!/usr/bin/env python

# Only rick-rolls present here.
# Flag found statically

first = [ 0x7f, 0x56, 0x71, 0x4e #0x4e71567f
		, 0x61, 0x52, 0x7d, 0x43 #0x437d5261
		, 0x7b, 0x19, 0x70, 0x58 #0x5870197b
		, 0x7e, 0x37] #0x377e]

rick_roll = [0x5d, 0x5e, 0x70, 0x52	# l = 50
		, 0x32, 0x17, 0x5b, 0x52
		, 0x61, 0x52, 0x33, 0x5e
		, 0x60, 0x17, 0x67, 0x5f
		, 0x76, 0x17, 0x60, 0x58
		, 0x7f, 0x42, 0x67, 0x5e
		, 0x7c, 0x59, 0x29, 0x17
		, 0x7b, 0x43, 0x67, 0x47
		, 0x60, 0x0d, 0x3c, 0x18
		, 0x74, 0x58, 0x7c, 0x19
		, 0x74, 0x5b, 0x3c, 0x5f
		, 0x57, 0x6d, 0x45, 0x56
		, 0x57, 0x37]

the_witcher = [  0x4a, 0x58, 0x66, 0x17 #0x17 66 58 4a l = 96
		, 0x72, 0x45, 0x76, 0x17 #0x17 76 45 72
		, 0x7f, 0x5e, 0x78, 0x52 #0x52 78 5e 7f
		, 0x33, 0x70, 0x76, 0x45 #0x45 76 70 33
		, 0x72, 0x5b, 0x67, 0x17 #0x17 67 5b 72
		, 0x7c, 0x51, 0x33, 0x65 #0x65 33 51 7c
		, 0x7a, 0x41, 0x7a, 0x56 #0x56 7a 41 7a
		, 0x33, 0x51, 0x61, 0x58 #0x58 61 51 33
		, 0x7e, 0x17, 0x47, 0x5f #0x5f 47 17 7e
		, 0x76, 0x17, 0x44, 0x5e #0x5e 44 17 76
		, 0x67, 0x54, 0x7b, 0x52 #0x52 7b 54 67
		, 0x61, 0x17, 0x71, 0x42 #0x42 71 17 61
		, 0x67, 0x17, 0x75, 0x58 #0x58 75 17 67
		, 0x61, 0x17, 0x61, 0x52 #0x52 61 17 61
		, 0x65, 0x52, 0x61, 0x44 #0x44 61 52 65
		, 0x76, 0x17, 0x76, 0x59 #0x59 76 17 76
		, 0x74, 0x5e, 0x7d, 0x52 #0x52 7d 5e 74
		, 0x76, 0x45, 0x7a, 0x59 #0x59 7a 45 76
		, 0x74, 0x19, 0x3d, 0x19 #0x19 3d 19 74
		, 0x33, 0x14, 0x61, 0x52 #0x52 61 14 33
		, 0x65, 0x5f, 0x66, 0x59 #0x59 66 5f 65
		, 0x67, 0x17, 0x71, 0x4e #0x4e 71 17 67
		, 0x33, 0x4f, 0x76, 0x53 #0x53 76 4f 33
		, 0x7a, 0x05, 0x26, 0x37]#0x37 26 05 7a]



def decrypt(buf, l):
	for edx in range(l):
		eax = edx & 0x80000001
		if eax > 0:
			buf[edx] ^= 0x37
		elif eax == 0:
			buf[edx] ^= 0x13
		else:
			eax = (eax - 1 | -2) + 1
	return buf

print ''.join(map(chr, decrypt(first, 14)))
                                                        
                                                        
#flag: PAN{Wow, reverser! Great moves, keep it up, proud of you!}