from Crypto.Util.number import *
import libnum
from flag import flag
m=libnum.s2n(flag)

e=65537
p=getPrime(2048)
q=getPrime(2048)

phi=(p-1)*(q-1)
n=p*q
c=pow(m,e,n)

GCD=gcd(p-1,q-1)
hint=phi/GCD

print("c =",c)
print("n =",n)
print("hint=",hint)

'''
c = 548918572159722522767929865993884081082164492286009195879504761164385535413394380346515573138589082475811151249884949132027796060727835931366540512957547484598946951338033492942121877234601646315097424157500221712337398058375776770809529010333956405620717560472054213904575002918129721781115591508525601291375001796943078707791398264769111677252679566310517744960402816362216531474625479211532215702150550579959448670945771700445969397399242235136798885228063177817517744786863763945724704818763307119621861807775593682374422469453049736640627538951648539077132244792766526816703530735560046664282672622060377458680421270153331947283376367383644576532255533802984474910253879438028683742079699496595439647969411072916552843149561671840528735127360856696927069645471003201383622113450672077167251158051620186343784977770496145018239575143446040014565487987627034826582703780985661852665743065254134289295684699408207834654025186306092111873644434247435166473035624127258366262865796854085433441167734285300586554525682317118649462360090048269675448229634142281310807282733699374116475689281346950107129481937123640529573588902046083231329976164638832980821251410856466654580160140585766073271336220269127710282722918316377343028805778
n = 658604261957549588069099740702227657915405343781794260454924305587219011048454022674572497710138981771356792169803570714992697522268110617605562391868746642013038998976524536771193252086367356322299294368629516507818826241107204850049335472512795982422402182231402607017071807361288866172330683045608086285301233089117697928158077231075256100733395539869647257365152628196726038815499338736674388057299973824992512794794004151383724582315063016305976404811116630373385619744653449589599571911512997762382238269607235057918030227444157472580219508948951770517999616208093258504613695169376278619857787172962826566315196235615144923162984109342359188905026199109621718865970375924354681679904150184206741335878576339388418351016876586100164945053369699374053936529690644480085399450121923336177618787192884736410589036874346994751888896083738320170607433630028535197854810290431262475673571116518607375992672129753349099917781630293510198167987582933227256731031320697012724876739138074965037962573118524084761315736024265183871666533356240299523943954099313303312430808517635511826803490241975190327593237515563682626924660285875171997578864716488315070415709503319317933695653560530105088303163843358343914110128989518037263225213531
hint= 65860426195754958806909974070222765791540534378179426045492430558721901104845402267457249771013898177135679216980357071499269752226811061760556239186874664201303899897652453677119325208636735632229929436862951650781882624110720485004933547251279598242240218223140260701707180736128886617233068304560808628530123308911769792815807723107525610073339553986964725736515262819672603881549933873667438805729997382499251279479400415138372458231506301630597640481111663037338561974465344958959957191151299776238223826960723505791803022744415747258021950894895177051799961620809325850461369516937627861985778717296282656631514487325966238209756347785687224233942358787594053214937671390689146087228372622247970280386170541499572435066186629936046780214698192554056571910888340866043064640382381104252229306018886267097083382691705202922514605421762161183464444563335398115615580231884682636097459090938124806142155602007990269219682403838636214677326969213610650687618196365082141152594696773211681827701197811967537967964426670645926954792671503395852714039443123054404639762626741664610434643794653257547703883366513331584122097943175151679341722618876773742836151080361456662639975444674739807774293544688484378119996101100317626386377600
'''