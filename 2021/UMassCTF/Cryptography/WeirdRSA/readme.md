# Weird RSA

>Wanna take a look at this challenge? I tried the normal decryption for RSA but for some reason it isn't working.
>
>http://static.ctf.umasscybersec.org/crypto/3e057374-8731-4bf5-be5c-c436a8dab580/chall.py
>
>Created by Soul#8230



### solve.py

```
#!/usr/bin/env python3

# Imports
import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

sys.setrecursionlimit(5000)

# Parameters
N = 18378141703504870053256589621469911325593449136456168833252297256858537217774550712713558376586907139191035169090694633962713086351032581652760861668116820553602617805166170038411635411122411322217633088733925562474573155702958062785336418656834129389796123636312497589092777440651253803216182746548802100609496930688436148522617770670087143010376380205698834648595913982981670535389045333406092868158446779681106756879563374434867509327405933798082589697167457848396375382835193219251999626538126258606572805220878283429607438382521692951006432650132816122705167004219371235964716616826653226062550260270958038670427
C = 14470740653145070679700019966554818534890999807830802232451906444910279478539396448114592242906623394239703347815141824698585119347592990685923384931479024856262941313458084648914561375377956072245149926143782368239175037299219241806241533201175001088200209202522586119648246842120571566051381821899459346757935757111233323915022287370687524912870425787594648397524189694991735372527387329346198018567010117587531474035014342584491831714256980975368294579192077738910916486139823489975038981139084864837358039928972730135031064241393391678984872799573965150169368237298603189344477806873779325227557835790957023000991
E = 0x10001
# I used Fermat's factorisation method to get p and q using SAGE
P = 135566004969921829046861317679102794894163252891621004552763069255612086965641424719754859767153782381891044077537624735662301899417143962916558791489710971298124937969427903581890089403413545652984524659790357002447801666607195021452029447206533810446315939039775701027454771450154054624400219767469987538497
Q = 135566004969921829046861317679102794894163252891621004552763069255612086965641424719754859767153782381891044077537624735662301899417143962916558791489710971298124937969427903581890089403413545652984524659790357002447801666607195021441224446867180097273643121640903324702747770969633717818870639347019154977691

# LUCRSA Cryptosystem (based on second order Lucas sequence (!))
# See https://www.researchgate.net/publication/26623030_A_New_Computation_Algorithm_for_a_Cryptosystem_Based_on_Lucas_Functions
D = C**2 - 4
LS_P = gmpy2.legendre(D,P)
LS_Q = gmpy2.legendre(D,Q)

# Get that decryption bread
d = gmpy2.invert(E, gmpy2.lcm(P-LS_P, Q-LS_Q))

# If you can, prevent v_dict{} from initialising again as it'll save you time for future computations :)
v_dict = {}

# Function I got from Soul, what a nice guy!
def v(n):
    if n == 0:
        return 2
    if n == 1:
        return m
    if n in v_dict.keys():
        return v_dict[n]
    if(n % 2 == 0):
        ret = (pow(v(n // 2), 2, N) - 2 * pow(Q, n, N)) % N
    else:
        ret = (m * pow(v(n // 2), 2, N) - Q * v(n // 2) * v((n // 2) - 1) - m * pow(Q, n, N)) % N
    v_dict[n] = ret
    return ret

m = C; Q = 1

print('Capturing the flag...')
print()

flag = v(d)
print('Got it!')
print(long_to_bytes(flag))

# b'UMASS\\{who_said_we_had_to_multiply_117a1b8a68814dc478ad78bc67d7d7d4\\}'
# :)
```