import numpy as np
import matplotlib as mplt 
import matplotlib.pyplot as plt
a=[1,2,1,1]
b=[0,0,1,0]
 
def f(x):
    return(1+np.cos(x+2))
    
def g(x):
    return(np.sin(x)/8+1/2-np.cos(3*x)/8)
    
def ru(t):
    return (f(t),g(t))
'''
motif() renvoie le graphe de l'arc paramétré (I,ru) où I est un intervalle.
'''
def motif():
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')
    plt.title('arc paramétré(1+cos(x+1),sin(x)/8+1/2-cos(3x)/8)')
    
'''
 groupe1(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses.
'''   
def groupe1(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)                                      
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1) 
    plt.grid(True)#affiche un quadrillage
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    plt.title(' groupe <T>')#affiche le titre du graphe
    plt.show()
    
'''
 groupe2(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses et toute réflexion verticale par rapport à l'axe x=L/2(ou un multiple entier).
'''    
def groupe2(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.title(' groupe <T,Rv>')#affiche le titre du graphe
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=reflexion_verticale(ru(t)[0],ru(t)[1],L/2)#affiche graphiquement la réflexion du motif de départ par rapport à l'axe x=L/2
    translation(w,z,n,L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(ru(t)[0])):
        ru(t)[0][i]=2*(L/2)-ru(t)[0][i]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()
'''
 groupe3(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses et toute réflexion horizontale par rapport à l'axe des abscisses.
'''    
def groupe3(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.title('<T,Rh>')#affiche le titre du graphe
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=reflexion_horizontale(ru(t)[0],ru(t)[1])#affiche graphiquement la réflexion du motif de départ par rapport à l'axe des abscisses
    translation(w,z,n,L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(ru(t)[1])):
        ru(t)[1][i]=-1*ru(t)[1][i]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()
'''
 groupe4(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses et toute symétrie glissée de longueur L/2.
'''        
def groupe4(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.title('<T,Sg>')#affiche le titre du graphe
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=symetrie_glissee(ru(t)[0],ru(t)[1],L)#affiche graphiquement la réflexion glissée de longueur L/2 du motif de départ
    translation(w,z,n,L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(ru(t)[0])):
        ru(t)[0][i]=ru(t)[0][i]-L/2
    for i in range(0,len(ru(t)[1])):
        ru(t)[1][i]=-1*ru(t)[1][i]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()
'''
 groupe5(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses et toute symétrie centrale par rapport au point (L/2,0).
'''       
def groupe5(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.title('<T,Rotation180>')#affiche le titre du graphe
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=symetrie_centrale(ru(t)[0],ru(t)[1],L/2)#affiche graphiquement la symétrie centrale par rapport au point (L/2,0) du motif de départ
    translation(w,z,n,L)#affiche graphiquement n motifs(de la symétrie centrale) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la symétrie centrale) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(ru(t)[0])):
        ru(t)[0][i]=2*(L/2)-ru(t)[0][i]
    for i in range(0,len(ru(t)[1])):
        ru(t)[1][i]=-1*ru(t)[1][i]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()
'''
 groupe6(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses, toute réflexion verticale par rapport à l'axe L/2(ou un multiple) et toute symétrie glissée de longueur L/2.
'''     
def groupe6(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.title('<T,Sg,Rv>')#affiche le titre du graphe
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=symetrie_glissee(ru(t)[0],ru(t)[1],L)#affiche graphiquement la réflexion glissée de longueur L/2 du motif de départ
    translation(w,z,n,L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(ru(t)[0])):
        ru(t)[0][i]=ru(t)[0][i]-L/2
    for i in range(0,len(ru(t)[1])):
        ru(t)[1][i]=-1*ru(t)[1][i]#le motif a pour coordonnées celles qu'il avait au départ
    W,Z=reflexion_verticale(ru(t)[0],ru(t)[1],L/2)#affiche graphiquement la réflexion du motif de départ par rapport à l'axe x=L/2
    translation(W,Z,n,L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur L selon l'axe des abscisses
    translation(W,Z,n,-L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur -L selon l'axe des abscisses
    U,V=symetrie_glissee(W,Z,L)#affiche graphiquement la réflexion glissée de longueur L/2 du motif qui a subit la réflexion verticale
    translation(U,V,n,L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur L selon l'axe des abscisses
    translation(U,V,n,-L)#affiche graphiquement n motifs(de la réflexion glissée) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(U)):
        U[i]=U[i]-L/2
    for i in range(0,len(V)):
        V[i]=-1*V[i]
    for i in range(0,len(W)):
        W[i]=2*(L/2)-W[i]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()
'''
 groupe7(ru,n,L) prend pour argument la fonction ru et renvoie graphiquement une frise de période minimale L, constituée de blocs élémentaires de longueur L répétés n fois, dont le motif principale est la courbe représentative de la fonction ru. Cette frise reste inchangée par toute translation de longueur L selon l'axe des abscisses, toute réflexion verticale par rapport à l'axe L/2(ou un multiple) et toute réflexion horizontale par rapport à l'axe des abscisses.
'''    
def groupe7(ru,n,L):
    x=np.arange(0,10,0.1)
    t=np.arange(0,11,0.1)
    plt.plot(ru(t)[0],ru(t)[1],color='r')#affiche graphiquement l'arc paramétré servant de motif de départ
    plt.title('<T,Rv,Rh>')#affiche le titre du graphe
    plt.plot(x,[1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière supérieure de la frise (droite y=1)
    plt.plot(x,[0 for k in x],'_',color='b',linewidth=1)#affiche graphiquement en tiret l'axe des abscisses coupant en 2 parties égales la frise
    plt.plot(x,[-1 for k in x],color='b',linewidth=2)#affiche graphiquement la frontière inférieure de la frise (droite y=-1)
    plt.grid(True)#affiche un quadrillage
    plt.ylim(-2,2)#le graphe est limité selon l'axe des ordonnées de -2 à 2
    plt.xlim(0,10)#le graphe est limité selon l'axe des abscisses de 0 à 10
    translation(ru(t)[0],ru(t)[1],n,L)#affiche graphiquement n motifs(du départ) translatés de longueur L selon l'axe des abscisses
    translation(ru(t)[0],ru(t)[1],n,-L)#affiche graphiquement n motifs(du départ) translatés de longueur -L selon l'axe des abscisses
    w,z=reflexion_verticale(ru(t)[0],ru(t)[1],L/2)#affiche graphiquement la réflexion du motif de départ par rapport à l'axe x=L/2
    translation(w,z,n,L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur L selon l'axe des abscisses
    translation(w,z,n,-L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(w)):
        w[i]=2*(L/2)-w[i]#le motif a pour coordonnées celles qu'il avait au départ
    W,Z=reflexion_horizontale(ru(t)[0],ru(t)[1])#affiche graphiquement la réflexion du motif de départ par rapport à l'axe des abscisses
    translation(W,Z,n,L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur L selon l'axe des abscisses
    translation(W,Z,n,-L)#affiche graphiquement n motifs(de la réflexion) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(Z)):
        Z[i]=-1*Z[i]#le motif a pour coordonnées celles qu'il avait au départ
    U,V=symetrie_centrale(W,Z,L/2)#affiche graphiquement la symétrie centrale par rapport au point (L/2,0) du motif de départ
    translation(U,V,n,L)#affiche graphiquement n motifs(de la symétrie centrale) translatés de longueur L selon l'axe des abscisses
    translation(U,V,n,-L)#affiche graphiquement n motifs(de la symétrie centrale) translatés de longueur -L selon l'axe des abscisses
    for i in range(0,len(V)):
        V[i]=-1*V[i]
    for k in range(0,len(U)):
        U[k]=2*(L/2)-U[k]#le motif a pour coordonnées celles qu'il avait au départ
    plt.show()

'''
reflexion_horizontale(x,y) prend pour arguments les coordonnées(x,y) des points d'une courbe du plan R^2 et renvoie graphiquement les symétriques des points de cette courbe par rapport à l'axe des abscisses 
'''
def reflexion_horizontale(x,y):
    for i in range(0,len(y)):
        y[i]=-1*y[i]#changement des coordoonnées des points constituant le motif de départ
    plt.plot(x,y,color='r')#affiche graphiquement le nouveau motif
    return(x,y)
    
'''
reflexion_verticale(x,y,u)  prend pour arguments les coordonnées(x,y) des points d'une courbe du plan R^2 et l'axe x=u sur lequel on veut appliquer la fonction et renvoie graphiquement les symétriques des points de cette courbe par rapport à l'axe x=u
'''
def reflexion_verticale(x,y,u):
    for i in range(0,len(x)):
        x[i]=2*u-x[i]#changement des coordoonnées des points constituant le motif de départ
    plt.plot(x,y,color='r')#affiche graphiquement le nouveau motif
    return(x,y)
    
'''
translation(x,y,n,L) prend pour arguments les coordonnées(x,y) des points d'une courbe du plan R^2 et renvoie graphiquement n-1 translations de L selon l'axe des abscisses de ces points de la courbe 
'''
def translation(x,y,n,L):
    p=0
    while p<n:#tant que le motif n'a pas été translaté n fois
        for i in range(0,len(x)):
            x[i]=x[i]+L#le motif est translaté de L selon l'axe des abscisses
        p=p+1
        plt.plot(x,y,color='r')#affichage graphique du motif translaté
    for i in range(0,len(x)):
        x[i]=x[i]-L*p#le motif a pour coordonnées celles qu'il avait au départ
    return(x,y)

'''
symetrie_glissee(x,y,L) prend pour arguments les coordonnées(x,y) des points d'une courbe du plan R^2 et renvoie graphiquement  les symétriques des points de cette courbe par rapport à l'axe des abscisses translatés de L/2 selon l'axe des abscisses
'''
def symetrie_glissee(x,y,L):
    for i in range(0,len(y)):
        y[i]=-1*y[i]#le motif subit une réflexion par rapport à l'axe des abscisses
    for k in range(0,len(x)):
        x[k]=x[k]+L/2#le motif est translaté de L/2 selon l'axe des abscisses
    plt.plot(x,y,color='r')#affichage graphique du nouveau motif
    return(x,y)
    
'''
symetrie_centrale(x,y,u) prend pour arguments les coordonnées(x,y) des points d'une courbe du plan R^2 et renvoie graphiquement les symétriques des points de cette courbe par rapport au point d'intersection de l'axe des abscisses et l'axe x=u
'''
def symetrie_centrale(x,y,u):
    for i in range(0,len(y)):
        y[i]=-1*y[i]#le motif subit une réflexion par rapport à l'axe des abscisses
    for k in range(0,len(x)):
        x[k]=2*u-x[k]#le motif subit une réflexion par rapport à l'axe x=L/2
    plt.plot(x,y,color='r')#affichage graphique du nouveau motif
    return(x,y)