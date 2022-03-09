##### [make](https://www.gnu.org/software/make/)
 	make  [COMMAND]
 	
 	      help
 	      init                initialize requirements
 	
 	      venv                create python3 virtual environment
 	
 	make  venv && . venv/bin/activate
 	
 	      test-venv           python3 ./tests/test.py
 	      test-gnupg          python3 ./tests/0x20bf/depends/gnupg/setup.py
 	                                  ./tests/0x20bf/depends/gnupg/test_gnupg.py
 	      test-clean-venv     rm -rf venv
 	
 	      build               python3 setup.py build
 	      install             python3 -m pip install -e .
 	      report              environment args
 	      initialize          run scripts/initialize
 	      requirements        pip install --user -r requirements.txt
 	      seeder              make -C vendor/seeder
 	      legit               pushd vendors/legit && cargo build --release
 	      gogs                make -C vendors/gogs
 	      vendors             make seeder legit gogs
 	      install-gnupg       install python gnupg on host
 	      install-p2p         install python p2p-network
 	      install-fastapi     install python fastapi
 	      fastapi
 	      depends             build depends
 	      depends-gnupg-test  test 0x20bf/depends/gnupg library
 	      pre-commit          pre-commit run -a
 	      docs                build docs from sources/*.md
