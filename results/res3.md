I was able to get another full run today of the various experiments (with many new ones).  Some of the big differences here are 
* Now running the gain test with
    * 10 Mhz Buffer
    * No buffer or overlap
    * 5 MHz overlap
    * 10 MHz overlap
    * 20 MHz overlap
    * Full overlap (only mode from previous test results)
* Now running the tdd test with
    * No buffer or overlap
    * 5 MHz overlap
    * Full overlap (only mode from previous test results)
    


Here are the results (so you can pour over them before we meet on Thursday):

---

# Experiment #1 (Gain Test)

In this experiment, the good GNode B has a gain of 31 db.  The evil GNodeB's gain is varied from 1 db to 31 db in 2db increments. Various frequency overlap between the Good and Evil gNodeBs.  No other parameters changed.

---
#### Experiment #1 (Gain Test) (Full Overlap) - Download Bandwidth
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/dl_bandwidth.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_dl_bandwidth.png)

---
#### Experiment #1 (Gain Test) - CQI
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/cqi.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/cqi.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/cqi.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/cqi.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/cqi.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_cqi.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_cqi.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_cqi.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_cqi.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_cqi.png)

---
#### Experiment #1 (Gain Test) - MCS
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/mcs.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/mcs.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/mcs.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/mcs.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/mcs.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_mcs.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_mcs.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_mcs.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_mcs.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_mcs.png)

---
#### Experiment #1 (Gain Test) - PUSCH SINR
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/pusch.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/pusch.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/pusch.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/pusch.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/pusch.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_pusch.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_pusch.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_pusch.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_pusch.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_pusch.png)

---
#### Experiment #1 (Gain Test) - Rank Indicator
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/ri.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/ri.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/ri.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/ri.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/ri.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/ri.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_ri.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_ri.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_ri.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_ri.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_ri.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_ri.png)

#### Experiment #1 (Gain Test) - DL Buffer Status
Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/dl_bs.png)

Full Overlap         ![asdf](2024-11-16_190121_gaintest/graphs/boxplot_dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-17_191842_gaintwentymhzoverlap/graphs/boxplot_dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-17_175653_gaintenmhzoverlap/graphs/boxplot_dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_170549_gainfivemhzoverlap/graphs/boxplot_dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-16_194956_gainwithoutoverlaptest/graphs/boxplot_dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-17_115715_gaintenmhzbuffertest/graphs/boxplot_dl_bs.png)

---




# Experiment #2 (Center Frequency Test)
In this test, the only change is the dl_arfcn values.  Test runs with the default 40MHz bandwidth.  The Good gNodeB runs with a center frequency of 3450 MHz (3430 MHz - 3470 MHz).  The Evil gNodeB starts at 3400 MHz (3380 MHz - 3420MHz) which has a buffer from the good gNodeB of 10MHz.  Then the evil gNodeB's center frequency is adjusted by 2 MHz for each subsequent test towards the good gNodeB's center frequency until they are totally overlapping.  Please note for these plots there is a lot of data.  The box plot gives a better idea.

#### Experiment #2 (Center Frequency Test) - Download Bandwidth
![asdf](2024-11-17_151553_arcntest/graphs/dl_bandwidth.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_dl_bandwidth.png)



#### Experiment #2 (Center Frequency Test) - CQI
![asdf](2024-11-17_151553_arcntest/graphs/cqi.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_cqi.png)


#### Experiment #2 (Center Frequency Test) - MCS
![asdf](2024-11-17_151553_arcntest/graphs/mcs.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_mcs.png)



#### Experiment #2 (Center Frequency Test) - PUSCH SINR
![asdf](2024-11-17_151553_arcntest/graphs/pusch.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_pusch.png)



#### Experiment #2 (Center Frequency Test) - Rank Indicator
![asdf](2024-11-17_151553_arcntest/graphs/ri.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_ri.png)


Experiment #2 (Center Frequency Test) - DL Buffer Status
![asdf](2024-11-17_151553_arcntest/graphs/dl_bs.png)
![asdf](2024-11-17_151553_arcntest/graphs/boxplot_dl_bs.png)





---
# Experiment #3 (TDD Misconfiguration Test)
In this experiment, the TDD configuration for the good gNodeB uses the default 5 download and 4 upload slots (total 9 slots).  The evil gNodeB's TDD configuration is varied, running each allocation of the ul and download slots (8dl and 1ul, 7dl and 2ul, .....)

#### Experiment #3 (TDD Misconfiguration Test) - Download Bandwidth
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/dl_bandwidth.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_dl_bandwidth.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - CQI
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/cqi.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/cqi.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_cqi.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_cqi.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - MCS
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/mcs.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/mcs.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_mcs.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_mcs.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - PUSCH SINR
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/pusch.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/pusch.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_pusch.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_pusch.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - Rank Indicator
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/ri.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/ri.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/ri.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_ri.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_ri.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_ri.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - DL Buffer Status
Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/dl_bs.png)

Full Overlap         ![asdf](2024-11-17_001736_tddtest/graphs/boxplot_dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-17_203530_tddfivemhzoverlap/graphs/boxplot_dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-17_200958_tddwithoutoverlap/graphs/boxplot_dl_bs.png)



---
# Experiment #4 (Center Frequency Test - testing the gap)
In this test, the only change is the dl_arfcn values.  Test runs with the default 40MHz bandwidth.  The Good gNodeB runs with a center frequency of 3450 MHz (3430 MHz - 3470 MHz).  The Evil gNodeB starts at 3406 MHz (3380 MHz - 3420MHz) which has a buffer from the good gNodeB of 10MHz.  Then the evil gNodeB's center frequency is adjusted by 0.4 MHz for each subsequent test towards the good gNodeB's center frequency until it hits 3416.  Please note for these plots there is a lot of data.  The box plot gives a better idea.

#### Experiment #4 (Center Frequency Test) - Download Bandwidth
![asdf](2024-11-16_225633_gaptest/graphs/dl_bandwidth.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_dl_bandwidth.png)



#### Experiment #4 (Center Frequency Test) - CQI
![asdf](2024-11-16_225633_gaptest/graphs/cqi.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_cqi.png)


#### Experiment #4 (Center Frequency Test) - MCS
![asdf](2024-11-16_225633_gaptest/graphs/mcs.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_mcs.png)



#### Experiment #4 (Center Frequency Test) - PUSCH SINR
![asdf](2024-11-16_225633_gaptest/graphs/pusch.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_pusch.png)



#### Experiment #4 (Center Frequency Test) - Rank Indicator
![asdf](2024-11-16_225633_gaptest/graphs/ri.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_ri.png)


#### Experiment #4 (Center Frequency Test) - DL Buffer Status
![asdf](2024-11-16_225633_gaptest/graphs/dl_bs.png)
![asdf](2024-11-16_225633_gaptest/graphs/boxplot_dl_bs.png)

Hopefully all these numbers seem reasonably sane to you.

Mike