#!/bin/bash
# echo "Hello World !"

# 一、教程##############################
# 1.
# 变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界
# 推荐给所有变量加上花括号
# my_name="amber"
# echo $my_name
# echo ${my_name}

# 2. 循环某个目录，打印文件名
#for file in $(ls /etc); do
    #echo "file_name is ${file}"
#done


# 二、变量##################################
# 3.只读变量
# myUrl="http://www.google.com"
# readonly myUrl
# myUrl="http://www.runoob.com"
# 删除变量，变量被删除后不能再次使用。unset 命令不能删除只读变量
# unset myUrl
# echo ${myUrl}
# haha="122";
# unset haha
# echo ${haha}

# shell字符串
# 单双引号

# 拼接字符串
# your_name="qinjx"
# greeting="hello, "$your_name" !"
# greeting_1="hello, ${your_name} !"
# echo $greeting $greeting_1

# 获取字符串长度
# string="abcd"
# echo ${#string} #输出 4

# 提取子字符串
# 以下实例从字符串第 2 个字符开始截取 4 个字符：
# string="runoob is a great site"
# echo ${string:1:4} # 输出 unoo

# 查找子字符串
# 查找字符 "i 或 s" 的位置：
# string="runoob is a great company"
# echo `expr index "$string" i`  # 输出 8
# echo `expr index "$string" is`     #报错！！！！！！！

# 定义数组   bash支持一维数组（不支持多维数组），并且没有限定数组的大小
# array_name=(value0 value1 value2 value3)
# echo ${array_name[0]}
# echo ${array_name[@]}  # 获取所有元素

# 获取数组长度
# 取得数组元素的个数
# :<<'    #多行注释 ' 可以换成 EOF 或者 ！
# length=${#array_name[@]}
# echo ${length}
# # 或者
# length=${#array_name[*]}
# echo ${length}
# # 取得数组单个元素的长度
# lengthn=${#array_name[n]}
# echo ${length}
# '


#三、传递参数################################

#在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：$n
#n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……
# echo "Shell 传递参数实例！"
# echo "执行的文件名：$0"
# echo "第一个参数为：$1"
# echo "第二个参数为：$2"
# echo "第三个参数为：$3"
# echo "参数个数为：$#"
# echo "传递的参数作为一个字符串显示：$*"
# echo "test：$$"

# echo "-- \$* 演示 ---"
# for i in "$*"; do
#     echo $i
# done

# echo "-- \$@ 演示 ---"
# for i in "$@"; do
#     echo $i
# done


# 在为shell脚本传递的参数中如果包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收。
# 在有参数时，可以使用对参数进行校验的方式处理以减少错误发生
# 注意：的是中括号 [] 与其中间的代码应该有空格隔开 
# if [ -n "$1" ]; then
#     echo "包含第一个参数"
# else
#     echo "没有包含第一参数"
# fi


#四、数组###################################
#数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小（与 PHP 类似）。
#与大部分编程语言类似，数组元素的下标由0开始。
#Shell 数组用括号来表示，元素用"空格"符号分割开，
# my_array=(A B "Cdd" D)
# echo "第一个元素为: ${my_array[0]}"
# echo "${#my_array[@]}"
# echo "${#my_array[*]}"
# echo "单个元素的长度：${#my_array[2]}"


#五、shell基本运算符
# Shell 和其他编程语言一样，支持多种运算符，包括：
# 算数运算符
# 关系运算符
# 布尔运算符
# 字符串运算符
# 文件测试运算符
# 原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。
# expr 是一款表达式计算工具，使用它能完成表达式的求值操作。


#################算数运算######################
# val=`expr 2 + 2`
# echo "两数之和为 : $val"

# a=10
# b=20

# val=`expr $a + $b`
# echo "a + b : $val"

# val=`expr $a - $b`
# echo "a - b : $val"

# val=`expr $a \* $b`
# echo "a * b : $val"

# val=`expr $b / $a`
# echo "b / a : $val"

# val=`expr $b % $a`
# echo "b % a : $val"

# if [ $a == $b ]
# then
#    echo "a 等于 b"
# fi
# if [ $a != $b ]
# then
#    echo "a 不等于 b"
# fi

#echo $(( 2+2 ))
#echo $(( 2*2 ))

#string="runoob is a great company"
#echo `expr index "$string" i` 
#echo $(( index "$string" i ))


###################关系运算##################
# 关系运算符只支持数字，不支持字符串，除非字符串的值是数字。
# a=10
# b=20

# if [ $a -eq $b ]
# then
#    echo "$a -eq $b : a 等于 b"
# else
#    echo "$a -eq $b: a 不等于 b"
# fi
# if [ $a -ne $b ]
# then
#    echo "$a -ne $b: a 不等于 b"
# else
#    echo "$a -ne $b : a 等于 b"
# fi
# if [ $a -gt $b ]
# then
#    echo "$a -gt $b: a 大于 b"
# else
#    echo "$a -gt $b: a 不大于 b"
# fi
# if [ $a -lt $b ]
# then
#    echo "$a -lt $b: a 小于 b"
# else
#    echo "$a -lt $b: a 不小于 b"
# fi
# if [ $a -ge $b ]
# then
#    echo "$a -ge $b: a 大于或等于 b"
# else
#    echo "$a -ge $b: a 小于 b"
# fi
# if [ $a -le $b ]
# then
#    echo "$a -le $b: a 小于或等于 b"
# else
#    echo "$a -le $b: a 大于 b"
# fi

###################布尔运算##################
# a=10
# b=20

# if [ $a != $b ]
# then
#    echo "$a != $b : a 不等于 b"
# else
#    echo "$a != $b: a 等于 b"
# fi
# if [ $a -lt 100 -a $b -gt 15 ]
# then
#    echo "$a 小于 100 且 $b 大于 15 : 返回 true"
# else
#    echo "$a 小于 100 且 $b 大于 15 : 返回 false"
# fi
# if [ $a -lt 100 -o $b -gt 100 ]
# then
#    echo "$a 小于 100 或 $b 大于 100 : 返回 true"
# else
#    echo "$a 小于 100 或 $b 大于 100 : 返回 false"
# fi
# if [ $a -lt 5 -o $b -gt 100 ]
# then
#    echo "$a 小于 5 或 $b 大于 100 : 返回 true"
# else
#    echo "$a 小于 5 或 $b 大于 100 : 返回 false"
# fi

#################逻辑运算###########################
# a=10
# b=20

# if [[ $a -lt 100 && $b -gt 100 ]]
# then
#    echo "返回 true"
# else
#    echo "返回 false"
# fi

# if [[ $a -lt 100 || $b -gt 100 ]]
# then
#    echo "返回 true"
# else
#    echo "返回 false"
# fi


#################字符串运算符###########################
# a="abc"
# b="efg"

# if [ $a = $b ]
# then
#    echo "$a = $b : a 等于 b"
# else
#    echo "$a = $b: a 不等于 b"
# fi
# if [ $a != $b ]
# then
#    echo "$a != $b : a 不等于 b"
# else
#    echo "$a != $b: a 等于 b"
# fi
# if [ -z $a ]
# then
#    echo "-z $a : 字符串长度为 0"
# else
#    echo "-z $a : 字符串长度不为 0"
# fi
# if [ -n "$a" ]
# then
#    echo "-n $a : 字符串长度不为 0"
# else
#    echo "-n $a : 字符串长度为 0"
# fi
# if [ $a ]
# then
#    echo "$a : 字符串不为空"
# else
#    echo "$a : 字符串为空"
# fi


#################文件测试运算符###########################
#文件测试运算符用于检测 Unix 文件的各种属性


# 六、echo命令
# 显示普通字符
# echo "It is a test"  #这里的双引号完全可以省略
# echo It is a test
# #显示转义字符
# echo "\"It is a test\""
# 显示变量  终端 输入sh ./shell_demo.sh
# read name 
# echo "$name It is a test"
# read 命令一个一个词组地接收输入的参数，每个词组需要使用空格进行分隔；
# 如果输入的词组个数大于需要的参数个数，则多出的词组将被作为整体为最后一个参数接收。
# read -p "请输入一段文字:" -n 6 -t 5 -s password
# echo -e "\npassword is $password"
# 参数说明：
#  -p 输入提示文字
#  -n 输入字符长度限制(达到6位，自动结束)
#  -t 输入限时
#  -s 隐藏输入内容

# 显示换行
# echo -e "OK! \n" # -e 开启转义
# echo "It it a test"
# 显示不换行
# echo -e "OK! \c" # -e 开启转义 \c 不换行
# echo "It is a test"
# 显示结果定向至文件
# echo "It is a test" > ./myfile.txt
# 原样输出字符串，不进行转义或取变量(用单引号)
# echo '$name\"'
# 显示命令执行结果
# echo `date` #显示当前用户

#####总结
#echo输出的字符串总结
# ===================================================================

#        能否引用变量  |  能否引用转移符  |  能否引用文本格式符(如：换行符、制表符)

# 单引号  |   否      |       否       |               否

# 双引号  |   能      |       能       |               能

# 无引号  |   能      |       能       |               否                          

# ===================================================================



# 七、printf命令
# printf 命令模仿 C 程序库（library）里的 printf() 程序。
# printf 由 POSIX 标准所定义，因此使用 printf 的脚本比使用 echo 移植性好。
# printf 使用引用文本或空格分隔的参数，外面可以在 printf 中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等。
# 默认 printf 不会像 echo 自动添加换行符，我们可以手动添加 \n。

# printf 命令的语法：
# printf  format-string  [arguments...]
# 参数说明：
# format-string: 为格式控制字符串
# arguments: 为参数列表。

# format-string为双引号
# printf "%d %s\n" 1 "abc"
# 单引号与双引号效果一样 
# printf '%d %s\n' 1 "abc" 
# 没有引号也可以输出
# printf %s abcdef
# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
# printf %s abc def
# printf "%s\n" abc def
# printf "%s %s %s\n" a b c d e f g h i j
# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
# printf "%s and %d \n" S
#printf "a string, no processing:<%b>\n" "A\nB"

######总结
# %d %s %c %f 格式替代符详解:
# d: Decimal 十进制整数 -- 对应位置参数必须是十进制整数，否则报错！
# s: String 字符串 -- 对应位置参数必须是字符串或者字符型，否则报错！
# c: Char 字符 -- 对应位置参数必须是字符串或者字符型，否则报错！
# f: Float 浮点 -- 对应位置参数必须是数字型，否则报错！
# 如：其中最后一个参数是 "def"，%c 自动截取字符串的第一个字符作为结果输出。
# $  printf "%d %s %c\n" 1 "abc" "def"
# 1 abc d


# 八、Shell test 命令
# 代码中的 [] 执行基本的算数运算
# a=5
# b=6
# result=$[a+b] # 注意等号两边不能有空格
# echo "result 为： $result"

# if test -e ./shell_demo.sh
# then
#     echo '文件已存在!'
# else
#     echo '文件不存在!'
# fi

# 九、Shell 流程控制
# 和Java、PHP等语言不一样，sh的流程控制不可为空
# 在sh/bash里，如果else分支没有语句执行，就不要写这个else。

# if
# if 语句语法格式：

# if condition
# then
#     command1 
#     command2
#     ...
#     commandN 
# fi
# 写成一行（适用于终端命令提示符）：

# if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
# 末尾的fi就是if倒过来拼写，后面还会遇到类似的。

# if else
# if else 语法格式：

# if condition
# then
#     command1 
#     command2
#     ...
#     commandN
# else
#     command
# fi

# for 循环
# for循环一般格式为：
# for var in item1 item2 ... itemN
# do
#     command1
#     command2
#     ...
#     commandN
# done
# 写成一行：
# for var in item1 item2 ... itemN; do command1; command2… done;
# for((i=1;i<=5;i++));do
#     echo "这是第 $i 次调用";
# done;

# while 语句
# while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件
# int=1
# while(( $int<=5 ))
# do
#     echo $int
#     let int++
# done

# echo '按下 <CTRL-D> 退出'
# echo -n '输入你最喜欢的网站名: '
# while read FILM
# do
#     echo "是的！$FILM 是一个好网站"
# done

# echo '输入 1 到 4 之间的数字:'
# echo '你输入的数字为:'
# read aNum
# case $aNum in
#     1)  echo '你选择了 1'
#     ;;
#     2)  echo '你选择了 2'
#     ;;
#     3)  echo '你选择了 3'
#     ;;
#     4)  echo '你选择了 4'
#     ;;
#     *)  echo '你没有输入 1 到 4 之间的数字'
#     ;;
# esac
#esac
#case的语法和C family语言差别很大，它需要一个esac（就是case反过来）作为结束标记，每个case分支用右圆括号，用两个分号表示break

# 跳出循环
# 在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell使用两个命令来实现该功能：break和continue
# break命令允许跳出所有循环（终止执行后面的所有循环）
# continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

# 十、Shell 函数
# linux shell 可以用户定义函数，然后在shell脚本中可以随便调用
# 函数返回值在调用该函数后通过 $? 来获得。
# 注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至shell解释器首次发现它时，才可以使用。调用函数仅使用其函数名即可。 
# funWithReturn(){
#     echo "这个函数会对输入的两个数字进行相加运算..."
#     echo "输入第一个数字: "
#     read aNum
#     echo "输入第二个数字: "
#     read anotherNum
#     echo "两个数字分别为 $aNum 和 $anotherNum !"
#     return $(($aNum+$anotherNum))
# }
# funWithReturn
# echo "输入的两个数字之和为 $? !"

# 函数参数
# funWithParam(){
#     echo "第一个参数为 $1 !"
#     echo "第二个参数为 $2 !"
#     echo "第十个参数为 $10 !"
#     echo "第十个参数为 ${10} !"
#     echo "第十一个参数为 ${11} !"
#     echo "参数总数有 $# 个!"
#     echo "作为一个字符串输出所有参数 $* !"
# }
# funWithParam 1 2 3 4 5 6 7 8 9 34 73
#注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数

######## 还有几个特殊字符用来处理参数
# 参数处理	说明
# $#	    传递到脚本的参数个数
# $*	    以一个单字符串显示所有向脚本传递的参数
# $$	    脚本运行的当前进程ID号
# $!	    后台运行的最后一个进程的ID号
# $@	    与$*相同，但是使用时加引号，并在引号中返回每个参数。
# $-	    显示Shell使用的当前选项，与set命令功能相同。
# $?	    显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
