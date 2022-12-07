#!/usr/bin/env python3
# @lint-avoid-python-3-compatibility-imports
#
# SAFE CRUSH!!!!!!!!!!!!

from __future__ import print_function
from bcc import BPF

# define BPF programn
bpf_text = """
#include <uapi/linux/ptrace.h>

int execve_hook(struct pt_regs *ctx) {
 int *p = (int*)0x1234;
 *p = 0xffffff;
 return 0;
}
"""

bpf = BPF(text=bpf_text)
bpf.attach_kprobe(event=bpf.get_syscall_fnname("execve"),
                                    fn_name="execve_hook")

# load BPF program
b = BPF(text=bpf_text)

print("Going to safe crush")
