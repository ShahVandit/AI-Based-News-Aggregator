# coding=utf8
# ENGLISH
import nltk
import pandas as pd
import random
import numpy as np
import tensorflow as tf
import json
import matplotlib.pyplot as plt
from indicnlp.tokenize import sentence_tokenize
import indicnlp
import nltk
import gensim
import re
def cleanText(text):
      # text=re.sub(r'(\d+)',r'',text)
      text=text.replace(u',','')
      text=text.replace(u'"','')
      text=text.replace(u'"','')
      text=text.replace(u':','')
      text=text.replace(u"'",'')
      text=text.replace(u"‘‘",'')
      text=text.replace(u"’’",'')
      text=text.replace(u"''",'')
      text=text.replace(u".",'')
      text=text.replace(u"?",'')
      text=text.replace(u")",'')
      text=text.replace(u"(",'')
      return text
english_text="NEW DELHI: Domestic passengers can now seamlessly fly out of Delhi, Bengaluru and Varanasi by registering for DigiYatra (DY) that enables paperless travel through biometric facial recognition technology (FRT). This means that a facial scan will confirm the identity of DY-registered passengers, who then do not need to show any physical ID proof. Their travel details will also be captured in this technology. The FRT was rolled out for three airport by Union aviation minister Jyotiraditya Scindia at Delhi’s IGIA on Thursday. In the first phase, 7 airports will be DY-enabled starting with Delhi, Bengaluru and Varanasi on Thursday. Then by March 2023, Hyderabad, Kolkata, Pune and Vijayawada airports will get this facility. Subsequently other airports will get the same, the aviation ministry said in a statement. “The project envisages travellers pass through various check points at airports through a paperless and contactless processing using facial features to establish their identity which could be linked to their boarding pass. To use this facility, one-time registration on DY App is required using Aadhar-based validation and a self-image capture. The project has tremendous advantages of improving passenger convenience and ease of travel,” Scindia said. Allaying data security concerns for people registering on the app, the minister said: “There is no central storage of ‘personally identifiable information’ (PII) keeping in mind privacy (issues). Passenger’s ID and travel credentials are stored in a secure wallet in the passenger’s smartphone itself. The uploaded data will utilise blockchain technology and all the data will be purged from the servers within 24 hours of use.” The DY project has been conceived by the Digi Yatra Foundation under Union aviation ministry. With domestic air traffic reviving post Omicron, long queues are back at airports right from terminal entry to check-in, security and immigration. While using DY is optional as passengers can continue to show physical ID cards and tickets, those who use it can hope to clear some queues faster — especially terminal entry. Delhi airport has even marked some lanes for DY-registered domestic passengers. The roll out DY will enable airports in India to join the ranks of world class airports like London Heathrow and Atlanta that use biometric identification. Citing the example of Dubai International airport, Scindia said that passengers who use this technology can save 40% time required to be spent at the airport. “A similar technology saved nine minutes per aircraft time at Atlanta Airport. Compared to other airports (that have biometric technology), the Indian system has been made far more seamless from entry to exit and therefore will be one of the most efficient systems from across the world,” he added. How DigiYatra worksEnrolment process:* Download DigiYatra App by Digi Yatra Foundation from Play Store (Android) or App Store (iOS) and register using your Aadhaar-linked mobile number and OTP * Link your identity credentials using DigiLocker or offline Aadhaar. XML file to be uploaded for offline Aadhaar * Take a clear selfie with no obstructions when prompted and upload onto the app * Update your boarding pass on the DigiYatra App and share with the departure airport. Name on the boarding pass, flight ticket and Aadhaar must be the same At DY-enabled departure airport:* Arrive at DY-designated gate. In Delhi’s case: E-Gate, gate number 2 at Terminal 3 * Share and scan your bar-coded boarding pass/ mobile boarding pass * Look into the face recognition system (FRS) installed gate camera * On successful validation, the E-Gate will open to let you inside the airport * Once inside the terminal, drop your luggage at the airline check-in desk. If you have no luggage, proceed towards the DigiYatra Gate. In Delhi’s case, Zone 1 pre embarkation security check near business class entry * Look into the Face Recognition System (FRS) installed E-Gate camera * On successful validation, the E-Gate will open to allow you in for security check (Source: Delhi Airport website)"
def english_summary(indic_string):
# indic_string="NEW DELHI: Domestic passengers can now seamlessly fly out of Delhi, Bengaluru and Varanasi by registering for DigiYatra (DY) that enables paperless travel through biometric facial recognition technology (FRT). This means that a facial scan will confirm the identity of DY-registered passengers, who then do not need to show any physical ID proof. Their travel details will also be captured in this technology. The FRT was rolled out for three airport by Union aviation minister Jyotiraditya Scindia at Delhi’s IGIA on Thursday. In the first phase, 7 airports will be DY-enabled starting with Delhi, Bengaluru and Varanasi on Thursday. Then by March 2023, Hyderabad, Kolkata, Pune and Vijayawada airports will get this facility. Subsequently other airports will get the same, the aviation ministry said in a statement. “The project envisages travellers pass through various check points at airports through a paperless and contactless processing using facial features to establish their identity which could be linked to their boarding pass. To use this facility, one-time registration on DY App is required using Aadhar-based validation and a self-image capture. The project has tremendous advantages of improving passenger convenience and ease of travel,” Scindia said. Allaying data security concerns for people registering on the app, the minister said: “There is no central storage of ‘personally identifiable information’ (PII) keeping in mind privacy (issues). Passenger’s ID and travel credentials are stored in a secure wallet in the passenger’s smartphone itself. The uploaded data will utilise blockchain technology and all the data will be purged from the servers within 24 hours of use.” The DY project has been conceived by the Digi Yatra Foundation under Union aviation ministry. With domestic air traffic reviving post Omicron, long queues are back at airports right from terminal entry to check-in, security and immigration. While using DY is optional as passengers can continue to show physical ID cards and tickets, those who use it can hope to clear some queues faster — especially terminal entry. Delhi airport has even marked some lanes for DY-registered domestic passengers. The roll out DY will enable airports in India to join the ranks of world class airports like London Heathrow and Atlanta that use biometric identification. Citing the example of Dubai International airport, Scindia said that passengers who use this technology can save 40% time required to be spent at the airport. “A similar technology saved nine minutes per aircraft time at Atlanta Airport. Compared to other airports (that have biometric technology), the Indian system has been made far more seamless from entry to exit and therefore will be one of the most efficient systems from across the world,” he added. How DigiYatra worksEnrolment process:* Download DigiYatra App by Digi Yatra Foundation from Play Store (Android) or App Store (iOS) and register using your Aadhaar-linked mobile number and OTP * Link your identity credentials using DigiLocker or offline Aadhaar. XML file to be uploaded for offline Aadhaar * Take a clear selfie with no obstructions when prompted and upload onto the app * Update your boarding pass on the DigiYatra App and share with the departure airport. Name on the boarding pass, flight ticket and Aadhaar must be the same At DY-enabled departure airport:* Arrive at DY-designated gate. In Delhi’s case: E-Gate, gate number 2 at Terminal 3 * Share and scan your bar-coded boarding pass/ mobile boarding pass * Look into the face recognition system (FRS) installed gate camera * On successful validation, the E-Gate will open to let you inside the airport * Once inside the terminal, drop your luggage at the airline check-in desk. If you have no luggage, proceed towards the DigiYatra Gate. In Delhi’s case, Zone 1 pre embarkation security check near business class entry * Look into the Face Recognition System (FRS) installed E-Gate camera * On successful validation, the E-Gate will open to allow you in for security check (Source: Delhi Airport website)"
  # print(indic_string)
  tokenized_sentences=[]
  for i in sentence_tokenize.sentence_split(indic_string, lang='en'):
    tokenized_sentences.append(i)
  # stop word elimination
  no_stop_sentence=[]
  no_stop_sentences=[]
  list_no_stop_sentences=[]
  # remove punctuations
  sentences_clean=[cleanText(sentence) for sentence in tokenized_sentences]
  # nltk.download('stopwords')
  from nltk.corpus import stopwords
  stop_words=stopwords.words('english')
  for sentence in sentences_clean:
    for item in [x for x in sentence.split(' ') if not str(x) in stop_words]:
      no_stop_sentence.append(item)
    # no_stop_sentences.append(no_stop_sentence)
    list_no_stop_sentence=" ".join(no_stop_sentence)
    no_stop_sentences.append(no_stop_sentence)
    list_no_stop_sentences.append(list_no_stop_sentence)
    list_no_stop_sentence=[]
    no_stop_sentence=[]
  # word embedding
  # from collections import Mapping, defaultdict
  # from gensim.models import Word2Vec
  w2v=gensim.models.Word2Vec(no_stop_sentences,min_count=1,iter=1000)
  # vec += model_w2v.wv[word].reshape((1, size))
  sentence_embeddings=[[w2v[word][0] for word in words] for words in no_stop_sentences]
  # len(sentence_embeddings)
  max_len=max([len(tokens) for tokens in no_stop_sentences])
  sentence_embeddings=[np.pad(embedding,(0,max_len-len(embedding)),'constant') for embedding in sentence_embeddings]
  # similarity matrix
  from scipy import spatial
  import networkx as nx
  similarity_matrix = np.zeros([len(no_stop_sentences), len(no_stop_sentences)])
  for i,row_embedding in enumerate(sentence_embeddings):
      for j,column_embedding in enumerate(sentence_embeddings):
          similarity_matrix[i][j]=1-spatial.distance.cosine(row_embedding,column_embedding)
  # page ranking
  import math
  from collections import OrderedDict
  nx_graph = nx.from_numpy_array(similarity_matrix)
  try:
    scores = nx.pagerank(nx_graph,max_iter=600, tol=1.0e-1)
    # print(scores)
    top_sentence={sentence:scores[index] for index,sentence in enumerate(tokenized_sentences)}
    # Printing sorted dictionary
    top=dict(sorted(top_sentence.items(), key=lambda x: x[0], reverse=True)[:math.floor(len(tokenized_sentences)*0.4)])
    counter=0
    sumamry_w2v=""
    for sent in tokenized_sentences:
        if sent in top.keys():
          sumamry_w2v+=sent
          counter+=1
  except:
     sumamry_w2v=tokenized_sentences[:6]
  return (sumamry_w2v)
gujarati_text='પાકિસ્તાનમાં ફસાયેલા ભારતીય નાગરિકો ખેડૂત પરિવાર સાથે સંબંધ ધરાવતા ઇશાકભાઈ બોકડા પાકિસ્તાનના કરાચીમાં એક લગ્નપ્રસંગમાં સામેલ થવા માટે 11 માર્ચે ભારતથી ગયા હતા. તેમનું કહેવું છે કે માર્ચમાં જ તેમને ત્યાંથી પરત આવવાનું હતું, પરંતુ લૉકડાઉનને કારણે 26 લોકો ત્યાં ફસાઈ ગયા છે. ઇશાકભાઈ અને તેમની સાથેના અન્ય ભારતીય નાગરિકો પણ ભારત પરત આવવા માગે છે અને એ માટે તેમણે ભારત સરકારની મદદ પણ માગી છે. તેમણે બીબીસી સાથે વાતચીતમાં કહ્યું કે અમે ઇસ્લામાબાદમાં ભારતીય હાઈકમિશનને અરજી કરી છે, પરંતુ હજી સુધી કોઈ ઠોસ માહિતી નથી મળી. બીબીસીએ આ અંગે વાત કરવા માટે ભારતીય વિદેશમંત્રાલયનો સંપર્ક કર્યો હતો, પરંતુ આ લખાઈ રહ્યું છે ત્યાં સુધી કોઈ જવાબ મળી શક્યો નથી. ઇશાકભાઈ કહે છે કે અમૃતસરથી ગુજરાત આવવા માટે તેમણે ચાર જૂનની ટ્રેનની ટિકિટનું બુકિંગ પણ કરાવી લીધું છે અને અન્ય તમામ વ્યવસ્થા થઈ ગઈ છે, પરંતુ પાકિસ્તાનથી ભારત આવવા માટે અટારી-વાઘા સરહદ પાર કરવાની પરવાનગી મળી શકી નથી. ગોધરાના આ પરિવારે રમઝાન અને ઈદ પણ પાકિસ્તાનમાં ઊજવી છે. ઇશાકભાઈ જણાવે છે કે "રમઝાન અને ઈદ પણ અમે પરિવારથી દૂર અહીં પાકિસ્તાનમાં ઊજવી છે, પણ હવે ઘરે જવું છે." ઇશાકભાઈ પોતાનાં પત્ની, પુત્રી, ભાણેજ અને અન્ય બે લોકો સાથે પાકિસ્તાનના કરાચીમાં છે. તેમણે કહ્યું, "ગોધરાથી વરરાજા સાથે 26 લોકો બારાતમાં પાકિસ્તાનના કરાચી ગયા હતા. નિકાહ માર્ચની 14 તારીખે પઢવામાં આવ્યા હતા. દુલ્હા અને દુલ્હનને જરૂરી દસ્તાવેજ તૈયાર કરીને થોડો સમય પાકિસ્તાનમાં રોકાવાનું હતું, પરંતુ બાકીના લોકો જે નિકાહમાં સામેલ થવા માટે ભારતથી ગયા હતા તેમને પાછું આવવાનું હતું." તેઓ જણાવે છે કે 22 માર્ચે જનતા કર્ફ્યુ જાહેર થયા પછી બૉર્ડર બંધ કરવામાં આવી હતી એટલે તેઓ પાછા ફરી ન શક્યા. ઇશાકભાઈ વધુમાં કહે છે કે પાકિસ્તાનમાં નવવિવાહિત દંપતી તો સાથે છે, પરંતુ તેમની બારાતમાં આવેલા નવયુવાનોના પરિવારો ભારતમાં તેમની રાહ જોઈ રહ્યા છે. \'અબ્બુ ક્યારે ઘરે આવશો?\' પાકિસ્તાનમાં ફસાયેલા ભારતીય નાગરિકો તો ગોધરામાં દરજીકામ કરતા ઇમરાનભાઈનું કહે છે, "વતન તો વતન છે, બાળકો ઘરે રાહ જોઈ રહ્યાં છે." ઇમરાનભાઈ તેમનાં પત્ની આયેશા અને સાસુ મેહરુનિસ્સા સાથે કરાચીમાં એક નિકાહમાં સામેલ થવા માટે ફેબ્રુઆરીની 28 તારીખે ગયા હતા. તેમણે બીબીસીને જણાવ્યું કે તેઓ કરાચીમાં પોતાનાં ફોઈનાં પુત્રીનાં નિકાહમાં ગયા હતા. 19 માર્ચે પાછું આવવાનું હતું પણ જનતા કર્ફ્યુ અને પછી લૉકડાઉનને કારણે તેમણે ત્યાં જ રહી દસ દિવસ વધુ રોકાવાનું નક્કી કર્યું હતું. તેઓ કહે છે, "મારી બે પુત્રી છે અને એક નાનો પુત્ર. આઠ વર્ષનો પુત્ર દરરોજ ફોન પર કહે છે કે અબ્બા ક્યારે આવશો? " ઇમરાનભાઈનું કહેવું છે. "આ વખતે તો ઈદ પણ બાળકો વગર સરહદ પાર ઉજવવી પડી. હવે તો બસ રાહ જોઈએ છીએ કે ક્યારે અમને અમારા ઘરે જવાનો મોકો મળે. માતાપિતા, ભાઈ બહેન બાળકો બધાં જ ત્યાં અમારી રાહ જોઈ રહ્યાં છે. " ઇમરાનભાઈ જણાવે છે કે પાકિસ્તાનના કરાચીમાં ઈદની નમાજ પઢવા તેઓ મસ્જિદમાં ગયા હતા. મસ્જિદમાં સોશિયલ ડિસ્ટન્સિંગનું ધ્યાન રાખીને નમાજ પઢવામાં આવી હતી. પાકિસ્તાનમાં લૉકડાઉનમાં છૂટછાટ પાકિસ્તાનમાં ઈદ અને રમઝાનમાં બજાર ખોલી દેવામાં આવ્યાં હતાં. ત્યારબાદ ત્યાં ભીડ પણ જોવા મળી હતી અને ત્યાં કોરોના સંક્રમણ વધવાના પણ અહેવાલ આવ્યા હતા. 20 મેથી પાકિસ્તાનમાં આંશિક રીતે રેલસેવા પણ શરૂ કરવામાં આવી હતી. જૉન્સ હૉપકિન્સ યુનિવર્સિટી પ્રમાણે, પાકિસ્તાનમાં અત્યાર સુધી કોરોના સંક્રમણના 66 હજારથી વધારે કેસ આવ્યા છે અને 1395 મૃત્યુ થયાં છે. ઇશાક બોકડાનું કહેવું છે કે અન્ય દેશોમાંથી ભારતના નાગરિકોને વતન પાછા લાવવામાં આવ્યા છે તો પાકિસ્તાનમાંથી તેમને લાવવામાં આવે. ઇશાકભાઈએ ગોધરાથી બીબીસીના સહયોગી દક્ષેશ શાહને એક ઈમેલ પણ મોકલ્યો છે, જેમાં ભારતીય વિદેશમંત્રાલયને 26 ભારતીય નાગરિકો અંગેની માહિતી અને ચાર જૂનની \'ગોલ્ડન ટેમ્પલ ટ્રેન\'ની ટિકિટની કૉપી મોકલીને તેમને પાકિસ્તાનથી ભારતમાં આવવાની પરવાનગી માટે મદદ કરવા જણાવાયું છે. ઇશાકભાઈનું કહેવું છે કે જો તેમને ચોક્કસ માહિતી આપવામાં આવે તો તેઓ કરાચીથી લાહોર જવા માટે સ્થાનિક પ્રશાસન પાસેથી ડિપાર્ચર પાસ માટે અરજી કરી શકે અને અટારી-વાઘા સુધીની યાત્રાની વ્યવસ્થા કરી શકે. ઉલ્લેખનીય છે કે ભારતમાં તારીખ 31 મેથી લૉકડાઉન પૂર્ણ થઈ રહ્યું છે અને એ બાદ અનલૉક-1 અંતર્ગત લૉકડાઉનની મુદ્દત વધારવામાં આવી છે. જોકે, આ દરમિયાન \'વંદે ભારત મિશન\'માં 45 હજારથી વધુ ભારતીયોને વિદેશમાંથી વતન લાવવામાં આવ્યા છે. વંદે ભારત મિશનમાં 45 હજારથી વધારે ભારતીય વતન આવ્યા ભારત સરકાર દ્વારા આ અભિયાન હેઠળ કોરોના મહામારી વચ્ચે વિદેશમાં ફસાયેલા ભારતીયોને પરત લાવવા માટેની કામગીરી ચલાવવામાં આવી રહી છે. નોંધનીય છે કે કોરોના સંક્રમણ વધતાં આંતરરાષ્ટ્રીય યાત્રા બંધ કરવામાં આવી હતી, જેથી અનેક દેશોમાં ભારતીય નાગરિકો ફસાયેલા છે. સમાચાર એજન્સી પીટીઆઈ મુજબ વિદેશ મંત્રાલયના પ્રવક્તા અનુરાગ શ્રીવાસ્તવે જણાવ્યું કે \"વંદે ભારત મિશન હેઠળ અત્યાર સુધી વિદેશમાં ફસાયેલા 45 હજાર જેટલા ભારતીય નાગરિકોને પરત લાવવામાં આવ્યા હતા.\" તેમણે એમ પણ જણાવ્યું કે 13 જૂન સુધીમાં બીજા એક લાખ જેટલા ભારતીયોને પરત લાવવામાં આવશે. વિદેશમાં કોરોના મહામારીને કારણે ફસાયેલા ભારતીય નાગરિકોને સ્વદેશ લાવવા માટે ભારત સરકારે વંદે ભારત મિશન તારીખ સાત મેના રોજ લૉન્ચ કર્યું હતું. આફ્રિકા, લૅટિન અમેરિકાના દેશો અને યુરોપના કેટલાક ભાગોમાંથી ભારતીય નાગરિકોને વતન લાવવાની કામગીરી હાથ ધરવામાં આવી છે. અનુરાગ શ્રીવાસ્તવે ગુરુવારે જણાવ્યું હતું કે અત્યાર સુધી 45,216 ભારતીયોને વતન લાવવામાં આવ્યા હતા, જેમાંથી 8,069 પ્રવાસી શ્રમિકો, 7656 વિદ્યાર્થીઓ અને 5,107 વ્યવસાયિકોને પાછા લાવવામાં આવ્યા છે. પાડોશી દેશો નેપાળ અને બાંગ્લાદેશમાંથી જમીનના રસ્તે સરહદ પાર કરીને પાંચ હજાર જેટલા ભારતીયો વતન પાછા ફર્યા છે. મીડિયામાં આવેલા અહેવાલ મુજબ પાકિસ્તાનમાં ફસાયેલા 300 ભારતીય નાગરિકોને શનિવારે ભારત પાછા લાવવામાં આવશે. મીડિયા અહેવાલો મુજબ આ ભારતીયો અટારી-વાઘા બૉર્ડર પરથી સરહદ પાર કરીને વતન પાછા ફરશે. જોકે બીબીસી આ દાવાની પુષ્ટિ નથી કરી શક્યું. ભારતથી વતન પાછા ફર્યા પાકિસ્તાની નાગરિકો સમાચાર એજન્સી પીટીઆઈ મુજબ તારીખ 27 મેના દિવસે બાળકો સહિત 179 પાકિસ્તાની નાગરિકો અટારી બૉર્ડરથી પાકિસ્તાન પાછા ગયા હતા. તેઓ લૉકડાઉનને કારણે ભારતમાં ફસાયા હતા. 179 પાકિસ્તાની નાગરિકોમાંથી કેટલાક લોકો મેડિકલ વિઝા પર ભારત આવ્યા હતા અને હૃદયરોગો, કિડની અને લીવરની બીમારીની સારવાર કરાવી રહ્યા હતા. કેટલાક લોકો ધાર્મિક યાત્રા પર હતા અને કેટલાક લોકો સંબંધીઓને મળવા આવ્યા હતા. પીટીઆઈ મુજબ તેમાંથી 120 હિંદુ, બે શીખ અને બાકી મુસ્લિમ લોકો હતા. આ લોકો ગુજરાત, મધ્ય પ્રદેશ, મહારાષ્ટ્ર, છત્તીસગઢ, દિલ્હી, હરિયાણા, ઉત્તર પ્રદેશ અને પંજાબ જેવાં રાજ્યોમાં ગયા હતા. આ પહેલાં લૉકડાઉન દરમિયાન પાંચમી મેના દિવસે 193 પાકિસ્તાની નાગરિકોને પાકિસ્તાન જવા દેવામાં આવ્યા હતા. તમે અમને ફેસબુક, ઇન્સ્ટાગ્રામ, યૂટ્યૂબ અને ટ્વિટર પર ફોલો કરી શકો છો'
def gujarati_summary(indic_string):
  tokenized_sentences=[]
  for i in sentence_tokenize.sentence_split(indic_string, lang='gu'):
    tokenized_sentences.append(i)
  # stop word elimination
  no_stop_sentence=[]
  no_stop_sentences=[]
  list_no_stop_sentences=[]
  # remove punctuations
  sentences_clean=[cleanText(sentence) for sentence in tokenized_sentences]
  stop_words=[]
  stop_word_txt='api\stop_words\A.List.of.210.Gujarati.Stop.Words.txt'
  for line in open(stop_word_txt, encoding="utf8"):
    without_spaces=line.rstrip()
    word=without_spaces.split('\n')
    stop_words.append(word)
  stop_words=stop_words[:210]
  stop_words[0]='मैं'
  stop=['અથવા']
  for i in stop_words[1:]:
    stop.append(i[0])
  stop_words=stop
  for sentence in sentences_clean:
    for item in [x for x in sentence.split(' ') if not str(x) in stop_words]:
      no_stop_sentence.append(item)
    # no_stop_sentences.append(no_stop_sentence)
    list_no_stop_sentence=" ".join(no_stop_sentence)
    no_stop_sentences.append(no_stop_sentence)
    list_no_stop_sentences.append(list_no_stop_sentence)
    list_no_stop_sentence=[]
    no_stop_sentence=[]
  # word embedding
  from gensim.models import Word2Vec
  w2v=Word2Vec(no_stop_sentences,size=1,min_count=1,iter=1000)

  sentence_embeddings=[[w2v[word][0] for word in words] for words in no_stop_sentences]
  # len(sentence_embeddings)
  max_len=max([len(tokens) for tokens in no_stop_sentences])
  sentence_embeddings=[np.pad(embedding,(0,max_len-len(embedding)),'constant') for embedding in sentence_embeddings]
  # similarity matrix
  from scipy import spatial
  import networkx as nx
  similarity_matrix = np.zeros([len(no_stop_sentences), len(no_stop_sentences)])
  for i,row_embedding in enumerate(sentence_embeddings):
      for j,column_embedding in enumerate(sentence_embeddings):
          similarity_matrix[i][j]=1-spatial.distance.cosine(row_embedding,column_embedding)
  # page ranking
  import math
  # from collections import OrderedDict
  nx_graph = nx.from_numpy_array(similarity_matrix)
  scores = nx.pagerank(nx_graph,max_iter=500, tol=1.0e-3)
  top_sentence={sentence:scores[index] for index,sentence in enumerate(tokenized_sentences)}
  # Printing sorted dictionary
  # print("Sorted dictionary using sorted() and keys() is : ")
  top=dict(sorted(top_sentence.items(), key=lambda x: x[0], reverse=True)[:math.floor(len(tokenized_sentences)*0.4)])
  counter=0
  sumamry_w2v=""
  for sent in tokenized_sentences:
      if sent in top.keys():
        sumamry_w2v+=sent
        counter+=1
  return sumamry_w2v

def hindi_summary(indic_string):
  tokenized_sentences=[]
  for i in sentence_tokenize.sentence_split(indic_string, lang='hi'):
    tokenized_sentences.append(i)
  # stop word elimination
  no_stop_sentence=[]
  no_stop_sentences=[]
  list_no_stop_sentences=[]
  # remove punctuations
  sentences_clean=[cleanText(sentence) for sentence in tokenized_sentences]
  stop_words=[]
  stop_word_txt='api\\stop_words\\final_stopwords.txt'
  for line in open(stop_word_txt, encoding="utf8"):
    without_spaces=line.rstrip()
    word=without_spaces.split('\n')
    stop_words.append(word)
  stop_words=stop_words[:210]
  stop_words[0]='मैं'
  stop=['અથવા']
  for i in stop_words[1:]:
    stop.append(i[0])
  stop_words=stop
  for sentence in sentences_clean:
    for item in [x for x in sentence.split(' ') if not str(x) in stop_words]:
      no_stop_sentence.append(item)
    list_no_stop_sentence=" ".join(no_stop_sentence)
    no_stop_sentences.append(no_stop_sentence)
    list_no_stop_sentences.append(list_no_stop_sentence)
    list_no_stop_sentence=[]
    no_stop_sentence=[]
  # word embedding
  from gensim.models import Word2Vec
  w2v=Word2Vec(no_stop_sentences,size=1,min_count=1,iter=1000)

  sentence_embeddings=[[w2v[word][0] for word in words] for words in no_stop_sentences]
  max_len=max([len(tokens) for tokens in no_stop_sentences])
  sentence_embeddings=[np.pad(embedding,(0,max_len-len(embedding)),'constant') for embedding in sentence_embeddings]
  # similarity matrix
  from scipy import spatial
  import networkx as nx
  similarity_matrix = np.zeros([len(no_stop_sentences), len(no_stop_sentences)])
  for i,row_embedding in enumerate(sentence_embeddings):
      for j,column_embedding in enumerate(sentence_embeddings):
          similarity_matrix[i][j]=1-spatial.distance.cosine(row_embedding,column_embedding)
  # page ranking
  import math
  nx_graph = nx.from_numpy_array(similarity_matrix)
  scores = nx.pagerank(nx_graph)
  top_sentence={sentence:scores[index] for index,sentence in enumerate(tokenized_sentences)}
  top=dict(sorted(top_sentence.items(), key=lambda x: x[0], reverse=True)[:math.floor(len(tokenized_sentences)*0.4)])
  counter=0
  sumamry_w2v=""
  for sent in tokenized_sentences:
      if sent in top.keys():
        sumamry_w2v+=sent
        counter+=1
  return sumamry_w2v
hindi_text='पार्टी की युवा इकाई के सम्मेलन को संबोधित करते हुए पारा ने कहा कि पांच अगस्त 2019 के बाद एक चीज नहीं बदली है जो युवाओं का मारा जाना है. केंद्र सरकार ने पांच अगस्त 2019 को अनुच्छेद 370 के अधिकतर प्रावधानों को हटा दिया था. उन्होंने कहा, “कश्मीरी युवा उससे पहले भी मारे जा रहे थे और अब भी मारे जा रहे हैं. वे उन्हें जो भी नाम दें, युवाओं की सुरक्षा की अब भी कोई गारंटी नहीं है.” पारा ने कहा, “हमारे खिलाफ जो कुछ भी हुआ है, वह हिंसा या बंदूक की वजह से जायज है. हमें सतर्कता से फैसला लेना है कि जिद और बंदूकें काम नहीं करेंगी और हमें लोकतांत्रिक स्तर पर लड़ना होगा ताकि युवाओं के मारे जाने को जायज नहीं ठहराया जा सके.” उन्होंने कहा कि कश्मीरी लोगों को और दलों तथा नेताओं की जरूरत नहीं है, लेकिन नेतृत्व की जरूरत है. पारा ने कहा कि कश्मीर में "शून्य" है और हालात 1990 से बदतर हैं. उन्होंने कहा, “न सिर्फ बंदूक थामे युवक, बल्कि टास्क फोर्स (पुलिस का विशेष अभियान समूह) और बड़े पैमाने पर गिरफ्तारियां भी. सरकार वही कर रही थी जो आतंकवादी कर रहे थे.” पारा को जम्मू कश्मीर और लद्दाख उच्च न्यायालय ने इस साल मई में ज़मानत दे दी थी. वह आतंकवाद का वित्तपोषण करने के मामले में 18 महीने जेल में रहे थे.'
# print(hindi_summary(hindi_text))

