7.2 ubuntu环境下挂载新硬盘
--------------------------

1. 显示硬盘及所属分区情况，在终端窗口中输入如下命令

.. code:: shell

   fdisk -lu

可以看到要挂载的磁盘

2. 对硬盘进行分区，在终端窗口中输入如下命令：

.. code:: shell

   fdisk /dev/sdb

步骤如下：

-  在Command (m for help)提示符后面输入m显示一个帮助菜单。

-  在Command (m for help)提示符后面输入n，执行 add a new partition
   指令给硬盘增加一个新分区。

-  出现Command action时，输入p。

-  出现Partition number(1-4)时，输入１表示只分一个区。

-  后续指定起启柱面（cylinder）号完成分区。

-  在Command (m for help)提示符后面输入p，显示分区表。

-  在Command (m for help)提示符后面输入w，保存分区表。

-  系统提示：The partition table has been altered!

-  格式化分区

ext4 表示将分区格式化成ext4文件系统类型

.. code:: shell

   mkfs.ext4 /dev/sdd1

-  挂载分区

指定硬盘分区文件系统类型为ext4 ，同时将 /dev/sdb1
分区挂载到目录/media/sdb1

.. code:: shell

   mkdir /media/sdd1

   cat /etc/fstab

   /dev/mapper/ubuntu--vg-root /        ext4  errors=remount-ro 0    1

   /dev/mapper/ubuntu--vg-swap_1 none      swap  sw       0    0

   /dev/sdb1        /media/sdb1       ext4  rw       0   0

   /dev/sdc1        /media/sdc1       ext4  rw       0   0

   /dev/sdd1        /media/sdd1       ext4  rw       0   0

重启服务器执行命令查看挂载效果

.. code:: shell

   df -h
