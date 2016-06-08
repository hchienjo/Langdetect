# Langdetect
Simple flask language detection app with API

##Frontend
Built with w3.css and fontawesome

##Dependencies
Pycld2

##API
urlname/api/
####Usage  
Exmaple to check "habari yako"
l27.0.0.1:5000/api/habari+yako  

returns:
      {
  "lang": "SWAHILI",
  "match": "92.0000 %",
  "reliablity": true
}

The + sign represents spaces

###Link
http://langdetect.pythonanywhere.com/  
The API will not  work since the hosting profile used does not allow external communication


