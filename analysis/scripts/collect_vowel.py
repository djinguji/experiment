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

def mean(a):
    return np.mean(np.array(a))

def main():
    a = [-1, 0.2, 0.9, 2.1]
    print(slope(a), mean(a))
    print(slope([-.4, 0.2, 0.9, 1.6]))
    infile = open('vowel_word.txt')
    outfile = open('vowel_new.txt', 'w')
    l = infile.readline().split('\t')
    while len(l) > 5:
        print(l)
        if l[3] == 'seg0':
            spkr = l[0]
            vowel = l[1]
            orth = l[9]
            time = l[2]
            f1 = []
            f2 = []
            f3 = []
            outfile.write('%s+%s+%s+%s\t' % (spkr, vowel, orth, time))
            print('%s: %s' % (spkr, orth))
            f1.append(float(l[6]))
            f2.append(float(l[7]))
            f3.append(float(l[8]))
            for i in range(2):
                l = infile.readline().split('\t')
                if spkr != l[0]:
                    print('speaker error', spkr, 'not', l[0])
                if vowel != l[1]:
                    print('vowel error', vowel, 'not', l[1])
                if orth != l[9]:
                    print('orth error', orth, 'not', l[9])
                if time != l[2]:
                    print('time error', time, 'not', l[2])
                f1.append(float(l[6]))
                f2.append(float(l[7]))
                f3.append(float(l[8]))
            outfile.write('%.2f\t%.2f\t' % (slope(f1), mean(f1)))
            outfile.write('%.2f\t%.2f\t' % (slope(f2), mean(f2)))
            outfile.write('%.2f\t%.2f\t' % (slope(f3), mean(f3)))
            f1 = []
            f2 = []
            f3 = []
            for i in range(4):
                l = infile.readline().split('\t')
                if spkr != l[0]:
                    print('speaker error', spkr, 'not', l[0])
                if vowel != l[1]:
                    print('vowel error', vowel, 'not', l[1])
                if orth != l[9]:
                    print('orth error', orth, 'not', l[9])
                if time != l[2]:
                    print('time error', time, 'not', l[2])
                f1.append(float(l[6]))
                f2.append(float(l[7]))
                f3.append(float(l[8]))
            outfile.write('%.2f\t%.2f\t' % (slope(f1), mean(f1)))
            outfile.write('%.2f\t%.2f\t' % (slope(f2), mean(f2)))
            outfile.write('%.2f\t%.2f\t' % (slope(f3), mean(f3)))
            f1 = []
            f2 = []
            f3 = []
            for i in range(3):
                l = infile.readline().split('\t')
                if spkr != l[0]:
                    print('speaker error', spkr, 'not', l[0])
                if vowel != l[1]:
                    print('vowel error', vowel, 'not', l[1])
                if orth != l[9]:
                    print('orth error', orth, 'not', l[9])
                if time != l[2]:
                    print('time error', time, 'not', l[2])
                f1.append(float(l[6]))
                f2.append(float(l[7]))
                f3.append(float(l[8]))
            outfile.write('%.2f\t%.2f\t' % (slope(f1), mean(f1)))
            outfile.write('%.2f\t%.2f\t' % (slope(f2), mean(f2)))
            outfile.write('%.2f\t%.2f\n' % (slope(f3), mean(f3)))
            l = infile.readline().split('\t')
    print(slope([-1, 0.2, 0.9, 2.1]))
    print(slope([-.4, 0.2, 0.9, 1.6]))
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
