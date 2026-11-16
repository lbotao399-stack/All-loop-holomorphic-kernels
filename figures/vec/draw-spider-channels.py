"""Figure 7.1: exact representative Wick channels, drawn with vector code."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    'font.family': 'STIXGeneral',
    'mathtext.fontset': 'stix',
    'font.size': 18,
    'svg.fonttype': 'path',
    'savefig.facecolor': 'white',
})

MATTER = '#35678A'
GAUGE = '#AD742C'
SUPER = '#833A65'
INK = '#222630'
OUTPUT = '#3A576A'
MUTED = '#626A73'

fig, axes = plt.subplots(1, 3, figsize=(16.2, 5.5))
fig.subplots_adjust(left=.025, right=.99, top=.98, bottom=.13, wspace=.07)


def edge(ax, p, q, color=MATTER):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=2.15,
            solid_capstyle='round', zorder=1)


def output(ax, p, q, label, tx, ty, size=21):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=10,
                                lw=1.5, color=OUTPUT, shrinkA=6, shrinkB=3,
                                zorder=2))
    ax.text(tx, ty, label, ha='center', va='center', fontsize=size, color=INK)


def node(ax, p, color, label=None, offset=(.045,-.045), insertion=False):
    if insertion:
        ax.plot(*p, marker='s', markersize=10, markerfacecolor='white',
                markeredgecolor=INK, markeredgewidth=1.8, zorder=5)
    else:
        ax.add_patch(Circle(p, .019, facecolor=color, edgecolor='white',
                            lw=1.1, zorder=5))
    if label:
        ax.text(p[0]+offset[0], p[1]+offset[1], label, fontsize=18,
                ha='left', va='center', color=INK)


def common(ax, panel, n, A, B, wlabel, input_label):
    ax.set_xlim(-.16, 1.12)
    ax.set_ylim(-.18, 1.12)
    ax.axis('off')
    ax.text(.45, 1.065, rf'$({panel})\quad n={n}$', fontsize=20,
            ha='center', va='center', color=INK)
    ax.text(-.105, .40, r'$\bar\partial$', fontsize=29,
            ha='center', va='center', color=INK)
    node(ax,A,SUPER,r'$A$',offset=(.065,.005))
    node(ax,B,INK,insertion=True)
    output(ax,A,(A[0],.825),wlabel,A[0],.925,size=21)
    ax.text(B[0],.045,r'$B=\mathcal{O}$',ha='center',va='center',fontsize=19,color=INK)
    ax.text(B[0],-.080,input_label,ha='center',va='center',fontsize=23,color=INK)


# The label on A is its surviving derivative of W, not a complete Q_n value.
# (a) One arm, length one: three beta-gamma contractions.
ax=axes[0]
A=(.62,.68); B=(.62,.19); v1=(.22,.43)
for p,q in [(v1,A),(v1,B),(A,B)]: edge(ax,p,q)
common(ax,'a',1,A,B,
       r'$\dfrac{\partial^2\bar W}{\partial\gamma_k\,\partial\gamma_j}$',
       r'$\beta^i\beta^j$')
node(ax,v1,MATTER,r'$v_{1,1}$',offset=(-.045,-.070))
output(ax,v1,(.12,.66),r'$\mathsf{c}^D$',.105,.735)

# (b) One arm, length two: the inner c contracts with the b at B.
ax=axes[1]
A=(.67,.68); B=(.67,.19); v2=(.32,.59); v1=(.20,.35)
for p,q in [(v1,v2),(v2,A),(v1,B),(A,B)]: edge(ax,p,q)
edge(ax,v2,B,GAUGE)
common(ax,'b',2,A,B,
       r'$\dfrac{\partial^2\bar W}{\partial\gamma_k\,\partial\gamma_j}$',
       r'$\beta^i\beta^j\mathsf{b}_E$')
node(ax,v1,MATTER,r'$v_{1,1}$',offset=(-.045,-.070))
node(ax,v2,MATTER,r'$v_{1,2}$',offset=(-.050,.070))
output(ax,v1,(.07,.58),r'$\mathsf{c}^D$',.045,.665)

# (c) Two arms, each of length one: both c fields survive.
ax=axes[2]
A=(.52,.68); B=(.52,.19); v1=(.17,.43); v2=(.87,.43)
for p,q in [(v1,A),(v2,A),(v1,B),(v2,B),(A,B)]: edge(ax,p,q)
common(ax,'c',2,A,B,
       r'$\dfrac{\partial^3\bar W}{\partial\gamma_l\,\partial\gamma_m\,\partial\gamma_k}$',
       r'$\beta^i\beta^j\beta^k$')
node(ax,v1,MATTER,r'$v_{1,1}$',offset=(-.045,-.070))
node(ax,v2,MATTER,r'$v_{2,1}$',offset=(-.045,-.070))
output(ax,v1,(.075,.65),r'$\mathsf{c}^D$',.055,.725)
output(ax,v2,(.965,.65),r'$\mathsf{c}^E$',.985,.725)

# Minimal species key. Arrow stubs show the fields left uncontracted.
handles=[Line2D([0],[0],color=MATTER,lw=2.15,label=r'$\beta$--$\gamma$'),
         Line2D([0],[0],color=GAUGE,lw=2.15,label=r'$\mathsf{b}$--$\mathsf{c}$')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.005),
           ncol=2,frameon=False,fontsize=17,handlelength=2.2,columnspacing=2.6)
fig.savefig(HERE/'spider-channels-20261116.pdf',bbox_inches='tight',pad_inches=.08)
