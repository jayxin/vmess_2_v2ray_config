#!/bin/bash

if [[ -x "$(which python3)" ]] ; then
  if [[ -n "$1" ]] ; then
    vmess_addr_fname=$(python3 ./py/base64_2_vmess.py "$1")
    python3 ./py/vmess_2_server_info.py "$vmess_addr_fname"
  else
    echo "Error!"
  fi
fi
