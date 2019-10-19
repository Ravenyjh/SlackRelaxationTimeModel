import matplotlib.pyplot as plt
import pandas as pd

def plotDetail():
    a = pd.read_table('../thermalConductivity/detail', sep='\s+', header=None, engine='python')
    b = pd.read_table('../ShengBTE-compare/detail', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:,0]
    omegaQe = omegaQe.tolist()
    omegaShengBTE = b.loc[:,0]
    omegaShengBTE = omegaShengBTE.tolist()

    cphQe = a.loc[:,1]
    cphQe = cphQe.tolist()
    cphShengBTE = b.loc[:,1]
    cphShengBTE = cphShengBTE.tolist()

    gvQe = a.loc[:,2]
    gvQe = gvQe.tolist()
    gvShengBTE = b.loc[:,2]
    gvShengBTE = gvShengBTE.tolist()


    scatteringRateQe = a.loc[:,3]
    scatteringRateQe = scatteringRateQe.tolist()
    scatteringRateShengBTE = b.loc[:,3]
    scatteringRateShengBTE = scatteringRateShengBTE.tolist()

    qindexQe = [x for x in range(len(scatteringRateQe))]
    qindexShengBTE = [x for x in range(len(scatteringRateShengBTE))]

    plt.figure(1)
    ax1 = plt.subplot(111)
    ax1.plot(qindexQe,omegaQe,'.',label="Qe")
    ax1.plot(qindexShengBTE,omegaShengBTE,'.',label="ShengBTE")

    plt.figure(2)
    ax2 = plt.subplot(111)
    ax2.plot(qindexQe,cphQe,'.',label="Qe")
    ax2.plot(qindexShengBTE,cphShengBTE,'.',label="ShengBTE")

    plt.figure(3)
    ax3 = plt.subplot(111)
    ax3.plot(qindexQe,gvQe,'.',label="Qe")
    ax3.plot(qindexShengBTE,gvShengBTE,'.',label="ShengBTE")

    plt.figure(4)
    ax4 = plt.subplot(111)
    scatteringRateQe = [1/x for x in scatteringRateQe]
    scatteringRateShengBTE = [1/x for x in scatteringRateShengBTE]
    ax4.plot(qindexQe,scatteringRateQe,'.',label="Qe")
    ax4.plot(qindexShengBTE,scatteringRateShengBTE,'.',label="ShengBTE")
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
    a = pd.read_table('../DOS/Dos', sep='\s+', header=None, engine='python')
    b = pd.read_table('../ShengBTE-compare/BTE.dos_acoustic_noHead', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:, 0]
    omegaQe = omegaQe.tolist()
    omegaShengBTE = b.loc[:, 0]
    omegaShengBTE = omegaShengBTE.tolist()

    DosQe = a.loc[:, 1]
    DosQe = DosQe.tolist()
    DosShengBTE = b.loc[:, 1]
    DosShengBTE = DosShengBTE.tolist()

    plt.figure(1)
    ax1 = plt.subplot(111)
    ax1.plot(omegaQe, DosQe, '.', label="Qe")
    ax1.plot(omegaShengBTE, DosShengBTE, '.', label="ShengBTE")

    ax1.legend(loc=0)
    ax1.set_xlabel('Omega')
    ax1.set_ylabel('Dos')
    plt.show()

def main():
    # plotDos()
    plotDetail()

main()