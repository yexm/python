import smtplib
from email.mime.text import MIMEText
def send_mail(sub,content):
    mailto_list=['@126.com']           
    mail_host="smtp.126.com"            
    mail_user="@126.com"                        
    mail_pass=""                           
    mail_postfix="126.com"                    
    me="<@126.com>"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)   
    server = smtplib.SMTP()
    server.connect(mail_host)                           
    server.login(mail_user,mail_pass)               
    server.sendmail(me, mailto_list, msg.as_string())
    server.close()
    return True           
for i in range(1):                             
    if send_mail(str(i) + " : " + str([ "%.2f%% "%(t) for t in range( 0, 40, 5 )]),"11231321313"): 
        print( "done!" )
    else:
        print( "failed!" )
