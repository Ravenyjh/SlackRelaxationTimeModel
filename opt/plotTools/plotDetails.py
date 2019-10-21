import matplotlib.pyplot as plt
import pandas as pd

def plotDetail():
    a = pd.read_table('../../SlackModelOutput/Slack.detail', sep='\s+', header=None, engine='python')

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
    a = pd.read_table('../../SlackModelOutput/Slack.Dos', sep='\s+', header=None, engine='python')

    omegaQe = a.loc[:, 0]
    omegaQe = omegaQe.tolist()

    DosQe = a.loc[:, 1]
    DosQe = DosQe.tolist()

    plt.figure(1)
    ax1 = plt.subplot(111)
    ax1.plot(omegaQe, DosQe, '.', label="Qe")
    # ax1.plot(omegaQe, DosQe, '.')

    ax1.legend(loc=0)
    ax1.set_xlabel('Omega')
    ax1.set_ylabel('Dos')
    plt.show()

def main():
    plotDos()
	# plotDetail()

main()
