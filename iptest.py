import socket, subprocess, re
import smtplib
def get_ipv4_address():
    """
    Returns IP address(es) of current machine.
    :return:
    """
    fromaddr = 'FROM@gmail.com'
    toaddrs = 'TO@gmail.com'

    p = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
    ifc_resp = p.communicate()
    patt = re.compile(r'inet\s*\w*\S*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    resp = patt.findall(ifc_resp[0])
    print resp
    ip = resp[0]
    msg = str(ip)

    username = 'YOURUSERNAME@gmail.com'
    password = 'YOURPASSWORD'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


get_ipv4_address()
