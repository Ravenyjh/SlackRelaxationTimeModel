import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
import math
import os
import sys
lib_path = os.path.abspath(os.path.join('.'))
sys.path.append(lib_path)
import config

params = config.params

pylab.rcParams.update(params)
#plt.rc('font',family='Times New Roman', size=config.configs['labelSize'])

def generateAccumulateK(omegaQe,cphQe,gvQe,scatteringRateQe,mesh):
    meanFreePathDependedK = []
    for i in range(len(omegaQe)):
        meanFreePath = math.fabs(gvQe[i] * 1E3) / scatteringRateQe[i]
        k_modelx = cphQe[i] * (gvQe[i] * 1E3) ** 2 / (scatteringRateQe[i] * mesh)
        meanFreePathDependedK.append([meanFreePath, k_modelx])
    meanFreePathDependedK.sort(key=lambda x: x[0])

    accumulateFun = []
    for i in range(len(omegaQe)):
        k_modelx += meanFreePathDependedK[i][1]
        accumulateFun.append([meanFreePathDependedK[i][0], k_modelx])

    meanFreePath = [x[0]*1E6 for x in accumulateFun] # 将单位从m变成nm
    accumulateK = [x[1] for x in accumulateFun]
    return meanFreePath,accumulateK

def plotAccumate(config):
    plt.figure()
    ax1 = plt.subplot(111)

    mesh = config.configs['mesh'][0] * config.configs['mesh'][1] * config.configs['mesh'][2]
    a = pd.read_table('SlackModelOutput/Slack.detail', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:, 0]
    omegaQe = omegaQe.tolist()
    cphQe = a.loc[:, 1]
    cphQe = cphQe.tolist()

    minMeanFreePath = 10000
    maxMeanFreePath = 0
    for direction in range(3):
        gvQe = a.loc[:, 2 + direction]
        gvQe = gvQe.tolist()
        scatteringRateQe = a.loc[:, 5 + direction]
        scatteringRateQe = scatteringRateQe.tolist()
        meanFreePath, accumulateK = generateAccumulateK(omegaQe,cphQe,gvQe,scatteringRateQe,mesh)
        if meanFreePath[-1] < minMeanFreePath:
            minMeanFreePath = meanFreePath[-1]
        if meanFreePath[-1] > maxMeanFreePath:
            maxMeanFreePath = meanFreePath[-1]
        label = ['kxx', 'kyy', 'kzz']
        # ax1.plot(meanFreePath, accumulateK, '-', label=label[direction])
        ax1.plot(meanFreePath, accumulateK, '-')

    ax1.set_xlim(0, (minMeanFreePath + maxMeanFreePath)/2)
    # ax1.legend(loc=0)
    ax1.set_xlabel('Mean free path (um)')
    ax1.set_ylabel('Cumulative thermal conductivity (W/(m-K)')
    plt.savefig('SlackModelOutput/CumulativeK.png', bbox_inches='tight')

def plotDetail():
    a = pd.read_table('SlackModelOutput/Slack.detail', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:,0]
    omegaQe = omegaQe.tolist()

    cphQe = a.loc[:,1]
    cphQe = cphQe.tolist()

    gvQe = a.loc[:,2]
    gvQe = gvQe.tolist()


    scatteringRateQe = a.loc[:,3]
    scatteringRateQe = scatteringRateQe.tolist()

    qindexQe = [x for x in range(len(scatteringRateQe))]

    plt.figure(1)
    ax1 = plt.subplot(111)
    ax1.plot(qindexQe,omegaQe,'.',label="Qe")

    plt.figure(2)
    ax2 = plt.subplot(111)
    ax2.plot(qindexQe,cphQe,'.',label="Qe")

    plt.figure(3)
    ax3 = plt.subplot(111)
    ax3.plot(qindexQe,gvQe,'.',label="Qe")

    plt.figure(4)
    ax4 = plt.subplot(111)
    scatteringRateQe = [1/x for x in scatteringRateQe]
    ax4.plot(qindexQe,scatteringRateQe,'.',label="Qe")
    ax4.set_ylim(0, 0.3 * 1E-8)


    ax1.legend(loc=0)
    ax1.set_xlabel('k')
    ax1.set_ylabel('Omega')

    ax2.legend(loc=0)
    ax2.set_xlabel('k')
    ax2.set_ylabel('cph')

    ax3.legend(loc=0)
    ax3.set_xlabel('k')
    ax3.set_ylabel('gv')

    ax4.legend(loc=0)
    ax4.set_xlabel('k')
    ax4.set_ylabel('Relaxation time')

    plt.show()

def plotDos():
    a = pd.read_table('SlackModelOutput/Slack.Dos', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:, 0]
    omegaQe = omegaQe.tolist()
    omegaQe = [ i/0.188369895509244 * 0.02998 for i in omegaQe]

    DosQe = a.loc[:, 1]
    DosQe = DosQe.tolist()

    #plt.figure(figsize=config.configs['figSize'])
    ax1 = plt.subplot(111)
    ax1.plot(omegaQe, DosQe, '-')
    # ax1.plot(omegaQe, DosQe, '.', color="black")

    # ax1.legend(loc=0)
    #ax1.tick_params(labelsize=config.configs['labelSize'])
    ax1.set_xlabel('Frequency(THz)')
    ax1.set_ylabel('DOS')
    # plt.show()
    plt.savefig('SlackModelOutput/DosCurve.png',  bbox_inches='tight')
    # plt.savefig('/Users/apple/Desktop/DosCurve.png', bbox_inches='tight')

def main():
    # plotDos()
	# plotDetail()
    plotAccumate(config)

main()
