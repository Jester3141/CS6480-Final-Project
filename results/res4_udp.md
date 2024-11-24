I re-ran all experiments.  This time the big change is using UDP.  I set the UDP target to 150M in iperf.   This results in much more consistent results.  As before I'm running the gain and tdd tests with various amounts frequency overlap (10MHz buffer, no buffer or overlap, 5MHz overlap, 10MHz overlap, 20MHz overlap, and full overlap)

    
Here are the results (so you can pour over them before we meet on Thursday???):

---

# Experiment #1 (Gain Test)

In this experiment, the good GNode B has a gain of 31 db.  The evil GNodeB's gain is varied from 1 db to 31 db in 2db increments.  Channel bandwidth is 40MHz.  Various frequency overlap between the Good and Evil gNodeBs.  No other parameters changed.

---
#### Experiment #1 (Gain Test) (Full Overlap) - Download Bandwidth
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/dl_bandwidth.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_dl_bandwidth.png)

---
#### Experiment #1 (Gain Test) - CQI
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/cqi.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/cqi.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/cqi.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/cqi.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/cqi.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_cqi.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_cqi.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_cqi.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_cqi.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_cqi.png)

---
#### Experiment #1 (Gain Test) - MCS
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/mcs.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/mcs.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/mcs.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/mcs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/mcs.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_mcs.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_mcs.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_mcs.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_mcs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_mcs.png)

---
#### Experiment #1 (Gain Test) - PUSCH SINR
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/pusch.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/pusch.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/pusch.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/pusch.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/pusch.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_pusch.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_pusch.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_pusch.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_pusch.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_pusch.png)

---
#### Experiment #1 (Gain Test) - Rank Indicator
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/ri.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/ri.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/ri.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/ri.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/ri.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/ri.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_ri.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_ri.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_ri.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_ri.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_ri.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_ri.png)

#### Experiment #1 (Gain Test) - DL Buffer Status
Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/dl_bs.png)

Full Overlap         ![asdf](2024-11-22_102607_gaintest_udp/graphs/boxplot_dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-23_012725_gaintwentymhzoverlap_udp/graphs/boxplot_dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-23_072803_gaintenmhzoverlap_udp/graphs/boxplot_dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_003751_gainfivemhzoverlap_udp/graphs/boxplot_dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-23_021651_gainwithoutoverlap_udp/graphs/boxplot_dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_dl_bs.png)

---




# Experiment #2 (Center Frequency Test)
In this test, the only change is the dl_arfcn values.  Test runs with the default 40MHz bandwidth.  The Good gNodeB runs with a center frequency of 3450 MHz (3430 MHz - 3470 MHz).  The Evil gNodeB starts at 3400 MHz (3380 MHz - 3420MHz) which has a buffer from the good gNodeB of 10MHz.  Then the evil gNodeB's center frequency is adjusted by 2 MHz for each subsequent test towards the good gNodeB's center frequency until they are totally overlapping.  Please note for these plots there is a lot of data.  The box plot gives a better idea.

#### Experiment #2 (Center Frequency Test) - Download Bandwidth
![asdf](2024-11-22_220638_arcntest_udp/graphs/dl_bandwidth.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_dl_bandwidth.png)



#### Experiment #2 (Center Frequency Test) - CQI
![asdf](2024-11-22_220638_arcntest_udp/graphs/cqi.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_cqi.png)


#### Experiment #2 (Center Frequency Test) - MCS
![asdf](2024-11-22_220638_arcntest_udp/graphs/mcs.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_mcs.png)



#### Experiment #2 (Center Frequency Test) - PUSCH SINR
![asdf](2024-11-22_220638_arcntest_udp/graphs/pusch.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_pusch.png)



#### Experiment #2 (Center Frequency Test) - Rank Indicator
![asdf](2024-11-22_220638_arcntest_udp/graphs/ri.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_ri.png)


Experiment #2 (Center Frequency Test) - DL Buffer Status
![asdf](2024-11-22_220638_arcntest_udp/graphs/dl_bs.png)
![asdf](2024-11-22_220638_arcntest_udp/graphs/boxplot_dl_bs.png)





---
# Experiment #3 (TDD Misconfiguration Test)
In this experiment, the TDD configuration for the good gNodeB uses the default 5 download and 4 upload slots (total 9 slots).  Channel bandwidth is 40MHz.  The evil gNodeB's TDD configuration is varied, running each allocation of the ul and download slots (8dl and 1ul, 7dl and 2ul, .....)  NOTE: 1d8u was not a valid mode (evil gNodeB wouldn't start with that setting) and was not ran.

#### Experiment #3 (TDD Misconfiguration Test) - Download Bandwidth
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/dl_bandwidth.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_dl_bandwidth.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_dl_bandwidth.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_dl_bandwidth.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_dl_bandwidth.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - CQI
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/cqi.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/cqi.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/cqi.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/cqi.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/cqi.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_cqi.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_cqi.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_cqi.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_cqi.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_cqi.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_cqi.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - MCS
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/mcs.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/mcs.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/mcs.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/mcs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/mcs.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_mcs.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_mcs.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_mcs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_mcs.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_mcs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_mcs.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - PUSCH SINR
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/pusch.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/pusch.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/pusch.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/pusch.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/pusch.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_pusch.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_pusch.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_pusch.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_pusch.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_pusch.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_pusch.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - Rank Indicator
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/ri.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/ri.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/ri.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/ri.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/ri.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/ri.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_ri.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_ri.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_ri.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_ri.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_ri.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_ri.png)

---
#### Experiment #3 (TDD Misconfiguration Test) - DL Buffer Status
Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/dl_bs.png)

Full Overlap         ![asdf](2024-11-22_214502_tddtest_udp/graphs/boxplot_dl_bs.png)
20 Mhz Overlap       ![asdf](2024-11-23_050111_tddtwentymhzoverlap_udp/graphs/boxplot_dl_bs.png)
10 Mhz Overlap       ![asdf](2024-11-23_103545_tddtenmhzoverlap_udp/graphs/boxplot_dl_bs.png)
 5 Mhz Overlap       ![asdf](2024-11-23_041725_tddfivemhzoverlap_udp/graphs/boxplot_dl_bs.png)
No Overlap or Buffer ![asdf](2024-11-23_035528_tddwithoutoverlap_udp/graphs/boxplot_dl_bs.png)
10 Mhz Buffer        ![asdf](2024-11-23_030611_gaintenmhzbuffer_udp/graphs/boxplot_dl_bs.png)
 


---
# Experiment #4 (Center Frequency Test - testing the gap)
In this test, the only change is the dl_arfcn values.  Test runs with the default 40MHz bandwidth.  The Good gNodeB runs with a center frequency of 3450 MHz (3430 MHz - 3470 MHz).  The Evil gNodeB starts at 3406 MHz (3380 MHz - 3420MHz) which has a buffer from the good gNodeB of 10MHz.  Then the evil gNodeB's center frequency is adjusted by 0.4 MHz for each subsequent test towards the good gNodeB's center frequency until it hits 3416.  Please note for these plots there is a lot of data.  The box plot gives a better idea.

#### Experiment #4 (Center Frequency Test) - Download Bandwidth
![asdf](2024-11-23_091425_gaptest_udp/graphs/dl_bandwidth.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_dl_bandwidth.png)



#### Experiment #4 (Center Frequency Test) - CQI
![asdf](2024-11-23_091425_gaptest_udp/graphs/cqi.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_cqi.png)


#### Experiment #4 (Center Frequency Test) - MCS
![asdf](2024-11-23_091425_gaptest_udp/graphs/mcs.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_mcs.png)



#### Experiment #4 (Center Frequency Test) - PUSCH SINR
![asdf](2024-11-23_091425_gaptest_udp/graphs/pusch.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_pusch.png)



#### Experiment #4 (Center Frequency Test) - Rank Indicator
![asdf](2024-11-23_091425_gaptest_udp/graphs/ri.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_ri.png)


#### Experiment #4 (Center Frequency Test) - DL Buffer Status
![asdf](2024-11-23_091425_gaptest_udp/graphs/dl_bs.png)
![asdf](2024-11-23_091425_gaptest_udp/graphs/boxplot_dl_bs.png)




---
# Experiment #5 (TDD CLI test)
In this experiment, the TDD configuration for the good gNodeB uses the default 5 download and 4 upload slots (total 9 slots).  Channel bandwidth is 40MHz.  The evil gNodeB's TDD configuration is varied, running each allocation of the ul and download slots (8dl and 1ul, 7dl and 2ul, .....)  Previous test varied frequency overlap.  This test varies the Evil GnodeB's tx power  (31db, 25db, 20db, 15db, 10db, 5db).

#### Experiment #5 (TDD CLI test) - Download Bandwidth
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/dl_bandwidth.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/dl_bandwidth.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/dl_bandwidth.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/dl_bandwidth.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/dl_bandwidth.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/dl_bandwidth.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_dl_bandwidth.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_dl_bandwidth.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_dl_bandwidth.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_dl_bandwidth.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_dl_bandwidth.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_dl_bandwidth.png)



#### Experiment #5 (TDD CLI test) - CQI
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/cqi.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/cqi.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/cqi.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/cqi.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/cqi.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/cqi.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_cqi.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_cqi.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_cqi.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_cqi.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_cqi.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_cqi.png)



#### Experiment #5 (TDD CLI test) - MCS
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/mcs.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/mcs.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/mcs.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/mcs.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/mcs.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/mcs.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_mcs.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_mcs.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_mcs.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_mcs.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_mcs.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_mcs.png)


#### Experiment #5 (TDD CLI test) - PUSCH SINR
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/pusch.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/pusch.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/pusch.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/pusch.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/pusch.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/pusch.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_pusch.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_pusch.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_pusch.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_pusch.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_pusch.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_pusch.png)



#### Experiment #5 (TDD CLI test) - Rank Indicator
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/ri.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/ri.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/ri.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/ri.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/ri.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/ri.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_ri.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_ri.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_ri.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_ri.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_ri.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_ri.png)



#### Experiment #5 (TDD CLI test) - DL Buffer Status
31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/dl_bs.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/dl_bs.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/dl_bs.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/dl_bs.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/dl_bs.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/dl_bs.png)

31db Evil gNodeB Tx Gain    ![asdf](2024-11-23_235740_tddgainE31_udp/graphs/boxplot_dl_bs.png)
25db Evil gNodeB Tx Gain    ![asdf](2024-11-24_001746_tddgainE25_udp/graphs/boxplot_dl_bs.png)
20db Evil gNodeB Tx Gain    ![asdf](2024-11-24_003752_tddgainE20_udp/graphs/boxplot_dl_bs.png)
15db Evil gNodeB Tx Gain    ![asdf](2024-11-24_005758_tddgainE15_udp/graphs/boxplot_dl_bs.png)
10db Evil gNodeB Tx Gain    ![asdf](2024-11-24_011759_tddgainE10_udp/graphs/boxplot_dl_bs.png)
 5db Evil gNodeB Tx Gain    ![asdf](2024-11-24_013801_tddgainE05_udp/graphs/boxplot_dl_bs.png)



Hopefully all these numbers seem reasonably sane to you.

Mike