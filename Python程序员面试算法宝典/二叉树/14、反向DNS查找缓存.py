"""
IP  ---->  域名

1、将IP地址添加到缓存中的URL映射
2、根据给定IP地址查找对应的URL

方法一：
    字典存储
方法二：
    Trie树
    1、使用Trie树，在最欢的情况下的时间复杂度为O(1),而哈希方法在平均情况下的时间复杂度为O(1)
    2、Trie树可以实现前缀搜索(对于有相同前缀的IP地址，可以寻找所有的URL)
        当然，由于树这种数据结构本身的特性，所以使用树结构的一个最大的缺点就是需要耗费更多的内存，但是对于本题而言，这却不是
        一个问题，因为Internet IP地址只包含有11个字母(0-9)。所以，本题实现的主要思路为：在Trie树中存储IP地址，而在最后一个结点中
        存储对应的域名。
"""






















