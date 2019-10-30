configs = { 
	"natom": 9,
	"mass": [28.085, 28.085, 28.085, 15.999, 15.999, 15.999, 15.999, 15.999, 15.999],
	"temperature": 300,
	"gru_ave23": [1.9778,1.9778,0.99356],
	"V": 1.1324994110707298e-28,
	"lattice_constants": [0.4921, 0.4921, 0.5400], # 单位是nm
	"mesh":[30, 30, 30],
	"figSize": (9,8)
}

params={
    'axes.labelsize': '32', # label size
    'axes.linewidth': '2',  #外边框
    'xtick.labelsize':'32',
    'ytick.labelsize':'32',
    'lines.linewidth':2 ,
    'legend.fancybox': 'false',         #边框是否圆角
    'legend.fontsize': '32',
    'legend.edgecolor': 'black',       # 边框颜色
    'legend.framealpha': '1.0',       # 边框透明度
    'figure.figsize'   : '10, 8',    # set figure size
    'font.family': 'Times New Roman'   # 使用 matplotlib 2.2.3 才不会出现Times New Roman字体自动加粗
}