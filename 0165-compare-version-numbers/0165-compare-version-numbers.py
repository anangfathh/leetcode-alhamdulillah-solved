class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        while len(ver1) < len(ver2):
            ver1.append('0')
        while len(ver2) < len(ver1):
            ver2.append('0')
        
        for i in range(len(ver1)):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            if int(ver1[i]) > int(ver2[i]):
                return 1
            
        return 0