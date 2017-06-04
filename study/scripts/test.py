#coding:utf-8
#!/usr/bin/env python
import psutil as pt
mem = pt.virtual_memory()
#print type(mem)
print mem[0]
print "总内存数是:%s\n已使用的内存数是:%s\n空闲的内存数是:%s" % (mem.total,mem.used,mem.free)
diskinfo = pt.disk_partitions()
#print diskinfo[0],diskinfo[1],diskinfo[2]
upids = pt.pids()
print '列出所有PID %s, 进程总数: %s' % (upids,len(upids))




