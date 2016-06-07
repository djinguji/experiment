# collect data for MS presentation

import numpy as np

PLAIN_AA = ['alan', 'ktab', 'mlabs', 'ratb', 'tab', ]
EMPH_SAA = ['Samt', 'anfSal', 'antSar', ]
EMPH_DAA = ['alfDa\?g', 'rDa\?g', ]
EMPH_DHAA = ['ant\D-am', 'n\D-afh', ]
EMPH_TAA = ['awTan', 'balTa\?grh', 'fTam', 'STam', ]
EMPH_AAS = ['alnaSrh', 'baS', 'faSl', 'mtwaSl', ]
EMPH_AAD = ['maD', 'maDy', 'naDj', ]
EMPH_AAD = ['maDy', 'naDj', 'naDr', ]
EMPH_AADH = ['mna\D-r', 'mwa\D-bh', ]
EMPH_AAT = ['bsaTh', 'mwaTn', ]

PLAIN_II = ['hy', 'jzyrh', 'sdyd', 'tlyfwn', ]
EMPH_SII = ['mSyr', 'nSyb', ]
EMPH_DII = ['maDy', 'mtwDy\?g', 'nDyf', 'wDy\?g', ]
EMPH_DHII = ['n\D-yf', 'w\D-yfh', ]
EMPH_TII = ['fTyrh', 'yTyr', 'mTyh', ]
EMPH_IIS = []
EMPH_IID = []
EMPH_IIDH = []
EMPH_IIT = ['wsyTh', ]

PLAIN_UU = ['ftwr', 'hw', 'skwt', 'tlyfwn', 'zhwr', ]
EMPH_SUU = ['aSwl', ]
EMPH_DUU = ['fDwl', 'wDw\?g', 'wDwh', ]
EMPH_DHUU = []
EMPH_TUU = ['fTwr', 'sTwr', ]
EMPH_UUS = []
EMPH_UUD = []
EMPH_UUDH = []
EMPH_UUT = ['\shrwT', 'smwT', ]

PLAIN_S = ['mlabs', 'sdyd', 'syf', 'skwt', 'jrs', ]
EMPH_S = EMPH_SAA + EMPH_AAS + EMPH_SII + EMPH_SUU
EMPH_SA = EMPH_SAA + EMPH_AAS

PLAIN_T = ['ktab', 'ratb', 'tab', 'tlyfwn', ]
EMPH_T = EMPH_TAA + EMPH_AAT + EMPH_TII + EMPH_IIT + EMPH_TUU + EMPH_UUT
EMPH_TA = EMPH_TAA + EMPH_AAT 

PLAIN_D = ['sdyd', ]
EMPH_D = EMPH_DAA + EMPH_AAD + EMPH_DII + EMPH_DUU
EMPH_DA = EMPH_DAA + EMPH_AAD

def slope(a):
    A = np.vstack([np.array(range(len(a))), np.ones(len(a))]).T
    y = np.array(a)
    m, c = np.linalg.lstsq(A, y)[0]
    return m

def main():
    
    print(slope([-1, 0.2, 0.9, 2.1]))
    print(slope([-.4, 0.2, 0.9, 1.6]))

if __name__ == '__main__':
    main()
