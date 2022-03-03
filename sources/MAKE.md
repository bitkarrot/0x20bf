##### [make](https://www.gnu.org/software/make/)
 	  help
 	  init           initialize requirements
 	  install        pip install -e .
 	  report         environment args
 	  initialize     run scripts/initialize
 	  requirements   pip install --user -r requirements.txt
 	  seeder         make -C depends/seeder
 	  legit          pushd depends/legit && cargo build --release
 	  gogs           make -C depends/gogs
 	  gnupg          setup python-gnupg
 	  gnupg-test     test depends/gnupg library
 	  depends        build depends
 	  pre-commit     pre-commit run -a
 	  docs           build docs from sources/*.md
