#!/bin/bash
#i can send mail to your email

export PATH=/usr/sbin:/usr/bin:$PATH
obj=`date +"%m%d"`"mycar"
users=(
"你的邮箱1"
"你的邮箱2"
"你的邮箱3"
)

for mails in ${users[@]}
do
	echo 'From: pycar' > mailbody
	echo "Bcc:<${mails}>">> mailbody
	echo -e 'Subject: '$obj'\nContent-Type: text/html\n' >> mailbody
	cat /root/pycar/newurl | grep -v ^$|sed '/Now URL/d'| while read oneline
	do
		filename=`echo $oneline | grep -P '(?i)tumblr_.*?(?=\.|$)' -o`
		echo -e '<p ><video style="width:540px;height:304px" poster="https://media.tumblr.com/'$filename'_frame1.jpg" controls><source src="'$oneline'" type="video/mp4"><a href="'$oneline'">'$oneline'</a></video></p>\n' >> mailbody
	done

	/usr/sbin/sendmail -t < mailbody
	rm -f mailbody
done
