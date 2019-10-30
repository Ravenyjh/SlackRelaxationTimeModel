import math
import pandas as pd
import numpy as np
import sys
import os
lib_path = os.path.abspath(os.path.join('.'))
sys.path.append(lib_path)
import config


def tau_model(file, config):
    hbar = 1.054571726E-34
    k_B = 1.3806488E-23
    m_0 = 1.6605E-27
    mass = config.configs['mass']
    mass_ave = sum(mass) / len(mass)
    # mass_total = sum(mass)
    temperature = config.configs['temperature']
    gru_ave23 = config.configs['gru_ave23']
    nbranch = config.configs['natom']
    V = config.configs['V']

    # omega
    a = pd.read_table(file + 'freq', sep='\s+', header=None, index_col=0, engine='python')
    omega_full = a.loc[:,
                 [x for x in range(5,nbranch*3 + 5)]]
    omega_full = omega_full.values.tolist()
    nptk = len(omega_full)
    Nbands = len(omega_full[0])
    print (nptk, Nbands)

    # gv
    b1 = pd.read_table(file + 'SlackModelOutput/Slack.groupQEx', sep='\s+', header=None, index_col=0, engine='python')
    gv1 = b1.loc[:,
          [x for x in range(4,nbranch*3 + 4)]]
    gv1 = gv1.values.tolist()

    b2 = pd.read_table(file + 'SlackModelOutput/Slack.groupQEy', sep='\s+', header=None, index_col=0, engine='python')
    gv2 = b2.loc[:,
          [x for x in range(4, nbranch*3 + 4)]]
    gv2 = gv2.values.tolist()

    b3 = pd.read_table(file + 'SlackModelOutput/Slack.groupQEz', sep='\s+', header=None, index_col=0, engine='python')
    gv3 = b3.loc[:,
          [x for x in range(4, nbranch*3 + 4)]]
    gv3 = gv3.values.tolist()


    c =np.loadtxt('SlackModelOutput/Slack.Dos')
    omega_dos2 = [x[0] for x in c]
    dos2 = [x[1] for x in c]

    sum_dos2 = 0.0
    sum_omega2 = 0.0
    for ii in range(1, len(dos2)):
        sum_dos2 = sum_dos2 + dos2[ii - 1] * (omega_dos2[ii] - omega_dos2[ii - 1])
        sum_omega2 = sum_omega2 + dos2[ii - 1] * omega_dos2[ii - 1] ** 2 * (omega_dos2[ii] - omega_dos2[ii - 1])
    debye2 = math.sqrt(5 * hbar ** 2 * sum_omega2 / 3 / k_B ** 2 / sum_dos2) * 1.0E12

    gv0_T1 = 1000.0 * math.sqrt(gv1[0][0] ** 2 + gv2[0][0] ** 2 + gv3[0][0] ** 2)
    gv0_T2 = 1000.0 * math.sqrt(gv1[0][1] ** 2 + gv2[0][1] ** 2 + gv3[0][1] ** 2)
    gv0_L = 1000.0 * math.sqrt(gv1[0][2] ** 2 + gv2[0][2] ** 2 + gv3[0][2] ** 2)
    gv_ave = 3.0 / (1.0 / gv0_T1 + 1.0 / gv0_T2 + 1.0 / gv0_L)

    coeffx = 2 * hbar * gru_ave23[0] ** 2 * math.exp(-debye2 / (3 * temperature)) / (mass_ave * m_0) / debye2 * temperature / gv_ave ** 2
    coeffy = 2 * hbar * gru_ave23[1] ** 2 * math.exp(-debye2 / (3 * temperature)) / (mass_ave * m_0) / debye2 * temperature / gv_ave ** 2
    coeffz = 2 * hbar * gru_ave23[2] ** 2 * math.exp(-debye2 / (3 * temperature)) / (mass_ave * m_0) / debye2 * temperature / gv_ave ** 2
    print('##########')
    print ('Group velocity at Gamma point:', gv_ave)
    print('Debye temperature',debye2)
    print ('##########')

    k_modelx = 0.0
    k_modely = 0.0
    k_modelz = 0.0
    detail=[]
    for ii in range(nptk):
        for jj in range(Nbands):
            # 将频率从 cm^-1 转化为 rad/s
            omega_full[ii][jj] = omega_full[ii][jj] * 0.1883698952939957 * 1E12
            x_var = hbar * omega_full[ii][jj] / k_B / temperature
            if x_var != 0.0:
                cph = k_B * x_var ** 2 * math.exp(x_var) / (math.exp(x_var) - 1.0) ** 2 / V
            else:
                cph = 0.0
            if omega_full[ii][jj]*1E-12 > 0.01:
                detail.append([omega_full[ii][jj]*1E-12, cph, gv1[ii][jj], gv2[ii][jj], gv3[ii][jj], (coeffx * omega_full[ii][jj] ** 2),
                                (coeffy * omega_full[ii][jj] ** 2), (coeffz * omega_full[ii][jj] ** 2)])
                k_modelx = k_modelx + cph * (gv1[ii][jj] * 1E3) ** 2 / ((coeffx * omega_full[ii][jj] ** 2))
                k_modely = k_modely + cph * (gv2[ii][jj] * 1E3) ** 2 / ((coeffy * omega_full[ii][jj] ** 2))
                k_modelz = k_modelz + cph * (gv3[ii][jj] * 1E3) ** 2 / ((coeffz * omega_full[ii][jj] ** 2))
    np.savetxt('SlackModelOutput/Slack.detail', detail)
    print('Thermal conductivity',k_modelx / nptk, k_modely / nptk, k_modelz / nptk)
    final_results = [gv_ave, debye2 ,k_modelx / nptk, k_modely / nptk, k_modelz / nptk]
    np.savetxt('SlackModelOutput/Slack.kappa', final_results)

if __name__ == '__main__':
    tau_model('', config)
