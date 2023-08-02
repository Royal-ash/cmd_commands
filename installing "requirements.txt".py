#for installing:
pip install -r requirements.txt
#if not installing then first freeze all requirements then write code for installing
pip freeze > requirements.txt
pip install -r requirements.txt
#if showing warning for permission then
pip install --user -r requirements.txt 
