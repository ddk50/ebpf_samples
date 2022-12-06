#!/bin/bash

for a in {00..01}; do
    fio --name=global --filename=/dev/zvol/zpool0/zvol0 --ioengine=libaio --direct=1 --time_based --runtime=60 --refill_buffers --name=test --rw=randwrite --randrepeat=0 --bs=4k --iodepth=16 | tee fio$a.log;
done
