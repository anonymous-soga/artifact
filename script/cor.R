library(stats)

avgview <- c(1994.870, 
             956.313, 
             2178.551, 
             3673.258,
             2779.281, 
             2849.415, 
             3471.748, 
             1480.305, 
             2434.888, 
             2868.616, 
             2305.692, 
             617.977, 
             1894.350, 
             2473.399, 
             2352.014, 
             2425.970, 
             1309.452, 
             1690.907, 
             1022.625, 
             1083.783 )
avgFav <- c(0.410, 
            0.232, 
            0.400, 
            1.161, 
            0.479, 
            0.565, 
            0.528, 
            0.252, 
            0.505, 
            0.561, 
            0.509, 
            0.250, 
            0.376, 
            0.784, 
            0.484, 
            0.492, 
            0.284, 
            0.356, 
            0.250, 
            0.237 )
avgAns <- c(3.880,
            1.759, 
            4.089, 
            9.194, 
            3.723, 
            4.242, 
            4.031, 
            2.180, 
            3.903, 
            4.367, 
            3.187, 
            1.045, 
            2.631, 
            4.779, 
            2.900, 
            3.241, 
            1.702, 
            2.215, 
            1.250, 
            1.411 )
avgScore <- c(0.947, 
              0.857, 
              0.951, 
              1.226, 
              1.022, 
              0.977, 
              1.128, 
              0.864, 
              0.944, 
              1.034, 
              1.020, 
              0.727, 
              0.758, 
              1.099, 
              1.119, 
              0.972, 
              0.835, 
              0.882, 
              0.750, 
              0.816 )

ansRate_so <- c(0.657,
                0.688,
                0.634,
                0.806,
                0.702,
                0.664,
                0.753,
                0.649,
                0.622,
                0.706,
                0.681,
                0.568,
                0.561,
                0.676,
                0.750,
                0.646,
                0.614,
                0.644,
                0.547,
                0.605)
acceptRate_so <- c(0.359,
                   0.384,
                   0.343,
                   0.452,
                   0.407,
                   0.387,
                   0.444,
                   0.370,
                   0.327,
                   0.412,
                   0.372,
                   0.205,
                   0.293,
                   0.376,
                   0.404,
                   0.369,
                   0.314,
                   0.352,
                   0.250,
                   0.297)
timeFA_so <- c(6.358,
               5.564,
               6.880,
               5.157,
               6.401,
               5.188,
               4.839,
               16.122,
               12.376,
               5.653,
               10.629,
               24.123,
               13.107,
               15.468,
               9.308,
               10.141,
               13.685,
               11.151,
               15.025,
               15.097)
timeAA_so <- c(7.209,
               1.663,
               10.008,
               8.068,
               6.175,
               4.799,
               5.962,
               16.047,
               11.112,
               4.605,
               10.932,
               70.959,
               4.528,
               15.468,
               10.120,
               12.217,
               14.126,
               10.686,
               18.363,
               16.701)
textSize_so <- c(1177.122,
                 1372.313,
                 1129.391,
                 1010.806,
                 1582.679,
                 1371.768,
                 1513.436,
                 2256.178,
                 1685.332,
                 1107.757,
                 1530.747,
                 1199.932,
                 1293.701,
                 1575.484,
                 1707.510,
                 1406.246,
                 2039.552,
                 1884.596,
                 2127.125,
                 2136.546)

#acceptRate_gh <- c(0.53,NA,0.53,NA,0.69,0.54,0.67,0.80,1.00,0.57,0.68,0.80,NA,0.50,0.67,0.67,0.70,0.50,NA,0.74)
#timeFA_gh <- c(371.16,197.21,370.51,704.18,464.64,570.56,273.87,531.94,387.51,535.13,430.55,739.73,108.95,55.79,298.6,494.37,336.46,358.61,353.78,63.66)
#timeAA_gh <- c(274.23,333.83,248.0,309.43,412.54,683.92,1505.75,2758.32,1524.7,685.7,744.23,1039.3,4268.38,1207.34,636.59,666.94,853.4,612.29,1319.53,445.48)
#textSize_gh <- c(1305.96,2001.44,1126.54,922.22,1556.5,1528.06,2203.18,1535.65,1107.89,1284.24,1532.56,1420.22,1498.32,1549.72,1348.46,1719.41,2079.8,1945.53,2190.45,2025.73)

#popularity vs difficulty
cor.test(avgview,ansRate_so,method="spearman")
cor.test(avgview,acceptRate_so,method="spearman")
cor.test(avgview,timeFA_so,method="spearman")
cor.test(avgview,timeAA_so,method="spearman")
cor.test(avgview,textSize_so,method="spearman")

cor.test(avgFav,ansRate_so,method="spearman")
cor.test(avgFav,acceptRate_so,method="spearman")
cor.test(avgFav,timeFA_so,method="spearman")
cor.test(avgFav,timeAA_so,method="spearman")
cor.test(avgFav,textSize_so,method="spearman")

cor.test(avgAns,ansRate_so,method="spearman")
cor.test(avgAns,acceptRate_so,method="spearman")
cor.test(avgAns,timeFA_so,method="spearman")
cor.test(avgAns,timeAA_so,method="spearman")
cor.test(avgAns,textSize_so,method="spearman")

cor.test(avgScore,ansRate_so,method="spearman")
cor.test(avgScore,acceptRate_so,method="spearman")
cor.test(avgScore,timeFA_so,method="spearman")
cor.test(avgScore,timeAA_so,method="spearman")
cor.test(avgScore,textSize_so,method="spearman")


#difficulty
cor.test(ansRate_so,acceptRate_so,method="spearman")
cor.test(ansRate_so,timeFA_so,method="spearman")
cor.test(ansRate_so,timeAA_so,method="spearman")
cor.test(ansRate_so,textSize_so,method="spearman")

cor.test(acceptRate_so,timeFA_so,method="spearman")
cor.test(acceptRate_so,timeAA_so,method="spearman")
cor.test(acceptRate_so,textSize_so,method="spearman")

cor.test(timeFA_so,timeAA_so,method="spearman")
cor.test(timeFA_so,textSize_so,method="spearman")

cor.test(timeAA_so,textSize_so,method="spearman")
