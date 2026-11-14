# coding: ascii
# tiny-chess-01 entrypoint: ASCII-armored self-extracting loader.
# The chess engine source is lzma-compressed (FORMAT_ALONE, lc3 lp0
# pb0) and base85-armored; the armor text is split across this file
# (D, first chunk) and payload.py (payload.E, second chunk). At
# startup the two chunks are concatenated, base85-decoded back to
# the exact compressed bytes, decompressed, and exec'd in place.
# Resubmit build: the engine clears its search-path set at the
# start of every root search (a stale set silently scored live
# lines as draws), keeps its transposition table between moves
# under a size cap, and no longer treats the a1 square as an
# en-passant target when no en-passant square is set.
import lzma,sys
from base64 import b85decode
from os.path import dirname,abspath
sys.path.insert(0,dirname(abspath(__file__)))
import payload
D="""0{{RJ0RR90|NsC0{{S?cCB?5^w9NaJG8}0oT~2%M@`<8lV+IS8+`Rv|H>a}$L{>ef%F@E^!qKYi;;gsarEK&63&Kr1d-Y|lSgT#-W$e%YNc-aFie$Q*>)OL-Eg-(TPEyc!NzWSBGaY9i(8`!YtZzm9zqpVds^2$V=>FNxGqL!m=e(6ZY9xlc7bk21-SJR{%`hR3z;NI1XbOudRcj%S;{K*gDPrUAU}|2SznYP93k(^5<FFc~P@;@iW(Q07kAOr+i+h2OxNf15E}?=~VDx?M7IzDES_Y%d(BoGCS6(T2y=yI1%T`#8*{doeeNfa(-&A$wrxba7GV=Orm$s~@tiT~cg~Se)YeV@gAX=<BaQ@zTe31aZH_j666PkHecPit|js&B8I4?gxTscg*9O6Pk3&_9>XW=Ttwxk**4PF9R0kd^(G!Ka0ZdWe}eTRj^W_l9vH?tv=$EJl|ZwP4J+1a_Hkr*OqQC5rYe&XKHLqE5DY!8o)Oav$0SOER%cpj}HSLS(v4w1tMTUUZP@N|?=VgR0ifxhJ{RIz8OMwA**?e%3M&7$zbU1K2oggC(g^F-NvQm|mFVu_`uUIk$gIe15a?{A%T7;PXE@Uh!FeHxCS^N^M{LrbK4dmxy*pu>+hi#XBaob&AY&4Fz$r~6t#SC5GJs|bYX9)a~mY{JpjT{h=v1{i@q*vne5p@cKCCZa@WV2`2^vcfsyM7z*cxYH!@r<=mG^YH_=^Kd*Ya)}qT&XbvHL|RlkHd_ljMLm*<^w>O5fu6hh=+x-9S(-+j?HOBkY((UEoe?sNiP`(sGxQ*TYwBI{n(Y;wSn63hnaj8%dAslSM6nlp3Qv}OTu1sMS%uW?hMf(aaR}v|8ltxbzQ$kfAwy6p;IyC4x=H6mvr;>nL?Gp^Q^zI}g#naO1|Q1*=EWXzvZ}@DF^6W!46ZHC?<3Tm2R9box>3rqI(P@3VM^B*`?f%u%Y`sK0-}|K(*(TFTfj+~YxO%xR(?K3ClB47<7_KB>eG;k`&i~EXA+!2yAM%-tP}6-@<B|@&Wwq6ZZG#Lyg<^Raxb;Y|A&_(!PpscKTA&<PDqPS63R)Ni&>`il*cUXy*nuZSO{d+^giKVWQ6QWlR)<?|7_w=SHLSO8SbUfKlgi}Fa5qWEjfEE4V1%SK`Q73td#V?LrZ-6M}GNJsyss4q)nIUW46TPl25;l6>19a6yd5ASrBU-t}!Q%w!vf2mR(Nk!K9N?1>qh346T@pd4)IV?wZ4+6iHJ$7<<IEV|;1&UC9VUqNEIccUUQ3EEQeQaIU%#7KQojxZ8CGsB8)PQk!s8pvNEa72SUT$fIqF_g_E%lAK=$IFldJ!O5rQc#8!f8R^Fc9$0@qd-J`poC^bL1Ni7ZUG)nwk0ZQ2X>!fw#R?@pdslnu>QIm2NKx;is&BnrL>-=>0Siw{+iIt=vYnITNDh%2r*^KnwOT7a>A=yh4l7MNXWhDqxP>?XM2sjEcg5l8(6QC1YTur}=~;|zEQmI9qMsJ`9sZg6t7vVp)PA@4!}eF^KC>bENb+xiRqF8(ql9W+utquoK{kO5;|`Yo#awV8l&A7Q8lvOnVt{fr?%uXcP2c^0(E8RB^{-JOWb*qVs3bNR%fwb`oAO||s_u~PgXA5lzc65k50@eaBkZ>$p!)cu^hi32Ggd~9SGQh&LU`&i{(Lws_-SZyPiT1I0w@hbW@BV`vA#y|POeMp_*aV23r&4v+Odo!hSb}h${l}#aL11JK~xO3{jIh5g2;8~8R|nTP7`jz<c$V9?sB;EM3y(Q1WbnOlt|k?Ap6hdO9OdME#|WHyY`H0#3}MuUkLv4oyAf8{yG@@E=@b(%pI7R)5d16ECUMYxfed)8(0DP@5cgeUtv@yo}*S%OGfA`ervMC{kg3fNNUN+E6M2knMW@y-U?ORx#QNgj_0wCkciE?uj37J5ytbk8UgVc+uqVKT1>Zujy~cJ^1`y=as-p!j)S~?v{T!~ScR9`sH*m_9DL(LdZCKuB2Sf1s-(^*>>!{aGPph>>%3347qy>l9`cH<AFS7T%LeoSwy#gPz}PMKcM_udeLXU)o<1zfax#WK4A*1cz8vAE##6rC6P`&ksG4UTXrZ1DB&4R&p^N~o_(nE$Hcr>ams}zwd?nKqhsRJ%CHQH+R3u$re-8u-veTVL2F%gMgOiJ`_YmP3__x{!%!t74T78DOw||;vY4L@+j8o+EckSYsybYUrws?JNgR(2XF98BJoVPzVM?9lJ_|0Da`BXIzD><G_7VOPWS6JariR8vH*NICq4$rKO6NL=FJ6A@OAQ@Y~x=JkV5Qx&+sPr8@?!^(q4`~pn)g}^g%<h2Ga=rW&N(34s$3R}4f?T5bBXpI5g0Q*&0#nq~TvSh)XG!=^7i70kQDdaH_o#g+>^kXG5wx^!^t**~HLdVMuMao6eYQxac$*dXoyP(0(S>Z?j9W6M?c+|=gUM(eS=VT84J=0ik9cWbULSx@_Z?v&c=MZtppk2dP!-g1OJ`cEG>Nph-&a|0B8{COA_Swx;3V50RAl!g;2C#3Z$N;deRjSxJU>xyRA_UnM2$~Q`p|?57UXlWp>aI2kRQs%ZR2B^F4E%`eNa5HXzTl}WjAi^T0CxHjlMz4Cfe_#EH}mf%v{TH"""
exec(lzma.decompress(b85decode(D+payload.E),format=lzma.FORMAT_ALONE))
