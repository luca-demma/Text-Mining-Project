import shutil

DIRS_BASE_PATH = '/home/luca/UNI/Text Mining/processed/release/'

json = {
	"9news.com.au":{"lng":["en"],"clean":False,"country":"Australia","wa":"9news.com.au","name":"9News","wa_only":False,"sweb":27.42},
	"abcnews.go.com":{"lng":["en"],"clean":True,"country":"USA","wa":"abcnews.go.com","name":"ABC News","wa_only":False,"sweb":42.06},#-seems like loads wrong...
	"abendblatt.de":{"lng":["de"],"clean":True,"country":"Germany","wa":"abendblatt.de","name":"Hamburger Abendblatt","wa_only":False,"sweb":3.85},
	"foxnews.com":{"lng":["en"],"clean":True,"country":"USA","wa":"foxnews.com","name":"Fox News","wa_only":True,"sweb":363.28},
	"msnbc.com":{"lng":["en"],"clean":True,"country":"USA","wa":"msnbc.com","name":"MSNBC","wa_only":False,"sweb":23.25},
	"thehill.com":{"lng":["en"],"clean":True,"country":"USA","wa":"thehill.com","name":"The Hill","wa_only":False,"sweb":67.95},
	"washingtontimes.com":{"lng":["en"],"clean":True,"country":"USA","wa":"washingtontimes.com","name":"Washington Times","wa_only":False,"sweb":7.85},
	"inquirer.com":{"lng":["en"],"clean":True,"country":"USA","wa":"inquirer.com","name":"Philadelphia Inquirer","wa_only":False,"sweb":9.14},
	"washingtonpost.com":{"lng":["en"],"clean":True,"country":"USA","wa":"washingtonpost.com","name":"Washington Post","wa_only":True,"sweb":185.22},
	"thetimes.co.uk":{"lng":["en"],"clean":True,"country":"UK","wa":"thetimes.co.uk","name":"The Times","wa_only":False,"sweb":27.03},#Update issued
	"theguardian.com":{"lng":["en"],"clean":True,"country":"UK","wa":"theguardian.com/uk"},
	"liverpoolecho.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#- check the RE-Read - with show titles
	"dailymail.co.uk":{"lng":["en"],"clean":True,"country":"UK","wa":"dailymail.co.uk/home/index.html"},#Update issued
	"telegraph.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#Update issued
	"thesun.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#Update issued
	"economist.com":{"lng":["en"],"clean":True,"country":"UK","wa":"economist.com","name":"The Economist","wa_only":False,"sweb":13.47},#Revisit
	"news.sky.com":{"lng":["en"],"clean":True,"country":"UK"},
	"walesonline.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#Foreign indeed some welsh bits.
	"standard.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#Foreign are structural.
	"csmonitor.com":{"lng":["en"],"clean":True,"country":"USA"},#Skipping many "cs monitor daily bits"
	"latimes.com":{"lng":["en"],"clean":True,"country":"USA"},#Large number of foreign are articles in Spanish.
	"reuters.com":{"lng":["en"],"clean":True,"country":"UK"},
	"nytimes.com":{"lng":["en"],"clean":True,"country":"USA"},
	"politico.com":{"lng":["en"],"clean":True,"country":"USA"},#Many structural pages cut off by foreign
	"itv.com":{"lng":["en"],"clean":True,"country":"UK","wa":"itv.com/news"},#Revisit
	"independent.co.uk":{"lng":["en"],"clean":True,"country":"UK","wa_only":True},#Revisit
	"dailystar.co.uk":{"lng":["en"],"clean":True,"country":"UK","wa_only":True},
	"edition.cnn.com":{"lng":["en"],"clean":True,"country":"USA"},
	"express.co.uk":{"lng":["en"],"clean":True,"country":"UK"},#Revisit
	"bostonglobe.com":{"lng":["en"],"clean":True,"country":"USA"},#Revisit
	"usatoday.com":{"lng":["en"],"clean":True,"accept_foreign":True,"country":"USA"},
	"chicagotribune.com":{"lng":["en"],"clean":True,"country":"USA"},#Foreign are Spanish, #REVISIT
	"breitbart.com":{"lng":["en"],"clean":False,"country":"USA"},#Foreign are structural pages to authors
	"aljazeera.com":{"lng":["en"],"clean":True,"country":"International"},
	"bbc.com":{"lng":["en"],"clean":True,"country":"UK","wa":"bbc.com/news","name":"BBC","wa_only":False,"sweb":433.26},
	"nypost.com":{"lng":["en"],"clean":True,"country":"USA"},
	"newsweek.com":{"lng":["en"],"clean":True,"country":"USA"},#Revisit
	"npr.org":{"lng":["en"],"clean":True,"country":"USA","wa_only":True},
	"theatlantic.com":{"lng":["en"],"clean":True,"country":"USA"},
	"channel4.com":{"lng":["en"],"clean":True,"country":"UK","wa":"channel4.com/news"},
	"huffpost.com":{"lng":["en"],"clean":True,"country":"USA"},#Foreign are structural
	"cnbc.com":{"lng":["en"],"clean":True,"country":"USA"},
	"metro.co.uk":{"lng":["en"],"clean":True,"accept_foreign":True,"country":"UK"},#---
	"wnd.com":{"lng":["en"],"clean":True,"country":"USA"},
	"lepoint.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"nbcnews.com":{"lng":["en"],"clean":False,"country":"USA"},#<-
	"thewest.com.au":{"lng":["en"],"clean":True,"country":"Australia"},
	"sbs.com.au":{"lng":["en"],"clean":True,"country":"Australia","wa":"sbs.com.au/news"},
	"afr.com":{"lng":["en"],"clean":False,"country":"Australia"},
	"news.com.au":{"lng":["en"],"clean":False,"country":"Australia","accept_foreign":True,},#Videos appear to have the same title and description.
	"theage.com.au":{"lng":["en"],"clean":False,"country":"Australia"},
	"smh.com.au":{"lng":["en"],"clean":False,"country":"Australia"},
	"newshub.co.nz":{"lng":["en"],"clean":False,"country":"New Zealand","wa":"home.html"},#-
	"rnz.co.nz":{"lng":["en"],"clean":False,"country":"New Zealand"},#-
	"scoop.co.nz":{"lng":["en"],"clean":False,"country":"New Zealand"},#-
	"nzherald.co.nz":{"lng":["en"],"clean":False,"country":"New Zealand"},
	"stuff.co.nz":{"lng":["en"],"clean":False,"country":"New Zealand"},
	"slate.com":{"lng":["en"],"clean":True,"country":"USA"},
	"scotsman.com":{"lng":["en"],"clean":True,"country":"UK"},
	"wsj.com":{"lng":["en"],"clean":True,"country":"USA"},
	"news.yahoo.com":{"lng":["en"],"clean":False,"country":"USA","wa_only":True},
	"mirror.co.uk":{"lng":["en"],"clean":True,"country":"UK"},
	"morningstaronline.co.uk":{"lng":["en"],"clean":True,"country":"UK"},
	"apnews.com":{"lng":["en"],"clean":True,"country":"USA"},
	"businessinsider.com":{"lng":["en"],"clean":False,"country":"USA"},
	"cbsnews.com":{"lng":["en"],"clean":False,"country":"USA"},#TODO
	"time.com":{"lng":["en"],"clean":True,"country":"USA"},
	"rfi.fr":{"lng":["en"],"clean":False,"accept_foreign":True,"country":"International","wa_only":True,"wa":"rfi.fr/en/"},#<-
	"rt.com":{"lng":["en"],"clean":True,"country":"International"},
	"dw.com":{"lng":["en"],"clean":False,"country":"International","wa":"dw.com/en/top-stories/s-9097"},
	"euronews.com":{"lng":["en"],"clean":False,"accept_foreign":True,"country":"International"},#<-
	"westernjournal.com":{"lng":["en"],"clean":True,"country":"USA"},
	"upi.com":{"lng":["en"],"clean":True,"country":"USA"},
	"handelsblatt.com":{"lng":["de"],"clean":True,"country":"Germany"},
	"tagesspiegel.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"focus.de":{"lng":["de"],"clean":True,"accept_foreign":True,"country":"Germany"},
	"bild.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"faz.net":{"lng":["de"],"clean":True,"country":"Germany","wa":"faz.net/aktuell"},
	"welt.de":{"lng":["de"],"clean":True,"accept_foreign":True,"country":"Germany"},
	"stern.de":{"lng":["de"],"clean":True,"country":"Germany"},#Structural links are responsible for lots of foreign annotations.
	"francetvinfo.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"lexpress.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"tagesschau.de":{"lng":["de"],"clean":True,"accept_foreign":True,"country":"Germany"},
	"spiegel.de":{"lng":["de"],"clean":True,"country":"Germany","wa_only":True},#Many english articles.
	"bz-berlin.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"rtl.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"morgenpost.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"fr.de":{"lng":["de"],"clean":True,"country":"Germany"},
	"wdr.de":{"lng":["de"],"clean":True,"country":"Germany","wa_only":True,},#Afer redoing entries with many links, check if worked.
	"ndr.de":{"lng":["de"],"clean":True,"country":"Germany"},#Afer redoing entries with many links, check if worked.
	"n-tv.de":{"lng":["de"],"clean":True,"country":"Germany"},#Many structural and "links" to videos des tages
	"20minutes.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"lemonde.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"lci.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"lefigaro.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"liberation.fr":{"lng":["fr"],"clean":True,"country":"France"},
	"journaldemontreal.com":{"lng":["fr"],"clean":True,"country":"Canada"},
	"macleans.ca":{"lng":["en"],"clean":True,"country":"Canada"},
	"rcinet.ca":{"lng":["en"],"clean":True,"country":"Canada"},
	"ctvnews.ca":{"lng":["en"],"clean":True,"country":"Canada"},
	"thestar.com":{"lng":["en"],"clean":True,"country":"Canada"},
	"torontosun.com":{"lng":["en"],"clean":True,"country":"Canada"},
	"montrealgazette.com":{"lng":["en"],"clean":True,"country":"Canada"},
	"lapresse.ca":{"lng":["fr"],"clean":True,"country":"Canada","accept_foreign":True},
	"ici.radio-canada.ca":{"lng":["fr"],"clean":True,"country":"Canada"},
	"cbc.ca":{"lng":["en"],"clean":True,"country":"Canada"},
	"vancouversun.com":{"lng":["en"],"clean":True,"country":"Canada"},
	"theglobeandmail.com":{"lng":["en"],"clean":True,"country":"Canada"},
	"globalnews.ca":{"lng":["en"],"clean":True,"country":"Canada"},#many structural
	"france24.com":{"lng":["en"],"clean":True,"country":"International","wa":"france24.com/en","wa_only":True,"accept_foreign":True},
	"noz.de":{"lng":["de"],"clean":True,"country":"Germany"},#Many structural and "links" to videos des tages
	"bfmtv.com":{"lng":["fr"],"clean":True,"country":"France"},
	"abc.net.au":{"lng":["en"],"clean":True,"country":"Australia","wa":"abc.net.au/news"},
	"rte.ie":{"lng":["en"],"clean":True,"country":"Ireland","wa":"rte.ie/news/"},
	"irishmirror.ie":{"lng":["en"],"clean":True,"country":"Ireland"},
	"breakingnews.ie":{"lng":["en"],"clean":True,"country":"Ireland"},
	"thejournal.ie":{"lng":["en"],"clean":True,"country":"Ireland"},
	"irishexaminer.com":{"lng":["en"],"clean":True,"country":"Ireland"},
	"independent.ie":{"lng":["en"],"clean":True,"country":"Ireland","wa_only":True,},
	"irishtimes.com":{"lng":["en"],"clean":True,"country":"Ireland"}, #Foreign are actually Irish (?)
	"thesun.ie":{"lng":["en"],"clean":True,"country":"Ireland"}, #Afer redoing entries with many links, check if worked.
	"lavanguardia.com":{"lng":["es"],"clean":True,"country":"Spain"},
	"larazon.es":{"lng":["es"],"clean":True,"country":"Spain","accept_foreign":True},
	"cuatro.com":{"lng":["es"],"clean":True,"country":"Spain"},
	"elmundo.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"elperiodico.com":{"lng":["es"],"clean":True,"country":"Spain","wa":"elperiodico.com/es/","accept_foreign":True},
	"antena3.com":{"lng":["es"],"clean":True,"country":"Spain"},
	"elpais.com":{"lng":["es"],"clean":True,"country":"Spain","accept_foreign":True}, #foreign actually not spanish.
	"elespanol.com":{"lng":["es"],"clean":True,"country":"Spain"},
	"rtve.es":{"lng":["es"],"clean":True,"country":"Spain","accept_foreign":True,"wa":"http://rtve.es/noticias/"},
	"telecinco.es":{"lng":["es"],"clean":True,"country":"Spain","wa":"http://telecinco.es/informativos/"},
	"ondacero.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"cadenaser.com":{"lng":["es"],"clean":True,"country":"Spain"}, #foreign actually some other language
	"publico.es":{"lng":["es"],"clean":True,"country":"Spain"}, #foreign are catalan
	"huffingtonpost.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"cope.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"20minutos.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"europapress.es":{"lng":["es"],"clean":True,"country":"Spain","wa_only":True},
	"eldiario.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"abc.es":{"lng":["es"],"clean":True,"country":"Spain"},
	"fanpage.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"lastampa.it":{"lng":["it"],"clean":True,"country":"Italy"}, #foreign are actually english.
	"repubblica.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"tiscali.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"rai.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"ilsole24ore.com":{"lng":["it"],"clean":True,"country":"Italy"}, #foreign actually english
	"huffingtonpost.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"ansa.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"ilfattoquotidiano.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"corriere.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"liberoquotidiano.it":{"lng":["it"],"clean":True,"country":"Italy","wa_only":True,},
	"ilmessaggero.it":{"lng":["it"],"clean":True,"country":"Italy","accept_foreign":True},
	"ilmattino.it":{"lng":["it"],"clean":True,"country":"Italy"},
	"kp.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"iz.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"rg.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"kommersant.ru":{"lng":["ru"],"clean":True,"country":"Russia","accept_foreign":True},
	"ng.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"mk.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"newsru.com":{"lng":["ru"],"clean":True,"country":"Russia"},
	"tvzvezda.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"interfax.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"aif.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"lenta.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"tass.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"rbc.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"ren.tv":{"lng":["ru"],"clean":True,"country":"Russia"},
	"gazeta.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"rambler.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"vesti.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"ria.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
	"ntv.ru":{"lng":["ru"],"clean":True,"country":"Russia"},
}



for outlet in json:
	if json[outlet]['lng'][0] != "en":
		shutil.rmtree(DIRS_BASE_PATH + outlet, ignore_errors=True)
		print("Deleted: ", outlet, " Lang: ", json[outlet]["lng"][0])

