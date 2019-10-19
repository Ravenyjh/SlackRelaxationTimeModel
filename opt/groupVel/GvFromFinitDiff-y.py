import findiff as fi
import numpy as np
import os
import sys
lib_path = os.path.abspath(os.path.join('.'))
sys.path.append(lib_path)
import config

def ddx(groupSameYZ, nBranch,dx):
    trans0 = np.array([x[0] for x in groupSameYZ])
    trans1 = np.array([x[1] for x in groupSameYZ])
    trans2 = np.array([x[2] for x in groupSameYZ])
    trans3 = np.array([x[3] for x in groupSameYZ])
    # tran = np.vstack((trans0,trans1,trans2,trans3))
    l = [[]]*nBranch
    for i in range(nBranch):
        # 将频率的单位 cm^-1 转化成 THZ
        y = np.array([x[4+i]*0.02998 for x in groupSameYZ])
        # print (y)
        d_dx = fi.FinDiff(0, dx, 1)
        res1 = np.array(d_dx(y))
        l[i] = res1
    l = np.array(l)
    tran = np.vstack((trans0, trans1, trans2, trans3,l))
    tran = tran.transpose(1, 0)
    return tran

def mapCoordinate(row,lattice_constant):
    # 单位为 1/nm
    row[0] = row[0] /  lattice_constant
    row[1] = row[1] /  lattice_constant
    row[2] = row[2] /  lattice_constant
    return row[0],row[1],row[2]

# 分组得到不同的平面（y,z固定）的k点
def getGroups(a):
    group = []
    init = a[0]
    temp = [a[0]]
    for i in range(1, len(a)):
        if a[i][1] == init[1] and a[i][3] == init[3]:
            temp.append(a[i])
        else:
            group.append(temp)
            init = a[i]
            temp = [a[i]]
    group.append(temp)
    return group

def main(config):
    # branch个数
    nBranch = 3 * config.configs['natom']
    # 晶格常数 a,b,c (nm)
    lattice_constants = config.configs['lattice_constants']

    a = np.loadtxt('freq')
    a = np.array(a)
    # 删除无用的第二列信息得到信息文件，列名：index k1,k2,k3(*2pi/a后为k点坐标) w_1...w_n*3 (n为晶胞内原子数)
    a = np.delete(a,1,axis=1)


    # 设置的dx偏分的点的差值
    for row in a:
        row[1], row[2], row[3] = mapCoordinate([row[1], row[2], row[3]], lattice_constants[1])
    a = sorted(a, key=lambda x: (x[1], x[3]))
    dx = a[1][2] - a[0][2]

    # 分组得到不同的平面（y,z固定）的k点
    group = getGroups(a)

    # 对不同平面的k点偏分，组合，按原有index排列，列名：index k1,k2,k3(/2pi后为分数坐标) gv_xx_1...gv_xx_n*3 (n为晶胞内原子数，单位km/s)
    res = []
    for i in group:
        res+=list(ddx(i,nBranch,dx))
    res = sorted(res, key=lambda x:x[0])
    np.savetxt('SlackModelOutput/Slack.groupQEy',res,fmt="%.5f")

if __name__ == '__main__':
    main(config)


