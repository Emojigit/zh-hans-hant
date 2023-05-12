import re, requests

__version__ = "0.0.1"

findpattern = re.compile("-{H\|(.+?)}-")

def NoteTA(*args):
    if len(args) > 10:
        return "".join(NoteTA(*(args[i:i+10])) for i in range(0,len(args),10))
    return "{{NoteTA" + "".join("|G{}={}".format(i+1,d) for i,d in enumerate(args)) + "}}"

def expandtemplate(text):
    r = requests.get("https://zh.wikipedia.org/w/api.php",data={
        "action": "expandtemplates",
        "format": "json",
        "text": text,
        "prop": "wikitext",
        "utf8": 1
    })
    return r.json()["expandtemplates"]["wikitext"]

def listofrules(text):
    return tuple(x[1] for x in re.findall("-{H\|(.+?)}-",a.json()["expandtemplates"]["wikitext"]))

def choosesequence(*args):
    for x in args:
        if x:
            return x

def st_variant(variant):
    if variant in ("zh_cn","zh_my","zh_sg"):
        return "zh_hans"
    elif variant in ("zh_tw","zh_hk","zh_mo"):
        return "zh_hant"
    return variant

class ConverterBase:
    def __call__(self,text,variant):
        return text # NO changes!

class SimpleConverter(ConverterBase):
    def __init__(self,zh_hans=None,zh_hant=None,zh_cn=None,zh_hk=None,zh_mo=None,zh_my=None,zh_sg=None,zh_tw=None):
        self.zh_hans = choosesequence(zh_hans,zh_cn,zh_my,zh_sg)
        self.zh_hant = choosesequence(zh_hant,zh_tw,zh_hk,zh_mo)

        self.zh_cn = choosesequence(zh_cn,self.zh_hans)
        self.zh_hk = choosesequence(zh_hk,self.zh_hant)
        self.zh_mo = choosesequence(zh_mo,self.zh_hant)
        self.zh_my = choosesequence(zh_my,self.zh_hans)
        self.zh_sg = choosesequence(zh_sg,self.zh_hans)
        self.zh_tw = choosesequence(zh_tw,self.zh_hant)
    def __call__(self,text,variant):
        RSTR = text
        for x in ("zh_cn","zh_hk","zh_mo","zh_my","zh_sg","zh_tw"):
            if x == variant: continue
            RSTR = RSTR.replace(getattr(self,x),getattr(self,variant))
        return RSTR

class OneDirectionConverter(ConverterBase):
    def __init__(self,from_t,variant,to_t):
        self.from_t = from_t
        self.variant = variant
        self.to_t = to_t
    def __call__(self,text,variant):
        if variant == self.variant or st_variant(variant) == self.variant:
            return text.replace(self.from_t,self.to_t)
        else:
            return text

