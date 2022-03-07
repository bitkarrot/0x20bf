##### [make](https://www.gnu.org/software/make/)
 	  help
 	  init                initialize requirements
 	  venv                create python3 virtual environment
 	  test-venv           python3 ./tests/py.test
 	  test-gnupg          python3 ./tests/depends/gnupg/setup.py install
 	                      python3 ./tests/depends/gnupg/test_gnupg.py
 	  build               python3 setup.py build
 	  install             python3 -m pip install -e .
 	  report              environment args
 	  initialize          run scripts/initialize
 	  requirements        pip install --user -r requirements.txt
 	  seeder              make -C depends/seeder
 	  legit               pushd depends/legit && cargo build --release
 	  gogs                make -C depends/gogs
 	  install-gnupg       install python gnupg on host
 	  gnupg-test          test depends/gnupg library
 	  install-p2p         install python p2p-network on host
 	  fastapi             install python fastapi
 	  install-fastapi     install python fastapi
 	  depends             build depends
 	  pre-commit          pre-commit run -a
 	  docs                build docs from sources/*.md
