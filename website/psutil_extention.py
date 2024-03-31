# -*- coding = utf-8 -*-
# @Time: 2023/9/26 12:22
# @Author: YK
# @File: 获取系统信息.py
# @Software: PyCharm
import psutil as pl

class psutil_extention:

    def showComputerInfo():
    
        print("CPU信息：")
        # # logical=False 查看物理核心数
        cpuCountsPhysical = pl.cpu_count(logical=False)
        print(f"    CPU物理核数：{cpuCountsPhysical}")
        #
        # # logical=True 获取逻辑核心数（线程数）
        cpu_count = pl.cpu_count(logical=True)
        print(f"    CPU线程数：{cpu_count}")
        #
        # # CPU的使用率
        cpu_percent = pl.cpu_percent(interval=1)
        print(f"    CPU使用率：{cpu_percent}%")
        #
        print('内存信息：')
        # # 物理内存总量
        total_memory = pl.virtual_memory().total
        print(f'    内存总量：{int(total_memory/1024/1024)}M')
        #
        # # 可用内存总量
        availabele_memory = pl.virtual_memory().available
        print(f'    可用内存：{int(availabele_memory/1024/1024)}M')
        #
        # # 内存使用率
        memory_percent = pl.virtual_memory().percent
        print(f'    内存使用率：{memory_percent}%')
    
        print("磁盘信息：")
        # 获取磁盘分区信息
        disk_parts = pl.disk_partitions()
        for disk in disk_parts:
            try:
                print(f'    分区名称：{disk.mountpoint.split(":")[0]} 文件类型：{disk.fstype}',end=' ')
                print(f'磁盘利用率：{int(pl.disk_usage(disk.mountpoint).total/1024/1024/1024)}G',end=' ')
                print(f'磁盘空间：{pl.disk_usage(disk.mountpoint).percent}%')
            except Exception as e:
                print("转换失败：" + str(e))
    
        # 获取网卡信息
        print('网卡信息：')
        ip_adds = pl.net_if_addrs()
        keys = ip_adds.keys()
        for key in keys:
            print(f"    网卡名称：{key}",end=' ')
            print(f"网卡MAC：{ip_adds[key][0].address}",end=' ')
            print(f"网卡IP：{ip_adds[key][1].address}")
            
        psutil_extention.getNetworkInfo
    
    
    def getNetworkInfo(self):
        print("获取网络连接信息")
        netConnect = pl.net_connections()
        print('本地地址'.ljust(23),'远程地址'.ljust(22),'PID'.ljust(10),'进程名')
        for nc in netConnect:
            if nc[5] == 'ESTABLISHED':
                if nc[3][0].startswith('10') :
                    precessName = psutil_extention.getPidNname(nc[6])
                    print(f'{nc[3][0]}:{nc[3][1]}'.ljust(25),f'{nc[4][0]}:{nc[4][1]}'.ljust(25),f'{nc[6]}'.ljust(10),precessName)
    
    def getPidNname(self,pid):
        processList = pl.process_iter()
        for process in processList:
            if process.pid == pid:
                return process.name()
    
    # showComputerInfo()
    # getNetworkInfo()