#Developer：ZhengDeHui
#Developer Time： 2022/8/8 16:46

import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\demo\\exercise', filename))


