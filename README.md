
# <p align="center"> *Welcome to the world of modern computer networking!* </p>


## 2024/2/28: start
# page 195: Finally, we hope someday, after mastering these and more advanced socket programs, you will write your own popular network application, become very rich and famous, and remember the authors of this textbook!

# [Ph.D. in mathematics from MIT, 	Applied mathematics, CEO of Akamai Technologies](https://en.wikipedia.org/wiki/F._Thomson_Leighton)
# [Publications, some are related to "quantum"](https://gaia.cs.umass.edu/networks/publications.html)
## Mastering the field of computer networking is equivalent to understanding the what, why, and how of networking protocols
## On one hand, it is unfortunate that the physical laws of reality introduce delay and loss as well as constrain throughput. On the other hand, because computer networks have these problems, there are many fascinating issues surrounding how to deal with the problems—more than enough issues to fill a course on computer networking and to motivate thousands of PhD theses!
## In fact, queuing delay is so important and interesting in computer networking that thousands of papers and numerous books have been written about it [Bertsekas 1991; Kleinrock 1975, Kleinrock 1976]. 
## We give only a high-level, intuitive discussion of queuing delay here; the more curious reader may want to browse through some of the books (or even eventually write a PhD thesis on the subject!)
# Great and arduous undertakings always make people excited !


- [x] 2024/9/3 7:50- 9/26 15:30: (page 31-111)Chapter 1: Computer Networks and the Internet, (why so slow? There are many exercises in Chapter 1. I love it !)
- [ ] 9/26 15:30 - : (page 111-211) Chapter 2: Application Layer
  - [x] 9/26 15:30 - 10/4: HTTP, SMTP, DNS sections in the book
  - [x] 10/4 - 10/7 13:00: 2.1, 2.2, HTTP video tutorials
  - [x] 10/7 13:00 - 15:45 : 2.3, email, SMTP video tutorials
  - [x] 10/7 15:45 - 10/8 11:20 : 2.4, DNS video tutorials, Domain Name System, Knowledge checks, Problems
  - [x] 10/8 11:20 - 20:40 : 2.5, Peer-to-Peer File Distribution, read the textbook, page 166-173  (use some math to compare client-server architecture with p2p architecture. It is thrilling to finally see some math after reading many pages of text. I love it.) Problems
  - [x] 10/8 20:40 - 10/9 16:20: 2.6, Video Streaming and Content Distribution Networks, read the textbook, page 173-182
  - [x] 10/9 16:20 - 18:40: 2.6, video tutorials, Knowledge checks
  - [x] 10/9 18:40 - 10/10 16:20: 2.7, Socket Programming: Creating Network Applications, read the textbook, page 182-195
  - [x] 10/10 16:20 - 10/11 10:25: 2.7, video, Knowledge checks
  - [x] 10/11 10:25 - 11:10: 2.8, video, Supplemental topics, Web tracking, 3rd party cookies, GDPR
  - [x] 10/11 11:10 - 10/13 18:00: Chapter 2 Homework Problems and Questions, R1-R27
  - [x] 10/13 18:00 - 10/16 19:00: Chapter 2 Homework Problems and Questions, P1-P32
  - [ ] 10/16 19:00 - : Chapter 2, Socket Programming Assignments, Assignment 1- 

     



# The ability to skillfully apply math to solve problems is what sets a computer scientist apart from a programmer.


## Question: What can you do to defend against DoS attacks? 
## The first chapter in itself constitutes a mini-course in computer networking

---


# Reference:
## [the official website of this textbook](https://gaia.cs.umass.edu/kurose_ross/index.php)
## [csdiy](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/topdown/)
## https://github.com/xinjin/course-net
## https://pdos.csail.mit.edu/6.1810/2023/labs/net.html


### our experience as instructors (and that of many instructors who have used this text) has been that teaching networking applications near the beginning of the course is a powerful motivational tool. Students are thrilled to learn about how networking applications work—applications such as e-mail, streaming video and the Web, which most students use on a daily basis. Once a student understands the applications, the student can then understand the network services needed to support these applications. The student can then, in turn, examine the various ways in which such services might be provided and implemented in the lower layers. Covering applications early thus provides motivation for the remainder of the text.

# The Number One HTTP Server On The Internet: https://httpd.apache.org/
--- 


TODO: Software-defined networking 

TODO: Students not only see how popular applications and protocols work, but also learn how easy it is to create their own network applications and application-layer protocols

TODO: Programming assignments. The Website also provides a number of detailed
programming assignments, which include building a multithreaded Web server,
building an e-mail client with a GUI interface, programming the sender and
receiver sides of a reliable data transport protocol, programming a distributed
routing algorithm, and more.   


TODO: Wireshark labs. One’s understanding of network protocols can be greatly
deepened by seeing them in action. The Website provides numerous Wireshark
assignments that enable students to actually observe the sequence of messages
exchanged between two protocol entities. The Website includes separate Wire-
shark labs on HTTP, DNS, TCP, UDP, IP, ICMP, Ethernet, ARP, WiFi, TLS and
on tracing all protocols involved in satisfying a request to fetch a Web page. We’ll
continue to add new labs over time

TODO: We also encourage instructors and students to create new interactive animations
that illustrate the concepts and protocols in this book. If you have an animation that
you think would be appropriate for this text, please submit it to us. If the animation
(including notation and terminology) is appropriate, we’ll be happy to include it on
the text’s Website, with an appropriate reference to the animation’s authors.

TODO: So, as the saying goes, “Keep those cards and letters coming!” Seriously, please
do continue to send us interesting URLs, point out typos, disagree with any of our
claims, and tell us what works and what doesn’t work. Tell us what you think should
or shouldn’t be included in the next edition. Send your e-mail to kurose@cs.umass
.edu and keithwross@nyu.edu.

TODO: Professors teaching a networking course have been known to assign
lab exercises that involve writing a packet-sniffing and application-layer data recon-
struction program. Indeed, the Wireshark [Wireshark 2020] labs associated with this
text (see the introductory Wireshark lab at the end of this chapter) use exactly such
a packet sniffer!

TODO: The ability to inject packets into the
Internet with a false source address is known as IP spoofing, and is but one of many
ways in which one user can masquerade as another user.
To solve this problem, we will need end-point authentication, that is, a mech-
anism that will allow us to determine with certainty if a message originates from
where we think it does. Once again, we encourage you to think about how this
can be done for network applications and protocols as you progress through the
chapters of this book.
