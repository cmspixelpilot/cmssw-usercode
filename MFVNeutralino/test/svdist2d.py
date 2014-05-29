#!/usr/bin/env python

from array import array
from math import atan2, pi
from JMTucker.Tools.ROOTTools import ROOT, set_style, plot_saver

set_style()
ps = plot_saver('plots/svdist2d', size=(600,600), root=False)

events = [ #JMTBAD
('ttbarhadronic', 11, 0.038701, (0.261774, 0.408543, 5.461642), (0.227344, 0.390869, 5.455204)),
('ttbarhadronic', 13, 0.052628, (0.256565, 0.375338, 6.423751), (0.216289, 0.409213, 6.422791)),
('ttbarhadronic', 13, 0.035594, (0.242142, 0.408818, 9.065842), (0.242830, 0.373231, 9.031754)),
('ttbarhadronic', 22, 0.035238, (0.256337, 0.386669, 12.382702), (0.221108, 0.385888, 12.389077)),
('ttbarhadronic', 14, 0.047271, (0.265458, 0.405046, -2.695619), (0.241287, 0.364422, -2.724167)),
('ttbarhadronic', 16, 0.035710, (0.234981, 0.383859, 3.376724), (0.270516, 0.387383, 3.372786)),
('ttbarhadronic', 15, 0.043497, (0.266564, 0.379380, 2.645792), (0.230433, 0.403599, 2.642178)),
('ttbarhadronic', 13, 0.005584, (0.255890, 0.389789, -5.614880), (0.261179, 0.391579, -5.632700)),
('ttbarhadronic', 14, 0.045643, (0.227548, 0.410070, -3.065305), (0.270651, 0.395057, -3.077112)),
('ttbarhadronic', 11, 0.026877, (0.253156, 0.376443, 5.128539), (0.255399, 0.403226, 5.124454)),
('ttbarhadronic', 14, 0.032884, (0.255983, 0.405007, -8.209767), (0.237292, 0.377952, -8.198071)),
('ttbarhadronic', 10, 0.031105, (0.231817, 0.387824, 3.532544), (0.259541, 0.401928, 3.530664)),
('ttbarhadronic', 10, 0.029926, (0.257093, 0.400376, -5.239875), (0.228456, 0.391689, -5.243913)),
('ttbarhadronic', 16, 0.053752, (0.269075, 0.394132, -7.130037), (0.217579, 0.409540, -7.126348)),
('ttbarhadronic', 14, 0.029036, (0.248531, 0.403836, -5.928278), (0.251489, 0.374951, -5.968768)),
('ttbarhadronic', 12, 0.038412, (0.277733, 0.400785, -4.486256), (0.245794, 0.422124, -4.502941)),
('ttbarhadronic', 12, 0.022547, (0.234883, 0.381776, 3.450872), (0.245009, 0.361631, 3.413937)),
('ttbarhadronic', 12, 0.035867, (0.231730, 0.393902, -4.327154), (0.263719, 0.410125, -4.301592)),
('ttbarhadronic', 15, 0.032213, (0.239994, 0.372933, -14.086270), (0.260160, 0.398052, -14.074339)),
('ttbarhadronic', 11, 0.048556, (0.233032, 0.419259, -8.775222), (0.244513, 0.372079, -8.765034)),
('ttbarhadronic', 16, 0.035112, (0.261019, 0.388552, -3.532264), (0.225916, 0.389328, -3.552430)),
('ttbarhadronic', 13, 0.043130, (0.215646, 0.385747, 4.265156), (0.258040, 0.393680, 4.279354)),
('ttbarhadronic', 10, 0.032733, (0.249804, 0.414212, 7.159348), (0.225952, 0.391794, 7.156300)),
('ttbarhadronic', 11, 0.062074, (0.256153, 0.422300, 0.543187), (0.239470, 0.362510, 0.565448)),
('ttbarhadronic', 12, 0.038225, (0.228277, 0.384568, 4.141894), (0.249055, 0.416653, 4.141676)),
('ttbarhadronic', 14, 0.030651, (0.243041, 0.381545, -14.264445), (0.251085, 0.411122, -14.281893)),
('ttbarhadronic', 13, 0.027132, (0.257195, 0.393079, 5.300949), (0.230072, 0.393780, 5.306590)),
('ttbarhadronic', 13, 0.036615, (0.254927, 0.405136, 6.218462), (0.226065, 0.382604, 6.228491)),
('ttbarhadronic', 13, 0.037736, (0.257154, 0.393210, 6.238013), (0.219834, 0.398799, 6.252401)),
('ttbarhadronic', 13, 0.036091, (0.222047, 0.393729, 4.010117), (0.258060, 0.391356, 4.017677)),
('ttbarhadronic', 12, 0.035892, (0.241920, 0.374157, 0.107589), (0.219389, 0.402096, 0.108714)),
('ttbarhadronic', 12, 0.030473, (0.253490, 0.412192, 6.064500), (0.272426, 0.388318, 6.046736)),
('ttbarhadronic', 17, 0.031091, (0.257323, 0.406246, 9.533103), (0.234369, 0.385276, 9.538775)),
('ttbarhadronic', 11, 0.030642, (0.256716, 0.383004, 8.010702), (0.240387, 0.408932, 8.011196)),
('ttbarhadronic', 12, 0.024412, (0.244803, 0.407390, 0.216023), (0.257426, 0.386495, 0.236428)),
('ttbarhadronic', 11, 0.043450, (0.261794, 0.389029, -4.626170), (0.218434, 0.391825, -4.635489)),
('ttbarhadronic', 13, 0.025250, (0.231915, 0.392398, -3.808438), (0.257105, 0.394148, -3.779503)),
('ttbarhadronic', 18, 0.032695, (0.259504, 0.393508, 12.857185), (0.227262, 0.398935, 12.857462)),
('ttbarhadronic', 11, 0.028932, (0.234207, 0.403653, 1.902911), (0.249383, 0.379021, 1.896924)),
('ttbarhadronic', 11, 0.037733, (0.250584, 0.367955, -1.889866), (0.245795, 0.405382, -1.895459)),
('ttbarhadronic', 12, 0.031327, (0.239456, 0.408642, -6.565908), (0.240848, 0.377346, -6.561104)),
('ttbarhadronic', 11, 0.030632, (0.227864, 0.391526, -4.268200), (0.256909, 0.381797, -4.233783)),
('ttbarhadronic', 11, 0.028730, (0.248359, 0.377262, -4.881135), (0.247598, 0.405982, -4.854982)),
('ttbarhadronic', 11, 0.040421, (0.230395, 0.403082, -1.950852), (0.259047, 0.374570, -1.907626)),
('ttbarsemilep', 11, 0.031826, (0.245567, 0.408691, 7.969666), (0.255001, 0.378295, 7.973600)),
('ttbarsemilep', 16, 0.034505, (0.259908, 0.398028, -1.836077), (0.227067, 0.387441, -1.836747)),
('ttbarsemilep', 10, 0.024929, (0.247409, 0.405600, -4.956808), (0.232222, 0.385831, -4.963808)),
('ttbarsemilep', 13, 0.039928, (0.250731, 0.375288, -6.276837), (0.245005, 0.414804, -6.314315)),
('ttbarsemilep', 16, 0.036345, (0.228102, 0.400075, -4.004355), (0.263833, 0.393423, -3.999746)),
('ttbarsemilep', 14, 0.004070, (0.227979, 0.386167, 0.751764), (0.225782, 0.382741, 0.707583)),
('ttbarsemilep', 16, 0.033545, (0.233942, 0.409929, 0.673804), (0.261400, 0.390660, 0.692134)),
('ttbarsemilep', 11, 0.039194, (0.252763, 0.365911, -1.874623), (0.252573, 0.405104, -1.880237)),
('ttbarsemilep', 10, 0.054586, (0.244123, 0.358922, 1.530907), (0.267812, 0.408101, 1.544266)),
('ttbarsemilep', 11, 0.026633, (0.260321, 0.401859, 1.750917), (0.275874, 0.380239, 1.746354)),
('ttbarsemilep', 16, 0.024805, (0.229209, 0.391487, 5.140284), (0.250317, 0.404515, 5.121445)),
('ttbarsemilep', 11, 0.036160, (0.254123, 0.382416, 7.464678), (0.244901, 0.417381, 7.468283)),
('ttbarsemilep', 12, 0.033067, (0.253745, 0.378405, 7.162079), (0.239531, 0.408260, 7.154380)),
('ttbarsemilep', 13, 0.024418, (0.235910, 0.382939, 10.198140), (0.247804, 0.404265, 10.180593)),
('ttbarsemilep', 10, 0.030207, (0.246734, 0.379393, 1.492085), (0.244984, 0.409549, 1.489637)),
('ttbarsemilep', 14, 0.034996, (0.252636, 0.384203, 9.913699), (0.222502, 0.401998, 9.942034)),
('ttbarsemilep', 13, 0.016696, (0.257172, 0.406113, 2.154545), (0.257426, 0.389419, 2.136598)),
('ttbarsemilep', 12, 0.046914, (0.242177, 0.375487, -4.412486), (0.262619, 0.417712, -4.409223)),
('ttbarsemilep', 12, 0.010382, (0.233841, 0.393914, 3.301536), (0.228302, 0.385134, 3.266938)),
('ttbarsemilep', 11, 0.027283, (0.258238, 0.408334, -19.207090), (0.230984, 0.409601, -19.185354)),
('ttbarsemilep', 11, 0.026724, (0.258213, 0.401267, -0.098736), (0.242278, 0.379814, -0.080527)),
('ttbarsemilep', 16, 0.034684, (0.228029, 0.388869, 1.397051), (0.262259, 0.394466, 1.412738)),
('ttbarsemilep', 13, 0.037387, (0.263866, 0.402585, 8.039712), (0.230027, 0.386688, 8.028935)),
('ttbarsemilep', 11, 0.032185, (0.230817, 0.398790, 6.651732), (0.262783, 0.395031, 6.612658)),
('ttbarsemilep', 14, 0.018567, (0.264100, 0.404621, 8.216182), (0.248700, 0.414994, 8.236205)),
('ttbarsemilep', 13, 0.026827, (0.258878, 0.397428, -0.226971), (0.239706, 0.378664, -0.239883)),
('ttbarsemilep', 11, 0.043971, (0.245935, 0.404951, 4.224583), (0.215630, 0.373091, 4.242571)),
('ttbarsemilep', 12, 0.038202, (0.253742, 0.380504, 4.861063), (0.243114, 0.417197, 4.852141)),
('ttbarsemilep', 12, 0.034055, (0.232482, 0.404072, 1.647906), (0.244581, 0.372239, 1.646769)),
('ttbarsemilep', 13, 0.046729, (0.227131, 0.381352, 9.258919), (0.270069, 0.399790, 9.277014)),
('ttbarsemilep', 11, 0.020765, (0.236023, 0.404813, 0.882777), (0.256478, 0.401244, 0.886532)),
('ttbarsemilep', 10, 0.053447, (0.266908, 0.407504, 1.768390), (0.232672, 0.366462, 1.753822)),
('ttbarsemilep', 11, 0.030015, (0.262439, 0.386612, 0.347358), (0.246987, 0.412343, 0.338805)),
('ttbarsemilep', 17, 0.043424, (0.245861, 0.415844, -0.220396), (0.229203, 0.375742, -0.209014)),
('ttbarsemilep', 12, 0.028505, (0.231765, 0.401564, -6.833236), (0.258937, 0.392951, -6.849461)),
('ttbarsemilep', 11, 0.054220, (0.246547, 0.407563, 1.132278), (0.210238, 0.367296, 1.121953)),
('ttbarsemilep', 13, 0.031854, (0.228428, 0.391833, 5.364110), (0.260282, 0.391760, 5.333476)),
('ttbarsemilep', 11, 0.048765, (0.219194, 0.380352, 2.077436), (0.264316, 0.398846, 2.074665)),
('ttbarsemilep', 11, 0.038296, (0.242644, 0.376394, 7.810289), (0.250211, 0.413935, 7.809881)),
('ttbardilep', 11, 0.035490, (0.256243, 0.383283, -0.621124), (0.227632, 0.404282, -0.627584)),
('ttbardilep', 15, 0.048394, (0.252329, 0.412225, 16.728769), (0.235339, 0.366912, 16.705204)),
('ttbardilep', 13, 0.021676, (0.261392, 0.400320, 1.801897), (0.256793, 0.379138, 1.840762)),
('qcdht0500', 14, 0.031216, (0.259793, 0.386807, 14.018899), (0.233294, 0.403306, 14.045001)),
('qcdht0500', 14, 0.035681, (0.229137, 0.385552, 2.830137), (0.264634, 0.381939, 2.819033)),
('qcdht0500', 10, 0.030847, (0.257073, 0.384037, -6.783942), (0.230863, 0.400304, -6.815997)),
('qcdht0500', 10, 0.035895, (0.243853, 0.370969, 2.395457), (0.238683, 0.406489, 2.407749)),
('qcdht0500', 12, 0.045145, (0.216766, 0.393802, 4.149904), (0.261910, 0.393419, 4.128311)),
('qcdht0500', 11, 0.033487, (0.226527, 0.385951, 6.554352), (0.257724, 0.398122, 6.579831)),
('qcdht0500', 15, 0.033719, (0.250790, 0.378456, -7.072565), (0.257341, 0.411533, -7.071732)),
('qcdht0500', 13, 0.033311, (0.250953, 0.402390, -3.354647), (0.217684, 0.400710, -3.371771)),
('qcdht0500', 11, 0.038460, (0.229164, 0.417618, -1.956006), (0.263980, 0.401278, -1.981340)),
('qcdht0500', 12, 0.036045, (0.220862, 0.395612, 6.890242), (0.256903, 0.395058, 6.852194)),
('qcdht0500', 12, 0.042488, (0.216964, 0.394643, -4.943839), (0.258883, 0.387711, -4.954834)),
('qcdht1000', 12, 0.020897, (0.232967, 0.387422, -3.795327), (0.253287, 0.382546, -3.781423)),
('qcdht1000', 11, 0.030876, (0.228178, 0.395587, 3.123396), (0.258020, 0.387662, 3.121744)),
('qcdht1000', 12, 0.048159, (0.226795, 0.399825, -7.200914), (0.268803, 0.376274, -7.215221)),
('qcdht1000', 14, 0.038332, (0.247611, 0.374368, 5.226603), (0.252036, 0.412443, 5.227739)),
('qcdht1000', 10, 0.028460, (0.253969, 0.387228, 0.200368), (0.229735, 0.402151, 0.226905)),
('qcdht1000', 14, 0.043101, (0.269236, 0.391707, -1.603156), (0.226879, 0.399683, -1.592224)),
('qcdht1000', 10, 0.024867, (0.255381, 0.390902, 5.283243), (0.274483, 0.406822, 5.292409)),
('qcdht1000', 12, 0.013975, (0.227702, 0.389219, -4.015036), (0.224136, 0.375707, -3.978168)),
('qcdht1000', 16, 0.041697, (0.227543, 0.390958, -5.096049), (0.254458, 0.422804, -5.096879)),
('qcdht1000', 12, 0.024221, (0.243114, 0.409392, 1.665213), (0.261673, 0.393828, 1.695791)),
('qcdht1000', 12, 0.031332, (0.237805, 0.402070, 3.296449), (0.258966, 0.378964, 3.319068)),
('qcdht1000', 14, 0.037790, (0.258977, 0.384943, -7.500850), (0.221241, 0.386951, -7.507568)),
('qcdht1000', 19, 0.033464, (0.234830, 0.403472, -11.265083), (0.259856, 0.381258, -11.276914)),
('qcdht1000', 12, 0.028400, (0.254533, 0.400248, -4.506886), (0.236491, 0.378316, -4.534570)),
('qcdht1000', 13, 0.029901, (0.230584, 0.401468, -6.218827), (0.242164, 0.373901, -6.206750)),
('qcdht1000', 16, 0.026469, (0.250757, 0.379914, 4.717221), (0.228766, 0.394645, 4.710238)),
('qcdht1000', 15, 0.041596, (0.232985, 0.403169, -3.814898), (0.270559, 0.385326, -3.814059)),
('qcdht1000', 17, 0.031583, (0.258578, 0.406750, 11.371336), (0.229904, 0.393512, 11.375998)),
('qcdht1000', 13, 0.037326, (0.269267, 0.391133, 9.229137), (0.233829, 0.379413, 9.192720)),
('qcdht1000', 11, 0.040115, (0.261291, 0.388357, -1.434937), (0.221197, 0.389665, -1.441461)),
('qcdht1000', 11, 0.026610, (0.246650, 0.404755, 0.164131), (0.229340, 0.384545, 0.171293)),
('qcdht1000', 14, 0.044737, (0.257603, 0.388177, 4.226021), (0.213935, 0.397899, 4.218983)),
('qcdht1000', 15, 0.030106, (0.260525, 0.394337, -10.134151), (0.231608, 0.385962, -10.108851)),
('qcdht1000', 10, 0.031233, (0.231103, 0.380252, 2.551840), (0.242572, 0.409303, 2.570316)),
('qcdht1000', 13, 0.028415, (0.257211, 0.390462, -9.134892), (0.228839, 0.388902, -9.140739)),
('qcdht1000', 11, 0.043168, (0.229081, 0.397498, -0.302181), (0.269128, 0.381382, -0.288588)),
('qcdht1000', 14, 0.039587, (0.228525, 0.400860, 6.921945), (0.258938, 0.375519, 6.920234)),
('qcdht1000', 14, 0.033116, (0.243835, 0.411088, 3.311372), (0.252551, 0.379139, 3.300946)),
('qcdht1000', 15, 0.032980, (0.228323, 0.390648, -9.407327), (0.260781, 0.384800, -9.410151)),
('qcdht1000', 15, 0.030062, (0.247755, 0.377203, 0.616671), (0.241735, 0.406655, 0.600577)),
('qcdht1000', 15, 0.060362, (0.251551, 0.411217, -3.324126), (0.209912, 0.367517, -3.300309)),
('qcdht1000', 11, 0.035403, (0.234506, 0.378969, -5.646155), (0.259828, 0.403711, -5.643841)),
('qcdht1000', 12, 0.037491, (0.242003, 0.411026, 0.149441), (0.234260, 0.374343, 0.164819)),
('qcdht1000', 16, 0.029332, (0.259696, 0.390450, 3.163644), (0.232744, 0.402025, 3.163779)),
('qcdht1000', 16, 0.042497, (0.231463, 0.402637, 4.072507), (0.247837, 0.363421, 4.089777)),
('qcdht1000', 17, 0.037624, (0.257214, 0.387308, 6.095485), (0.228596, 0.411733, 6.075747)),
('qcdht1000', 12, 0.031878, (0.240344, 0.403977, 1.021576), (0.224094, 0.376552, 1.058210)),
('qcdht1000', 12, 0.036368, (0.261610, 0.403122, -1.899366), (0.245276, 0.370628, -1.903476)),
('qcdht1000', 11, 0.034701, (0.251157, 0.413297, -0.124734), (0.219187, 0.399803, -0.162090)),
('qcdht1000', 11, 0.025764, (0.251666, 0.404393, -12.351637), (0.239824, 0.381512, -12.343326)),
('qcdht1000', 12, 0.031533, (0.254696, 0.386244, 6.976066), (0.264452, 0.416229, 7.002819))]

def debs(v):
    return (v[0] - 0.244, v[1] - 0.3928)

def phi(v):
    return atan2(v[1], v[0])

def dphi(v0, v1):
    phi0 = phi(v0)
    phi1 = phi(v1)
    res = phi0 - phi1
    while res > pi:
        res -= 2*pi
    while res <= -pi:
        res += 2*pi
    return res

h_y_x = []
for i in xrange(0,10):
    h_y_x.append(ROOT.TH2F('svdist2d_%i'%i, '%i um <= svdist2d < %i um;x (cm);y (cm)'%(100*i,100*(i+1)), 200, -0.1, 0.1, 200, -0.1, 0.1))

h_dz = ROOT.TH1F('h_dz', '', 100, -0.2, 0.2)
h_dphi = ROOT.TH1F('h_phi', '', 100, -pi, pi)

h_y_x_g = [[] for x in xrange(10)]
h_dzs = [ROOT.TH1F('h_dz_%i' % x, '', 100, -0.2, 0.2) for x in xrange(10)]
h_dphis = [ROOT.TH1F('h_dphi_%i' % x, '', 100, -pi, pi) for x in xrange(10)]

for sample, ntracks01, svdist2d, v0, v1 in events:
    svdist2d *= 10000
    bin = int(svdist2d / 100)
    #print svdist2d, bin, event[3][0]-0.244, event[3][1]-0.3928, event[4][0]-0.244, event[4][1]-0.3928

    dz = v0[-1] - v1[-1]
    v0 = debs(v0)
    v1 = debs(v1)
    dp = dphi(v0, v1)

    h_y_x[bin].Fill(v0[0], v0[1])
    h_y_x[bin].Fill(v1[0], v1[1])

    h_dz.Fill(dz)
    h_dzs[bin].Fill(dz)

    h_dphi.Fill(dp)
    h_dphis[bin].Fill(dp)

    xs = array('d', [v0[0], v1[0]])
    ys = array('d', [v0[1], v1[1]])

    g = ROOT.TGraph(2, xs, ys)
    h_y_x_g[bin].append((g, dp))

for i in xrange(0,10):
    h_y_x[i].Draw('colz')
    ps.save('svdist2d%i'%i, logz=True)

h_dz.Draw()
ps.save('h_dz')

h_dphi.Draw()
ps.save('h_dphi')

maxax = 0.05
g_axes = ROOT.TGraph(4, array('d', [-maxax, maxax, maxax, -maxax]), array('d', [-maxax, -maxax, maxax, maxax]))
g_axes.SetMarkerColor(ROOT.kWhite)
g_axes.SetLineColor(ROOT.kWhite)

for i,gs in enumerate(h_y_x_g):
    if not gs:
        continue

    title = '%i um <= svdist2d < %i um;x (cm);y (cm)'%(100*i,100*(i+1))
    
    h_dzs[i].Draw()
    h_dzs[i].SetTitle(title + ';dz (cm)')
    ps.save('h_dz_%i' % i)

    h_dphis[i].Draw()
    h_dphis[i].SetTitle(title + ';dphi (rad)')
    ps.save('h_dphis_%i' % i)

    ps.c.Clear()
    g_axes.SetTitle(title + ';x (cm);y (cm)')
    g_axes.Draw('ALP')

    for g,dp in gs:
        c = ROOT.kRed if abs(dp) > 2.5 else ROOT.kBlack
        g.SetLineColor(c)
        g.SetMarkerColor(c)
        g.SetMarkerStyle(20)
        g.SetMarkerSize(0.5)
        g.Draw('LP')

    ps.save('g_svdist2d%i'%i, log=False)