使用Slack relaxation time model计算声子热导率，需要频率文件和Gruneisen 作为输入，中间过程会输出Debye temperature, density of state, group velocity等参数。

1. 安装docker后执行以下命令
	1.1 docker build -t SlackModel .
	1.2 docker container run -it SlackModel /bin/bash 

2. 容器启动后进入bash环境，执行以下命令
	1.1 python opt/Dos/countDos.py										// 计算density of state
	1.2 python opt/groupVel/GvFromFinitDiff-x.py						// 计算x方向 Group velocity    
	1.3 python opt/groupVel/GvFromFinitDiff-x.py						// 计算y方向 Group velocity
	1.4 python opt/groupVel/GvFromFinitDiff-x.py						// 计算z方向 Group velocity
	1.4 python opt/thermalConductivity/klemens_model-qeinput.py			// 计算热导率和相关系数 

3. 需要的输入文件和参数参考Example中的例子
