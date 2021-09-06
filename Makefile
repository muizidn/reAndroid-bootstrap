APKFILE := $(APKFILE_CLI)

decompile:
	python3 decompile.py $(APKFILE)

recompile_aapt2:
	python3 recompile_aapt2.py $(APKFILE)

jarsigner:
	python3 jarsigner.py $(APKFILE)

verify:
	python3 verify.py $(APKFILE)

all: # use this to test whether current apk will successfully passes reverse engineering phases
	make decompile
	make recompile_aapt2
	make jarsigner
	make verify

install:
	python3 install.py $(APKFILE)

recompile_after_edit:
	make recompile_aapt2
	make jarsigner
	make verify
