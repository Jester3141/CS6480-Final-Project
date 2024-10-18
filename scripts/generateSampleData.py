#!/usr/bin/env python3

from datetime import datetime, timedelta
import random
import json



if __name__ == "__main__":
    print("Generating data to sample_data.json")


    ret = []


    pci = 1
    rnti = 17921
    cqi = 15
    ri = 1
    dl_mcs = 27
    dl_brate = 291680.0
    dl_nof_ok = 352
    dl_nof_nok = 0
    dl_bs = 0
    pusch_snr_db = 24.025097
    ul_mcs = 26
    ul_brate = 12838928.0
    ul_nof_ok = 431
    ul_nof_nok = 0
    bsr = 0



    for i in reversed(range(0, 3000)):
        ts = datetime.now() - timedelta(seconds=i)

        pci += 1
        rnti += 17921
        cqi = random.randint(0, 15)
        ri += 1
        dl_mcs = 27
        dl_brate = dl_brate + random.randint(-5000,5000)
        dl_nof_ok = 352
        dl_nof_nok = 0
        dl_bs = 0
        pusch_snr_db += 24.025097 + random.random()
        ul_mcs = 26
        ul_brate = ul_brate + random.randint(-5000,5000)
        ul_nof_ok = 431
        ul_nof_nok += 5
        bsr -= 1
        
        
        ret.append(
            {
                "timestamp": ts.timestamp(),
                "ue_list": [
                    {
                    "ue_container": {
                        "pci": pci,
                        "rnti": rnti,
                        "cqi": cqi,
                        "ri": ri,
                        "dl_mcs": dl_mcs,
                        "dl_brate": dl_brate,
                        "dl_nof_ok": dl_nof_ok,
                        "dl_nof_nok": dl_nof_nok,
                        "dl_bs": dl_bs,
                        "pusch_snr_db": pusch_snr_db,
                        "ul_mcs": ul_mcs,
                        "ul_brate": ul_brate,
                        "ul_nof_ok": ul_nof_ok,
                        "ul_nof_nok": ul_nof_nok,
                        "bsr": bsr
                        }
                    }
                ]
            }
        )

    with open("sample_data.json", "w") as f:
        json.dump(ret, f, indent=4)
