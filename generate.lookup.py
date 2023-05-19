#!/usr/bin/env python3


def severity(n):
    if n % 8 == 0:
        return "emergency"
    elif n % 8 == 1:
        return "alert"
    elif n % 8 == 2:
        return "critical"
    elif n % 8 == 3:
        return "error"
    elif n % 8 == 4:
        return "warning"
    elif n % 8 == 5:
        return "notice"
    elif n % 8 == 6:
        return "info"
    elif n % 8 == 7:
        return "debug"


def facility(n):
    if n < 8:       return "kernel"
    elif n < 16:    return "user"
    elif n < 24:    return "mail"
    elif n < 32:    return "system"
    elif n < 40:    return "security"
    elif n < 48:    return "syslog"
    elif n < 56:    return "lpd"
    elif n < 64:    return "nntp"
    elif n < 72:    return "uucp"
    elif n < 80:    return "time"
    elif n < 88:    return "security"
    elif n < 96:    return "ftpd"
    elif n < 104:    return "ntpd"
    elif n < 112:    return "logaudit"
    elif n < 120:    return "logalert"
    elif n < 128:    return "clock"
    elif n < 136:    return "local0"
    elif n < 144:    return "local1"
    elif n < 152:    return "local2"
    elif n < 160:    return "local3"
    elif n < 168:    return "local4"
    elif n < 176:    return "local5"
    elif n < 184:    return "local6"
    elif n < 192:    return "local7"

    else:
        return "0"


print(f"\"syslogcode\",\"severity\",\"facility\"")

for n in range(191 + 1):
    print(f"\"{n}\",\"{severity(n)}\",\"{facility(n)}\"")

