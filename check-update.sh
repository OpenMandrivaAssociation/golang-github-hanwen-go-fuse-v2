#!/bin/sh
curl "https://github.com/hanwen/go-fuse/tags" 2>/dev/null |grep "tag/v2" |sed -e 's,.*tag/v,,;s,\".*,,;' |head -n1

