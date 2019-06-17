#!/bin/bash
#By Brian Vanderwende and Thomas Hilton Johnson III
#Reference: Leland Barton, https://stackoverflow.com/questions/31871858/cant-redirect-command-output-to-file
#Reference: https://www.cyberciti.biz/faq/how-to-use-sed-to-find-and-replace-text-in-files-in-linux-unix-shell/
#Reference: https://stackoverflow.com/questions/48817042/how-to-find-a-with-regular-expressions
#Reference: https://regexr.com
#Reference: https://unix.stackexchange.com/questions/345132/sed-command-to-replace-word1-word2-to-nothing
#Reference: https://lin-chen-va.github.io/Linux/regularExpression.htm

#module avail &> result_module_output.txt
#sed -i "s/\([A-Z][a-z]*\)|\(\([A-Z]:\)*\)//g" result_module_output.txt

module av |& xargs -n1 | grep -e "^.*/.*" &> result_module_output.txt
