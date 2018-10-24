import argparse
import os
import subprocess

content = r'''\documentclass{article}
\title{Lorem Ipsum}
\author{Dongzhuoran Zhou}
\usepackage{graphicx}
\begin{document}
\maketitle
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla orci enim, elementum vitae bibendum non, tincidunt id leo. Nulla ultrices nisl id elit imperdiet mollis. Maecenas at egestas nisl, eu tincidunt diam. Donec rutrum, purus eu molestie maximus, lectus libero tristique velit, non sollicitudin tortor est ut augue. Integer hendrerit mollis vulputate. Donec placerat pretium fermentum. Mauris dictum ut turpis eu fermentum. Morbi vitae feugiat tellus. In interdum ultrices velit, a iaculis tortor. Fusce in eros luctus, condimentum justo nec, volutpat nunc. Morbi interdum arcu lectus, sed iaculis metus volutpat ut. Aliquam in scelerisque ex. Donec nisi lorem, tristique pharetra magna eu, consectetur fringilla arcu. Phasellus non pretium erat, sed molestie libero.

Aliquam lobortis turpis velit, id dapibus risus facilisis eget. Nunc laoreet enim ac ligula elementum, vitae lobortis sapien posuere. Vestibulum a dolor enim. Fusce est enim, interdum ut elit in, convallis suscipit justo. Maecenas auctor in ligula at viverra. Aliquam quam nibh, sagittis laoreet egestas vitae, facilisis ac sapien. Nulla massa leo, iaculis ac vestibulum eget, iaculis vel ante. Nullam elementum dictum velit, et finibus ligula vestibulum a. Vivamus sed risus elementum, consequat metus sit amet, efficitur quam. Nullam efficitur condimentum dolor at consequat. Fusce at eros dui. Proin ac enim dictum, mattis dolor vel, varius arcu. Nullam sit amet hendrerit dui. Donec orci metus, blandit non congue et, varius quis ipsum.

Phasellus vitae pulvinar quam. Phasellus congue massa lacinia, aliquam dui ut, euismod metus. Sed imperdiet et leo ut varius. Ut interdum vehicula enim, et varius felis egestas nec. Integer eu nunc in nunc lacinia posuere. Donec eget egestas sem. Nulla feugiat arcu ut sem mollis vehicula. Mauris imperdiet sem vel nisl porttitor suscipit. Vivamus gravida efficitur maximus. Morbi velit nunc, fermentum at finibus nec, iaculis sed erat. Etiam vehicula lacus sed elit fringilla, eu auctor justo auctor. Suspendisse a lectus nec est ultrices condimentum. Curabitur tempor vestibulum faucibus. In luctus volutpat posuere. Pellentesque vitae iaculis erat. Aenean vel eleifend arcu, a vulputate ex.

Mauris euismod erat tellus. Aliquam luctus sit amet nisi vel placerat. Nullam dignissim elit at semper commodo. Pellentesque enim nisl, euismod eu justo id, dictum feugiat lorem. Donec sit amet cursus urna. Nam commodo ligula risus, eu dictum ex hendrerit vitae. Nulla a tempor tortor. Nam in magna quis turpis ultrices tincidunt non in ante.

Aliquam sed tempus massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam accumsan molestie mi at bibendum. Vivamus rhoncus in magna non tincidunt. Nam nec gravida nulla. Morbi vulputate neque enim, vel fermentum diam commodo id. Curabitur placerat tortor eget mi fringilla, quis faucibus libero semper. Phasellus eget condimentum urna. Sed lobortis tincidunt augue vitae rutrum.

\includegraphics[width = .8\textwidth]{Doggy.jpg}
\end{document}
'''




with open('LatexProject.tex','w') as f:
    f.write(content)



cmd = ['Xelatex', '-interaction', 'nonstopmode', 'LatexProject.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('LatexProject.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

#os.unlink('cover.tex')
#os.unlink('cover.log')

