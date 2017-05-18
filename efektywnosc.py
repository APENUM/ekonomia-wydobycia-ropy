import projekt as prj
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rdm

cena_gazu = np.zeros([10000,30])
cena_gazu[:,0]=0.9
plt.figure("cena gazu")
for row in range(0,10000):
    for col in range(1,30):
        cena_gazu[row,col] = cena_gazu[row,col-1]+cena_gazu[row,col-1]*np.random.triangular(-0.05,0,0.05)
    if row%100==0:
        plt.plot(cena_gazu[row,:])
plt.show()
    
stopa_dyskotowa=0.07
koszt_zmienny=0.054; koszt_zmienny=rdm.triangular(0.05,0.054,0.06,10000).reshape(10000,1)
stawka_amortyzacji=0.07
przyrost_kosztow_stalych=96.255
oplata_eksploatacyjna_gazu=5.89/1E3
stawka_podatku=0.19
naklady_inwestycyjne=90*1e06; naklady_inwestycyjne=rdm.normal(90*1e06,1500000,10000).reshape(10000,1)
koszty_stale=2025000

Q = prj.q*365/35.315*1E6/1
Qrdm=[]
for Q in Q:
    Qrdm.append(rdm.normal(Q,Q*0.15,10000))
wydobycie_gazu=np.transpose(Qrdm)

przychody =  wydobycie_gazu * cena_gazu
oplaty_eksploatacyjne = wydobycie_gazu * oplata_eksploatacyjna_gazu
koszty_zmienne = wydobycie_gazu * koszt_zmienny
amortyzacja  = stawka_amortyzacji * naklady_inwestycyjne
suma_kosztow = amortyzacja + koszty_stale + koszt_zmienny + oplaty_eksploatacyjne

zysk_brutto = przychody - suma_kosztow
podatek = stawka_podatku * zysk_brutto
zysk_netto = zysk_brutto - podatek; zysk_netto=np.insert(zysk_netto,[0],0,axis=1)

TiempoDeAmor=naklady_inwestycyjne[0]/(naklady_inwestycyjne[0]*stopa_dyskotowa)
TiempoDeAmor=TiempoDeAmor.astype(int)

#naklady_inwestycyjne=naklady_inwestycyjne.reshape(1,10000)
cash_flow = zysk_netto
cash_flow[:,0]=-naklady_inwestycyjne.reshape(1,10000)
#cash_flow[:,1::]=cash_flow[:,1::]+=amortyzacja
cash_flow[:,1:TiempoDeAmor+1]+=amortyzacja

plt.figure("cum_cash_flow")
cum_cash_flow=[]
for i in range(10000):
    cum_cash_flow.append(np.cumsum(cash_flow[i,:]) - naklady_inwestycyjne[i])
    if i%100==0:
        plt.plot(cum_cash_flow[i])
plt.show()
print np.shape(cum_cash_flow)

plt.figure("cash_flow")
zero=np.zeros(31)
for i in range(0,1000,10):
    plt.plot(cash_flow[i,:])
plt.plot(zero)
plt.show()

NPV=[]; IRR=[]
for i in range(10000):
    NPV.append(np.npv(stopa_dyskotowa,cash_flow[i,:]))
    IRR.append(np.irr(cash_flow[i,:]))
NPV=np.array(NPV); IRR=np.array(IRR)

plt.figure("NPV")
plt.hist(NPV, bins=100); plt.show()

plt.figure("IRR")
plt.hist(IRR, bins=100); plt.show()

#wiela lat bedzie sie ekplatowac?
# - kiej keszflol spadnie ponizy zera:
wiela=[]
for i in range(10000):
    wiela.append( len(cash_flow[i,:][cash_flow[i,:]>0]) )
plt.figure("Ile lat eksploatacja bedzie oplacalna?")
plt.hist(wiela, bins=100); plt.show()
#print len(cum_cash_flow[cum_cash_flow>0])
