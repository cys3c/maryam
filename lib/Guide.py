from color.dtectcolors import Style,Fore,Back,init;
init();
GR =   Style.DIM+Fore.WHITE;   # gray
W  =   Style.BRIGHT+Fore.WHITE # gray and white
Y  =   Fore.YELLOW             # yellow
C  =   Style.BRIGHT+Fore.GREEN # green
import sys
def options():
        print 
        print C+"[1] >"+W+" Information  "
        print C+"[2] >"+W+" About "
        print C+"[99] >"+W+" exit "
        print C+"[100] >"+W+" options "
        print
def op_info():
        print
        print C+"[1] >"+W+" whois => "+Y+"Lookup information on a Domain or IP address."
        print C+"[2] >"+W+" trace route => "+Y+"Trace the servers between ViewDNS and a remote host."
        print C+"[3] >"+W+" scan port (service) => "+Y+"Finding open ports and active service on the server."
        print C+"[4] >"+W+" scan port (fast) => "+Y+"Finding open ports on the server..Fast."
        print C+"[5] >"+W+" scan port (auto) => "+Y+"Finding open and important ports. Automatic."
        print C+"[6] >"+W+" reverse ip => "+Y+"Show all sites on the server."
        print C+"[7] >"+W+" ping => "+Y+"Test the latency of a remote system."
        print C+"[8] >"+W+" ip api => "+Y+"Find the geographic location of an IP Address."
        print C+"[9] >"+W+" http header => "+Y+"View the HTTP headers returned by a domain."
        print C+"[10] >"+W+" cloud flare => "+Y+"Find sub-active domains bound to the list."
        print C+"[11] >"+W+" dnslookup => "+Y+"View all DNS records for a specified domain."
        print C+"[12] >"+W+" domain map => "+Y+"Viewing all DNS records for your domain is displayed in the image format."
        print C+"[13] >"+W+" reverse whois => "+Y+"Find domain names owned by an individual or company."
        print C+"[14] >"+W+" ip history => "+Y+"Show historical IP addresses for a domain."
        print C+"[15] >"+W+" dns report => "+Y+"Provides a complete report on your DNS settings."
        print C+"[16] >"+W+" find shared dns => "+Y+"Find more targets with a DNS server shared record search."
        print C+"[17] >"+W+" trace ip using mtr => "+Y+"Trace the Internet connection path using the mtr traceroute tool."
        print C+"[18] >"+W+" reverse ns => "+Y+"Find all sites that use a given nameserver."
        print C+"[19] >"+W+" reverse mx => "+Y+"Find all sites that use a given mail server."
        print C+"[20] >"+W+" dns propagation => "+Y+"Check whether recent DNS changes have propagated."
        print C+"[21] >"+W+" find records => "+Y+"Find forward DNS (A) records for a domain."
        print C+"[22] >"+W+" extract links => "+Y+"Find all web page links."
        print C+"[23] >"+W+" Crawler => "+Y+"Find all web page links."
        print C+"[24] >"+W+" robot => "+Y+"Extract important tags on the web page."
        print C+"[25] >"+W+" admin finder asp => "+Y+"Finding the page of ASP admin pages is limited to the page list."
        print C+"[26] >"+W+" admin finder php => "+Y+"Finding the page of PHP admin pages is limited to the page list."
        print C+"[27] >"+W+" admin finder js => "+Y+"Finding the page of JS admin pages is limited to the page list."
        print C+"[28] >"+W+" admin finder cgi => "+Y+"Finding the page of CGI admin pages is limited to the page list."
        print C+"[29] >"+W+" admin finder brf => "+Y+"Finding the page of BRF admin pages is limited to the page list."
        print C+"[30] >"+W+" hashAnalizer => "+Y+"Find the type of your hashed algorithm."
        print C+"[31] >"+W+" hashDeCrypter => "+Y+"Your hash flip is limited to 7 algorithms."
        print C+"[32] >"+W+" frameworks Activ => "+Y+"find all Frameworks Activ in Web Server."
        print C+"[98] >"+W+" Back "
        print C+"[99] >"+W+" exit "
        print C+"[100] >"+W+" options "
        print GR+'[Type 98 to Back]'+W
        print GR+'[Type 99 to Exit]'+W
        print GR+'[Type 100 to options]'+W
        print
if __name__ == '__main__':
        print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[1])
        sys.exit(1)