#!/bin/bash

(echo "###################Hardware Details>#####################################" 

echo "========================Sys Info=========================================="
echo "SYSTEM-MANUFACTURER: $( dmidecode -s system-manufacturer)"
echo "SYSTEM-PRODUCT-NAME: $( dmidecode -s system-product-name)"
echo "SYSTEM-SERIAL-NUMBER: $( dmidecode -s system-serial-number)"
echo "SYSTEM-UUID: $( dmidecode -s system-uuid)"
echo "SYSTEM-FAMILY: $( dmidecode -s system-family)"

echo "======================Baseboard Info======================================"
echo "BASEBOARD-MANUFACTURER: $( dmidecode -s baseboard-manufacturer)"
echo "BASEBOARD-PRODUCT-NAME: $( dmidecode -s baseboard-product-name)"
echo "BASEBOARD-SERIAL-NUMBER: $( dmidecode -s baseboard-serial-number)"

echo "======================Chasis Info========================================="
echo "CHASSIS-MANUFACTURER: $( dmidecode -s chassis-manufacturer)"
echo "CHASSIS-TYPE: $( dmidecode -s chassis-type)"
echo "CHASSIS-SERIAL-NUMBER: $( dmidecode -s chassis-serial-number)"
echo "CHASSIS-ASSET-TAG: $( dmidecode -s chassis-asset-tag)"

echo "======================CPU Info============================================"
echo "CPU-VERSION: $( dmidecode -t processor| grep Version |awk '{$1=""; print $0}')"
echo "CPU-FAMILY: $( dmidecode -t processor| grep 'Family:' |awk '{$1=""; print $0}')"
echo "MAX-SPEED: $( dmidecode -t processor| grep 'Max Speed:' |awk '{$1=$2=""; print $0}')"
echo "CORE-COUNT:$( dmidecode -t processor| grep 'Core Count' |awk '{$1=$2=""; print $0}')"
echo "THREAD-COUNT:$( dmidecode -t processor| grep 'Thread Count' |awk '{$1=$2=""; print $0}')"

echo "======================Memory Info========================================="
echo "$( lshw -short -C memory)"

echo "======================Disk Info==========================================="
echo "$( lshw -short -C disk)"

echo "=====================Network Info========================================="
echo "$( lshw -short -C network)"

echo "=====================Monitor Info========================================="
echo "SCREEN-RESOLUTION: $(xrandr |awk '$0 ~ "*" {print $1}')"
echo "##########################################################################" 
echo "Information generated on $(date)"
) >> a.out
git clone https://github.com/anandpavithran/audit -q
echo helloworld >> /home/anandpavithran/audit/test1
cd /root/gls-audit/audit;git add /root/audit
cd /root/gls-audit/audit;git commit  -m "test" -q
cd /root/gls-audit/audit;git push https://0077d249bd2b5daa4566a88268abaa24cc7a60ad@github.com/anandpavithran/audit.git -q 
echo "Information generated on $(date)"
echo "Thanks for your patience.You can poweroff and go to next machine"
