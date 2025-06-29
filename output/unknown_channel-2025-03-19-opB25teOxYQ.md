URL: https://www.youtube.com/watch?v=opB25teOxYQ

0.08s: today in this video I'm going to show
1.76s: you how I built montor find.com in just
4.80s: 7 Days basically it is a directory
7.36s: website that will be SEO optimized and
10.44s: it has 7,000 listings thereabouts and I
13.76s: scraped a whole bunch of data from the
15.28s: internet and I did this all basically
17.72s: with AI tools turned around a pretty
19.60s: nice little website so I think anyone
21.32s: can do this these days if you're
22.60s: remotely competent online I mean if you
24.96s: even know what SEO means I'm sure you're
26.76s: competent enough to figure this out
28.40s: we're going to use cursor Ai and bolt.
30.44s: new so without further Ado let's get
32.52s: started first I'll just show you the
34.00s: website and what we're looking at
35.40s: basically you can go to any state in the
37.96s: Union and you can find a Monas School a
41.40s: list of Monas schools as you can see it
43.08s: has the the name of the city the name of
45.04s: the State uh and then we've got reviews
47.24s: that are scraped from Google Maps so
48.76s: here's a four a five star review um out
51.16s: of four total I might have to clean that
52.76s: up it's got a map embed here with the
54.88s: proper instructions it's got a link to
56.80s: Google Maps and it's got phone number
59.40s: it's got it so all this these
61.28s: descriptions in every single uh listing
65.44s: were scraped with python script open
67.76s: source called crawl for AI which we're
69.60s: going to get into and then an llm an
71.60s: open source llm was used to make these
73.92s: descriptions um pretty fun project
76.20s: overall here's the project window in
78.44s: cursor as you can see we've got a big
81.32s: Json file full of all the listings here
83.88s: which will converted from a um from a
86.08s: CSV we've got a Blog in here as well um
89.72s: and a pretty fairly easy system for
91.72s: making new SEO blog posts and then
94.88s: there's a frequently asked questions
96.64s: which in and of itself I think is a bit
98.32s: of a masterpiece though I can't take
100.00s: full credit for it because Claude AI
102.48s: really helped me the first thing you
104.00s: need to do which I won't be covering in
105.24s: this video is find your lucrative Niche
107.44s: find the right search term which doesn't
109.08s: have a lot of competition check out Frey
110.72s: ch's video shout out to Frey who
112.12s: inspired me to build this so we're going
113.56s: to focus on just the build process so
115.56s: once you have your topic then you're
118.28s: obviously going to want to scrape
119.28s: listings on Google Maps we're focused on
121.40s: local listings here that are more
123.56s: Evergreen that people would need in
125.28s: their like neighborhood so first we're
127.24s: going to go to Google Maps and we're in
129.20s: Miami area here it's already searching
131.60s: for monor schools let's just come up
133.84s: with something new let's say we're
135.36s: looking for um shoe repair shops in
138.92s: Florida let's just say Florida McFarland
141.60s: shoe repair okay shoe repair okay so we
143.96s: got some results here we're going to
145.48s: make a shoe repair website shoe repair
148.36s: directory all right for in his YouTube
150.92s: video recommends using a website like
153.60s: outscar where you can actually it's kind
155.76s: of cool cuz you can pay with Bitcoin um
157.60s: you pay PayPal whatever you want but
159.04s: it's got a Google Maps scraper basically
160.84s: so you so we would say
162.76s: Sho uh repair shop great shoe repair
166.12s: shop and we want to say just Florida
167.88s: here so we're choosing this Florida all
171.52s: right unlimited results enhanced results
173.48s: with other services we don't need any of
175.60s: that in some cases it might come in
177.12s: handy but contains one of sh repair shop
179.44s: delete duplicates use zip codes all
181.76s: right so we're going to click get data
183.12s: it's going to tell you how much money
184.00s: it's going to cost from $9 to
186.60s: $61 um I'm not going to pay for that but
189.24s: you can if you want instead I'm going to
190.96s: show you how to use a script on your own
193.16s: computer that just uses Google API
195.40s: credits that you actually get free I
198.44s: think $300 free credit when you sign up
200.72s: at the time of me recording this so you
202.48s: can technically actually get it all for
204.44s: free yeah so you can see here I've got
206.92s: $141 of free credit so we're going to
209.52s: use that to scrape this data okay so
211.52s: first things first is you're going to
212.60s: want cursor cursor is an AI coding app
215.68s: uh it's a lot like Visual Studio code
217.60s: where basically you're going to have all
218.88s: these files over here you're going to
220.32s: have access to your git repository lots
222.60s: of plugins but there's an AI agent over
225.04s: here that helps you do anything the
226.72s: agent will build the ask agent normally
229.04s: uses a different model and uh it just
231.36s: helps you figure things out um I have
233.28s: never really used edit yet but it's
234.72s: probably for editing software but the
235.80s: agent helps you build so we're here we
238.24s: have nothing so I'm going to make a I'm
240.52s: not even going to do anything yet I'm
241.52s: going to say write a script that uses
245.16s: Google Maps
247.04s: API um I think it's called places um to
252.12s: scrape Google maps of all listings in
257.20s: the State of
259.12s: Florida for the term shoe repair shop
264.68s: export the results as a CSV file which
269.08s: includes one rating and then I'm Al okay
272.24s: so let's just do that okay one how about
274.48s: we say this one positive rating and one
277.40s: negative rating so maybe you want more
279.72s: ratings um the ratings is something I'm
281.72s: going to integrate a system into monor
283.64s: find later but for now it's good to
285.88s: start with ratings and we're just doing
287.28s: a sample video here so I'm just going to
288.44s: do one rating so Watch What Happens I
290.04s: send
292.92s: that okay so it shows python when I did
296.36s: mon story find I used JavaScript but
297.88s: that's okay python ends up doing a lot
299.44s: of the data scraping later when we want
300.80s: to generate the descriptions so as you
302.52s: can see over here it's literally coding
305.20s: everything I just said I want it uh and
308.00s: it gets even crazier later when we're
309.32s: going to use bolt to then plug in the
311.04s: data we scrape into a website and it
312.96s: just makes a website so this is all
314.32s: still the back end we can't use bolt yet
316.76s: so here it says make a new file
318.64s: requirements. text and you can either
320.60s: press this check mark here accept or
322.56s: just uh Apple y command y or just accept
325.64s: boom uh scrape sheet repair okay now I
328.16s: made a python script here it is
330.16s: this in green shows you what it added
334.16s: and then later when we edit you'll see
335.68s: things in red things in green red means
337.20s: it's cutting it green means it's adding
338.52s: it so it just wrote this whole script um
341.72s: now you can obviously vet the script and
343.88s: look through it and if you really want
345.08s: to learn how to understand coding then
347.96s: you simply go in here and Google
350.44s: everything you don't understand or you
351.80s: copy it and you say what does that do
355.08s: but let's do that in a minute so I can I
356.96s: can just copy it and say like what if I
358.88s: don't want what if the AI is just
360.16s: putting malicious code on my computer um
362.12s: I'm going to add it to the chat and I
363.72s: can say what does this do and as you can
366.56s: see here it knows lines 36 to 44 which
368.84s: is what I highlighted that's its context
371.04s: and then me explains what it does now I
373.00s: Ed the agent for that I should have used
374.84s: ask if anything it'll just save the
376.52s: credits but whatever all right so then
379.04s: it tells me exactly what this does it
381.36s: starts from Florida Center
383.80s: coordinates latitude blah blah blah and
385.96s: so I just copied these lines right here
388.64s: there's obviously a whole script here so
390.00s: if you just go through the whole thing
391.44s: you can actually learn what each thing
392.80s: does you don't need to be a coder
393.96s: anymore you just have to learn how to
394.92s: tell it what to do so anyway I'm going
397.00s: back to up here and it's giving me the
400.64s: script and I say accept file boom it
403.56s: accepts it and it'll save it
404.96s: automatically and then you'll notice
406.84s: here it's loading environmental
408.08s: variables we're going to need one of
409.64s: those files as well because we're going
412.04s: to need an API key uh and then a read me
414.68s: so we say yes to the readme okay so then
416.52s: it gave us everything and it's cool is
418.04s: in that readme it tells us what to do
420.24s: it says Okay first install the
421.64s: requirements then you create a n file
424.48s: with your Google Maps key so I'm going
426.28s: to copy that I'm going to make a new
428.20s: file right here call it. EnV boom now
432.68s: I'm not going to show you this screen
434.16s: again but basically I'm going to paste
436.68s: the Google Maps key right there so we
438.56s: simply go to Google Cloud I've got my
440.12s: monor Schools project here you're going
441.52s: to have to make a new project you can
442.96s: Google it it's fairly straightforward go
444.76s: to apis and services go to credentials
447.96s: and you're going to create credentials
449.72s: you're going to create an API key and
452.32s: then it's going to give it to you and
453.76s: you're going to paste it into your end
455.28s: file now if you've never coded before
457.72s: you might have to install python on your
459.76s: computer or JavaScript or whatever
461.68s: cursor asks you to do in this case I
463.68s: already have Pip installed uh if we look
465.88s: at a command line pip means like what
468.00s: software we're using pip or python or
469.84s: node npm that's like the general like
472.92s: what language does it need to use to
475.00s: launch the script and then this is the
476.92s: command install and then boom it's it's
479.56s: going to install whatever it reads from
481.12s: the requirements file so we're going to
482.56s: open a terminal new terminal we want to
484.72s: run pip install requirements now we're
487.32s: going to have an issue here maybe
489.32s: because on my computer like we'll
490.48s: definitely have an issue here with
491.48s: python script Sho repair we're going to
492.72s: need to use Python 3 Let's see looks
495.72s: like it worked okay so it's installing
497.36s: all that if you get an error you copy it
500.56s: and then you either send it to the chat
502.80s: or you Google it and then it'll tell you
504.52s: what to do this is a normal part of
506.76s: coding and processing something will
508.72s: always go wrong and we need to be
510.60s: confident and Sovereign enough in our
512.92s: abilities to figure out the issue it's
514.88s: easier than ever now thanks to llms so
518.40s: I'm making this I'm making this video
520.00s: now cuz I'm confident doing it and I
521.76s: think you can be confident too just
523.48s: takes experience we only get experience
526.00s: by building okay now we have an
528.44s: error this is a lot so see how it even
530.92s: gives me this button add to chat see how
533.40s: it's got the context here the lines and
535.80s: I just say what happened not fully
538.84s: compatible let me modify the
540.40s: requirements so basically it knows I'm
541.96s: using python 313 but it's not compatible
545.44s: with that version of pandas which it
546.76s: needs so it's changing the requirement
548.56s: the dependency here I accept it I save
550.72s: it and then I simply press up uh on the
554.12s: terminal and it's going to go back to
555.96s: that pip install requirements and I
558.40s: press enter to run it let's give that a
560.16s: minute it looks like it happened fast
562.68s: boom there we go we got it now the next
565.88s: thing we got to do if we scroll back up
570.00s: we can run the script so if I try to run
572.04s: it now it's probably going to give me an
573.28s: error because it doesn't have python but
574.96s: it does have Python 3 so it's scrape
578.04s: shoe repair. python okay now let's do
583.60s: it now see how it's got some it's called
586.52s: Uh I don't even know it's called verbose
587.96s: logs in there so basically it's kind of
589.96s: telling you what it's doing data
591.64s: exported okay it found 24 shops great
593.76s: that probably wasn't very expensive
595.72s: hopefully it wasn't very expensive so it
598.16s: gave us something we haven't looked at
600.16s: it yet and we don't know if it did it
601.96s: right so this is what's really important
604.08s: as as we get AIS to do things for us
606.72s: especially if we don't know how to do
607.84s: them ourselves we don't know if they're
609.60s: going to work right but that's why we do
611.36s: step- by-step in iterations so let's
613.64s: take a look at the CSV file looks like
615.96s: it made all these columns in fact let's
617.92s: just open this in a CSV Viewer okay so I
621.24s: hope this isn't too small we've got name
623.44s: address rating total ratings latitude
625.56s: longitude positive review negative
627.40s: review if they got one the CSV looks
629.56s: good but I'm realizing we forgot a
630.84s: couple important things mainly the
632.24s: website so I'm going to exit that out
634.24s: and I'm going to say add a column for
637.40s: website and description um into the into
642.04s: the scrape shoe repair
645.04s: script okay so we're it gave us his
647.16s: changes let's add those let's say yes
650.44s: cool accept and then say we also need to
653.96s: add a zip code
657.44s: separate full address street address ZIP
661.40s: code and city into their own unique
666.52s: columns okay so even if we realize we
669.76s: need more data here this is just what
671.12s: it's going to be because this is just a
672.88s: tutorial video but as you can see we can
674.96s: keep enhancing this script in the
676.80s: beginning we obviously don't want to use
679.16s: too much data to for our apri credits to
681.96s: pay money until we know exactly what we
683.40s: want I accept that it's got street
685.40s: address city state ZIP code full address
687.40s: okay great um okay so it's doing
690.00s: everything we want now can we also
692.20s: scrape for a description of the
695.88s: listing now we are going to use an llm
698.96s: to scrape the listings website but this
701.92s: is also a good move just in case like
704.40s: Florida Sho repair how many websites do
706.24s: they have I mean maybe they have lots of
708.08s: websites or maybe they're these old mom
709.52s: and pop businesses that just run off of
711.00s: board and mouth and they don't think
712.08s: they need a website and they don't cuz
713.36s: their business is still going um we're
715.44s: going to try both ways here so we're
716.92s: going to accept the accept there okay
719.28s: okay so now we're going to run this
721.88s: script again all I got to do is press up
724.04s: python scrape shoe repair I'm going to
725.72s: open up our original CSV and just delete
727.68s: it just so there's no potential issues
729.84s: there Python 3 scrapes shoe repair. piy
732.16s: boom okay it worked so now after few
735.76s: back and forths we're getting the
738.36s: address the full address the country the
740.44s: state the city the ZIP code we got the
742.56s: phone number we got the URL and we got a
746.28s: negative review and a positive review
748.12s: great so now we have to work with and we
750.12s: got 42 listings that's like perfect
752.64s: actually it's less than that I think
753.60s: it's 24 24 listings great little mini
756.24s: tutorial website so the next thing I'm
757.92s: going to do uh I'm going to clear my
760.00s: files out here a bit I'm going to make a
761.40s: new file and I'm going to call it
763.40s: organized data. piy and I'm going say
768.72s: in this file and I'm going to tag it
772.08s: organized data. py write a script that
775.68s: removes listings from our CSV file that
779.36s: has no
781.04s: address or no
783.48s: state if there is no
787.12s: website um add no
790.92s: website uh but where are we going to add
792.84s: it so let's do this um add no website
797.28s: yeah to the website column let's just
799.68s: add that there for now so what that's
801.40s: going to do is just parse everything and
803.00s: say hey this one doesn't have an address
804.92s: this one might not be real so just
806.24s: remove it and I'm going to rename our
808.48s: CSV file to just data. CSV so it's
812.08s: easier all right so now it's writing an
814.32s: organization script to just filter out
816.20s: if anything's broken uh right here it
818.88s: says hey you know choose your CSV file
821.36s: what I like to do so we can use this
823.44s: again later is send it to the chat and
826.12s: say make it so I can choose the
830.00s: CSV file in the command line and the
833.76s: output file is simply file name updated.
838.56s: CSV now we got organized data and it
840.80s: says to run it all we do is say
843.60s: organized data your your input file to
845.92s: CSV so I say Python 3 for you it might
848.88s: be python for me it's Python 3 we're
851.32s: going to run organize data. piy and
853.64s: we're going to data. CSV boom so now we
856.88s: got data updated over here and
861.28s: um let's do this again let's add a
864.96s: success message that
867.16s: shares how many
869.60s: um rows were updated or deleted so we
873.72s: don't even know what happened so let's
876.88s: add in that
882.48s: message and what you can do also the
884.92s: next level if you have a lot of listings
886.24s: it say send all the failed ones to a new
889.32s: CSV file so I can just check them
891.16s: manually and that is a step that I'm
893.60s: still working on and organizing my data
895.40s: from monor find okay so it added this
897.52s: new stuff let's run it
899.80s: again now it says updated entries four
903.12s: so to four entries it added no website
906.04s: perfect so we're going to go to Swift
908.48s: Shoe Repair Inc because it said no
916.16s: website okay there's
918.20s: Swifts um and it's true doesn't look
920.40s: like it has a website um bag clinic and
923.12s: shoe
924.08s: repair does look real and open this is
926.60s: how we enhance the data you know we just
928.44s: check it out 5 years ago when were these
930.92s: reviews 3 months ago okay so it's still
933.20s: there um but then I would just go
934.64s: through each one of these ones with no
936.60s: URL and um and just check to see if
940.48s: they're still around boom um then we see
943.96s: missing address is none address without
945.80s: Florida none okay so there we have our
947.92s: file it's clean depending on your data
949.96s: you might have a lot to do here and it
951.52s: might take a while um or you do it in a
953.44s: future round but in general I try to at
956.20s: least get out like the dead ones before
958.52s: we even go live so now we have our data
960.36s: here okay data updated. CSV and now
964.12s: we're basically ready to start a brand
966.44s: new project here okay so we've got our
968.32s: base data but now we need to make a
969.92s: description in order to do that we need
972.04s: to scrape the URLs of each website in
974.84s: here go through it find the important
977.20s: information and then generate a
978.56s: description from it so for that we're
980.24s: going to use an llm AI and we're going
983.12s: to use software called crawl for AI
985.92s: which is an open source llm friendly web
987.52s: crawler and scraper and and it looks a
989.92s: little intimidating it was for me in the
991.40s: beginning but it actually is going to
992.92s: make a lot of sense as we go through it
994.92s: so first things first we are going to
998.16s: make a fresh file and we'll just call it
1001.32s: description
1002.92s: generator. Pi okay now the first thing
1006.64s: we need to do if we just make a quick
1007.88s: list we need to connect to the LM AI
1011.20s: which is going to be Venice and then we
1013.48s: got to uh so see and cursor it gets you
1015.96s: all this stuff from the GetGo um but it
1018.64s: doesn't know that we're not really
1019.72s: programming here then we need
1023.12s: to uh scrape the website for two to
1028.08s: three paragraphs of valid information
1031.12s: valid text and then we're going to
1034.04s: generate a description of the website
1035.76s: and we're going to Output the
1037.20s: description to the column uh to the
1041.28s: description column of the CSV file we're
1046.44s: going to repeat the process save the
1048.36s: updated yeah there we go um okay so
1052.12s: that's what we're going to do here and
1053.20s: we're actually going to copy and paste
1054.36s: that into the agent in a minute but
1056.44s: let's just first say okay how are we
1058.16s: going to scrape the website well we're
1060.52s: going to use crawl for AI and we're
1062.12s: going to use um what's basically called
1065.48s: llm extraction method which is llm
1067.96s: strategies here why would you use an llm
1070.04s: for scraping well it's going to help
1071.48s: structure the data if it's unstructured
1073.56s: the website itself it can reason through
1075.04s: it and be like okay that's necessary
1076.44s: that's not necessary just in general why
1078.12s: do we use l l m because they help us do
1080.60s: tedious things faster and this is very
1082.72s: definitely a tedious thing so the first
1084.68s: thing I'm going to do I've opened the
1086.40s: agent here and we're going to start
1088.08s: telling it what we want to do here but
1090.08s: the reason I made these steps is that it
1092.16s: can be a little complicated here so the
1094.36s: reason I made these steps is because
1096.68s: this can be complicated to tell the
1098.36s: agent to do it all at once so we're
1100.20s: basically going to test it step by step
1102.48s: until we know each step is working so
1104.68s: then by the time we run it we know it
1106.20s: can do what we want we could just say
1107.84s: hey
1109.40s: do this and it just sends it all of
1112.68s: there we could just say hey do this and
1115.84s: paste that all in
1117.24s: there but the truth is probably not
1120.16s: going to work very well so we're going
1122.40s: to start from the top first thing we're
1124.96s: going to do here is go is connect to the
1128.64s: llm AI so I'm going to actually make a
1130.52s: new document just going to call it
1132.28s: steps. MD or even steps. text we have
1135.92s: the steps we want to do so we are going
1138.48s: to write a script that's tell it what
1141.24s: it's called it's going to be called um
1143.16s: description generator. piy that scrapes
1146.76s: URLs in our data updated. CSV file for
1153.32s: information to summarize into a brief
1157.32s: summary first let's connect to the
1160.52s: Venice AI API now we can't just say that
1164.60s: with open AI maybe anthropic yeah but
1166.24s: Venice isn't as deep into the system so
1169.08s: we're going to go to Venice ai's
1171.80s: documentation and in here we're going to
1173.60s: go to their reference and basically I
1176.16s: don't know what a Swagger definition is
1177.92s: but in fact this is actually perfect
1179.88s: we're going to take that Swagger that
1182.48s: yaml Venice actually let's make a folder
1185.76s: called Venice
1187.76s: docs okay and in Venice docs we're going
1190.48s: to make a file called Swagger DOL going
1193.24s: to paste all that in there and that has
1195.96s: like all these little things that the
1198.16s: script is going to need to know in order
1199.72s: to communicate with the Venice aai
1201.60s: through their API including the URL that
1203.80s: might be enough um but basically I'm
1207.00s: going to copy all this in there too and
1209.60s: I'm going to say what do we call
1212.08s: Basics Mt copy that in there um all
1216.72s: right so now we've copied and pasted
1219.08s: whenever you're going to use an API or a
1220.88s: script which we're going to use with
1221.88s: craw for AI copy and paste it into your
1224.76s: workspace in a file so that way you can
1227.12s: drag this in and say okay write a script
1230.40s: we're going to write a script but first
1232.40s: let's connect to the Venice AI API
1234.88s: successfully check Venice
1237.40s: docks and add it to the python
1241.76s: script all right so now I hadn't saved
1245.92s: that but hopefully it's
1252.88s: okay so I've already got the Venice API
1255.52s: key in there and that's giv me the code
1258.12s: and I'm going to apply that to
1259.28s: description generator except file now
1261.68s: you can see it opens open AI cuz it uses
1263.96s: open ai's uh module and you just change
1266.76s: a few things to Venice looks like it's
1268.72s: got the right base URL um I've been
1271.00s: working with Venice AI enough to know
1273.32s: that this is working uh so okay we're
1275.20s: going to save that and now we are going
1278.36s: to install these
1283.32s: dependencies okay they're all installed
1285.56s: now now we're going to do Python 3
1288.76s: description generator.
1291.60s: py um it failed to do everything but it
1294.80s: looks like we didn't it yeah so add a
1298.28s: command so we can just test the API
1303.88s: connection all right so now it's just
1307.08s: going to add this little this um this
1310.32s: text basically so once we connect it
1312.20s: says hey it's work and we just have to
1315.04s: run Python 3
1319.28s: description generator test so this flag
1321.24s: here is just saying hey we're going to
1322.52s: test it that you can add like okay it it
1325.28s: failed so we're going to send this what
1331.48s: happened and our lovely AI agent is
1334.76s: going to tell us what
1337.16s: happened and let's
1340.76s: see okay so it's going to change
1342.72s: whatever it needs to change save it
1344.24s: let's try that
1345.36s: again testing connection successful all
1348.32s: right so that's step one all right now
1351.24s: let's go back to our steps and we got
1354.48s: okay so that one's done two scrape the
1356.32s: website all right so here's where crawl
1359.04s: for AI comes in so crawl for AI here is
1362.16s: a really awesome script here and
1365.12s: basically as we're going through we can
1367.08s: obviously ask the AI to write a code for
1368.64s: us but code creation is not simple
1371.12s: there's a reason it's a high paying
1373.24s: career F you know it's it's a big deal
1375.40s: it's been a big deal for so long cuz it
1377.08s: just takes time things don't always work
1378.80s: right even if you're in AI so while it
1380.88s: is getting better it still is great to
1382.56s: use project repositories Frameworks out
1385.00s: there that already built for you and
1386.92s: then the AI doesn't have to build it it
1388.12s: just says oh use that use that use that
1390.08s: so what we're going to do is we're going
1391.48s: to install we're going to do the quick
1393.16s: start here and we're going to install
1395.56s: and then we're going to implement crawl
1397.84s: for AI into our project that's
1400.36s: installed
1403.40s: setup
1405.00s: boom and then now it says verify your
1407.64s: installation make sure sure it's working
1409.52s: that's another python script going to
1411.76s: check through example.com it's going to
1413.48s: pull 300 characters so I'm just going to
1415.24s: copy that I'm going to make a new
1416.92s: document called test. python put that in
1420.48s: there save it and then just say Python 3
1423.16s: test. python it's going to test this
1424.96s: connection to example.com and it worked
1427.76s: got example domain this domain is that
1429.56s: that's what it that's what it scraped
1431.68s: all right so craw fre ey is open so back
1433.96s: to our steps so we want to scrape the
1435.60s: website and generate a description so
1437.48s: first off scrape the website so next we
1440.44s: want to scrape the U the
1443.52s: website URL from the from the listing
1447.72s: Row in data updated. CSV and we're just
1451.64s: going to say find two to three
1454.40s: paragraphs of relevant information to
1458.04s: summarize the
1460.32s: listing we can even say summarize the
1462.64s: shoe repair store format it to markdown
1466.80s: let's just say prune filter it and then
1470.24s: format it to markdown so that's the
1472.08s: first thing we're going to do um
1473.92s: basically and I I know that process
1476.36s: because I've been using it and I'm going
1477.48s: to walk you through it here now I
1479.20s: recommend you go through all of this
1480.84s: especially if you're going to do a lot
1481.72s: of data scraping but basically you copy
1484.44s: and paste what you want from the read me
1488.16s: just like we did with the Venice API
1489.92s: specs copied it into a document you do
1492.12s: the same thing here for this script so
1494.64s: then you you can just say hey use
1496.00s: browser config module use crawler run
1498.40s: config module or if you're doing deep
1500.40s: crawling use uh use uh deep crawl
1504.48s: strategy llm web scraping strategy so
1507.72s: instead of just blindly telling the AI
1510.52s: to do it you give it the documents so
1512.80s: you go to GitHub you just download the
1514.68s: zip and then I copied the docs folder
1517.04s: into cursor here and then here in mdv2
1521.12s: that's really where we see everything so
1523.32s: I'm going to document I'm going to drag
1525.20s: mdv2 which are the docs and I'm going to
1527.88s: put that
1529.32s: uh what needs to be higher up Okay C
1533.48s: documentation in
1535.72s: mdv2 now one thing we need to know
1538.32s: though is what modules do we want to use
1540.28s: use
1541.64s: modules all right so first off we're
1545.04s: going to that's simple crawling it's
1546.84s: basically going to do that on its own
1548.08s: we're definitely going to use async web
1549.64s: crawler because that's the very basics
1551.36s: of
1552.68s: everything um async web crawler we going
1556.32s: to need crawler result I believe
1559.00s: um yeah cuz this results
1563.12s: everything it puts out everything it
1565.48s: finds um llm config um we're going to
1569.24s: use LM
1573.04s: config we're going to use markdown
1576.24s: generation to clean it
1581.80s: up uh we're going to use fit markdown
1584.60s: and in order which is basically using a
1586.20s: Content filter like we mentioned so
1587.80s: we're going to use pruning content
1589.12s: filter here once again I'm very familiar
1591.40s: with this but you might have different
1592.84s: purposes like bm25 could be good if you
1596.40s: want to scrape search results for
1597.96s: example so make sure you go through all
1600.32s: this for your own use case I'm just
1602.12s: doing kind of the the be Basics here we
1605.32s: do want to make a cach so cach
1608.76s: mode that'll kind of speed things up a
1611.00s: little bit all right so I think that's
1613.48s: good we'll just say modules to consider
1619.16s: all right so it's not going to generate
1620.76s: it yet it's not going to generate
1622.64s: anything yet it's just going to scrape
1624.12s: the website and get the two to three
1625.40s: paragraphs of text how about we say
1627.64s: format it to markdown create a unique
1631.76s: directory per listing with its own
1634.72s: markdown file so it has the raw data we
1637.00s: got the two to three paragraphs okay so
1639.32s: we're going to send that out now and
1640.40s: we're going to see how it
1642.36s: does and once again it has the
1644.56s: documentation here for the script
1646.32s: doesn't mean it's going to do it right
1647.52s: but it looks so so far like it's doing
1649.04s: it right and if we said connect to vsai
1652.16s: and now scrape the website and now
1653.28s: generated description all at once it
1655.28s: wouldn't work in fact I recorded this
1657.16s: for an hour before and I did that and it
1658.68s: didn't work so I'm recording it again um
1660.96s: so that's a very important lesson I'm
1662.88s: trying to pass on to you there are the
1664.92s: changes here you're seeing it's
1666.00s: importing more modules it's added all
1667.56s: this code okay accept file okay so let's
1670.24s: see what happens here we got pyone 3 the
1673.72s: last thing we want to see is uh where is
1675.60s: it getting yeah it's getting the right
1677.08s: CSV file
1678.92s: Python
1680.20s: 3 description generator. py okay so we
1683.72s: got an error there um we highlight that
1686.72s: we add it to the chat what
1689.16s: happened uh we switched to ask for that
1693.32s: basically ask I believe you use like a
1695.84s: cheaper llm and then agent you use a
1697.72s: more powerful more expensive llm smarter
1700.64s: one all right so description generator
1703.32s: all right so whatever I don't know what
1704.44s: it did um oh you have to do it somewhere
1706.60s: else
1708.76s: whatever that is okay let's
1710.84s: see still not working let's send it to
1713.12s: the chat what
1717.20s: happened oh default markdown generat in
1719.40s: a different module so yeah I mean the AI
1722.16s: has to figure stuff out just like us
1724.08s: humans so the simpler you make and the
1726.64s: more concise all the directions the more
1729.20s: chance it'll be done accurately the
1731.12s: first time but of course you can okay so
1733.68s: the the script ran but of course you can
1734.96s: always just do it like this and just
1736.08s: debug as you go um all right so we got
1739.12s: an error there let's send it
1741.24s: here
1744.88s: happened prob URL right it didn't have
1747.88s: anything to
1749.88s: crawl still didn't work we're going to
1752.44s: say error again are we sure it's pulling
1756.48s: the URL from the
1758.76s: data updated. CSV file he so this part
1762.68s: of the video is kind of boring cuz I go
1763.96s: back and forth a bit so I'm going to cut
1765.16s: back in So once we solve the problem of
1766.68s: it finding the URL we go on to the next
1768.96s: problem the key Point here is solve one
1771.52s: problem at a time don't try to solve
1773.32s: multiple problems with one prompt it
1775.04s: will just make more problems probably
1777.48s: okay wait all right it's crawling it's
1778.96s: crawling okay we still failed but we got
1781.28s: some progress crawl result as no okay
1785.76s: so uh oh let's see we see that at least
1790.08s: it is scraping data it's getting the
1792.32s: original stuff yeah so there we go
1794.52s: that's probably like part of the
1795.40s: description quality so it's doing the
1796.88s: scraping right that much is working but
1799.52s: what's not working is whatever is next
1802.16s: so yeah generating a description
1808.28s: so not working it's something to do with
1811.40s: the Venice
1813.08s: API we need to remove Venice parameter
1815.68s: since we're using the async open AI
1817.16s: client fix the generate okay yeah so
1820.64s: basically this is just slight things to
1822.08s: do I think between open AI
1824.60s: versus Venice AI apis
1828.52s: let's see let's
1830.88s: see oh I think it
1834.20s: worked processing Row one all right so
1837.56s: let's cancel that and let's just see we
1840.24s: should have updated file
1843.92s: here it generated a description we just
1846.56s: didn't tell it where to put it and
1848.32s: that's perfect because all we wanted to
1850.28s: do is scrape website now it is
1852.76s: generating the description so we've got
1854.28s: the description so now we need to say um
1857.68s: make make sure the
1859.16s: script make sure the script outputs the
1862.32s: description the generated description to
1865.32s: the description
1866.76s: column of the uh of an updated CSV file
1872.52s: call that data
1875.20s: updated uh descriptions that's CSP and
1878.92s: we're almost
1880.76s: done I think it's already doing
1885.36s: this these last two might already be
1887.40s: built in we're going to find out okay so
1890.32s: there's our code we'll accept everything
1893.16s: there and I've got a good feeling that
1895.44s: we're we're getting
1897.20s: close
1898.92s: boom so it saved the markdown file not
1902.80s: seeing a new CSV file I have a feeling
1905.64s: it's doing it in the end which is why we
1909.20s: wrote these
1911.04s: steps so it's probably just putting the
1913.88s: descriptions it's generating into its
1915.84s: memory which might be adding extra
1918.36s: context yeah and then it makes the file
1919.92s: at the end exactly what it did
1922.32s: here
1923.92s: so there's a brief
1927.56s: description all right so let's open this
1930.20s: it's back here where is it right here
1932.52s: descriptions all right now we obviously
1934.32s: need to work on this prompt here's a
1935.64s: brief description of the shoe store um
1939.52s: yeah it's not working but it's close
1942.36s: Okay so at least it's like doing what we
1944.16s: want it's just not doing it right it
1946.24s: skipped the no website on that's good
1949.00s: they did have this here so that's the
1951.44s: description I gave first Sho repair also
1953.80s: known as America's gobler offers expert
1956.48s: shoe repair okay I mean they do it too
1958.68s: here so all right so it's good but it's
1961.96s: no cigar so we're going to
1966.52s: say um we don't even need to say this to
1969.96s: the agent let's just go to the
1972.60s: prompt and let's find
1980.84s: you are a helpful assistant that creates
1982.44s: concise informative descriptions of sh
1984.56s: repair businesses so this is the prompt
1985.96s: it's giving the llm focus on key
1988.04s: Services Specialties and unique
1989.88s: features um okay and then we just say um
1994.16s: do not output anything else with the
1997.48s: description thank you autofill um and we
1999.72s: all say do not make anything up if
2003.24s: there's not enough data say not enough
2006.60s: data okay so now we change that prompt
2010.16s: and um let's just say create a two to
2013.40s: three sentence
2015.60s: description all right so now I'm going
2017.32s: to delete that new CSV file so we don't
2020.12s: get all messed up and we're going to run
2021.68s: this new script
2023.60s: again if this is happening how it should
2026.20s: be which I'm not sure it is but it's got
2028.84s: these content MD files already there
2031.12s: that's just generating the descriptions
2032.52s: from there's one other thing we need to
2034.56s: do still which is actually steps five
2036.40s: and six together which is well it's
2039.00s: already repeating the process but then
2040.32s: save the updated CSV file as it goes so
2044.76s: let's save the rows with descriptions to
2049.92s: the new CSV file
2053.08s: one by one instead of
2058.04s: waiting so we're just going to have to
2059.80s: do that and then we're done with the
2060.96s: steps
2062.40s: document um once again we go to the
2064.64s: descriptions
2066.44s: here and let's just see how that line
2069.04s: did there we go McFarland shoe repair
2071.00s: also known as am's cobbler offers high
2072.36s: quality shoe repair services Drive shoe
2074.08s: repair not enough data Phenix muled
2076.44s: shoes inserts and braces Redwing shoe
2078.64s: store in Lakeland Florida okay so we got
2080.48s: it okay the last thing we would do like
2082.52s: I said we had say hey write it one by
2084.76s: one instead of all the time at the end
2087.00s: so if uh we delete that right
2089.64s: now and do that
2091.80s: again we're going to notice it makes a
2093.88s: new CSV file
2096.12s: sooner boom so it's there then it's got
2100.76s: uh yeah same description pretty much and
2102.48s: it's just going to add our new ones
2104.60s: there one at a time perfect so we have
2107.28s: some base data now but we're going to
2109.16s: want to clean it a little more which is
2111.84s: why like on this one not enough data
2114.56s: let's go to this website let's see I
2116.84s: mean yeah I see why there's not enough
2118.12s: data
2119.56s: huh um but it's it's there right it's
2122.56s: not actually a shoe store they fix
2126.08s: shoes they kind of fix shoes but we're
2129.76s: looking for
2130.76s: people I'm just going to delete that
2133.20s: that listing uh not enough data let's
2135.48s: check this one there's a Facebook link
2138.68s: that would be why now maybe in another
2140.84s: video we'll go over how we can give it
2142.24s: our Facebook login and like hey log in
2144.48s: and get this information I'm not going
2146.00s: to do that in this video um all right so
2148.60s: we're running it one last time we're
2150.48s: going to have our final data we're going
2152.36s: to delete a few listings and next up
2154.36s: we're going to put it into a website all
2157.44s: right so it's making the new
2159.48s: folder made the new CSV file boom we got
2163.28s: it and it's got descriptions okay great
2165.64s: so we have our data updated
2167.72s: descriptions. CSV okay so we got this
2170.20s: there's one last thing we want to do and
2172.24s: that is take the address and split it
2174.88s: into a few different columns CU we want
2176.64s: to have the city in its own column the
2179.00s: state not so much cuz it's all only just
2180.68s: Florida and the zip code so let's say
2183.40s: let's write let's make a new file and
2185.32s: let's call it um blit
2190.00s: address and we're going to say write a
2193.28s: script as split address that separates
2198.76s: the street address from the
2203.48s: city Z code State and Country into new
2210.04s: columns all right so here we go split
2212.44s: address.
2213.64s: piy um let's see what CSV file is it
2219.84s: using data updated descriptions that's
2222.08s: CSV Alpha file let say data updated
2224.84s: addresses okay fine so this is where
2226.96s: your taxonomy it's getting important
2229.12s: you're going to get all these data files
2230.40s: you got to stay organized I just keep
2231.64s: making new folders after a new uh leap
2234.92s: okay so we're going to run that now
2238.16s: well run
2240.08s: command all right cool so it worked
2243.24s: let's see now let's see we got
2249.68s: address street address city state ZIP
2252.16s: code
2253.68s: country go all the way to the end D
2257.16s: address city state ZIP code country
2259.64s: perfect so now we have all the data we
2261.20s: need now what we're going to do is
2263.20s: convert it to Json convert to json. Pi
2267.24s: and we're going to say we could just put
2269.64s: it here say write a script that converts
2275.12s: data updated addresses that's our latest
2278.60s: one to Json for use in populating a
2282.68s: directory website to a Json
2289.32s: file so CSV is great for spreadsheets uh
2293.36s: it's good for a lot of things it could
2294.72s: also work on a website but Json is the
2296.80s: standard so here we go we're going to
2299.64s: run this script now we're going to
2301.04s: convert our lovely
2304.80s: uh going to convert our lovely CSV file
2309.12s: Python 3 convert json. piy boom and now
2313.72s: you'll see what it looks like
2316.16s: is is stores. Json oh shoe stores great
2320.64s: so now we got stores. Json and it's
2322.48s: organized all that information this is
2324.28s: what a Json file looks like each new
2326.32s: squiggly line means it's a new entry
2328.96s: boom latitude longitude great we got all
2331.12s: the info we need now make our shoe
2333.76s: repair shop in Florida hey guys before
2336.40s: we continue with the best part of this
2338.32s: project making the website I just wanted
2340.16s: to let you know that this is a brand new
2342.12s: channel and if you're still watching if
2343.80s: you're finding value in this I would
2345.88s: absolutely love it if you could press
2347.48s: like and maybe even subscribe if you
2349.56s: want to continue building with me I'm
2351.24s: going to be making videos like this a
2352.56s: lot I love building I love using AI so
2355.84s: if you could do that that would be
2357.32s: really awesome okay let's build this
2359.28s: website we're going to go to bolt. new
2362.84s: there's also bolt. DIY which is a fork
2365.92s: of bolt. new uh and you can run it
2368.24s: locally with local models but it is
2370.36s: pretty slow so um I I'm using bt. new um
2375.08s: I love open source stuff but I tried
2376.56s: both on DIY it just took forever so I
2378.92s: have two two two million monthly tokens
2380.84s: remaining I'm going to try to use less
2382.00s: than half of that I used 8 million for
2383.88s: building monori fine uh and I was
2386.72s: learning bolt. new as I went so I
2388.52s: realized I could have done it for
2389.44s: cheaper I'm going to say build a direct
2393.96s: I'm not even gonna okay you could use
2396.00s: versel nextjs you could study up on
2398.44s: these Frameworks spelt um and choose
2401.48s: which one you want but we're just going
2402.88s: to let it do it okay um it's going to
2404.84s: use nextjs probably um but I'm going to
2408.04s: show you two ways to do this first we're
2410.44s: just going to give it to bolt. New build
2412.12s: a directory uh for shoe repair shops in
2418.36s: Florida uh the listings are in the
2422.80s: attached Json file include a Blog fact
2429.12s: the directory Eng opiz include a Blog uh
2433.36s: and
2434.20s: fact and photos of shoes from
2438.44s: unsplash all right this is going to be
2441.64s: fun to see what happened so let me give
2446.20s: it let's give it our stores. Json file
2449.36s: and let's watch the magic happen
2460.20s: okay so next what you just see is a
2461.88s: whole lot of things being built and
2465.00s: it'll tell you what's going on over
2466.12s: there this is what's crazy this is
2467.24s: what's changed everything for me you can
2468.96s: just say what you want it to do like in
2470.40s: terms of functionality with users and
2472.56s: logging in you could you could just keep
2474.28s: going and going a director website is
2476.04s: fairly simple for what's possible here
2478.64s: and in future projects I'll be exploring
2480.32s: that myself look it's even making blog
2482.88s: posts here how to make your shoes last
2484.44s: longer the art of shoe repair how do I
2486.68s: know if my shoes can be repaired back
2489.20s: frequently asked questions this is great
2491.20s: I mean when it's this easy it's like why
2493.28s: not why not make a Florida shoe repair
2495.44s: directory you know like why
2499.72s: not all right so it's starting the
2502.64s: application now it tells us what it did
2505.64s: and um I don't know how many tokens it
2507.96s: used apparently not that
2509.84s: many go to the preview here boom all
2514.48s: right let's check this
2515.92s: out find expert shoe repair in Florida
2520.72s: search McFarland shoe repair frequently
2524.48s: asked questions how to make your shoes
2527.12s: last longer okay let's go to McFarland
2528.92s: shoe repair here all right listings oh
2531.52s: it only has one
2532.76s: listing uh is this because of our Json
2535.84s: file did we mess up our Json file no
2538.92s: it's all there um so we need to tell it
2541.84s: to import the rest yeah import the rest
2545.56s: of the schools from this stores. Json
2551.00s: file as you can see here it's just
2553.56s: showing all the listings and you can
2555.68s: obviously go back and forth I'll show
2557.44s: you in a
2560.52s: second this is probably using more
2562.92s: tokens to add in all this
2570.16s: stuff it's populating everything now
2572.32s: there is a faster way to do this which
2574.60s: uh I'm going to show you in a moment but
2576.40s: for now we'll just leave it Let It Go
2578.20s: all right so I put all the stores in
2579.68s: there and now we can preview it again
2581.56s: boom it's got all the listings
2583.44s: here now what we could say is oh we
2585.80s: forgot we could say make the listings
2590.84s: page um show all available cities with
2596.00s: listings and then each City page shows
2599.92s: the entire feed of its listings and I
2602.48s: want to use one column I don't like this
2603.96s: two column thing in one column
2607.48s: now I'm just telling it what to do like
2610.28s: this is how it was for me when I was
2611.72s: working with developers I would just say
2613.20s: hey do this but they were always like
2615.08s: non-native English speakers and
2616.76s: obviously sometimes it's hard to explain
2618.80s: things like this even in the same
2620.68s: language uh so like this is great the AI
2623.80s: just understands what I want and it just
2625.16s: does
2626.48s: it so here we go and as you can see we
2629.20s: still don't seem to have used a lot of
2630.52s: tokens I think we've still Ed less than
2632.04s: 100,000 tokens that's crazy unless it
2635.40s: just hasn't updated it's to me on the
2637.56s: back end n all right so let's
2642.48s: see
2645.96s: starting all right so now we go to
2649.44s: cities and boom M land shows you all the
2653.28s: ones there and so as someone else can
2655.56s: explain better than me this is like this
2657.44s: is a good way of doing
2659.04s: um like SEO Pages it just has all this
2662.64s: all of them on one page and so there you
2664.64s: go we just made
2667.36s: uh Florida shoe repair store now there's
2670.12s: one more step here um obviously you can
2672.16s: keep going back and forth with the AI oh
2673.88s: I finally use 100,000 credits but you're
2675.32s: going to use credits so that's how I
2677.32s: wasted so many credits is I didn't
2678.72s: really realize how simple it would be to
2679.96s: fix things and this is where the coding
2681.60s: comes in or doesn't come in but
2683.40s: essentially for little things or for
2685.56s: bigger things try to get as much done in
2687.36s: Bolt while you're here especially for
2689.48s: like round one you can import a project
2691.60s: back into bolt later but for now I'm
2693.52s: just going to show you what happen so
2694.60s: you have this and you go to export and
2696.88s: you you can download the
2699.64s: file and you can open in stack blit so
2702.60s: you can do both and basically what I can
2705.44s: do now is edit it all so I can say like
2708.08s: okay the title of the page should not be
2709.64s: that it should be shoe repair shops in
2713.00s: Florida save and then I can click create
2716.12s: a repository here connect it to GitHub
2719.12s: and we say shoe repair shops
2723.12s: Florida and I could make a private I
2725.36s: would recommend making a private if you
2726.80s: have data that you worked really hard to
2728.36s: scrape there uh any public repo someone
2730.88s: can just take all the data and do it
2732.48s: themselves all right so let's enable
2734.88s: that bot why not so now we have a total
2736.92s: workspace looks like cursor right looks
2739.32s: like cursor but the difference is you
2740.80s: don't really have an AI agent with you
2742.20s: but you do you can see everything right
2743.72s: next to you as you work if there is an
2745.52s: AI agent in here I don't know how to use
2748.04s: it yeah so there we go now we have this
2751.40s: connected to GitHub I'm going to GitHub
2753.40s: I'm here at Shoop Sho Sho repair shops
2755.64s: Florida and I am going to SSH into it
2758.64s: I'm copying that I'm going to go to
2760.44s: cursor and then I'm going to say new
2762.80s: window and I'm going to say uh clone
2766.32s: repo and I'm going to paste
2769.72s: that boom now it's cloning
2773.76s: everything probably going to ask for my
2775.60s: password yep when you're using SSH
2777.92s: you're going to need a password that's
2779.60s: something you can find all over the
2780.68s: internet but if you have questions about
2782.36s: SSH let me know we're going to open it
2785.32s: here and now we have our site so now
2788.52s: when there's smaller changes or if we
2790.96s: want to use cursor then we just excuse
2793.84s: me cursor AI The Coop pilot and we can
2795.44s: just get in here so this is definitely
2797.84s: stuff for another video but I'll run
2799.64s: through it quickly basically in your
2800.88s: Source components this is how the blog
2803.08s: page will look this is how the city list
2805.76s: City page FAQ Store card will look and
2809.20s: you can essentially adjust everything so
2811.88s: if I want to run this site locally on my
2813.64s: computer so I can make changes then I go
2815.36s: to new terminal and I say mpm install
2819.64s: I'm pretty sure it's mpm yeah what I
2822.64s: would do is I would just um add the
2824.72s: source into here and say how do I run
2830.04s: this project write a read
2834.92s: me boom and then it's going to tell you
2838.16s: what to do run the script similar how it
2840.60s: tell helped us write write and launch
2842.72s: the Python scripts earlier
2850.48s: all right so now it's just going to do
2851.48s: that it's going to tell you what to do
2853.44s: we already did mpm install so we apply
2856.48s: to readme and boom it wrote us a readme
2859.00s: great I already did npm install now
2860.96s: we're going to do mpm
2863.52s: runev and now you can see I'm going make
2866.08s: this a little smaller
2868.36s: here and you can see you can command
2870.68s: click this Local Host link and you're
2873.44s: running Florida shoe rep shoe repair
2876.32s: shops on your
2877.92s: computer okay so now if I make a change
2881.56s: so for example uh header is this um
2885.80s: Florida shoe repa
2890.52s: three yeah Florida shoe directory so I
2893.88s: don't really like that hammer right I go
2896.36s: in here and I could just say all right
2898.72s: here in the header where it says Florida
2900.00s: shoe repair we could say like the number
2902.88s: one Florida shoe repair director yeah
2905.56s: I'll just change it as soon as I save
2906.64s: the file you'll see it uses that hammer
2909.56s: somewhere like right here it says Hammer
2911.40s: so I'm going to highlight it Apple K and
2913.76s: say change this graphic to a shoe oh a
2919.68s: shoe I said show oh yeah okay great and
2922.76s: new I save it and there is no shoe so
2928.00s: what happened I say why um the whole
2933.00s: site doesn't display after changing
2937.04s: Hammer
2938.32s: to now I know why show shoe because it
2942.12s: wasn't imported so up here you see how
2943.72s: it's importing Hammer from lucd react
2946.40s: which is the icon base so we needed to
2948.12s: say import
2949.88s: shoe um
2952.24s: so we accept the file I think I
2954.68s: accidentally can SH
2959.28s: now it also change that shoe oh so there
2963.48s: isn't a shoe icon so um I don't know
2966.24s: scissors
2968.08s: so I just said let's use
2970.36s: scissors I can also just go to the seed
2973.00s: react icons can Google that and I can
2975.92s: see what the icons are like
2978.84s: shoe nothing but whatever we'll change
2981.52s: it to
2982.52s: scissors and there are the scissors so
2985.48s: anything you want to change like text
2987.44s: SEO stuff you can just do that in there
2989.92s: pretty cool and
2992.24s: um yeah there's a lot of possibilities
2995.16s: here and it does to work for you so um
2999.80s: that's it for this video um just to give
3002.92s: you an idea of you know more that could
3005.04s: be possible what I've been working on
3006.72s: here is you go to a listing and you see
3010.92s: the hours you see the map and uh this is
3014.52s: just a map embed that you can tell bolt.
3016.36s: new to put in and you got to give it
3017.80s: your API key but you could say click
3020.00s: here for more or like fix this listing
3022.44s: or submit my own review so these buttons
3024.60s: are going to have added functionality
3025.88s: that help it become more interactive
3027.84s: basically so there's a lot more to
3030.52s: explore when you're building your shoe
3032.36s: repair shop or whatever your directory
3034.12s: is and um I hope this was valuable to
3036.40s: you if you have any questions leave in
3037.48s: the comment thanks for subscribing
3039.12s: giving a like if this was valuable to
3040.52s: you if you have any questions doing my
3042.48s: best to uh help you out sign up for my
3044.52s: newsletter if you want to hear more
3045.88s: about what I'm working on and the joy I
3048.68s: find in building and putting things
3050.32s: together thanks for joining me today
