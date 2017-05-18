import projekt as prj
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages('wykresy.pdf') as pdf:
    x=prj.t
    y=prj.q
    z=prj.Gp
    
    plt.figure("JEDNOSTKI NA WYKRESACH: q[MMscf/day], t[day], Gp[10^3MMscf]")
    
    plt.subplot(331)
    plt.plot(x,y)
    plt.title('xy --> q(t)')
    plt.grid(True)
    
    plt.subplot(332)
    plt.semilogy(x,y)
    plt.title('semilogy --> q(t)')
    plt.grid(True)
    
    plt.subplot(333)
    plt.loglog(x,y)
    plt.title('loglog --> q(t)')
    plt.grid(True)
    
    ######################################
    
    plt.subplot(337)
    plt.plot(z,y)
    plt.title('xy --> q(Gp)')
    plt.grid(True)
    
    plt.subplot(338)
    plt.semilogy(z,y)
    plt.title('semilogy --> q(Gp)')
    plt.grid(True)
    
    plt.subplot(339)
    plt.loglog(z,y)
    plt.title('loglog --> q(Gp)')
    plt.grid(True)
    
    plt.show()
    pdf.savefig()