from urllib.robotparser import RobotFileParser
rp = RobotFileParser('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))