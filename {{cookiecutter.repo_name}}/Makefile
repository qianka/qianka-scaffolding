default: web

install: bower pip

bower:
	npm install
	./ne bower install

pip:
	./ve pip install -r requirements.txt

shell:
	./ne ./ve python -m scripts.shell

assets:
	./ne ./ve python -m scripts.assets

web:
	./ne ./ve python -m scripts.web
