使用Slack relaxation time model计算声子热导率，需要频率文件和Gruneisen 作为输入，中间过程会输出Debye temperature, density of state, group velocity等参数。

可以选择使用Docker，避免自己安装依赖
	1. 安装docker后执行以下命令
		1.1 docker build -t SlackModel .
		1.2 docker container run -it SlackModel /bin/bash 

	2. 容器启动后进入bash环境，执行以下命令
		1.1 python opt/Dos/countDos.py										// 计算density of state
		1.2 python opt/groupVel/GvFromFinitDiff-x.py						// 计算x方向 Group velocity    
		1.3 python opt/groupVel/GvFromFinitDiff-x.py						// 计算y方向 Group velocity
		1.4 python opt/groupVel/GvFromFinitDiff-x.py						// 计算z方向 Group velocity
		1.5 python opt/thermalConductivity/klemens_model-qeinput.py			// 计算热导率和相关系数 
		1.6 python opt/plotTools/plotDetails.py								// 画DOS曲线,以及kappa随着Mean free path 的变化曲线

可以选择不使用使用Docker，需要使用python3.7，且需要安装Dockerfile中所示的相关包

3. 需要的输入文件和参数参考为config.py(用于设置材料参数)，configPlot.py(用于设置画图参数),freq（qe得到的q点等信息的输入文件）,Slack.* (画图的输入文件，用klemens_model-qeinput.pys生成),Example中的例子

4. 由于Slack relaxaction time 中弛豫时间和频率为倒数关系，所以如果出现非常低频率的点就会导致该点的热导率异常大，为避免这样的情况，程序将去除非常低频率的点
