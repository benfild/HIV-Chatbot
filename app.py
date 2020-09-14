from flask import Flask, request
import re
from flask.templating import render_template

app = Flask(__name__)  # initialize the app

qa = {
    "chatbot": "Unaweza niita chatbot",
    "greeting": "hi!, uhali gani?",
    "cheering": "Kila kitu kitakua sawa sema AMEN!!",
    "help": "Vizuri!!,Unaweza niuliza unachotaka kujua kuhusu Ukimwi",

    "hiv": "VVU kwa kirefu hujulikana kama Virusi Vya Ukimwi, Ni virusi vinavyosababisha Ukimwi",
    "aids": "UKIMWI ni Upungufu wa Kinga Mwilini.",
    "how does hiv lead to aids": "VVU huaribu kinga ya mwili na kuufanya mwili kua hatarini kupata magonjwa mengine "
                                 "hatari, na kusababisha UKIMWI",
    "infection diagnosed": "UKIMWI hupimwa kwa kipimo cha damu ya mtu kwa kuangalia vimelea vya VVU na kinga ya mwili "
                           "kama hushindwa kupambana na magonjwa mengine kwa mantiki hiyo kipimo cha damu kikionesha "
                           "vimelea vya VVU basi mtu hujulikana kua na UKIMWI.",
    "transmition": "VVU husambazwa kutoka kwa mtu mmoja mpaka mwingine kwaa njia ya:\nKujamiiana.\nKugusana kwa maji "
                   "maji ya mwili au vidonda na mtu mwenye Ukimwi.\nKuchangia vitu vyenye ncha kali.\nKuwekewa damu "
                   "iliyoathirika na VVU.",
    "symptoms of hiv": "Dalili za UKIMWI:\nKupungua haraka kwa uzito.\nHoma za mara kwa mara"
                       "\nKuchoka sana bila kujua kwa nini.\nMagonjwa ya ngozi pia ngozi kunyauka."
                       "\nKuharisha kwa takribani zaidi ya wiki."
                       "\nKusinyaa kwa ngozi ya mdomo na pia sehemu za siri.\nMagonjwa ya mapafu kama kifua kikuu.",
    "how long does it take for aids symptoms to develop after infection with hiv": "Kwa kawaida mtu anaweza "
                                                                                   "kuambukizwa VVU kwa zaidi ya "
                                                                                   "miaka 15 bila kuonesha dalili "
                                                                                   "zozote zile za UKIMWI lakini kwa "
                                                                                   "upande mwingine, "
                                                                                   "kuna baadhi ya watu huonesha "
                                                                                   "dalili za UKIMWI mapema tu baada "
                                                                                   "ya kuambukizwa VVU, "
                                                                                   "inachukua kama miezi michache tu "
                                                                                   "kuonesha dalili za ugonjwa huu.",
    "preventions or avoiding": "Njia za kuepuka au kujikinga na maambukizi ya VVU/UKIMWI. "
                               "Hii inamaana pia kujikinga na njia hatarishi za kupata UKIMWI.\nEpuka Ngono zembe, "
                               "tumia kinga, na ni vizuri kua na mwenza mmoja.\nUsishirikiane kutumia vifaa vya ncha "
                               "kali tumia vifaa vyako mwenyewe, vile vile sindano, vijiko, mswaki na vinginevyo "
                               "vitakavyoweza sambaza VVU.",
    "treatments or cure": "Kwa sasa hamna tiba kamili ya Ukimwi. Ila, "
                          "kuna matibabu yanayotolewa kukaribiana na uharibifu wa kinga ya mwili "
                          "unaofanywa na VVU.",
    "can hiv positive people have a baby": "Ndio, na mtoto anaweza zaliwa bila UKIMWI ila itakubidi ufate matibabu ya "
                                           "VVU (ART)",
    "life expectancy": "Ukipata matibabu mazuri ya VVU (ART) ukomo wa maisha ni sawa na ule wa mtu asiye na VVU.",
    "herbs or supplements": "Unashauriwa kua muangalifu na dawa za asili, labda kuwe na uthibitisho kutoka kwa "
                            "daktari wa afya.",
    "what is the best food if i am hiv positive": "Kama watu wengine, kula chakula kizuri chenye afya na virutubishio. "
                                                  "kuathirika na VVU haimaanishi kua kuna chakula maalum, kula kama "
                                                  "watu wengine kwa afya yako.\n ",
    "helpful": "Nafurahi kukusaidia. Karibu tena",
}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/get")
def ask():
    question = request.args.get('msg').lower().replace("?", "").strip(" ")

    if (re.findall("wewe|jina|unaitwa", question)) and (re.findall("nani", question)):
        return qa["chatbot"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (re.findall("muda|wakati", question)) and (re.findall("gani", question)) and (re.findall("kuonesha|onesha|tokeza", question)) and (re.findall("dalili|ishara", question)):
        return qa["how long does it take for aids symptoms to develop after infection with hiv"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question)))  and (re.findall("dalili|ishara", question)):
        return qa["symptoms of hiv"]

    elif (re.findall("nini|maana|kuhusu|inahusu", question)) and (re.findall("vvu", question)):
        return qa["hiv"]

    elif (re.findall("nini|maana|kuhusu|inahusu", question)) and (re.findall("ukimwi", question)):
        return qa["aids"]

    elif (re.findall("nashukuru|ahsante|asante|shukrani|shukurani", question)) and (re.findall("msaada|muda|umenisaidia", question)):
        return qa["helpful"]

    elif (re.findall("vvu", question)) and (re.findall("sababisha|pelekea", question)) and (re.findall("ukimwi", question)):
        return qa["how does hiv lead to aids"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (re.findall("onekana|pima|gundulika|gundua|juaje|pimwa", question)):
        return qa["infection diagnosed"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question)))  and (
    re.findall("sambaza|sambaa|eneza|ambukiz|kupata|enezwa", question)):
        return qa["transmition"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question)))  and (
    re.findall("zuia|jikinga|epuka|pambana", question)):
        return qa["preventions or avoiding"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (
    re.findall("matibabu|kinga|dawa", question)):
        return qa["treatments or cure"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (
    re.findall("athirika|mwenye|wenye|bila|nina", question)) and (re.findall("mtoto|watoto", question)):
        return qa["can hiv positive people have a baby"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (
    re.findall("maisha|ishi|kuishi", question)) and (re.findall("muda|wakati", question)):
        return qa["life expectancy"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (
    re.findall("mitishamba|asili|dawa", question)) :
        return qa["herbs or supplements"]

    elif ((re.findall("vvu", question)) or (re.findall("ukimwi", question))) and (
            re.findall("athirika|mwenye|wenye|wa", question)) and (re.findall("chakula", question)):
        return qa["what is the best food if i am hiv positive"]

    elif (re.findall("funga|hairisha", question)):
        return "Kwa heri, karibu tena :) "
    
    elif (re.findall("hello|hey|mambo|habari|hi", question)):
        return qa["greeting"]

    elif (re.findall("vizuri|sawa|salama|mpweke|vibaya|naumwa|mbaya|mzima|nzima|nzuri", question)):
        return qa["cheering"]

    elif (re.findall("amen|ameeen", question)):
        return qa["help"]

    else:
        return "Sina jibu sahihi la swali lako.\nLabda sijaelewa vizuri swali lako, samanahi uliza tena kuhusu VVU/UKIMWI kwa lugha rahisi(Swahili)"


if __name__ == "__main__":
    app.run(debug=True)
