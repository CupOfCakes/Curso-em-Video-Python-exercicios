aluno = {"nome": str(input("Nome: ")).title()}
aluno["media"] = float(input(f"Media de {aluno['nome']}: "))

print("=" * 40)
for v, k in aluno.items():
    print(f"{v} é igual a {k}")

if aluno["media"] <= 5:
    print(f"situação e igual a reprovado")
elif 5 < aluno["media"] < 7:
    print(f"situação igual a recuperação")
else:
    print(f"situação igual a aprovado")

'''kiss me more

kimi to dakiatta
ato wa sabishii yo
itsumo tarinai no ga
sono kuchibiru na no

motto kisu shite
konna seishun dakara
mou, uh-oh
tada no principle
hanasanaide kono mama
move, uh-oh

koko no futari
ai wo kizamou
oh, suki da yo, la-la-la
sono subete i want it
koko de futari
aiwo kizamou
oh,suki da yo, la-la-la
sono subete i want it

aa, abaredashitai
sunao de kanjouteki ni
atashi wa no dummy dummy
mada shiranai mirai ni

moshi mo kisu wo kawashi
moshikashite ii kanji
dakara nigeyo issho ni
soko de motto shitai

yaranai to wakannai yo
saisho soko ajiwattemiyou
datte kimi ga nozumu koto nan da yo
donna aji ga shita no?

amai dezaato no you de
fukai kisu wa nikai me
sono kuchi kandemitara
kimi no yokubou ga manman da, huh

motto kisu shie
konna seishun dakara
mou, uh-oh
tada no principle
hanasanaide kono mama
move, uh-oh

koko de futari
ai wo kizamou
oh, suki da yo, la-la-la
sono subete i want it
koko de futari
ai wo kizamou
oh, suki da yo, la-la-la
sono subete i want it

nee, chotto dake
romanchikku de
genkai wo koete yaru tte?
anata a atashi ga inai to
dame jan? minna sou omou yo

torawareta you da with you
iki ga dekinai with you
otomegojoro shiranai
kimi to wakarereba dou da?

hoka to fuzake
uso tsuichatte
dame na ku
you know that?

baigaeshi shite yaru yo dou da?
osaeru nanka wa iranai
kono mi wa real(ah)
drama make you fell(ah)
amai yume nado wo miseru yo

moto kisu shite
konna seishun dakara
mou, uh-oh
tada no principle
hanasanaide kono mama
move, uh-oh

koko de futari
ai wo kizamou
oh, suki da yo, la-la-la
sono subete i want it
koko de futari
ai wo kizamou
oh, suki da yo, la-la-la
sono subete i want it'''
