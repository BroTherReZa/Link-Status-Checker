#BroTher_ReZa
import urllib2
import sys
if len(sys.argv) == 1 or len(sys.argv) > 2:
    print "="*68
    print "#    ____         _______ _               _____      ______        #"
    print "#   |  _ \       |__   __| |             |  __ \    |___  /        #"
    print "#   | |_) |_ __ ___ | |  | |__   ___ _ __| |__) |___   / / __ _    #"
    print "#   |  _ <| '__/ _ \| |  | '_ \ / _ \ '__|  _  // _ \ / / / _` |   #"
    print "#   | |_) | | | (_) | |  | | | |  __/ |  | | \ \  __// /_| (_| |   #"
    print "#   |____/|_|  \___/|_|  |_| |_|\___|_|  |_|  \_\___/_____\__,_|   #"
    print "#                                   ______                         #"
    print "#                                  |______|                        #"					
    print "="*68
    print "# ToolsName :\tBrIs200 \n# Author :\tBroTher_ReZa \n# Date :\t28 Des 2015 \n# Usage :\tpython BrIs200.py UrlList.txt \n# Notics:\tUrlList Must Be Line by line"
    print "+"*70
else:
    if (sys.argv[1]):
        print "\n"+"+"*50
        print "# ToolsName :\tBrIs200 \n# Author :\tBroTher_ReZa \n# Usage :\tpython BrIs200.py UrlList.txt \n# Notics:\tUrlList Must Be Line by line"
        print "+"*50
        Brllist=open(sys.argv[1],"r")
        i=0
        j=0
        for bR in Brllist:
            print "-"*50
            j=j+1
            try:
                if "http://" or "https://" in bR:
                    br=bR
                else:
                    br="http://"+bR
                BroTher = urllib2.Request(br, headers={'User-Agent' : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT"})
                if urllib2.urlopen(BroTher).getcode() == 200 :
                    i=i+1
                    print "%d/%d|Ok| %s"%(i,j,br)
                    result=open("BrIs200.txt","a")
                    result.write(br)
                else:
                    print "%d/%d|No| %s"%(i,j,br)
            except:
                print "%d/%d|Error| %s"%(i,j,br)



