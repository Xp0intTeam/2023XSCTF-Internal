#!/bin/bash

cd $(dirname $0)
img_dup="/tmp/fs_$RANDOM.img"
cp fs.img $img_dup
LD_LIBRARY_PATH=./depend exec timeout --foreground 60s ./qemu-system-riscv64 \
	-machine virt \
	-bios none \
	-kernel kernel \
	-m 256M \
	-smp 3 \
	-nographic \
	-drive file=$img_dup,if=none,format=raw,id=x0 \
	-device virtio-blk-device,drive=x0,bus=virtio-mmio-bus.0 \
	-monitor /dev/null \
