# -*- encoding=utf-8 -*-
import getopt
import sys
import common.setting as setting
from common.runer import main

if __name__ == '__main__':
    argv=sys.argv[1:]
    device=""
    cap="MINICAP"
    touch="MINITOUCH"
    ori="MINICAPORI"
    try:
        opts, args = getopt.getopt(argv, "d:c:t:o:hp:")
    except getopt.GetoptError:
        print('main.py -d <设备编号> -c <capmethod> -t <touchmethod> -o <orimethod>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -d <设备编号> -c <capmethod> -t <touchmethod> -o <orimethod> [-h <help> -p<procote poco>]')
            sys.exit()
        elif opt in ("-d", ):
            device=arg
        elif opt in("-c",):
            cap=arg
        elif opt in("-t",):
            touch=arg
        elif opt in("-o",):
            ori=arg
        elif opt in ("-p",):
            p=arg
            setting.PROTECT_POCO_SERVICE=setting.initProtectPocoService(p)
    if device!="":
        deuri="dev1:android:///%s?cap_method=%s&touch_method=%s&ori_method=%s" % (device,cap,touch,ori)
        setting.DEVICE = setting.initDevice(deuri)
    main()


